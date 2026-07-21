#!/usr/bin/env python3
"""Render index.md, the landing page of the MyST site, from the newest snapshot.

scripts/templates/index.md holds the prose; this fills in the numbers so the
published summary can never drift from the data. Edit the template, never the
generated index.md.

The rest of the site is the repo's own markdown -- myst.yml pulls reports/ and
docs/ straight into the table of contents, so those render as HTML without any
transformation step.

Usage:
    python scripts/build_site.py
    myst build --html          # then build the site itself
"""

import argparse
import json
import pathlib

import report

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "scripts" / "templates" / "index.md"
OUT = ROOT / "index.md"
NOTES = ROOT / "notes"

TIER_LABEL = {
    "stale": "Published, but the book has stopped deploying",
    "degraded": "Published but slipping: failing CI, lagging deploy, or thin citation metadata",
    "abandoned": "Real content, never published, quiet for over a year",
    "incubating": "Real content, not yet in the gallery, still active",
    "healthy": "Working and citable",
    "not-a-cookbook": "Scaffold, sandbox, or archived",
}


def tier_table(counts):
    """Tier counts as a markdown table, ordered worst-first like the reports."""
    rows = [
        "| Tier | Count | Meaning |",
        "|---|---|---|",
    ]
    rows += [
        f"| [`{t}`](docs/rubric.md) | {counts[t]} | {TIER_LABEL[t]} |"
        for t in report.TIER_ORDER
        if counts[t]
    ]
    return "\n".join(rows)


def gap_table(live, gallery):
    """Headline cross-cutting findings, with their denominators."""

    def share(label, predicate, population):
        n = sum(1 for b in population if predicate(b))
        return f"| {label} | {n} of {len(population)} |"

    rows = [
        "| Finding | Count |",
        "|---|---|",
        share(
            "Published cookbooks that have stopped deploying",
            # A deploy age of 0 is falsy -- test for None explicitly.
            lambda b: b["build"]["days_since_deploy"] is None
            or b["build"]["days_since_deploy"] > 30,
            gallery,
        ),
        share(
            "Cookbooks with a failing or absent nightly build",
            lambda b: b["build"]["nightly_conclusion"] != "success",
            live,
        ),
        share(
            "Cookbooks with undocumented version pins",
            lambda b: b["environment"]["pinned_count"]
            and not b["environment"]["has_comments"],
            live,
        ),
        share(
            "Cookbooks pulling dependencies from pip rather than conda-forge",
            lambda b: b["environment"]["pip_dep_count"] > 0,
            live,
        ),
        share(
            "Published cookbooks without a Zenodo DOI",
            lambda b: not b["metadata"]["has_doi"],
            gallery,
        ),
        share(
            "Repositories still carrying pre-MyST Sphinx config",
            lambda b: bool(b["maintenance"]["sphinx_leftovers"]),
            live,
        ),
        share(
            "Repositories still linking back to the cookbook template",
            lambda b: b["maintenance"]["template_links"],
            live,
        ),
    ]
    return "\n".join(rows)


def ci_counts():
    """Headline numbers from the newest green-nightly-with-errors scan."""
    scans = sorted((ROOT / "data").glob("ci-errors-*.json"))
    if not scans:
        return {"CI_AFFECTED": 0, "CI_SCANNED": 0}
    data = json.loads(scans[-1].read_text())
    return {
        "CI_AFFECTED": data.get("green_with_errors", 0),
        "CI_SCANNED": data.get("scanned", 0),
    }


def live_summary():
    """One line per cookbook that has been live-checked, or a placeholder."""
    live = ROOT / "data" / "live"
    latest = {}
    for path in sorted(live.glob("*.json")):
        try:
            record = json.loads(path.read_text())
        except (json.JSONDecodeError, OSError):
            continue
        previous = latest.get(record["cookbook"])
        if previous is None or record.get("started_at", "") >= previous.get(
            "started_at", ""
        ):
            latest[record["cookbook"]] = record

    if not latest:
        return "*No cookbooks have been live-checked yet.*"

    rows = ["| Cookbook | Session | Execution | Peak memory | Errors |", "|---|---|---|---|---|"]
    for name, record in sorted(latest.items()):
        build = record.get("build") or {}
        execution = record.get("execution") or {}
        resources = record.get("resources") or {}
        # pss where available -- rss double-counts pages shared between the
        # server and its kernels, and can read above a limit never breached.
        peak = resources.get("peak_against_limit_bytes") or resources.get("peak_rss_bytes")
        limit = resources.get("memory_limit_bytes")
        memory = (
            f"{peak / 1e9:.2f} of {limit / 1e9:.1f} GB" if peak and limit else "—"
        )
        rows.append(
            f"| {name} "
            f"| {build.get('seconds')}s"
            f"{' (cached)' if build.get('image_cached') else ''} "
            f"| {execution.get('seconds', '—')}s "
            f"| {memory} "
            f"| {len(record.get('errors') or [])} |"
        )
    return "\n".join(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot", type=pathlib.Path)
    args = parser.parse_args()

    path = args.snapshot or report.newest_snapshot()
    books = json.loads(path.read_text())["cookbooks"]
    for book in books:
        book["_tier"] = report.tier(book)

    counts = {t: sum(1 for b in books if b["_tier"] == t) for t in report.TIER_ORDER}
    live = [b for b in books if b["_tier"] != "not-a-cookbook"]
    gallery = [b for b in live if b["discoverability"]["in_gallery"]]
    reviewed = len([p for p in NOTES.glob("*.md") if not p.name.startswith("_")])

    rendered = TEMPLATE.read_text()
    for key, value in {
        "DATE": path.stem.replace("snapshot-", ""),
        "SNAPSHOT": path.name,
        "TOTAL": len(books),
        "GALLERY": len(gallery),
        "NEEDS_ATTENTION": counts["stale"] + counts["degraded"],
        "REVIEWED": reviewed,
        "TIER_TABLE": tier_table(counts),
        "GAP_TABLE": gap_table(live, gallery),
        "LIVE_SUMMARY": live_summary(),
        **ci_counts(),
        # Must sit below the frontmatter -- MyST needs that block at the very
        # top of the file.
        "GENERATED_NOTE": (
            f"<!-- Generated by scripts/build_site.py from data/{path.name}."
            " Edit scripts/templates/index.md instead. -->"
        ),
    }.items():
        rendered = rendered.replace("{{" + key + "}}", str(value))

    OUT.write_text(rendered)
    print(f"Wrote {OUT} from {path.name}")


if __name__ == "__main__":
    main()
