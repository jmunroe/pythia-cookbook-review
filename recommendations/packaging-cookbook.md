# packaging-cookbook — Recommendations

Live outcome: **ran clean**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/packaging-cookbook.md) · [Repository](https://github.com/ProjectPythia/packaging-cookbook)

Static tier `healthy`. **Builds and runs clean — the items below are minor housekeeping toward the [publication criteria](../docs/criteria.md), not failures.**

This is Pythia's own tutorial on *how to package a cookbook*, so a couple of things that would look like
flags elsewhere are intentional here (e.g. `CONTRIBUTING.md` telling readers to click "Use this
template" on the cookbook-template is legitimate instructional content, not a stray link). The genuine
housekeeping is: dead Sphinx build deps, and a missing `CITATION.cff` / ORCIDs.

## Housekeeping

1. **Delete the dead Sphinx build dependencies.** `environment.yml` is just the build stack:

   ```
   dependencies:
     - jupyter-book
     - sphinx-pythia-theme
     - mystmd
   ```

   The repo builds with `mystmd` (valid `myst.yml`, no `conf.py` / `_config.yml` / `_toc.yml`), so
   `jupyter-book` and `sphinx-pythia-theme` are dead cruft from the Sphinx era:

   ```diff
    dependencies:
   -  - jupyter-book
   -  - sphinx-pythia-theme
      - mystmd
   ```

2. **Add a `CITATION.cff` with author ORCIDs.** There is no `CITATION.cff` in the repo, so the citation
   and ORCID criteria rows are unmet. Since the byline is "Project Pythia Community", a `CITATION.cff`
   listing the maintainers (with ORCIDs) — or at minimum the organization entry — would close both
   rows. A DOI badge (`508404588`) and nightly-build/Binder badges are already present in `README.md`.

## What was verified

- **`jupyter-book` and `sphinx-pythia-theme` are dead** — `myst.yml` present, no Sphinx config files in
  the tree.
- **No `CITATION.cff` file exists** (hence no ORCIDs) — confirmed by listing the repo root.
- **DOI/release present:** `README.md` carries a Zenodo DOI badge (`508404588`, this repo's own, not
  the template's) plus nightly-build and Binder badges.
- **No version pins and no `pip:` block** in `environment.yml`.
- **Template references are intentional:** `CONTRIBUTING.md`'s "Use this template" instruction points
  at cookbook-template on purpose (this cookbook teaches that workflow); the Turing-Way attribution in
  `notebook-template.ipynb` is standard boilerplate. Neither is an actionable template-link.
- **All notebook kernelspecs are `python3`** (checked every `**/*.ipynb`) — no latent kernel time-bomb.
- **Not verified:** which individuals should be credited in a new `CITATION.cff` — that is the
  maintainers' call.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
