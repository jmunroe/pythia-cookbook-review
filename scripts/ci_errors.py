#!/usr/bin/env python3
"""Find cookbooks whose nightly build is green but whose notebooks raised.

`myst build --execute` exits 0 when a cell raises: the exception is recorded in
the page and the build carries on. That command is the default in Pythia's
cookbook-actions, and the workflow's health is its exit status -- so a cookbook
whose notebooks fail can still report a passing nightly and deploy a book full
of tracebacks.

This reads each cookbook's own nightly log from the Actions API and looks for
MyST's execution-error marker:

    ⛔️ notebooks/01-easygems.ipynb An exception occurred during code execution,
       halting further execution

Note "halting further execution" -- everything after the failing cell is
skipped, so the published page is silently truncated.

Unlike live_check.py this uses no BinderHub capacity and reads Pythia's real CI
rather than a comparable-but-different environment, so it has no
Binder-versus-runner confound.

Usage:
    python scripts/ci_errors.py                # every gallery cookbook
    python scripts/ci_errors.py --limit 5
"""

import argparse
import concurrent.futures
import datetime
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
ORG = "ProjectPythia"

# MyST's marker for a cell that raised. The notebook path follows it.
ERROR_RE = re.compile(
    r"⛔️\s+(\S+\.ipynb)\s+An exception occurred during code execution"
)
# The exception class name, on the traceback line that follows.
ENAME_RE = re.compile(r"\x1b\[31m(\w+(?:Error|Exception|Warning))\x1b")


def gh(args):
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else None


def latest_nightly(name):
    """The most recent nightly-build run, whatever its conclusion."""
    out = gh(
        [
            "gh", "run", "list",
            "--repo", f"{ORG}/{name}",
            "--workflow", "nightly-build.yaml",
            "--limit", "1",
            "--json", "databaseId,conclusion,createdAt,url",
        ]
    )
    try:
        runs = json.loads(out or "[]")
    except json.JSONDecodeError:
        return None
    return runs[0] if runs else None


def scan(name):
    """Which notebooks raised in this cookbook's latest nightly."""
    print(f"  {name}", file=sys.stderr, flush=True)
    run = latest_nightly(name)
    if not run:
        return {"cookbook": name, "run": None, "notebooks": [], "reason": "no nightly runs"}

    log = gh(["gh", "run", "view", str(run["databaseId"]), "--repo", f"{ORG}/{name}", "--log"])
    if log is None:
        return {
            "cookbook": name,
            "run": run,
            "notebooks": [],
            "reason": "log unavailable (expired or too large)",
        }

    # Keep the exception type seen just after each marker, when we can get it.
    notebooks, lines = {}, log.splitlines()
    for index, line in enumerate(lines):
        match = ERROR_RE.search(line)
        if not match:
            continue
        notebook = match.group(1)
        ename = None
        for following in lines[index + 1 : index + 4]:
            found = ENAME_RE.search(following)
            if found:
                ename = found.group(1)
                break
        notebooks.setdefault(notebook, ename)

    return {
        "cookbook": name,
        "run": run,
        "notebooks": [{"notebook": n, "ename": e} for n, e in sorted(notebooks.items())],
        "reason": None,
    }


def gallery_names():
    text = gh(
        ["gh", "api",
         f"repos/{ORG}/cookbook-gallery/contents/cookbook_gallery.txt",
         "--jq", ".content"]
    )
    if not text:
        raise SystemExit("could not read cookbook_gallery.txt")
    import base64

    decoded = base64.b64decode(text).decode()
    return [line.strip() for line in decoded.splitlines() if line.strip()]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int)
    parser.add_argument("cookbooks", nargs="*", help="default: every gallery cookbook")
    args = parser.parse_args()

    names = args.cookbooks or gallery_names()
    if args.limit:
        names = names[: args.limit]

    print(f"Scanning {len(names)} nightly logs...", file=sys.stderr)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(scan, names))

    # Join with the static snapshot so each result carries what the gallery
    # *publishes*. The status page shows "passing" only when the badge passes
    # and the book deployed within the last week, so reproduce that rule rather
    # than assuming a green run means a green card.
    try:
        import report

        snapshot = json.loads(report.newest_snapshot().read_text())
        deploys = {
            b["name"]: (
                b["build"]["nightly_conclusion"],
                b["build"]["days_since_deploy"],
            )
            for b in snapshot["cookbooks"]
        }
    except Exception:  # noqa: BLE001 - the join is a bonus, not a requirement
        deploys = {}

    for r in results:
        conclusion, age = deploys.get(r["cookbook"], (None, None))
        r["published_as_passing"] = (
            conclusion == "success" and age is not None and age <= 7
        )

    green_with_errors = [
        r
        for r in results
        if r["notebooks"] and (r["run"] or {}).get("conclusion") == "success"
    ]
    published_passing_with_errors = [
        r for r in green_with_errors if r["published_as_passing"]
    ]

    today = datetime.date.today().isoformat()
    out = DATA / f"ci-errors-{today}.json"
    out.write_text(
        json.dumps(
            {
                "collected_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "scanned": len(results),
                "green_with_errors": len(green_with_errors),
                "published_as_passing_with_errors": len(published_passing_with_errors),
                "results": results,
            },
            indent=2,
        )
        + "\n"
    )

    print(f"\nWrote {out}")
    print(f"  scanned:                     {len(results)}")
    print(f"  green nightly, notebooks raised:         {len(green_with_errors)}")
    print(f"  gallery says passing, notebooks raised:  "
          f"{len(published_passing_with_errors)}")
    for r in green_with_errors:
        mark = "GALLERY: PASSING" if r["published_as_passing"] else "not published as passing"
        print(f"    {r['cookbook']:34} {len(r['notebooks']):2} nb  [{mark}]")


if __name__ == "__main__":
    main()
