# cacti-deep-convection — Recommendations

Live outcome: **ran clean**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/cacti-deep-convection.md) · [Repository](https://github.com/ProjectPythia/cacti-deep-convection)

Static tier `healthy`. **Builds and runs clean — the items below are minor housekeeping toward the [publication criteria](../docs/criteria.md), not failures.**

This cookbook runs clean but is still on the **legacy Jupyter Book / Sphinx build**: there is no
`myst.yml`, and it builds from `_config.yml` + `_toc.yml` (with `_static/` and `_templates/`) using
`html_theme: sphinx_pythia_theme`. So the Sphinx bits here are **not dead cruft** — they are the
active build system, and `sphinx-pythia-theme` / `jupyter-book` in `environment.yml` are load-bearing
until the cookbook migrates to MyST. `environment.yml` is conda-forge only with no pins and no pip.
DOI is present; a GitHub release and a couple of hygiene items are the open work.

## Housekeeping

1. **Migrate to the MyST build (mystmd).** The community has standardized on `mystmd`; this repo is
   still on the older `jupyter-book`/Sphinx toolchain. Add a `myst.yml`, then remove the now-dead
   `_config.yml`, `_toc.yml`, `_static/`, `_templates/`, and drop `jupyter-book` +
   `sphinx-pythia-theme` from `environment.yml`. Do the migration first; the deletions follow from it
   (deleting them now would break the current Sphinx build).

2. **Fix the template links in the README.** The two top badges still point at the template repo:

   ```
   README.md:5  .../ProjectPythia/cookbook-template/actions/workflows/nightly-build.yaml...
   README.md:6  .../v2/gh/ProjectPythia/cookbook-template/main?labpath=notebooks
   ```

   Repoint both to `ProjectPythia/cacti-deep-convection`. (The `cookbook-template` string in
   `.github/workflows/trigger-replace-links.yaml` is the standard `find:` pattern — leave it.)

3. **Normalize non-standard kernelspecs.** Five notebooks carry the kernelspec name `conda-base-py`
   (display "Python [conda env:base] *") instead of the standard `python3`:

   ```
   notebooks/Cloud_CrossSection.ipynb
   notebooks/Divergence_Calculations.ipynb
   notebooks/microphysical-aspects.ipynb
   notebooks/thermo-rain-lasso.ipynb
   notebooks/vic.ipynb
   ```

   Four of these (all but `vic.ipynb`) are in the executed `_toc.yml`, so this is more than latent —
   it happened not to break this run, but a non-portable kernel name is a time-bomb for any executor
   that honors the stored name. Reset each to the standard:

   ```json
   {"name": "python3", "display_name": "Python 3 (ipykernel)", "language": "python"}
   ```

4. **Cut a tagged GitHub release.** The repo has a Zenodo DOI badge
   (`10.5281/zenodo.11265276`) but no GitHub release/tag. Tag a release so the archived version and
   the citation line up.

## What was verified

- **Legacy build** — no `myst.yml`; `_config.yml` sets `html_theme: sphinx_pythia_theme`; `_toc.yml`,
  `_static/`, `_templates/` present; `publish-book.yaml` calls the shared `build-book.yaml`.
- **`environment.yml`** — conda-forge only, includes `jupyter-book` + `sphinx-pythia-theme`; no pins,
  no pip.
- **Template links** — README lines 5–6 point at `cookbook-template`.
- **Kernelspecs** — 5 notebooks are `conda-base-py`; 4 of them appear in the executed `_toc.yml`.
- **Metadata** — Zenodo DOI present, ORCIDs present in `CITATION.cff`; **no GitHub release**.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
