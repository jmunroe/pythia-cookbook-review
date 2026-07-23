# na-cordex-viz-cookbook — Recommendations

Live outcome: **ran clean**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/na-cordex-viz-cookbook.md) · [Repository](https://github.com/ProjectPythia/na-cordex-viz-cookbook)

Static tier `healthy`. **Builds and runs clean — the items below are minor housekeeping toward the [publication criteria](../docs/criteria.md), not failures.**

This cookbook is in good shape: conda-forge only (no `pip:` block), DOI and release present, ORCIDs
present, correct contributor links, and no leftover Sphinx config files. Two housekeeping items remain
— dead Sphinx build deps in `environment.yml`, and a set of version pins that the static audit flagged
as "documented" but which, on inspection, are not actually explained.

## Housekeeping

1. **Delete the dead Sphinx build dependencies.** `environment.yml` still carries the pre-MyST build
   stack under a "cookbook-related builds" comment:

   ```
   # For Pythia cookbook-related builds
   - jupyter-book
   - jupyterlab
   - jupyter_server
   - sphinx-pythia-theme
   - mystmd
   ```

   The repo builds with `mystmd` (a valid `myst.yml` is present and there is no `conf.py` / `_config.yml`
   / `_toc.yml`), so `jupyter-book` and `sphinx-pythia-theme` are dead cruft from the Sphinx era. They
   can be removed; keep `mystmd` (and `jupyterlab` / `jupyter_server` if you want an interactive env):

   ```diff
      # For Pythia cookbook-related builds
   -  - jupyter-book
      - jupyterlab
      - jupyter_server
   -  - sphinx-pythia-theme
      - mystmd
   ```

2. **Document or relax the version pins — the grouping comment does not justify them.** The static
   audit flagged this file as having documented pins because it contains comments, but the only comment
   (`# For Pythia cookbook-related builds`) merely groups the build deps; it does not explain any of the
   seven version constraints:

   ```
   - cftime>=1.0.4.2
   - dask>=2023.4.0
   - dask-jobqueue>=0.8.1
   - intake>=0.6.8
   - intake-esm>=2020.8.15
   - python<=3.11
   - xarray>=2023.4.2
   ```

   Six of these are lower-bound floors (the mildest kind) and are likely harmless, but they are
   unexplained. The one worth a closer look is `python<=3.11`, an **upper cap** — conda-forge is well
   past 3.11 now, and a cap like this quietly excludes newer Python and can make the environment harder
   to solve over time. Either add a one-line comment on why each constraint is needed, or relax the ones
   the notebooks do not actually require (especially the `python` cap, if it was only there to work
   around a since-fixed dependency):

   ```diff
   -  - python<=3.11
   +  - python          # or keep the cap WITH a comment on why >3.11 breaks
   ```

## What was verified

- **The build deps** `jupyter-book` and `sphinx-pythia-theme` are dead — `myst.yml` is present and no
  Sphinx config files remain (checked the tree).
- **The seven version constraints** and the fact that no comment justifies any of them — read from the
  current `environment.yml`.
- **DOI and release are present** (Zenodo badge `635958518`, GitHub-release link, both pointing at the
  correct repo) and **ORCIDs are present** for two authors in `CITATION.cff`, whose contributor link
  correctly points at this repo. No `pip:` block, no template links, and the single notebook's
  kernelspec is `python3`.
- **Not verified:** whether the notebooks actually require any given floor (e.g. `xarray>=2023.4.2`) —
  that is the author's call; the recommendation is to document the reason or confirm each can float.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
