#!/usr/bin/env python3
"""Turn live-check results into a readable report.

Reads the newest data/live/<cookbook>-<date>.json for each cookbook and writes
reports/live.md. Like the static reports, this is generated output -- never
hand-edit it.

Usage:
    python scripts/report_live.py
"""

import argparse
import json
import pathlib

import report

ROOT = pathlib.Path(__file__).resolve().parent.parent
LIVE = ROOT / "data" / "live"
REPORTS = ROOT / "reports"


def static_tiers():
    """Each cookbook's tier from the newest static snapshot, for comparison.

    The interesting cases are the disagreements: a cookbook the static checks
    call healthy that will not actually run, or one they call stale that runs
    fine and is simply not being redeployed.
    """
    try:
        snapshot = json.loads(report.newest_snapshot().read_text())
    except (SystemExit, OSError, json.JSONDecodeError):
        return {}
    return {b["name"]: report.tier(b) for b in snapshot["cookbooks"]}


def newest_per_cookbook():
    """The most recent run for each cookbook, by filename date."""
    latest = {}
    for path in sorted(LIVE.glob("*.json")):
        try:
            record = json.loads(path.read_text())
        except (json.JSONDecodeError, OSError):
            continue
        previous = latest.get(record["cookbook"])
        if previous is None or record.get("started_at", "") >= previous[1].get(
            "started_at", ""
        ):
            latest[record["cookbook"]] = (path, record)
    return latest


def gb(value):
    return f"{value / 1e9:.2f} GB" if isinstance(value, (int, float)) else "—"


def blob(record, path):
    """Link a repo-relative path to the exact ref that was built.

    Pinning to `ref` rather than main means the link still shows what was
    actually executed, even after the cookbook moves on.
    """
    return (
        f"https://github.com/ProjectPythia/{record['cookbook']}"
        f"/blob/{record['ref']}/{path}"
    )


def verdict(record):
    """A one-word live outcome, independent of the static tier."""
    if (record.get("build") or {}).get("failed"):
        return "build failed"
    execution = record.get("execution") or {}
    if execution.get("failed"):
        return "execution failed"
    if record.get("errors"):
        return "ran with errors"
    return "ran clean"


def summary_table(latest, tiers):
    """All live-checked cookbooks at a glance, beside their static tier."""
    lines = [
        "## At a glance",
        "",
        "| Cookbook | Live outcome | Static tier | Session | Execution | Peak memory | Errors |",
        "|---|---|---|---|---|---|---|",
    ]
    for name, (_, record) in sorted(latest.items()):
        build = record.get("build") or {}
        execution = record.get("execution") or {}
        resources = record.get("resources") or {}
        # pss where available -- rss double-counts shared pages (see describe()).
        peak = resources.get("peak_against_limit_bytes") or resources.get("peak_rss_bytes")
        limit = resources.get("memory_limit_bytes")
        lines.append(
            f"| [{name}](#{name.lower()}) "
            f"| {verdict(record)} "
            f"| `{tiers.get(name, '—')}` "
            f"| {build.get('seconds')}s"
            f"{' (cached)' if build.get('image_cached') else ''} "
            f"| {execution.get('seconds', '—')}s "
            f"| {f'{peak / 1e9:.2f} of {limit / 1e9:.1f} GB' if peak and limit else '—'} "
            f"| {len(record.get('errors') or [])} |"
        )
    lines += [
        "",
        "Where the live outcome and the static tier disagree, the live result is the more "
        "direct evidence — but read it as one sample of a network-dependent workflow, not a "
        "verdict. See [the limitations](../docs/live-assessment.md#limitations).",
        "",
    ]
    return lines


def describe(record, tiers):
    """One cookbook's result as markdown lines."""
    build = record.get("build") or {}
    execution = record.get("execution")
    resources = record.get("resources") or {}
    errors = record.get("errors") or []

    repo = f"https://github.com/ProjectPythia/{record['cookbook']}"
    lines = [f"## {record['cookbook']}", ""]
    lines.append(
        f"Run {record['started_at'][:19].replace('T', ' ')} UTC "
        f"against [{record['hub']}]({record['hub']}), building "
        f"[{record['cookbook']}]({repo}) at ref "
        f"[`{record['ref']}`]({repo}/tree/{record['ref']})."
    )
    lines.append("")

    # The cached-image caveat has to travel with the number, not sit in a
    # footnote -- a cached build time says nothing about the environment.
    if build.get("image_cached"):
        lines += [
            ":::{warning} Cached image",
            f"BinderHub reused an existing image, so the {build.get('seconds')}s "
            "is a pod launch and image pull. It does **not** test whether "
            "`environment.yml` still solves.",
            ":::",
            "",
        ]

    tier = tiers.get(record["cookbook"])
    rows = [
        "| Measure | Value |",
        "|---|---|",
        f"| Live outcome | **{verdict(record)}** |",
        f"| Static tier | `{tier}` |" if tier else "| Static tier | — |",
        f"| Time to a ready session | {build.get('seconds')}s"
        f"{' (cached image)' if build.get('image_cached') else ' (fresh build)'} |",
        f"| Build succeeded | {'no' if build.get('failed') else 'yes'} |",
    ]
    if execution:
        # `myst build --execute` exits 0 even when cells raise, so the exit code
        # alone would call a run with ten tracebacks a success. Report both.
        clean = not execution.get("failed") and not errors
        rows += [
            f"| Notebook execution | {execution.get('seconds')}s |",
            f"| Build command exit code | {execution.get('exit_code')}"
            + (" (zero despite cell errors)" if execution.get("exit_code") == 0 and errors else "")
            + " |",
            f"| Notebooks ran clean | {'yes' if clean else 'no'} |",
        ]
        if not execution.get("cache_cleared", True):
            rows.append("| Execution cache | **reused — timing is not execution** |")
    if resources.get("available"):
        basis = resources.get("limit_basis", "rss")
        rows += [
            f"| Peak memory ({basis}) | {gb(resources.get('peak_against_limit_bytes'))} |",
            f"| Pod memory limit | {gb(resources.get('memory_limit_bytes'))} |",
        ]
        fraction = resources.get("peak_fraction_of_limit")
        if fraction is not None:
            rows.append(f"| Peak as share of limit | {fraction:.1%} |")
        # rss double-counts pages shared between the server and its kernels, so
        # it can read above a limit the pod never breached. Show it as the upper
        # bound it is, not as the headline.
        if basis == "pss" and resources.get("peak_rss_bytes"):
            rows.append(
                f"| Peak rss (upper bound, shared pages double-counted) "
                f"| {gb(resources['peak_rss_bytes'])} |"
            )
        if resources.get("peak_cpu_percent") is not None:
            rows.append(f"| Peak CPU | {resources['peak_cpu_percent']}% |")
    else:
        rows.append(
            f"| Resource metrics | unavailable: {resources.get('reason', 'unknown')} |"
        )
    rows.append(f"| Errors raised | {len(errors)} |")
    lines += rows + [""]

    # Per-page timings isolate execution from theme rendering, so they say more
    # about the cookbook than the whole-command wall time does.
    pages = [
        p
        for p in ((execution or {}).get("page_seconds") or [])
        if p["page"].endswith(".ipynb")
    ]
    if pages:
        lines += ["| Notebook | Execute + render |", "|---|---|"]
        lines += [
            f"| [`{p['page']}`]({blob(record, p['page'])}) | {p['seconds']}s |"
            for p in pages
        ]
        lines.append("")

    notebooks = record.get("toc_notebooks") or []
    listed = (
        ", ".join(f"[`{n}`]({blob(record, n)})" for n in notebooks)
        if notebooks
        else "none"
    )
    lines.append(
        f"Executed {len(notebooks)} notebook(s) from the project toc: {listed}. "
        f"Notebooks not listed in [`myst.yml`]({blob(record, 'myst.yml')}) are never "
        "executed by a build, so a repo can carry notebooks no build ever touches."
    )
    lines.append("")

    if errors:
        lines += ["### Errors", ""]
        for error in errors:
            lines += [
                f"**`{error.get('ename')}`** — {error.get('evalue')}",
                "",
                f"in `{error.get('source')}`",
                "",
                "```",
                (error.get("traceback") or "")[:1200],
                "```",
                "",
            ]

    if build.get("failed") and build.get("log"):
        lines += ["### Build log (tail)", "", "```"]
        lines += [f"[{e['t']:>8.2f}s] {e['line']}" for e in build["log"][-25:]]
        lines += ["```", ""]

    return lines


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()

    latest = newest_per_cookbook()
    tiers = static_tiers()
    lines = [
        "# Live checks",
        "",
        "What happens when a cookbook is actually built and run on "
        "[Project Pythia's BinderHub](https://binder.projectpythia.org) — the environment its "
        "launch button sends learners to. Generated by `scripts/report_live.py`; do not edit.",
        "",
        "Read [the method and its limitations](../docs/live-assessment.md) before quoting any "
        "number here. In particular, a cached image makes build time meaningless, and a single "
        "failed run of a network-dependent notebook is a prompt to re-run rather than a finding.",
        "",
    ]

    if not latest:
        lines += ["No live checks recorded yet. Run `python scripts/live_check.py <cookbook>`.", ""]
    else:
        lines += summary_table(latest, tiers)
        for _, record in sorted(latest.items()):
            lines += describe(record[1], tiers)

    REPORTS.mkdir(parents=True, exist_ok=True)
    out = REPORTS / "live.md"
    out.write_text("\n".join(lines) + "\n")
    print(f"Wrote {out} ({len(latest)} cookbook(s))")


if __name__ == "__main__":
    main()
