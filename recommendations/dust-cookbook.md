# dust-cookbook — Recommendations

Live outcome: **ran clean**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/dust-cookbook.md) · [Repository](https://github.com/ProjectPythia/dust-cookbook)

Static tier `healthy`. **Builds and runs clean — the items below are minor housekeeping toward the [publication criteria](../docs/criteria.md), not failures.**

This cookbook already builds with MyST (`myst.yml` present; no `_config.yml` / `_toc.yml`), so the
Sphinx-era dependencies left in `environment.yml` are genuine **dead cruft**. Otherwise it is clean:
conda-forge only, no version pins, no pip deps; all four notebooks carry the standard `python3`
kernelspec; no template links; Zenodo DOI present. Two small items.

## Housekeeping

1. **Delete the dead Sphinx-era dependencies.** The build is MyST, but `environment.yml` still lists
   the old Jupyter Book / Sphinx toolchain:

   ```diff
   -  - jupyter-book
   -  - sphinx-pythia-theme
   ```

   Neither is used by the `mystmd` build (there is no `_config.yml`/`_toc.yml` for them to act on),
   so removing them slims the solve with no functional change. `mystmd` is already in the deps.

2. **Cut a tagged GitHub release.** A Zenodo DOI badge is present in the README, but the repo has no
   release/tag. Tag a release so the archived version matches the citation.

## What was verified

- **MyST build** — `myst.yml` present; **no** `_config.yml` / `_toc.yml` / `_static` / `_templates`,
  so `jupyter-book` and `sphinx-pythia-theme` are unused.
- **`environment.yml`** — conda-forge only, no pins, no pip section (aside from the two dead Sphinx
  deps above).
- **Kernelspecs** — all 4 notebooks under `notebooks/` are `python3`.
- **Template links** — none beyond the standard `trigger-replace-links.yaml` machinery.
- **Metadata** — Zenodo DOI present, ORCIDs present in `CITATION.cff`; **no GitHub release**.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
