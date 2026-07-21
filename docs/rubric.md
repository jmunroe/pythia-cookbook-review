# The rubric

What "good" means for a Project Pythia cookbook, and how we turn that into a tier.

This rubric is **not invented here**. It is Pythia's own published bar, restated as checkable
facts. The upstream sources, in order of authority:

1. [**`docs/criteria.md`**](./criteria.md) — the publication criteria stated at the Pythia
   community meeting of **2026-07-21**. This is the bar. Where this rubric disagrees with it, the
   criteria win and this file is wrong.
2. [`projectpythia.github.io/portal/cookbook-tasklist.md`][tasklist] — the Cookbook Author
   Checklist maintainers hand to authors before publication. Operational detail under (1).
3. [`cookbook-template`][template] — the canonical repo shape every cookbook is cut from.

When those change, this file changes. Do not add criteria that Pythia does not itself ask for.

Keep the community's rule of thumb in view throughout: **a cookbook doesn't need to be finished,
just useful.** Nothing below should be read as penalising a cookbook for being small or
in-progress.

[tasklist]: https://github.com/ProjectPythia/projectpythia.github.io/blob/main/portal/cookbook-tasklist.md
[template]: https://github.com/ProjectPythia/cookbook-template

## The four dimensions

### 1. Discoverability — can a learner find it?

| Check | Source of truth | Passes when |
|---|---|---|
| `in_gallery` | `cookbook-gallery/cookbook_gallery.txt` | repo name appears in the list |
| `site_live` | `https://projectpythia.org/<name>` | returns 200 |
| `has_gallery_info` | `_gallery_info.yml` | file exists |
| `has_thumbnail` | `_gallery_info.yml` → `thumbnail` | names a file that exists in the repo |
| `has_real_tags` | `_gallery_info.yml` → `tags` | `domains`/`packages` set and not the template's `sampledomain`/`samplepackage` |

The gallery card's title comes from `myst.yml` and its description from `CITATION.cff`, so a
cookbook with broken metadata renders as a broken card even when the book itself builds.

### 2. Build health — does it still work?

| Check | Source of truth | Passes when |
|---|---|---|
| `has_nightly` | `.github/workflows/nightly-build.yaml` | file exists |
| `uses_cookbook_actions` | that workflow's body | calls `ProjectPythia/cookbook-actions/...@main` |
| `nightly_conclusion` | Actions API, latest run | `success` |
| `days_since_deploy` | `gh-pages` branch head commit date | ≤ 7 |
| `has_link_check` | `.github/workflows/trigger-link-check.yaml` | file exists |

A nightly build is the only continuous evidence that a cookbook's code still runs against current
upstream packages. It is also the check most likely to be silently disabled — see
[methodology.md](./methodology.md) on stale badges.

### 3. Metadata & citability — can it be credited?

| Check | Source of truth | Passes when |
|---|---|---|
| `myst_extends_config` | `myst.yml` → `extends` | includes `pythia-config/main/pythia.yml` |
| `has_real_title` | `myst.yml` → `project.title` | set and not the template's title |
| `has_citation` | `CITATION.cff` | file exists and parses |
| `has_real_abstract` | `CITATION.cff` → `abstract` | set and not `"A sample cookbook description."` |
| `has_orcid` | `CITATION.cff` → `authors[].orcid` | at least one author has one |
| `has_doi` | `README.md` / `CITATION.cff` | a Zenodo DOI (`10.5281/…`) appears |
| `has_release` | Releases API | at least one published release |
| `has_license` | repo tree | `LICENSE` present |

The checklist makes the DOI and the tagged release the *last* steps before publication, so their
absence on a gallery cookbook means the publication flow was never finished.

### 4. Environment — is it installable, the way Pythia wants?

Straight from the community criteria: *"`environment.yml` is set up appropriately — favor
conda-forge over pip wherever possible; avoid version pins except where needed, and document
reasons."*

| Check | Source of truth | Signal |
|---|---|---|
| `has_environment` | `environment.yml` | file exists and parses |
| `uses_conda_forge` | `channels` | conda-forge is a declared channel |
| `pip_dep_count` | `dependencies` → `pip:` | how much falls outside conda-forge |
| `pinned_count` | dependency specs containing `=<>~!` | **how much is pinned** |
| `has_comments` | raw file | weak evidence the pins were explained |

**Read the pinning check in the right direction.** Pins are the thing being flagged, not their
absence. A cookbook with many pins and no comments explaining them is a finding; a cookbook with
floating deps and a green nightly is exactly what Pythia asked for. See
[criteria.md](./criteria.md) for why.

### 5. Maintenance & content — is anyone home?

| Check | Source of truth | Signal |
|---|---|---|
| `days_since_push` | `pushedAt` | activity (bot-noisy — see methodology) |
| `open_issues` / `open_prs` | Issues API | unattended backlog |
| `notebook_count` | repo tree, `notebooks/**/*.ipynb` | is there content at all |
| `sphinx_leftovers` | repo tree | `_config.yml` / `_toc.yml` — never migrated to MyST |
| `template_links` | `README.md`, `myst.yml` | still references `cookbook-template` — `trigger-replace-links` was never run |
| `template_only` | repo tree | `notebooks/` holds only `notebook-template.ipynb` |

## Health tiers

`scripts/report.py` assigns exactly one tier per cookbook. The tier is a **hypothesis** produced
from the checks above — a human note file may override it via `tier_override`.

| Tier | Rule | What it means |
|---|---|---|
| `healthy` | in gallery · nightly `success` · deployed ≤ 7d · dimension 3 complete | Working and citable. Leave alone. |
| `degraded` | in gallery · nightly failing, **or** deploy 8–30d, **or** missing DOI/citation metadata | Published but slipping. Highest-value place to spend effort. |
| `stale` | in gallery · no deploy in > 30d | Published and quietly broken. A learner hitting this gets old or dead content. |
| `incubating` | not in gallery · real notebooks · activity ≤ 6 months | In flight. Ask whether it needs an advocate to reach publication. |
| `abandoned` | not in gallery · real notebooks · no activity > 12 months | Someone's work is stranded. Revive, hand off, or archive. |
| `not-a-cookbook` | scaffold-only, test/sandbox repo, or no notebooks | Excluded from the health picture; listed so the count reconciles. |

Repos between 6 and 12 months of inactivity fall to `incubating` — the more generous read — on the
grounds that a cookbook is worth asking about before it is written off.

Archived repos are recorded and tiered `not-a-cookbook`; the archive flag is an explicit decision
already made, and re-litigating it is out of scope.

## What this rubric deliberately does not measure

Every check above is mechanical. Three of the community's seven publication criteria are not:

- **Geoscience relevance** — is the topic actually of interest to the broad Pythia community?
- **Narrative flow** — can a reader follow the code and understand the results?
- **"Appropriate" metadata, tags, and description** — the checks confirm these fields are
  *non-placeholder*, not that they are *right*.

No amount of green CI substitutes for reading the cookbook. That judgment is what `notes/` is for,
and the note template asks these three questions first.
