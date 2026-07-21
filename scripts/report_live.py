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

ROOT = pathlib.Path(__file__).resolve().parent.parent
LIVE = ROOT / "data" / "live"
REPORTS = ROOT / "reports"


def newest_per_cookbook():
    """The most recent run for each cookbook, by filename date."""
    latest = {}
    for path in sorted(LIVE.glob("*.json")):
        try:
            record = json.loads(path.read_text())
        except (json.JSONDecodeError, OSError):
            continue
        latest[record["cookbook"]] = (path, record)
    return latest


def gb(value):
    return f"{value / 1e9:.2f} GB" if isinstance(value, (int, float)) else "—"


def describe(record):
    """One cookbook's result as markdown lines."""
    build = record.get("build") or {}
    execution = record.get("execution")
    resources = record.get("resources") or {}
    errors = record.get("errors") or []

    lines = [f"## {record['cookbook']}", ""]
    lines.append(
        f"Run {record['started_at'][:19].replace('T', ' ')} UTC "
        f"against [{record['hub']}]({record['hub']}), ref `{record['ref']}`."
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

    rows = [
        "| Measure | Value |",
        "|---|---|",
        f"| Time to a ready session | {build.get('seconds')}s"
        f"{' (cached image)' if build.get('image_cached') else ' (fresh build)'} |",
        f"| Build succeeded | {'no' if build.get('failed') else 'yes'} |",
    ]
    if execution:
        rows += [
            f"| Notebook execution | {execution.get('seconds')}s |",
            f"| Execution succeeded | {'no' if execution.get('failed') else 'yes'} |",
        ]
        if not execution.get("cache_cleared", True):
            rows.append("| Execution cache | **reused — timing is not execution** |")
    if resources.get("available"):
        rows += [
            f"| Peak memory (rss) | {gb(resources.get('peak_rss_bytes'))} |",
            f"| Pod memory limit | {gb(resources.get('memory_limit_bytes'))} |",
        ]
        fraction = resources.get("peak_fraction_of_limit")
        if fraction is not None:
            rows.append(f"| Peak as share of limit | {fraction:.1%} |")
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
        lines += [f"| `{p['page']}` | {p['seconds']}s |" for p in pages]
        lines.append("")

    notebooks = record.get("toc_notebooks") or []
    lines.append(
        f"Executed {len(notebooks)} notebook(s) from the project toc: "
        + (", ".join(f"`{n}`" for n in notebooks) if notebooks else "none")
        + ". Notebooks not listed in `myst.yml` are never executed by a build."
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
        for _, record in sorted(latest.items()):
            lines += describe(record[1])

    REPORTS.mkdir(parents=True, exist_ok=True)
    out = REPORTS / "live.md"
    out.write_text("\n".join(lines) + "\n")
    print(f"Wrote {out} ({len(latest)} cookbook(s))")


if __name__ == "__main__":
    main()
