#!/usr/bin/env python3
"""Render the GitHub Pages summary from the newest snapshot.

site/template.html holds the page; this fills in the numbers so the published
summary can never drift from the data. Edit the template, never site/index.html.

Usage:
    python scripts/build_site.py
    python scripts/build_site.py --repo https://github.com/<user>/<repo>
"""

import argparse
import html
import json
import pathlib
import subprocess

import report

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
NOTES = ROOT / "notes"

DEFAULT_REPO = "https://github.com/jmunroe/pythia-cookbook-review"

TIER_LABEL = {
    "stale": "published, stopped deploying",
    "degraded": "published, but slipping",
    "abandoned": "real content, quiet over a year",
    "incubating": "real content, not yet published",
    "healthy": "working and citable",
    "not-a-cookbook": "scaffold, sandbox, or archived",
}


def git_remote():
    """The origin remote as a browsable https URL, or None."""
    result = subprocess.run(
        ["git", "-C", str(ROOT), "remote", "get-url", "origin"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None
    url = result.stdout.strip()
    if url.startswith("git@github.com:"):
        url = "https://github.com/" + url[len("git@github.com:") :]
    return url.removesuffix(".git") or None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot", type=pathlib.Path)
    parser.add_argument("--repo", help="repo URL to link back to")
    args = parser.parse_args()

    path = args.snapshot or report.newest_snapshot()
    data = json.loads(path.read_text())
    books = data["cookbooks"]
    for book in books:
        book["_tier"] = report.tier(book)

    counts = {t: sum(1 for b in books if b["_tier"] == t) for t in report.TIER_ORDER}
    live = [b for b in books if b["_tier"] != "not-a-cookbook"]
    gallery = [b for b in live if b["discoverability"]["in_gallery"]]

    tier_rows = "\n".join(
        f'  <li class="t-{t}"><span class="n">{counts[t]}</span>'
        f'<span class="name">{t}</span>'
        f'<span class="what">{html.escape(TIER_LABEL[t])}</span></li>'
        for t in report.TIER_ORDER
        if counts[t]
    )

    def share(predicate, population, label):
        n = sum(1 for b in population if predicate(b))
        return f"    <tr><td>{label}</td><td>{n} of {len(population)}</td></tr>"

    gap_rows = "\n".join(
        [
            share(
                lambda b: b["build"]["days_since_deploy"] is None
                or b["build"]["days_since_deploy"] > 30,
                gallery,
                "Published cookbooks that have stopped deploying",
            ),
            share(
                lambda b: b["build"]["nightly_conclusion"] != "success",
                live,
                "Cookbooks with a failing or absent nightly build",
            ),
            share(
                lambda b: b["environment"]["pinned_count"]
                and not b["environment"]["has_comments"],
                live,
                "Cookbooks with undocumented version pins",
            ),
            share(
                lambda b: b["environment"]["pip_dep_count"] > 0,
                live,
                "Cookbooks pulling dependencies from pip rather than conda-forge",
            ),
            share(
                lambda b: not b["metadata"]["has_doi"],
                gallery,
                "Published cookbooks without a Zenodo DOI",
            ),
            share(
                lambda b: bool(b["maintenance"]["sphinx_leftovers"]),
                live,
                "Repositories still carrying pre-MyST Sphinx config",
            ),
            share(
                lambda b: b["maintenance"]["template_links"],
                live,
                "Repositories still linking back to the cookbook template",
            ),
        ]
    )

    repo = args.repo or git_remote() or DEFAULT_REPO
    reviewed = len([p for p in NOTES.glob("*.md") if not p.name.startswith("_")])

    rendered = (SITE / "template.html").read_text()
    for key, value in {
        "DATE": path.stem.replace("snapshot-", ""),
        "SNAPSHOT": path.name,
        "TOTAL": len(books),
        "GALLERY": len(gallery),
        "NEEDS_ATTENTION": counts["stale"] + counts["degraded"],
        "REVIEWED": reviewed,
        "TIER_ROWS": tier_rows,
        "GAP_ROWS": gap_rows,
        "REPO": repo,
        "REPO_SHORT": repo.replace("https://github.com/", ""),
    }.items():
        rendered = rendered.replace("{{" + key + "}}", str(value))

    out = SITE / "index.html"
    out.write_text(rendered)
    print(f"Wrote {out} from {path.name}")


if __name__ == "__main__":
    main()
