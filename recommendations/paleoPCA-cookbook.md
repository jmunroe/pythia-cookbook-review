# paleoPCA-cookbook — Recommendations

Live outcome: **ran clean**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/paleoPCA-cookbook.md) · [Repository](https://github.com/ProjectPythia/paleoPCA-cookbook)

Static tier `healthy`. **Builds and runs clean — the items below are minor housekeeping toward the [publication criteria](../docs/criteria.md), not failures.**

This cookbook is in good shape: builds with `mystmd` (no Sphinx cruft), DOI and release present, three
authors with ORCIDs, and no stray template links. Two housekeeping items remain — a `pip:` block where
five of six entries are on conda-forge, and one undocumented pin.

## Housekeeping

1. **Move the conda-available pip deps up to the conda section; keep `pyleoclim` in pip.**
   `environment.yml` installs six packages via `pip:`:

   ```
   - pip:
     - pyleoclim
     - xarray
     - h5netcdf
     - nc-time-axis
     - eofs
     - h5py
   ```

   Verified on conda-forge (`api.anaconda.org/package/conda-forge/<pkg>`):

   | pip dep | on conda-forge? | recommendation |
   |---|---|---|
   | `xarray` | yes (`2026.7.0`) | move to conda |
   | `h5netcdf` | yes (`1.8.1`) | move to conda |
   | `nc-time-axis` | yes (`1.4.1`) | move to conda |
   | `eofs` | yes (`2.0.0`) | move to conda |
   | `h5py` | yes (`3.16.0`) | move to conda (binary dep — solves better from conda) |
   | `pyleoclim` | **no (404)** | **keep in pip** |

   Lift `xarray`, `h5netcdf`, `nc-time-axis`, `eofs`, and `h5py` into the conda `dependencies:` list;
   leave `pyleoclim` under `pip:` since it is not packaged on conda-forge (pip here is a flag, not a
   failure).

2. **Document or relax the one pin.** The conda section pins Python exactly:

   ```
   - python=3.12
   ```

   No comment explains it. If `pyleoclim` (or another dep) requires exactly 3.12, add a one-line note;
   otherwise a floor (`python>=3.12`) is easier on the solver.

## What was verified

- **Each of the six pip deps against conda-forge** via `api.anaconda.org` — results in the table above;
  only `pyleoclim` returns 404 (keep in pip).
- **The single pin** `python=3.12` and the absence of a justifying comment — read from the current
  `environment.yml`.
- **No Sphinx cruft:** `myst.yml` present, no `sphinx-*` deps, no `conf.py` / `_config.yml` / `_toc.yml`.
- **DOI and release present** (Zenodo badge `813352705`, this repo's own, plus nightly-build and Binder
  badges in `README.md`) and **three authors have ORCIDs** in `CITATION.cff`. The only cookbook-template
  reference is the standard `replace-links.yaml` workflow (expected, not an actionable link).
- **The single notebook's kernelspec is `python3`** (checked every `**/*.ipynb`) — no latent kernel
  time-bomb.
- **Not verified:** whether the notebook requires exactly Python 3.12 — that is the author's call.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
