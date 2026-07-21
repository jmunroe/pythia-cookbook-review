# Methodology

Where each metric comes from, and — more importantly — where it lies.

## Data sources

Everything is collected from public sources, authenticated with `gh` so we get the 5000/hr rate
limit rather than 60/hr.

| Source | Used for |
|---|---|
| `gh repo list projectpythia` | repo discovery, archive flag, `pushedAt`, open-issue count |
| `gh api repos/…/git/trees/<branch>?recursive=1` | file inventory: workflows, notebooks, `LICENSE`, thumbnails |
| `raw.githubusercontent.com/projectpythia/<name>/<branch>/…` | file *contents*: `myst.yml`, `CITATION.cff`, `_gallery_info.yml`, `environment.yml`, `README.md` |
| `gh api repos/…/actions/workflows/nightly-build.yaml/runs` | latest nightly run conclusion + timestamp |
| `gh api repos/…/branches/gh-pages` | last successful deploy date |
| `gh api repos/…/releases/latest` | tagged release presence |
| `cookbook-gallery/cookbook_gallery.txt` | gallery membership |

The file-fetch approach is lifted from [`cookbook-gallery/src/pythia_gallery.py`][collector], which
does the same thing to build the live gallery. Its central discipline is worth restating: **a
missing or unparseable file is a data point, never an exception.** Every probe in `audit.py`
returns `None` on failure and records why.

[collector]: https://github.com/ProjectPythia/cookbook-gallery/blob/main/src/pythia_gallery.py

## Known false signals

These are the traps. Read them before drawing conclusions from a snapshot.

**A disabled workflow keeps serving a passing badge.** GitHub's `badge.svg` shows the last run's
result forever. A cookbook whose nightly was turned off in 2024 still renders ✅ today. This is
precisely why the upstream gallery cross-checks the `gh-pages` deploy date and overrides any badge
with "⚠️ no longer updating" when there has been no deploy in a week. We query the Actions API for
the real latest run instead of the badge, which gives us the *timestamp* too — but the same rule
applies: **trust the deploy date over the build status.**

**A green nightly does not even mean the notebooks ran.** This turned out to be far worse than
first written here. `myst build --execute` — the default build command in `cookbook-actions` —
**exits 0 when a cell raises**: the exception is captured into the page and the build carries on.
Scanning Pythia's own nightly logs found **12 of 30 gallery cookbooks with notebooks raising
exceptions in a run that reported success**, all of them published as passing. See
[the report](../reports/ci-errors.md). Treat `nightly_conclusion == "success"` as "the build
command returned", nothing stronger.

**And a green nightly certainly does not mean the notebooks are correct.**
Silently wrong science, stale scientific guidance, dead-but-still-200 data endpoints, and figures
that no longer show what the prose claims all pass CI. This is the single largest gap between what
the harness measures and what matters, and it is the entire justification for `notes/`.

**`pushedAt` counts bot noise as activity.** Dependabot and pre-commit autoupdate PRs move
`pushedAt` without anyone having looked at the cookbook. Where activity matters, prefer the last
*human* commit; where the snapshot only has `pushedAt`, treat recency as weak evidence.

**A stale deploy may mean a stale *gallery*, not a stale cookbook.** Verified on 2026-07-21: the
upstream status page listed `intake-cookbook`, `kerchunk-cookbook`, and `feature-tracking-cookbook`
as not updating or failing, while our snapshot showed all three deployed the same morning. Our
read was the fresher one — the upstream page had not rebuilt since those deploys. It agreed exactly
with us on `esgf-cookbook`, `landsat-ml-cookbook`, `radar-cookbook`, and `xbatcher-ML-1-cookbook`.
When the two disagree, compare timestamps before assuming either is wrong. The status page is only as
fresh as the last build of the gallery site itself. Our snapshots have the same property in
reverse: they are a point-in-time read, and a cookbook fixed the day after a snapshot still looks
broken in it. Date every claim.

**Missing `nightly-build.yaml` is not always neglect.** A handful of cookbooks legitimately cannot
run in CI — they need credentials, large data, or an HPC allocation. Those need a note explaining
the exemption, not a red mark. Record the fact; let the human interpret it.

**The DOI check detects archiving, not the DOI.** In practice most cookbooks carry a Zenodo *badge*
(`zenodo.org/badge/671205314.svg`) whose URL contains the GitHub repo id, not the DOI. So
`has_doi` really means "Zenodo archiving is wired up and advertised" — which is what the community
criterion asks for. It will not catch a cookbook that is archived on Zenodo but never links to it,
and it does not verify that the DOI resolves to a current release.

**Absence of `_gallery_info.yml` on a non-gallery repo means nothing.** That file exists to render
a gallery card. An incubating cookbook has no reason to have one yet. Only score it for cookbooks
that are in — or are trying to get into — the gallery.

**Repo-name filtering misses cookbooks.** Discovery matches `*-cookbook` / `cookbook-*` plus
everything in `cookbook_gallery.txt`. Cookbooks named otherwise (`AtmosCol-2023`,
`thermodynamic-budgets`, `ml-hurricane-intensity`, `cacti-deep-convection`) are invisible to it.
Keep an eye on the reconciliation count, and add names to `EXTRA_REPOS` in `audit.py` as they turn
up.

## Reproducibility

`audit.py` writes `data/snapshot-YYYY-MM-DD.json` with a `collected_at` timestamp and the script
version. Snapshots are committed and **append-only** — they are the historical record, and the
whole point is being able to say "this got worse since March". Reports in `reports/` are
regenerated from the newest snapshot and may be overwritten freely.

HTTP responses are cached under `data/_cache/` (gitignored) so iterating on the script does not
re-fetch the whole org. Delete that directory to force a clean collection; `audit.py --no-cache`
does the same for one run.
