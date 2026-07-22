#!/usr/bin/env python3
"""Turn live-check results into a readable report.

Reads the newest data/live/<cookbook>-<date>.json for each cookbook and writes:

    reports/live.md              a lean overview -- coverage, plus every
                                 live-checked cookbook in one table grouped by
                                 outcome, each row linking to its detail page.
    reports/live/<cookbook>.md   one detail page per cookbook: measures, notebook
                                 timings, errors, and the build log. The heavy
                                 content (tracebacks, logs) lives here so the
                                 overview stays scannable across all 68 cookbooks.

Like the static reports, this is generated output -- never hand-edit it. The
per-cookbook pages are auto-included in the site via a `pattern` in myst.yml, so
no toc edit is needed as more cookbooks are checked.

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
DETAIL = REPORTS / "live"

# Live outcomes ordered worst-first, the same convention as reports/by-tier.md:
# a learner is hurt most by a build that never starts, least by a clean run.
OUTCOME_ORDER = ["build failed", "execution failed", "ran with errors", "ran clean"]

OUTCOME_BLURB = {
    "build failed": "The Binder image would not build, so the launch button gives a "
    "learner nothing. The most direct failure there is.",
    "execution failed": "The build succeeded but `myst build --execute` itself did not "
    "complete -- a timeout, a dead kernel, or a crash rather than a cell error.",
    "ran with errors": "The book built and ran, but at least one notebook cell raised. "
    "Read the per-cookbook page before calling it a defect: a missing credential or an "
    "upstream outage looks identical to a broken cookbook.",
    "ran clean": "Built and ran with no cell errors on this sample. Not a verdict -- a "
    "cached image never re-solves the environment, and one green run of a "
    "network-dependent notebook is a sample, not a guarantee.",
}


def snapshot_context():
    """The static tiers and the count of real cookbooks, from the newest snapshot.

    Tiers let the overview flag disagreements: a cookbook the static checks call
    healthy that will not actually run, or one they call stale that runs fine.
    The count (excluding the not-a-cookbook tier) is the coverage denominator --
    how many cookbooks a full live sweep would eventually cover.
    """
    try:
        snapshot = json.loads(report.newest_snapshot().read_text())
    except (SystemExit, OSError, json.JSONDecodeError):
        return {}, None
    tiers = {b["name"]: report.tier(b) for b in snapshot["cookbooks"]}
    total = sum(1 for t in tiers.values() if t != "not-a-cookbook")
    return tiers, total


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


def dur(value):
    """A duration for reading: seconds under a minute, else 'Xm Ys'.

    Build and execution times run to hundreds or thousands of seconds, which are
    hard to read as a bare `1145.43s`. Keep sub-minute values in seconds so short
    runs stay precise, and switch to minutes and seconds above that.
    """
    if not isinstance(value, (int, float)):
        return "—"
    if value < 60:
        return f"{value:g}s"
    minutes, seconds = divmod(int(round(value)), 60)
    return f"{minutes}m {seconds:02d}s"


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


def memory_cell(record):
    """Peak memory against the pod limit, or an em dash."""
    resources = record.get("resources") or {}
    # pss where available -- rss double-counts shared pages (see detail_page()).
    peak = resources.get("peak_against_limit_bytes") or resources.get("peak_rss_bytes")
    limit = resources.get("memory_limit_bytes")
    return f"{peak / 1e9:.2f} of {limit / 1e9:.1f} GB" if peak and limit else "—"


def detail_slug(name):
    """The per-cookbook detail page, as a link relative to reports/live.md."""
    return f"live/{name}.md"


def coverage(latest, total):
    """A one-line coverage statement plus a rollup of outcomes."""
    checked = len(latest)
    outcomes = {}
    for _, record in latest.values():
        outcomes[verdict(record)] = outcomes.get(verdict(record), 0) + 1

    denom = f"{total} cookbooks" if total else "the collection"
    lines = [
        "## Coverage",
        "",
        f"**{checked} of {denom} live-checked.** Each run is manual and uses shared "
        "BinderHub capacity — one cookbook at a time, never a scheduled sweep "
        "([why](../docs/live-assessment.md#resource-etiquette)). Coverage grows as runs "
        "accumulate; the rest have not been checked yet.",
        "",
        "| Outcome | Cookbooks |",
        "|---|---|",
    ]
    for outcome in OUTCOME_ORDER:
        if outcomes.get(outcome):
            lines.append(f"| {outcome} | {outcomes[outcome]} |")
    if total and total > checked:
        lines.append(f"| not yet checked | {total - checked} |")
    lines.append("")
    return lines


def overview_table(latest, tiers):
    """Every live-checked cookbook in one table, grouped by outcome worst-first.

    Compact by design -- tracebacks and build logs live on the per-cookbook
    pages, so this stays scannable however many cookbooks are checked.
    """
    grouped = {}
    for name, (_, record) in latest.items():
        grouped.setdefault(verdict(record), []).append((name, record))

    lines = ["## Results", ""]
    for outcome in OUTCOME_ORDER:
        group = grouped.get(outcome)
        if not group:
            continue
        lines += [
            f"### {outcome} — {len(group)}",
            "",
            OUTCOME_BLURB[outcome],
            "",
            "| Cookbook | Static tier | Session | Execution | Peak memory | Errors | Checked |",
            "|---|---|---|---|---|---|---|",
        ]
        for name, record in sorted(group, key=lambda item: item[0].lower()):
            build = record.get("build") or {}
            execution = record.get("execution") or {}
            lines.append(
                f"| [{name}]({detail_slug(name)}) "
                f"| `{tiers.get(name, '—')}` "
                f"| {dur(build.get('seconds'))}"
                f"{' (cached)' if build.get('image_cached') else ''} "
                f"| {dur(execution.get('seconds'))} "
                f"| {memory_cell(record)} "
                f"| {len(record.get('errors') or [])} "
                f"| {record.get('started_at', '')[:10]} |"
            )
        lines.append("")

    lines += [
        "Where the live outcome and the static tier disagree, the live result is the more "
        "direct evidence — but read it as one sample of a network-dependent workflow, not a "
        "verdict. See [the limitations](../docs/live-assessment.md#limitations).",
        "",
    ]
    return lines


def detail_page(record, tiers):
    """One cookbook's full result as a standalone page.

    Everything heavy -- the measures table, per-notebook timings, error
    tracebacks, and the build log -- lives here rather than on the overview, so
    the overview scales to the whole collection.
    """
    build = record.get("build") or {}
    execution = record.get("execution")
    resources = record.get("resources") or {}
    errors = record.get("errors") or []

    repo = f"https://github.com/ProjectPythia/{record['cookbook']}"
    lines = [
        f"# {record['cookbook']}",
        "",
        f"Live outcome: **{verdict(record)}**. "
        "[← All live checks](../live.md) · "
        f"[Repository]({repo})",
        "",
    ]
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
            f"BinderHub reused an existing image, so the {dur(build.get('seconds'))} "
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
        f"| Time to a ready session | {dur(build.get('seconds'))}"
        f"{' (cached image)' if build.get('image_cached') else ' (fresh build)'} |",
        f"| Build succeeded | {'no' if build.get('failed') else 'yes'} |",
    ]
    if execution:
        # `myst build --execute` exits 0 even when cells raise, so the exit code
        # alone would call a run with ten tracebacks a success. Report both.
        clean = not execution.get("failed") and not errors
        rows += [
            f"| Notebook execution | {dur(execution.get('seconds'))} |",
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
            f"| [`{p['page']}`]({blob(record, p['page'])}) | {dur(p['seconds'])} |"
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


def clear_detail_pages():
    """Wipe reports/live/*.md before regenerating.

    The detail pages are generated, so a cookbook dropped from data/live/ must
    not leave a stale page behind for the toc pattern to keep publishing.
    """
    if DETAIL.exists():
        for path in DETAIL.glob("*.md"):
            path.unlink()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()

    latest = newest_per_cookbook()
    tiers, total = snapshot_context()
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
        "Each row links to that cookbook's own page, where its measures, notebook timings, "
        "errors, and build log live.",
        "",
    ]

    REPORTS.mkdir(parents=True, exist_ok=True)
    clear_detail_pages()

    if not latest:
        lines += ["No live checks recorded yet. Run `python scripts/live_check.py <cookbook>`.", ""]
    else:
        lines += coverage(latest, total)
        lines += overview_table(latest, tiers)

        DETAIL.mkdir(parents=True, exist_ok=True)
        for name, (_, record) in latest.items():
            page = "\n".join(detail_page(record, tiers)) + "\n"
            (DETAIL / f"{name}.md").write_text(page)

    out = REPORTS / "live.md"
    out.write_text("\n".join(lines) + "\n")
    print(f"Wrote {out} and {len(latest)} detail page(s) in {DETAIL}")


if __name__ == "__main__":
    main()
