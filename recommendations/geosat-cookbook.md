# geosat-cookbook — Recommendations

Live outcome: **ran clean**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/geosat-cookbook.md) · [Repository](https://github.com/ProjectPythia/geosat-cookbook)

Static tier `healthy`. **Builds and runs clean — the items below are minor housekeeping toward the [publication criteria](../docs/criteria.md), not failures.**

This cookbook builds with mystmd (`myst.yml` present) and its authors carry ORCIDs. `environment.yml`
uses no version pins and no pip dependencies. Three housekeeping items remain, one of them a latent
kernelspec time-bomb worth fixing before any further TOC changes.

## Housekeeping

1. **Delete the dead Sphinx dependencies.** Because the repo now builds with mystmd, the pre-MyST
   Sphinx stack in `environment.yml` is dead cruft:

   ```
   - jupyter-book
   - sphinx-pythia-theme
   ```

   Neither is used by the MyST build. Remove both:

   ```diff
   -  - jupyter-book
    - jupyterlab
   -  - sphinx-pythia-theme
   ```

2. **Normalize (or remove) the non-standard kernelspec in `notebooks/09_to_delete.ipynb`.** One
   notebook carries a non-standard kernelspec:

   ```
   name = "conda-env-pytroll-py"   display = "Python [conda env:pytroll]"
   ```

   It is **not** in the current TOC (only `notebook-template.ipynb` is listed), so it does not run
   today — but it is a latent execution time-bomb: if it ever enters the executed TOC it will fail to
   launch a `pytroll` kernel. Its filename also suggests it is scratch work. Either delete it, or if it
   is kept, normalize the kernelspec to the standard:

   ```json
   {"name": "python3", "display_name": "Python 3 (ipykernel)", "language": "python"}
   ```

   All other twelve notebooks already use the standard `python3` kernelspec.

3. **Add a Zenodo DOI and cut a GitHub release.** The repo has no release tag and no DOI
   (`myst.yml` has no `doi:` field, and `CITATION.cff` carries no DOI entry). Archiving a tagged
   release to Zenodo and recording the DOI in `myst.yml` / `CITATION.cff` satisfies the
   archive-and-cite criteria rows.

## What was verified

- **`jupyter-book` and `sphinx-pythia-theme` in `environment.yml`, and the presence of `myst.yml`** —
  confirming the Sphinx deps are dead cruft. No leftover `conf.py`/`_config.yml`/`_toc.yml` files
  exist (env deps only).
- **The `conda-env-pytroll-py` kernelspec in `09_to_delete.ipynb`** and the standard `python3`
  kernelspec on all other notebooks (glob over `**/*.ipynb`); confirmed `09_to_delete.ipynb` is absent
  from the `myst.yml` TOC.
- **No pins and no pip dependencies** in `environment.yml`.
- **No release and no DOI** (no tags on the remote; no `doi:` in `myst.yml` or `CITATION.cff`).
  **ORCIDs are present** for all authors in `CITATION.cff`.
- **Not verified:** whether `09_to_delete.ipynb` is intended for publication — the author's call; the
  recommendation is to remove it or normalize its kernelspec.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
