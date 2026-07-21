#!/usr/bin/env python3
"""Collect status metrics for every Project Pythia cookbook.

Writes data/snapshot-YYYY-MM-DD.json: one record per cookbook repo, holding the
raw checkable facts defined in docs/rubric.md. This script only *collects* --
tiering and presentation live in report.py, so a snapshot stays useful even when
the rubric changes.

The file-probe approach (fetch raw.githubusercontent, tolerate every failure,
fan out with a thread pool) follows cookbook-gallery/src/pythia_gallery.py, the
collector that builds the live gallery. A missing file is a data point here,
never an exception.

Usage:
    python scripts/audit.py                 # full org
    python scripts/audit.py --limit 5       # sample, for development
    python scripts/audit.py --no-cache      # ignore data/_cache/
"""

import argparse
import concurrent.futures
import datetime
import hashlib
import json
import pathlib
import re
import subprocess
import sys
import urllib.error
import urllib.request

import yaml

SCRIPT_VERSION = "1.0"
ORG = "projectpythia"

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
CACHE = DATA / "_cache"

GALLERY_LIST_URL = (
    f"https://raw.githubusercontent.com/{ORG}/cookbook-gallery/main/cookbook_gallery.txt"
)

# Infrastructure, not cookbooks: they match the name filter but have no content
# to assess.
EXCLUDE = {
    "cookbook",
    "cookbook-actions",
    "cookbook-gallery",
    "cookbook-gallery-sphinx",
    "cookbook-template",
    "cookbook-template-deploy-test",
}

# Real cookbooks whose names don't match the *-cookbook pattern, so repo
# discovery would miss them. Add to this as they turn up -- see
# docs/methodology.md on name filtering.
EXTRA_REPOS = [
    "AtmosCol-2023",
    "cacti-deep-convection",
    "ml-hurricane-intensity",
    "thermodynamic-budgets",
]

# Files we fetch whole, to inspect their contents.
PROBE_FILES = [
    "myst.yml",
    "CITATION.cff",
    "_gallery_info.yml",
    "environment.yml",
    "README.md",
    "_config.yml",  # Sphinx leftover: never migrated to MyST
    "_toc.yml",  # ditto
]

# Placeholder values straight out of cookbook-template. Finding these means the
# author never filled the template in.
TEMPLATE_TITLE = "Project Pythia Cookbook Template"
TEMPLATE_ABSTRACT = "A sample cookbook description."
TEMPLATE_TAGS = {"sampledomain", "samplepackage"}

# Zenodo archiving shows up in three forms in practice: the resolved DOI, a
# doi.org link, or -- most commonly -- the badge, whose URL carries the GitHub
# repo id rather than the DOI itself. All three mean "archiving is wired up",
# which is what the criterion actually asks. See docs/methodology.md.
DOI_RE = re.compile(
    r"10\.5281/zenodo\.\d+|doi\.org/10\.\d+|zenodo\.org/(badge|record|doi)", re.I
)

use_cache = True


# --------------------------------------------------------------------------
# Fetching
# --------------------------------------------------------------------------


def cached(key, produce):
    """Memoize produce() on disk under data/_cache/, keyed by `key`.

    Keeps script iteration cheap: a full org pass is ~700 requests. `None`
    results are cached too -- "this file does not exist" is worth remembering.
    """
    if not use_cache:
        return produce()
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / (hashlib.sha256(key.encode()).hexdigest()[:32] + ".json")
    if path.is_file():
        return json.loads(path.read_text())["value"]
    value = produce()
    path.write_text(json.dumps({"key": key, "value": value}))
    return value


def fetch_text(url):
    """URL body as text, or None if it doesn't exist / can't be reached."""

    def produce():
        try:
            with urllib.request.urlopen(url, timeout=30) as response:
                return response.read().decode()
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError):
            return None

    return cached(f"GET {url}", produce)


def url_ok(url):
    """True if a HEAD/GET on `url` succeeds -- used for the live-site check."""

    def produce():
        request = urllib.request.Request(url, method="HEAD")
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return 200 <= response.status < 300
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError):
            return False

    return cached(f"HEAD {url}", produce)


def gh_api(path):
    """`gh api <path>` parsed as JSON, or None on any failure.

    A 404 is normal and expected here: no gh-pages branch, no releases, no
    nightly workflow are all things we're specifically looking for.
    """

    def produce():
        result = subprocess.run(
            ["gh", "api", path],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            return None
        try:
            return json.loads(result.stdout)
        except json.JSONDecodeError:
            return None

    return cached(f"gh api {path}", produce)


def parse_yaml(text):
    """Parse YAML text, or None if it's absent or malformed."""
    if not text:
        return None
    try:
        return yaml.safe_load(text)
    except yaml.YAMLError:
        return None


# --------------------------------------------------------------------------
# Discovery
# --------------------------------------------------------------------------


def list_org_repos():
    """Every repo in the org, with the metadata `gh repo list` gives us free."""
    result = subprocess.run(
        [
            "gh",
            "repo",
            "list",
            ORG,
            "--limit",
            "500",
            "--json",
            "name,description,isArchived,pushedAt,defaultBranchRef,"
            "stargazerCount,licenseInfo,repositoryTopics",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    return json.loads(result.stdout)


def is_cookbook_repo(name):
    lower = name.lower()
    if name in EXCLUDE:
        return False
    if name in EXTRA_REPOS:
        return True
    return lower.endswith("-cookbook") or lower.startswith("cookbook-")


def gallery_names():
    """Repo names listed in cookbook_gallery.txt -- the published set."""
    text = fetch_text(GALLERY_LIST_URL)
    if not text:
        print("WARNING: could not fetch cookbook_gallery.txt", file=sys.stderr)
        return set()
    return {line.strip() for line in text.splitlines() if line.strip()}


# --------------------------------------------------------------------------
# Per-repo checks
# --------------------------------------------------------------------------


def days_since(timestamp):
    """Whole days between an ISO timestamp and today, or None."""
    if not timestamp:
        return None
    try:
        when = datetime.datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    except ValueError:
        return None
    now = datetime.datetime.now(datetime.timezone.utc)
    return (now - when).days


def check_discoverability(name, in_gallery, files, tree_paths):
    gallery_info = parse_yaml(files.get("_gallery_info.yml"))
    tags = (gallery_info or {}).get("tags") or {}
    tag_values = {str(v) for group in tags.values() if group for v in group}
    thumbnail = (gallery_info or {}).get("thumbnail")
    return {
        "in_gallery": in_gallery,
        "site_live": url_ok(f"https://projectpythia.org/{name}") if in_gallery else None,
        "has_gallery_info": gallery_info is not None,
        "has_thumbnail": bool(thumbnail) and thumbnail in tree_paths,
        "has_real_tags": bool(tag_values) and not tag_values & TEMPLATE_TAGS,
        "tags": {k: v for k, v in tags.items() if v},
    }


def check_build_health(name, tree_paths):
    """Nightly build state and deploy freshness.

    We read the Actions API rather than the badge SVG, because a disabled
    workflow serves a passing badge forever (see docs/methodology.md). The
    deploy date is the check that actually catches that case.
    """
    has_nightly = ".github/workflows/nightly-build.yaml" in tree_paths
    nightly_body = (
        fetch_text(
            f"https://raw.githubusercontent.com/{ORG}/{name}/HEAD"
            "/.github/workflows/nightly-build.yaml"
        )
        if has_nightly
        else None
    )

    runs = gh_api(
        f"repos/{ORG}/{name}/actions/workflows/nightly-build.yaml/runs?per_page=1"
    )
    latest = (runs or {}).get("workflow_runs") or []
    latest = latest[0] if latest else {}

    pages = gh_api(f"repos/{ORG}/{name}/branches/gh-pages")
    deployed_at = (
        ((pages or {}).get("commit") or {}).get("commit", {}).get("committer", {}).get("date")
    )

    return {
        "has_nightly": has_nightly,
        "uses_cookbook_actions": bool(nightly_body and "cookbook-actions" in nightly_body),
        "nightly_conclusion": latest.get("conclusion"),
        "nightly_run_at": latest.get("run_started_at"),
        "has_link_check": ".github/workflows/trigger-link-check.yaml" in tree_paths,
        "workflows": sorted(
            p.split("/")[-1] for p in tree_paths if p.startswith(".github/workflows/")
        ),
        "deployed_at": deployed_at,
        "days_since_deploy": days_since(deployed_at),
    }


def check_metadata(name, files, tree_paths):
    myst = parse_yaml(files.get("myst.yml")) or {}
    project = myst.get("project") or {}
    extends = myst.get("extends") or []
    if isinstance(extends, str):
        extends = [extends]
    citation = parse_yaml(files.get("CITATION.cff")) or {}
    authors = citation.get("authors") or []

    title = project.get("title")
    abstract = citation.get("abstract")
    doi_haystack = (files.get("README.md") or "") + (files.get("CITATION.cff") or "")
    release = gh_api(f"repos/{ORG}/{name}/releases/latest")

    return {
        "myst_extends_config": any("pythia-config" in str(e) for e in extends),
        "title": title,
        "has_real_title": bool(title) and title != TEMPLATE_TITLE,
        "has_citation": bool(citation),
        "abstract": abstract,
        "has_real_abstract": bool(abstract) and abstract != TEMPLATE_ABSTRACT,
        "has_orcid": any(a.get("orcid") for a in authors if isinstance(a, dict)),
        "author_count": len(authors),
        "has_doi": bool(DOI_RE.search(doi_haystack)),
        "has_release": bool(release and release.get("tag_name")),
        "latest_release": (release or {}).get("tag_name"),
        "has_license": "LICENSE" in tree_paths,
    }


def check_environment(files):
    """The environment.yml checks the community meeting called out (2026-07-21).

    Note the direction of the pinning check: the community asks authors to
    *avoid* pins except where needed and to document the reason. So pins are the
    thing to flag, not their absence -- an over-pinned cookbook rots as the
    ecosystem moves. See docs/criteria.md.
    """
    environment = parse_yaml(files.get("environment.yml")) or {}
    raw = files.get("environment.yml") or ""
    deps = environment.get("dependencies") or []

    conda_deps = [d for d in deps if isinstance(d, str)]
    # pip deps appear as a trailing {"pip": [...]} mapping in the dependency list.
    pip_deps = [
        item
        for d in deps
        if isinstance(d, dict)
        for item in (d.get("pip") or [])
    ]
    pinned = [d for d in conda_deps if re.search(r"[=<>~!]", d)]
    channels = environment.get("channels") or []

    return {
        "has_environment": bool(environment),
        "channels": channels,
        "uses_conda_forge": any("conda-forge" in str(c) for c in channels),
        # pip is permitted, but conda-forge is preferred wherever possible --
        # a long pip list is worth a human look, not an automatic failure.
        "conda_dep_count": len(conda_deps),
        "pip_dep_count": len(pip_deps),
        "pip_deps": pip_deps,
        "pinned_deps": pinned,
        "pinned_count": len(pinned),
        # Any comment in the file is weak evidence that pins were explained.
        # A human confirms whether the explanation is real.
        "has_comments": any(line.lstrip().startswith("#") for line in raw.splitlines()),
    }


def check_maintenance(repo, files, tree_paths):
    notebooks = [
        p for p in tree_paths if p.endswith(".ipynb") and not p.startswith(".")
    ]
    readme = files.get("README.md") or ""
    myst_raw = files.get("myst.yml") or ""

    return {
        "days_since_push": days_since(repo.get("pushedAt")),
        "pushed_at": repo.get("pushedAt"),
        "open_issues": repo.get("_open_issues"),
        "open_prs": repo.get("_open_prs"),
        "notebook_count": len(notebooks),
        "notebooks": sorted(notebooks),
        "sphinx_leftovers": sorted(
            f for f in ("_config.yml", "_toc.yml") if files.get(f)
        ),
        # trigger-replace-links was never run: the cookbook still points at the
        # template it was cut from.
        "template_links": "cookbook-template" in readme or "cookbook-template" in myst_raw,
        "template_only": notebooks == ["notebooks/notebook-template.ipynb"],
    }


def collect(repo, in_gallery):
    """Every metric for one repo. Never raises -- failures become nulls."""
    name = repo["name"]
    branch = (repo.get("defaultBranchRef") or {}).get("name") or "main"
    print(f"  {name}", file=sys.stderr, flush=True)

    tree = gh_api(f"repos/{ORG}/{name}/git/trees/{branch}?recursive=1") or {}
    tree_paths = {entry["path"] for entry in tree.get("tree", []) if "path" in entry}

    files = {
        probe: fetch_text(
            f"https://raw.githubusercontent.com/{ORG}/{name}/{branch}/{probe}"
        )
        for probe in PROBE_FILES
        if probe in tree_paths
    }

    issues = gh_api(f"repos/{ORG}/{name}") or {}
    prs = gh_api(f"repos/{ORG}/{name}/pulls?state=open&per_page=100") or []
    # GitHub's open_issues_count includes PRs; subtract them for a true count.
    repo = dict(repo)
    repo["_open_prs"] = len(prs)
    repo["_open_issues"] = max(0, (issues.get("open_issues_count") or 0) - len(prs))

    return {
        "name": name,
        "description": repo.get("description"),
        "archived": repo.get("isArchived", False),
        "default_branch": branch,
        "stars": repo.get("stargazerCount"),
        "tree_truncated": tree.get("truncated", False),
        "discoverability": check_discoverability(name, in_gallery, files, tree_paths),
        "build": check_build_health(name, tree_paths),
        "metadata": check_metadata(name, files, tree_paths),
        "environment": check_environment(files),
        "maintenance": check_maintenance(repo, files, tree_paths),
    }


# --------------------------------------------------------------------------


def main():
    global use_cache

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, help="only audit the first N repos")
    parser.add_argument("--no-cache", action="store_true", help="ignore data/_cache/")
    parser.add_argument("--out", type=pathlib.Path, help="override the output path")
    args = parser.parse_args()
    use_cache = not args.no_cache

    print("Listing org repos...", file=sys.stderr)
    repos = [r for r in list_org_repos() if is_cookbook_repo(r["name"])]
    repos.sort(key=lambda r: r["name"].lower())
    if args.limit:
        repos = repos[: args.limit]

    gallery = gallery_names()
    print(f"Auditing {len(repos)} repos ({len(gallery)} in gallery)...", file=sys.stderr)

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        records = list(
            pool.map(lambda r: collect(r, r["name"] in gallery), repos)
        )

    missing = sorted(gallery - {r["name"] for r in records})
    if missing:
        print(
            f"WARNING: in gallery but not audited: {', '.join(missing)}",
            file=sys.stderr,
        )

    today = datetime.date.today().isoformat()
    snapshot = {
        "collected_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "script_version": SCRIPT_VERSION,
        "org": ORG,
        "gallery_count": len(gallery),
        "gallery_not_audited": missing,
        "cookbooks": records,
    }

    out = args.out or DATA / f"snapshot-{today}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(snapshot, indent=2) + "\n")
    print(f"Wrote {out} ({len(records)} cookbooks)", file=sys.stderr)


if __name__ == "__main__":
    main()
