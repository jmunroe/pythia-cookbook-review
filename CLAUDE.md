# Working conventions for this repo

A workspace for assessing the status of every Project Pythia cookbook. Read
[`README.md`](README.md) first, then [`docs/criteria.md`](docs/criteria.md).

## The sources of truth are upstream

This repo does not define what a good cookbook is. Pythia does. In order of authority:

1. `docs/criteria.md` — the publication criteria from the community meeting of 2026-07-21.
2. [`projectpythia.github.io/portal/cookbook-tasklist.md`][tasklist] — the author checklist.
3. [`cookbook-template`][template] — the canonical repo shape.
4. [`cookbook-gallery/cookbook_gallery.txt`][gallery] — who is actually published.

Never add an assessment criterion Pythia does not itself ask for. If a check seems obviously good
but isn't in those sources, it doesn't belong in the rubric — it belongs in a note as a personal
observation.

[tasklist]: https://github.com/ProjectPythia/projectpythia.github.io/blob/main/portal/cookbook-tasklist.md
[template]: https://github.com/ProjectPythia/cookbook-template
[gallery]: https://github.com/ProjectPythia/cookbook-gallery/blob/main/cookbook_gallery.txt

## Who writes what

| Path | Author | Rule |
|---|---|---|
| `data/` | `audit.py` | **Append-only.** Never edit or delete a snapshot — they are the historical record and the only way to say "this got worse". |
| `reports/` | `report.py` | **Generated.** Never hand-edit; the next run destroys it. Wrong output means `report.py` or the rubric is wrong. |
| `index.md` | `build_site.py` | **Generated** from the newest snapshot. Edit `scripts/templates/index.md`, never `index.md`. |
| `notes/` | **a human** | **Never generate these.** See below. |
| `docs/` | a human | Changes when upstream Pythia guidance changes. |

## Do not write notes for the user

`notes/*.md` is the whole point of this exercise: human judgment about whether a cookbook actually
teaches well — the three community criteria (geoscience relevance, narrative flow, appropriate
metadata) that no script can check.

A machine-written note would be indistinguishable from a real one and would quietly poison the
conclusions the project exists to produce. If asked to fill one in, gather evidence, quote what
the cookbook actually says, and leave the judgment to the human.

## The site is the repo

The published site is a [MyST](https://mystmd.org) build of this repo's own markdown: `myst.yml`
pulls `reports/` and `docs/` directly into the table of contents, so anything written there renders
as HTML with no separate authoring step. Adding a page means adding a file and listing it in
`myst.yml`'s `toc`.

Two things to preserve:

- **`myst.yml` deliberately does not extend `projectpythia/pythia-config`.** That shared config
  carries Pythia's logo, favicon, Google Analytics measurement ID, and the NSF funding disclaimer.
  This is an independent assessment, not an official Pythia product, and must not be dressed as
  one. Link to Pythia; don't wear its branding.
- **The Pages build needs `BASE_URL`.** It is a project site served from `/<repo-name>/`, so
  without that prefix every asset and internal link 404s. The workflow sets it from the repo name.

## Getting the pinning check right

The community asks authors to **avoid** version pins except where needed, and to document reasons.
Pins are therefore the thing being flagged, not their absence. Do not "fix" this to the more
intuitive direction — a floating `environment.yml` with a green nightly is exactly what Pythia
wants, and an over-pinned one silently teaches a frozen stack.

## Assessing, not acting

No PRs, no issues filed on ProjectPythia repos, no edits to cloned cookbooks from within this
workflow. Cookbook clones live as siblings (`../radar-cookbook`), never inside this repo. Any
upstream action is a separate, deliberate step taken with the community.

## Before trusting a number

Read [`docs/methodology.md`](docs/methodology.md) — particularly that a disabled workflow serves a
passing badge forever, that a green nightly says nothing about correctness, and that `pushedAt`
counts bot commits as activity.
