#!/usr/bin/env python3
"""Turn a snapshot into readable reports.

Reads the newest data/snapshot-*.json and regenerates:

    reports/dashboard.md   every cookbook, one row each
    reports/by-tier.md     grouped, with the specific failing checks spelled out
    reports/gaps.md        cross-cutting findings across the collection

Everything here is derived. Snapshots are the durable artifact; these files are
overwritten on every run, so never hand-edit them (see docs/workflow.md).

Usage:
    python scripts/report.py
    python scripts/report.py --snapshot data/snapshot-2026-07-21.json
"""

import argparse
import datetime
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
REPORTS = ROOT / "reports"
NOTES = ROOT / "notes"

# Ordered by how much a learner is hurt by the problem -- see docs/workflow.md.
TIER_ORDER = ["stale", "degraded", "abandoned", "incubating", "healthy", "not-a-cookbook"]

TIER_BLURB = {
    "stale": "Published, but the book has stopped deploying. A learner arriving from the "
    "gallery today may get dead or ancient content. Fix these first.",
    "degraded": "Published but slipping: failing CI, a lagging deploy, or incomplete "
    "citation metadata. Highest-value place to spend effort.",
    "abandoned": "Real work, never published, and quiet for over a year. Revive, hand off, "
    "or archive honestly.",
    "incubating": "Real work, not yet in the gallery, still active. Does it need an advocate "
    "to reach publication?",
    "healthy": "Working and citable. Sample a few to keep the harness honest; otherwise "
    "leave alone.",
    "not-a-cookbook": "Scaffold, sandbox, or archived. Listed so the counts reconcile.",
}


def newest_snapshot():
    snapshots = sorted(DATA.glob("snapshot-*.json"))
    if not snapshots:
        raise SystemExit("No snapshots in data/. Run scripts/audit.py first.")
    return snapshots[-1]


def tier(book):
    """Assign a health tier. A hypothesis -- a note file may override it.

    Deliberately does NOT consider size or completeness: the community's rule of
    thumb is that a cookbook needs to be useful, not finished.
    """
    disc, build, meta, maint = (
        book["discoverability"],
        book["build"],
        book["metadata"],
        book["maintenance"],
    )

    if book["archived"] or maint["notebook_count"] == 0 or maint["template_only"]:
        return "not-a-cookbook"

    deploy_age = build["days_since_deploy"]

    if disc["in_gallery"]:
        if deploy_age is None or deploy_age > 30:
            return "stale"
        citable = meta["has_doi"] and meta["has_real_abstract"] and meta["has_citation"]
        if build["nightly_conclusion"] != "success" or deploy_age > 7 or not citable:
            return "degraded"
        return "healthy"

    push_age = maint["days_since_push"]
    if push_age is not None and push_age > 365:
        return "abandoned"
    return "incubating"


def failures(book):
    """Human-readable list of what this cookbook fails, worst first."""
    disc, build, meta, env, maint = (
        book["discoverability"],
        book["build"],
        book["metadata"],
        book["environment"],
        book["maintenance"],
    )
    out = []

    age = build["days_since_deploy"]
    if age is None:
        out.append("never deployed (no gh-pages branch)")
    elif age > 30:
        out.append(f"no deploy in {age} days")
    elif age > 7:
        out.append(f"last deploy {age} days ago")

    if not build["has_nightly"]:
        out.append("no nightly-build workflow")
    elif build["nightly_conclusion"] != "success":
        out.append(f"nightly build: {build['nightly_conclusion'] or 'never run'}")
    if build["has_nightly"] and not build["uses_cookbook_actions"]:
        out.append("nightly does not use cookbook-actions")
    if not build["has_link_check"]:
        out.append("no link-check workflow")

    if not meta["has_doi"]:
        out.append("no Zenodo DOI")
    if not meta["has_release"]:
        out.append("no tagged release")
    if not meta["has_citation"]:
        out.append("no CITATION.cff")
    elif not meta["has_real_abstract"]:
        out.append("placeholder/missing abstract")
    if meta["has_citation"] and not meta["has_orcid"]:
        out.append("no author ORCID")
    if not meta["has_license"]:
        out.append("no LICENSE")
    if not meta["has_real_title"]:
        out.append("placeholder/missing title in myst.yml")
    if not meta["myst_extends_config"]:
        out.append("myst.yml does not extend pythia-config")

    if not env["has_environment"]:
        out.append("no environment.yml")
    else:
        if not env["uses_conda_forge"]:
            out.append("conda-forge not a declared channel")
        if env["pip_dep_count"]:
            out.append(f"{env['pip_dep_count']} pip dep(s) — prefer conda-forge")
        if env["pinned_count"] and not env["has_comments"]:
            out.append(f"{env['pinned_count']} version pin(s), undocumented")
        if env.get("sphinx_deps"):
            out.append(
                f"{len(env['sphinx_deps'])} Sphinx-era package(s) in environment.yml: "
                + ", ".join(f"`{d}`" for d in env["sphinx_deps"][:4])
                + (" …" if len(env["sphinx_deps"]) > 4 else "")
            )

    if disc["in_gallery"]:
        if not disc["has_gallery_info"]:
            out.append("no _gallery_info.yml")
        else:
            if not disc["has_thumbnail"]:
                out.append("thumbnail missing or unresolvable")
            if not disc["has_real_tags"]:
                out.append("placeholder/missing gallery tags")
        if disc["site_live"] is False:
            out.append("site not reachable at projectpythia.org")

    if maint["sphinx_leftovers"]:
        out.append(f"Sphinx leftovers: {', '.join(maint['sphinx_leftovers'])}")
    if maint["template_links"]:
        out.append("still links to cookbook-template (trigger-replace-links never run)")

    return out


def note_link(name):
    """Relative link to the human note for this cookbook, if one exists."""
    return f"[note](../notes/{name}.md)" if (NOTES / f"{name}.md").is_file() else ""


def yes(value):
    return {True: "yes", False: "no", None: "—"}.get(value, str(value))


def age_cell(days):
    return "never" if days is None else f"{days}d"


def write_dashboard(snapshot, books, out):
    lines = [
        "# Cookbook dashboard",
        "",
        f"Generated from `{snapshot.name}` "
        f"(collected {snapshot_date(snapshot)}). Do not edit — regenerate with "
        "`python scripts/report.py`.",
        "",
        f"{len(books)} cookbooks. Tiers are defined in [the rubric](../docs/rubric.md); "
        "the bar itself is [the community criteria](../docs/criteria.md).",
        "",
        "| Cookbook | Tier | Gallery | Nightly | Deploy | Push | DOI | Notebooks | Issues | Note |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for book in books:
        b, m, mt = book["build"], book["metadata"], book["maintenance"]
        lines.append(
            f"| [{book['name']}](https://github.com/ProjectPythia/{book['name']}) "
            f"| `{book['_tier']}` "
            f"| {yes(book['discoverability']['in_gallery'])} "
            f"| {b['nightly_conclusion'] or '—'} "
            f"| {age_cell(b['days_since_deploy'])} "
            f"| {age_cell(mt['days_since_push'])} "
            f"| {yes(m['has_doi'])} "
            f"| {mt['notebook_count']} "
            f"| {mt['open_issues'] if mt['open_issues'] is not None else '—'} "
            f"| {note_link(book['name'])} |"
        )
    out.write_text("\n".join(lines) + "\n")


def write_by_tier(snapshot, books, out):
    lines = [
        "# Cookbooks by tier",
        "",
        f"Generated from `{snapshot.name}` (collected {snapshot_date(snapshot)}). "
        "Do not edit — regenerate with `python scripts/report.py`.",
        "",
        "Each tier is a *hypothesis* from the automated checks. Confirm or override it in the "
        "cookbook's note file. Remember the community's rule of thumb: **a cookbook doesn't "
        "need to be finished, just useful** — incompleteness is not a defect here.",
        "",
    ]
    for name in TIER_ORDER:
        group = [b for b in books if b["_tier"] == name]
        if not group:
            continue
        lines += [f"## `{name}` — {len(group)}", "", TIER_BLURB[name], ""]
        for book in group:
            link = note_link(book["name"])
            heading = f"### {book['name']}" + (f" · {link}" if link else "")
            lines.append(heading)
            if book.get("description"):
                lines += ["", f"> {book['description']}"]
            problems = book["_failures"]
            lines.append("")
            if problems:
                lines += [f"- {p}" for p in problems]
            else:
                lines.append("- no automated findings")
            lines.append("")
    out.write_text("\n".join(lines) + "\n")


def write_gaps(snapshot, books, out):
    """Cross-cutting findings: patterns that span the collection."""
    live = [b for b in books if b["_tier"] != "not-a-cookbook"]
    gallery = [b for b in live if b["discoverability"]["in_gallery"]]

    def count(items, predicate):
        return sum(1 for i in items if predicate(i))

    findings = [
        (
            "Gallery cookbooks without a Zenodo DOI",
            count(gallery, lambda b: not b["metadata"]["has_doi"]),
            len(gallery),
            "The DOI is the last step of the publication checklist, and the community lists it "
            "as a basic criterion. Missing means the flow was never finished.",
        ),
        (
            "Gallery cookbooks with no tagged release",
            count(gallery, lambda b: not b["metadata"]["has_release"]),
            len(gallery),
            "The meeting suggests cutting a new release after review and revision.",
        ),
        (
            "Gallery cookbooks not deploying (>30d)",
            # NB: a deploy age of 0 is falsy -- test for None explicitly.
            count(
                gallery,
                lambda b: b["build"]["days_since_deploy"] is None
                or b["build"]["days_since_deploy"] > 30,
            ),
            len(gallery),
            "Published and quietly broken — the worst learner experience in the collection.",
        ),
        (
            "Cookbooks with a failing or absent nightly build",
            count(live, lambda b: b["build"]["nightly_conclusion"] != "success"),
            len(live),
            "Some are legitimately unable to run in CI (credentials, data volume). Those need a "
            "documented exemption, not a red mark.",
        ),
        (
            "Cookbooks with undocumented version pins",
            count(
                live,
                lambda b: b["environment"]["pinned_count"]
                and not b["environment"]["has_comments"],
            ),
            len(live),
            "The community asks authors to avoid pins except where needed, and to document why. "
            "Pins without explanation are the finding.",
        ),
        (
            "Cookbooks pulling deps from pip",
            count(live, lambda b: b["environment"]["pip_dep_count"] > 0),
            len(live),
            "conda-forge is preferred wherever possible; pip is a flag for human review, not an "
            "automatic failure.",
        ),
        (
            "Cookbooks with no environment.yml",
            count(live, lambda b: not b["environment"]["has_environment"]),
            len(live),
            "Nothing about the cookbook is reproducible without one.",
        ),
        (
            "Repos still carrying Sphinx config",
            count(live, lambda b: bool(b["maintenance"]["sphinx_leftovers"])),
            len(live),
            "`_config.yml`/`_toc.yml` means the MyST migration never reached this cookbook.",
        ),
        (
            "Cookbooks with Sphinx packages in environment.yml",
            count(live, lambda b: bool(b["environment"].get("sphinx_deps"))),
            len(live),
            "Cookbooks build with MyST now, so a Sphinx toolchain in the environment is dead "
            "weight from before the migration. It is rarely harmless: these entries are usually "
            "tightly pinned, and a live check found they can stop the Binder image building at "
            "all — see the live report.",
        ),
        (
            "Repos still linking to cookbook-template",
            count(live, lambda b: b["maintenance"]["template_links"]),
            len(live),
            "`trigger-replace-links` was never run — links point at the template, not the book.",
        ),
        (
            "Cookbooks with no author ORCID",
            count(live, lambda b: not b["metadata"]["has_orcid"]),
            len(live),
            "Author metadata is a basic publication criterion; ORCIDs make credit resolvable.",
        ),
    ]

    lines = [
        "# Cross-cutting gaps",
        "",
        f"Generated from `{snapshot.name}` (collected {snapshot_date(snapshot)}). "
        "Do not edit — regenerate with `python scripts/report.py`.",
        "",
        f"Denominators exclude the `not-a-cookbook` tier "
        f"({len(books) - len(live)} of {len(books)} repos).",
        "",
        "| Finding | Count | Of |",
        "|---|---|---|",
    ]
    lines += [f"| {title} | {n} | {total} |" for title, n, total, _ in findings]
    lines.append("")
    for title, n, total, why in findings:
        if n:
            lines += [f"## {title} — {n}/{total}", "", why, ""]
    out.write_text("\n".join(lines) + "\n")


def snapshot_date(path):
    return path.stem.replace("snapshot-", "")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot", type=pathlib.Path, help="snapshot to report on")
    args = parser.parse_args()

    path = args.snapshot or newest_snapshot()
    data = json.loads(path.read_text())
    books = data["cookbooks"]

    for book in books:
        book["_tier"] = tier(book)
        book["_failures"] = failures(book)

    books.sort(key=lambda b: (TIER_ORDER.index(b["_tier"]), b["name"].lower()))

    REPORTS.mkdir(parents=True, exist_ok=True)
    write_dashboard(path, books, REPORTS / "dashboard.md")
    write_by_tier(path, books, REPORTS / "by-tier.md")
    write_gaps(path, books, REPORTS / "gaps.md")

    counts = {t: sum(1 for b in books if b["_tier"] == t) for t in TIER_ORDER}
    print(f"Reported on {len(books)} cookbooks from {path.name}")
    for name, n in counts.items():
        if n:
            print(f"  {name:>15}: {n}")


if __name__ == "__main__":
    main()
