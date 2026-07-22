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

# Build-log lines kept in the record. The error is always at the tail, and a
# failed fresh build can emit thousands of lines of repo2docker output.
LOG_TAIL_LINES = 300

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

    # A failed fresh build emits the whole repo2docker log -- thousands of lines,
    # ~200 KB. The tail is where the actual error is, and these records are
    # committed and accumulate per run, so keep a bounded window.
    kept = lines[-LOG_TAIL_LINES:]

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
        "log": kept,
        "log_lines_total": len(lines),
        "log_truncated": len(kept) < len(lines),
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
        peak_pss = peak("pss")
        # rss is summed over the server and every child, so shared pages are
        # counted once per process -- radar-cookbook read 12.2 GB against an
        # 8.6 GB cgroup limit it never actually breached. pss apportions shared
        # memory and is the figure to compare against the limit; rss is kept as
        # an upper bound.
        against_limit = peak_pss if peak_pss else peak_rss

        # cpu_percent and disk are only present if the hub enabled tracking;
        # report them when they exist rather than inventing zeros.
        cpu = [s["cpu_percent"] for s in self.samples if "cpu_percent" in s]

        return {
            "available": True,
            "sample_count": len(self.samples),
            "sample_seconds": SAMPLE_SECONDS,
            "peak_rss_bytes": peak_rss,
            "peak_pss_bytes": peak_pss,
            # Which figure the fraction below is based on, so a reader never has
            # to guess whether shared memory was double-counted.
            "limit_basis": "pss" if peak_pss else "rss",
            "peak_against_limit_bytes": against_limit,
            "memory_limit_bytes": limit,
            "peak_fraction_of_limit": (
                round(against_limit / limit, 4) if against_limit and limit else None
            ),
            "peak_cpu_percent": max(cpu) if cpu else None,
            "cpu_count": self.samples[-1].get("cpu_count"),
        }


# --------------------------------------------------------------------------
# Execution
# --------------------------------------------------------------------------


def collect_env(names, env_file):
    """Values for the variables to inject, from our own environment or a file.

    Values are never taken from the command line: argv is visible to anyone
    running `ps` and is echoed into CI logs. `--env NAME` reads NAME from our
    environment; `--env-file` reads KEY=VALUE lines.
    """
    variables = {}
    if env_file:
        for line in pathlib.Path(env_file).read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            variables[key.strip()] = value.strip().strip("'\"")
    for name in names or []:
        value = os.environ.get(name)
        if value is None:
            log(f"WARNING: --env {name} requested but not set in this environment")
            continue
        variables[name] = value

    # Cheap sanity check: a credential with whitespace in it usually means a
    # paste picked up surrounding text. Python's http.client rejects every
    # character in [\x00-\x20\x7f] -- which includes a plain space -- and
    # reports it as "URL can't contain control characters", so the resulting
    # failure points nowhere near the real cause. Warn rather than refuse: a
    # value may legitimately contain spaces for uses other than a URL.
    for name, value in variables.items():
        if any(c.isspace() for c in value):
            log(
                f"WARNING: {name} contains whitespace. If it is used in a URL "
                "this will fail as \"URL can't contain control characters\". "
                "Check for text copied along with the value."
            )
    return variables


def seed_environment(session, variables):
    """Put variables into every kernel the session will later start.

    Notebooks read credentials with os.getenv, and that runs on the Binder pod --
    exporting a variable here does nothing, because the code executes there. The
    local environment genuinely does not cross over; binderbot's own test asserts
    exactly that ("CI" not in os.environ).

    IPython executes any .py file in ~/.ipython/profile_default/startup/ when a
    kernel starts, and the Jupyter contents API can write into the session's home
    directory. Doing that *before* MyST starts any kernel is the whole trick, and
    this is the one moment we control it.

    Caveats worth keeping in view: this only reaches Python kernels, and it
    depends on the hub allowing writes to hidden paths (ContentsManager
    .allow_hidden defaults to False, though Pythia's hub permits it). A failure
    here is reported loudly rather than swallowed -- silently skipping it
    produces baffling downstream errors like len(None).
    """
    if not variables:
        return {"attempted": False}

    def put(path, payload):
        url = session["url"].rstrip("/") + "/api/contents/" + path
        request = urllib.request.Request(
            url, data=json.dumps(payload).encode(), method="PUT"
        )
        request.add_header("Authorization", f"token {session['token']}")
        request.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return response.status, None
        except urllib.error.HTTPError as err:
            return err.code, err.read().decode()[:200]
        except (urllib.error.URLError, OSError) as err:
            return None, str(err)

    for directory in (
        ".ipython",
        ".ipython/profile_default",
        ".ipython/profile_default/startup",
    ):
        status, detail = put(directory, {"type": "directory"})
        if status not in (200, 201):
            log(f"WARNING: could not create {directory} on the session: {status} {detail}")
            return {
                "attempted": True,
                "ok": False,
                "reason": f"creating {directory} returned {status}: {detail}",
                "variables": sorted(variables),
            }

    body = "import os\n" + "".join(
        f"os.environ[{k!r}] = {v!r}\n" for k, v in sorted(variables.items())
    )
    status, detail = put(
        ".ipython/profile_default/startup/00-live-check-env.py",
        {"type": "file", "format": "text", "content": body},
    )
    ok = status in (200, 201)
    # Log the names only. The values are secrets and must never reach a log, a
    # record, or the repository.
    log(
        f"{'Injected' if ok else 'FAILED to inject'} "
        f"{', '.join(sorted(variables))} into the session"
    )
    return {
        "attempted": True,
        "ok": ok,
        "reason": None if ok else f"upload returned {status}: {detail}",
        "variables": sorted(variables),
    }


def build_size(clone):
    """Bytes currently sitting in the clone's _build, or 0."""
    build = clone / "_build"
    if not build.is_dir():
        return 0
    return sum(f.stat().st_size for f in build.rglob("*") if f.is_file())


def clear_build(clone):
    """Empty the clone's _build, keeping MyST's downloaded themes.

    _build/templates is ~130 MB of theme that MyST would otherwise re-download
    every run; it has no bearing on whether notebooks re-execute. Everything
    else -- execute/, site/, html/, cache/ -- goes, which is what forces a real
    execution rather than a cached replay.
    """
    build = clone / "_build"
    if not build.is_dir():
        return False
    removed = False
    for child in build.iterdir():
        if child.name == "templates":
            continue
        shutil.rmtree(child) if child.is_dir() else child.unlink()
        removed = True
    return removed


def execute_notebooks(clone, session, timeout, keep_cache=False):
    """Build the cookbook with its notebooks executed on the Binder session.

    `myst build --execute --html` is the documented binderbot handoff and the
    default build command in Pythia's own cookbook-actions, so a result here is
    comparable to a real cookbook build.

    MyST caches executed outputs under _build/execute. Left in place, a second
    run reports a fast "execution" that executed nothing -- the same trap as a
    cached Binder image. So we clear it by default and record that we did.
    """
    cleared = False
    if not keep_cache:
        cleared = clear_build(clone)
        if cleared:
            log("Cleared _build (kept templates) so notebooks really execute")

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
        # On timeout these come back as raw bytes even under text=True, so decode
        # before appending the marker -- concatenating str to bytes crashes, and
        # a slow cookbook that hits the timeout is exactly when we need a record.
        err = expired.stderr or ""
        if isinstance(err, bytes):
            err = err.decode(errors="replace")
        err += f"\nTIMEOUT after {timeout}s"
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

    # MyST writes each page's AST twice -- once under site/content and again
    # under html. Scanning both counts every error twice, so prefer the
    # canonical copy and only fall back to a full walk if it is absent.
    canonical = build / "site" / "content"
    roots = [canonical] if canonical.is_dir() else [build]

    errors = []
    seen = set()
    for path in (p for root in roots for p in root.rglob("*.json")):
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
            clean = re.sub(r"\x1b\[[0-9;]*m", "", str(traceback))[:2000]
            key = (path.name, node.get("ename"), node.get("evalue"), clean[:200])
            if key in seen:
                continue
            seen.add(key)
            errors.append(
                {
                    "source": str(path.relative_to(build)),
                    "ename": node.get("ename"),
                    "evalue": node.get("evalue"),
                    # Tracebacks carry ANSI colour codes; strip for readability.
                    "traceback": clean,
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
    parser.add_argument("cookbook", nargs="+",
                        help="repo name(s), e.g. HRRR-AWS-cookbook; run in sequence")
    parser.add_argument("--hub", default=DEFAULT_HUB)
    parser.add_argument("--ref", default="main")
    parser.add_argument("--build-token", default=os.environ.get("BINDER_BUILD_TOKEN"))
    parser.add_argument("--build-timeout", type=int, default=1800)
    parser.add_argument("--execute-timeout", type=int, default=1800)
    parser.add_argument("--env", action="append", metavar="NAME",
                        help="inject NAME from this environment into the session's "
                             "kernels (value is read from here, never from argv)")
    parser.add_argument("--env-file", metavar="PATH",
                        help="inject KEY=VALUE lines from PATH; keep this file "
                             "outside the repository")
    parser.add_argument("--keep-build", action="store_true",
                        help="keep the rendered output even on success")
    parser.add_argument("--keep-cache", action="store_true",
                        help="do not clear _build first (execution may be reused)")
    parser.add_argument("--dry-run", action="store_true", help="print the plan only")
    parser.add_argument("--out", type=pathlib.Path)
    args = parser.parse_args()

    if args.dry_run:
        for name in args.cookbook:
            clone = PARENT / name
            print(f"--- {name}")
            print(f"clone:   {clone} (exists: {clone.is_dir()})")
            print(f"toc notebooks: {executed_notebooks(clone) if clone.is_dir() else '?'}")
            print(
                "start:   binderbot start "
                f"{args.hub} --github-repo {ORG}/{name} "
                f"--github-ref {args.ref} --json"
            )
            print(f"sample:  GET <session>/api/metrics/v1 every {SAMPLE_SECONDS}s")
            print("execute: myst build --execute --html")
            print("stop:    binderbot stop <url> <token>")
        return 0

    for tool in ("binderbot", "myst"):
        if not shutil.which(tool):
            raise SystemExit(f"{tool} not found on PATH (npm install -g binderbot mystmd)")

    # Strictly one session at a time: several cookbooks in flight would multiply
    # our footprint on a hub that exists for learners.
    # Resolved once, so a missing variable is reported before any session starts.
    variables = collect_env(args.env, args.env_file)

    worst = 0
    for index, name in enumerate(args.cookbook, 1):
        if len(args.cookbook) > 1:
            log("")
            log(f"===== [{index}/{len(args.cookbook)}] {name}")
        worst = max(worst, check_one(name, args, variables))
    return worst


def check_one(name, args, variables=None):
    """Live-check a single cookbook. Returns 0 if it built and ran cleanly."""
    clone = PARENT / name
    if not clone.is_dir():
        raise SystemExit(f"{clone} missing -- run ./scripts/sync-clones.sh {name}")

    record = {
        "cookbook": name,
        "env_injection": {"attempted": False},
        "started_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "hub": args.hub,
        "ref": args.ref,
        "toc_notebooks": executed_notebooks(clone),
    }

    session = None
    sampler = None
    try:
        session, record["build"] = start_session(
            args.hub, name, args.ref, args.build_token, args.build_timeout
        )
        if session is None:
            log("Build failed; nothing to execute.")
            record["execution"] = None
            record["resources"] = None
            record["errors"] = []
        else:
            log(f"Session ready at {session['url']}")
            record["env_injection"] = seed_environment(session, variables)
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

    # Nothing the build produced is part of the result -- the record holds the
    # measurements. Keep the rendered output only when something failed and
    # there is a post-mortem to do; otherwise drop a few hundred MB per run.
    failed = record["build"]["failed"] or (
        record.get("execution") or {}
    ).get("failed")
    if failed or args.keep_build:
        record["build_artifacts"] = {
            "path": str(clone / "_build"),
            "bytes": build_size(clone),
            "kept_because": "run failed" if failed else "--keep-build",
        }
        log(f"Kept build output in {clone / '_build'} for inspection")
    else:
        clear_build(clone)
        record["build_artifacts"] = None

    # Second-resolution, because a same-day re-run is the normal case (fixing a
    # credential, re-testing a flaky network failure) and must not destroy the
    # earlier result.
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")
    out = args.out or LIVE / f"{name}-{stamp}.json"
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
            peak = resources.get("peak_against_limit_bytes") or resources["peak_rss_bytes"]
            limit = resources["memory_limit_bytes"]
            basis = resources.get("limit_basis", "rss")
            log(f"  peak {basis:<5} {peak / 1e9:.2f} GB"
                + (f" of {limit / 1e9:.2f} GB limit" if limit else " (no limit reported)"))
        else:
            log(f"  resources  unavailable: {resources.get('reason')}")
        log(f"  errors     {len(record['errors'])}")

    return 1 if build["failed"] or (execution and execution["failed"]) else 0


if __name__ == "__main__":
    sys.exit(main())
