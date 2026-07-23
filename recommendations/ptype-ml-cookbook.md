# ptype-ml-cookbook — Recommendations

Live outcome: **ran clean**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/ptype-ml-cookbook.md) · [Repository](https://github.com/ProjectPythia/ptype-ml-cookbook)

Static tier `healthy`. **Builds and runs clean — the items below are minor housekeeping toward the [publication criteria](../docs/criteria.md), not failures.**

This cookbook has a strong author list (eight contributors, all with ORCIDs) and builds with `mystmd`.
The housekeeping is mostly template leftovers that were never customized: the README badges, the
citation text, and `CITATION.cff` still describe the cookbook-template, so this cookbook effectively has
no DOI/release of its own. Plus a pair of dead Sphinx build deps.

## Housekeeping

1. **Replace the unfixed cookbook-template links.** Several places still point at
   `ProjectPythia/cookbook-template` instead of this repo:
   - `README.md` — the nightly-build badge and the Binder badge both target
     `ProjectPythia/cookbook-template` (should be `ptype-ml-cookbook`).
   - `notebooks/how-to-cite.md` — the "released on GitHub" link points at cookbook-template, and the
     DOI badge is `zenodo.org/badge/475509405.svg`, which is the **cookbook-template's** Zenodo ID.
   - `CITATION.cff` — `title: "Cookbook Template"`, `abstract: "A sample cookbook description."`, and
     the contributors link points at `.../cookbook-template/graphs/contributors`.

   Point all of these at `ptype-ml-cookbook` (and give the citation this cookbook's real title/abstract).

2. **Metadata/archive gaps (a consequence of #1).** Because the DOI badge and release link are still
   the template's, this cookbook has **no Zenodo DOI of its own** and **no GitHub release**. Cutting a
   release and minting a repo-specific Zenodo DOI (replacing badge `475509405`) closes the archive
   rows. (ORCIDs are already present for all eight authors — that row is met.)

3. **Delete the dead Sphinx build dependencies.** `environment.yml` still carries the Sphinx-era build
   deps alongside the real analysis stack:

   ```
   dependencies:
     - jupyter-book
     - jupyterlab
     - sphinx-pythia-theme
     - numpy
     - pandas
     - matplotlib
     - seaborn
     - pyarrow
     - scikit-learn
     - fastparquet
     - mystmd
   ```

   The repo builds with `mystmd` (valid `myst.yml`, no `conf.py` / `_config.yml` / `_toc.yml`), so
   `jupyter-book` and `sphinx-pythia-theme` are dead cruft:

   ```diff
    dependencies:
   -  - jupyter-book
      - jupyterlab
   -  - sphinx-pythia-theme
      - numpy
   ```

## What was verified

- **The template links** in `README.md` (both badges), `notebooks/how-to-cite.md` (release link + DOI
  `475509405`), and `CITATION.cff` (title, abstract, contributors link) — all still reference
  cookbook-template. The `.github/.../trigger-replace-links.yaml` `find:` entry is expected workflow
  config, not an actionable link.
- **`jupyter-book` and `sphinx-pythia-theme` are dead** — `myst.yml` present, no Sphinx config files in
  the tree.
- **DOI/release:** both are the template's placeholders (Zenodo `475509405`); no repo-specific DOI or
  GitHub release found. **ORCIDs present** for all eight authors in `CITATION.cff`.
- **No version pins and no `pip:` block** in `environment.yml` (all deps are conda-forge).
- **The single notebook's kernelspec is `python3`** (checked every `**/*.ipynb`) — no latent kernel
  time-bomb.
- **Not verified:** the final title/abstract wording for the citation — that is the authors' call.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
