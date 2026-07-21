#!/usr/bin/env python3
"""Run one cookbook for real on a BinderHub, and record what it cost.

The static audit (audit.py) reads configuration and CI state. This asks a
different question: does the cookbook actually run today, in the environment its
launch button sends learners to, and how much time and memory does it take?

The sequence:

    binderbot start   -> a live Jupyter session on the hub (+ build timing)
    /api/metrics/v1   -> sampled memory while the notebooks run
    myst build --execute -> the same command Pythia's own build uses
    binderbot stop    -> release the pod (always, even on failure)

Every run consumes shared BinderHub capacity, so this is manual and does one
cookbook at a time. See docs/live-assessment.md before trusting a number --
particularly the part about cached images making build time meaningless.

Usage:
    python scripts/live_check.py HRRR-AWS-cookbook --dry-run
    python scripts/live_check.py HRRR-AWS-cookbook
"""

import argparse
import datetime
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import threading
import time

import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
PARENT = ROOT.parent
LIVE = ROOT / "data" / "live"

ORG = "projectpythia"
DEFAULT_HUB = "https://binder.projectpythia.org"

# How often to ask the server for its resource usage while notebooks execute.
# Short enough to catch a plateau, long enough not to be a nuisance.
SAMPLE_SECONDS = 3

# BinderHub says this when it can reuse an existing image instead of building
# one. Distinguishing the two is the difference between a build time that means
# something and one that means nothing at all.
CACHED_MARKERS = (
    "Found built image",
    "Launching server",
)
BUILDING_MARKERS = (
    "Building conda environment",
    "Step 1/",
    "Successfully built",
    "Pushing image",
)


def log(message):
    print(message, file=sys.stderr, flush=True)


# --------------------------------------------------------------------------
# The Binder session
# --------------------------------------------------------------------------


def start_session(hub, repo, ref, build_token, timeout):
    """Start a Binder session, timing the build.

    Returns (session, build) where session is {"url","token"} or None. binderbot
    prints the build log to stderr under --json and the session JSON to stdout;
    it exits 1 on a failed build. We stamp each log line with its elapsed offset
    because binderbot emits the phase's *message* but not the phase itself, so
    timings plus log markers are how we recover the shape of the build.
    """
    command = [
        "binderbot",
        "start",
        hub,
        "--github-repo",
        f"{ORG}/{repo}",
        "--github-ref",
        ref,
        "--json",
    ]
    if build_token:
        command += ["--build-token", build_token]

    log(f"$ {' '.join(command)}")
    started = time.monotonic()
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,
    )

    lines = []

    def drain():
        for line in process.stderr:
            offset = round(time.monotonic() - started, 2)
            line = line.rstrip()
            lines.append({"t": offset, "line": line})
            log(f"  [{offset:7.2f}s] {line}")

    reader = threading.Thread(target=drain, daemon=True)
    reader.start()

    try:
        stdout, _ = process.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        process.kill()
        stdout = ""
        log(f"binderbot exceeded {timeout}s; killed")
    reader.join(timeout=5)

    elapsed = round(time.monotonic() - started, 2)
    text = "\n".join(entry["line"] for entry in lines)

    build = {
        "hub": hub,
        "ref": ref,
        "seconds": elapsed,
        "exit_code": process.returncode,
        "failed": process.returncode != 0,
        # A fresh build exercises environment.yml; a cached one tests nothing
        # about it. Never read a duration without this flag.
        "image_cached": any(m in text for m in CACHED_MARKERS)
        and not any(m in text for m in BUILDING_MARKERS),
        "log": lines,
    }

    session = None
    for line in (stdout or "").splitlines():
        line = line.strip()
        if line.startswith("{"):
            try:
                candidate = json.loads(line)
            except json.JSONDecodeError:
                continue
            if "url" in candidate and "token" in candidate:
                session = candidate
    if session is None:
        build["failed"] = True

    return session, build


def stop_session(session):
    """Release the pod. Best effort -- never raise out of a finally block."""
    if not session:
        return
    log("Stopping the Binder session")
    try:
        subprocess.run(
            ["binderbot", "stop", session["url"], session["token"]],
            timeout=120,
            capture_output=True,
            text=True,
        )
    except Exception as err:  # noqa: BLE001 - cleanup must not mask the real error
        log(f"WARNING: could not stop the session: {err}")


# --------------------------------------------------------------------------
# Resource sampling
# --------------------------------------------------------------------------


class ResourceSampler(threading.Thread):
    """Poll the session's /api/metrics/v1 and keep the peak.

    Works without any cooperation from the cookbook: repo2docker ships
    jupyter-resource-usage in its base environment, so every Binder image serves
    this endpoint. `rss` sums the server process and all its children, so it
    includes the kernel doing the work.

    A hub that does not serve the endpoint yields samples=[] and a null peak --
    that is a finding to report, not a reason to fail the run.
    """

    def __init__(self, session):
        super().__init__(daemon=True)
        self.url = session["url"].rstrip("/") + "/api/metrics/v1"
        self.token = session["token"]
        self.samples = []
        self.errors = []
        self._done = threading.Event()

    def poll(self):
        request = urllib.request.Request(
            self.url, headers={"Authorization": f"token {self.token}"}
        )
        with urllib.request.urlopen(request, timeout=15) as response:
            return json.loads(response.read().decode())

    def run(self):
        while not self._done.is_set():
            try:
                payload = self.poll()
                payload["t"] = round(time.monotonic(), 2)
                self.samples.append(payload)
            except (urllib.error.URLError, urllib.error.HTTPError, OSError) as err:
                if len(self.errors) < 5:
                    self.errors.append(str(err))
            self._done.wait(SAMPLE_SECONDS)

    def stop(self):
        self._done.set()

    def summary(self):
        if not self.samples:
            return {
                "available": False,
                "reason": self.errors[0] if self.errors else "no samples collected",
            }

        def peak(key):
            values = [s[key] for s in self.samples if isinstance(s.get(key), int)]
            return max(values) if values else None

        limit = None
        for sample in self.samples:
            candidate = ((sample.get("limits") or {}).get("memory") or {}).get("rss")
            if isinstance(candidate, int) and candidate > 0:
                limit = candidate
        peak_rss = peak("rss")

        # cpu_percent and disk are only present if the hub enabled tracking;
        # report them when they exist rather than inventing zeros.
        cpu = [s["cpu_percent"] for s in self.samples if "cpu_percent" in s]

        return {
            "available": True,
            "sample_count": len(self.samples),
            "sample_seconds": SAMPLE_SECONDS,
            "peak_rss_bytes": peak_rss,
            "peak_pss_bytes": peak("pss"),
            "memory_limit_bytes": limit,
            "peak_fraction_of_limit": (
                round(peak_rss / limit, 4) if peak_rss and limit else None
            ),
            "peak_cpu_percent": max(cpu) if cpu else None,
            "cpu_count": self.samples[-1].get("cpu_count"),
        }


# --------------------------------------------------------------------------
# Execution
# --------------------------------------------------------------------------


def execute_notebooks(clone, session, timeout, keep_cache=False):
    """Build the cookbook with its notebooks executed on the Binder session.

    `myst build --execute --html` is the documented binderbot handoff and the
    default build command in Pythia's own cookbook-actions, so a result here is
    comparable to a real cookbook build.

    MyST caches executed outputs under _build/execute. Left in place, a second
    run reports a fast "execution" that executed nothing -- the same trap as a
    cached Binder image. So we clear it by default and record that we did.
    """
    cache = clone / "_build"
    cleared = False
    if cache.is_dir() and not keep_cache:
        shutil.rmtree(cache)
        cleared = True
        log(f"Cleared {cache} so notebooks really execute")

    env = dict(os.environ)
    env["JUPYTER_BASE_URL"] = session["url"]
    env["JUPYTER_TOKEN"] = session["token"]
    # Cookbooks are project sites; without this MyST warns about asset paths.
    env.setdefault("BASE_URL", "")

    command = ["myst", "build", "--execute", "--html"]
    log(f"$ {' '.join(command)}  (in {clone})")
    started = time.monotonic()
    try:
        result = subprocess.run(
            command,
            cwd=clone,
            env=env,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        code, out, err = result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired as expired:
        code = None
        out = expired.stdout or ""
        err = (expired.stderr or "") + f"\nTIMEOUT after {timeout}s"
        log(f"myst build exceeded {timeout}s")

    elapsed = round(time.monotonic() - started, 2)
    if isinstance(out, bytes):
        out = out.decode(errors="replace")
    if isinstance(err, bytes):
        err = err.decode(errors="replace")

    return {
        "seconds": elapsed,
        "exit_code": code,
        "failed": code != 0,
        # False means MyST may have reused cached outputs, and `seconds` then
        # measures rendering rather than execution.
        "cache_cleared": cleared,
        # `seconds` covers rendering the theme too; these isolate each page.
        "page_seconds": per_page_timings(out),
        "stdout_tail": (out or "")[-4000:],
        "stderr_tail": (err or "")[-4000:],
    }


def collect_errors(clone):
    """Per-cell execution errors, read out of MyST's built JSON.

    MyST writes each page's AST (including cell outputs) under _build. An
    executed cell that raised carries an output with output_type == "error",
    which gives us the exception type, message and traceback per notebook --
    far better than scraping the build log.
    """
    build = clone / "_build"
    if not build.is_dir():
        return []

    errors = []
    for path in build.rglob("*.json"):
        try:
            data = json.loads(path.read_text())
        except (json.JSONDecodeError, OSError, UnicodeDecodeError):
            continue

        found = []

        def walk(node):
            if isinstance(node, dict):
                if node.get("output_type") == "error" or (
                    node.get("status") == "error" and node.get("ename")
                ):
                    found.append(node)
                for value in node.values():
                    walk(value)
            elif isinstance(node, list):
                for item in node:
                    walk(item)

        walk(data)
        for node in found:
            traceback = node.get("traceback") or []
            if isinstance(traceback, list):
                traceback = "\n".join(str(t) for t in traceback)
            errors.append(
                {
                    "source": str(path.relative_to(build)),
                    "ename": node.get("ename"),
                    "evalue": node.get("evalue"),
                    # Tracebacks carry ANSI colour codes; strip for readability.
                    "traceback": re.sub(r"\x1b\[[0-9;]*m", "", str(traceback))[:2000],
                }
            )
    return errors


def per_page_timings(stdout):
    """Per-page build times, parsed from MyST's own progress output.

    MyST prints e.g. "Built notebooks/example-workflows/plot-2mt.ipynb in 22 s".
    For a notebook that time is dominated by executing it on the Binder session,
    which is a far better signal than the whole-command wall time -- the latter
    also covers rendering the HTML theme.
    """
    timings = []
    for match in re.finditer(
        r"Built (\S+) in ([\d.]+)\s*(ms|s|m)\b", stdout or ""
    ):
        path, value, unit = match.groups()
        seconds = float(value) * {"ms": 0.001, "s": 1.0, "m": 60.0}[unit]
        timings.append({"page": path, "seconds": round(seconds, 2)})
    return timings


def executed_notebooks(clone):
    """Notebooks MyST actually executed -- i.e. the ones in the project toc.

    Not the same as notebooks in the repo: MyST only builds what the toc lists,
    so a repo can carry notebooks that no build ever touches.
    """
    myst = clone / "myst.yml"
    if not myst.is_file():
        return []
    return sorted(set(re.findall(r"file:\s*(\S+\.ipynb)", myst.read_text())))


# --------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cookbook", help="repo name, e.g. HRRR-AWS-cookbook")
    parser.add_argument("--hub", default=DEFAULT_HUB)
    parser.add_argument("--ref", default="main")
    parser.add_argument("--build-token", default=os.environ.get("BINDER_BUILD_TOKEN"))
    parser.add_argument("--build-timeout", type=int, default=1800)
    parser.add_argument("--execute-timeout", type=int, default=1800)
    parser.add_argument("--keep-cache", action="store_true",
                        help="do not clear _build first (execution may be reused)")
    parser.add_argument("--dry-run", action="store_true", help="print the plan only")
    parser.add_argument("--out", type=pathlib.Path)
    args = parser.parse_args()

    clone = PARENT / args.cookbook
    if args.dry_run:
        print(f"clone:   {clone} (exists: {clone.is_dir()})")
        print(f"toc notebooks: {executed_notebooks(clone) if clone.is_dir() else '?'}")
        print(
            "start:   binderbot start "
            f"{args.hub} --github-repo {ORG}/{args.cookbook} "
            f"--github-ref {args.ref} --json"
        )
        print(f"sample:  GET <session>/api/metrics/v1 every {SAMPLE_SECONDS}s")
        print("execute: myst build --execute --html")
        print("stop:    binderbot stop <url> <token>")
        return 0

    for tool in ("binderbot", "myst"):
        if not shutil.which(tool):
            raise SystemExit(f"{tool} not found on PATH (npm install -g binderbot mystmd)")
    if not clone.is_dir():
        raise SystemExit(f"{clone} missing -- run ./scripts/sync-clones.sh {args.cookbook}")

    record = {
        "cookbook": args.cookbook,
        "started_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "hub": args.hub,
        "ref": args.ref,
        "toc_notebooks": executed_notebooks(clone),
    }

    session = None
    sampler = None
    try:
        session, record["build"] = start_session(
            args.hub, args.cookbook, args.ref, args.build_token, args.build_timeout
        )
        if session is None:
            log("Build failed; nothing to execute.")
            record["execution"] = None
            record["resources"] = None
            record["errors"] = []
        else:
            log(f"Session ready at {session['url']}")
            sampler = ResourceSampler(session)
            sampler.start()
            record["execution"] = execute_notebooks(
                clone, session, args.execute_timeout, args.keep_cache
            )
            sampler.stop()
            sampler.join(timeout=10)
            record["resources"] = sampler.summary()
            record["errors"] = collect_errors(clone)
    finally:
        if sampler:
            sampler.stop()
        stop_session(session)

    record["finished_at"] = datetime.datetime.now(datetime.timezone.utc).isoformat()

    today = datetime.date.today().isoformat()
    out = args.out or LIVE / f"{args.cookbook}-{today}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(record, indent=2) + "\n")
    log(f"Wrote {out}")

    build, execution = record["build"], record.get("execution")
    log("")
    log(f"  build      {build['seconds']}s"
        f"{' (cached image)' if build['image_cached'] else ' (fresh image)'}"
        f"{' FAILED' if build['failed'] else ''}")
    if execution:
        log(f"  execute    {execution['seconds']}s"
            f"{' FAILED' if execution['failed'] else ''}")
        resources = record["resources"]
        if resources.get("available"):
            peak = resources["peak_rss_bytes"]
            limit = resources["memory_limit_bytes"]
            log(f"  peak rss   {peak / 1e9:.2f} GB"
                + (f" of {limit / 1e9:.2f} GB limit" if limit else " (no limit reported)"))
        else:
            log(f"  resources  unavailable: {resources.get('reason')}")
        log(f"  errors     {len(record['errors'])}")

    return 1 if build["failed"] or (execution and execution["failed"]) else 0


if __name__ == "__main__":
    sys.exit(main())
