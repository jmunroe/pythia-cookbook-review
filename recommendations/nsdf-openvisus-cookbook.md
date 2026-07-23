# nsdf-openvisus-cookbook — Recommendations

Live outcome: **ran clean**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/nsdf-openvisus-cookbook.md) · [Repository](https://github.com/ProjectPythia/nsdf-openvisus-cookbook)

Static tier `healthy`. **Builds and runs clean — the items below are minor housekeeping toward the [publication criteria](../docs/criteria.md), not failures.**

This cookbook builds with `mystmd` (no Sphinx cruft) and has an ORCID for its lead author. The
housekeeping here is: a `pip:` block where most entries are on conda-forge, one undocumented pin,
leftover template metadata (DOI/contributor link still point at the cookbook-template), and no GitHub
release.

## Housekeeping

1. **Move the conda-available pip deps up to the conda section; keep the two that are not.**
   `environment.yml` installs seven packages via `pip:`:

   ```
   - pip:
       - OpenVisus
       - openvisuspy
       - xarray
       - netcdf4
       - intake
       - intake-nexgddp
       - cartopy
   ```

   Verified on conda-forge (`api.anaconda.org/package/conda-forge/<pkg>`):

   | pip dep | on conda-forge? | recommendation |
   |---|---|---|
   | `xarray` | yes (`2026.7.0`) | move to conda |
   | `netcdf4` | yes (`1.7.4`) | move to conda |
   | `intake` | yes (`2.0.9`) | move to conda |
   | `cartopy` | yes (`0.25.0`) | **move to conda** (cartopy's C/GEOS stack is painful via pip) |
   | `OpenVisus` | yes (`1.3.12`) | available — see note below |
   | `openvisuspy` | **no (404)** | **keep in pip** |
   | `intake-nexgddp` | **no (404)** | **keep in pip** |

   `cartopy`, `netcdf4`, `xarray`, and `intake` are clear wins to move (native/binary deps solve far
   more reliably from conda-forge). `OpenVisus` *is* on conda-forge, but its companion `openvisuspy`
   is not — since the two are a paired native stack that usually needs matching versions, keeping
   `OpenVisus` in `pip` alongside `openvisuspy` may be intentional; leave that to the author. So a safe
   minimum is to lift `cartopy`, `netcdf4`, `xarray`, and `intake` into the conda `dependencies:` list
   and leave `OpenVisus`, `openvisuspy`, and `intake-nexgddp` under `pip:`.

2. **Document or relax the one pin.** The conda section pins Python exactly:

   ```
   - python=3.12
   ```

   This is an exact pin with no comment. If OpenVisus/openvisuspy require exactly 3.12, add a one-line
   comment saying so; otherwise a floor (`python>=3.12`) is friendlier to the solver.

3. **Refresh the leftover template metadata.** Several bits still point at the cookbook-template rather
   than this repo:
   - `CITATION.cff` — the contributors entry links to
     `https://github.com/ProjectPythia/cookbook-template/graphs/contributors` (should be
     `.../nsdf-openvisus-cookbook/graphs/contributors`).
   - `notebooks/how-to-cite.md` — the DOI badge is `zenodo.org/badge/475509405.svg`, which is the
     **cookbook-template's** Zenodo ID (the same one still in the template), so this cookbook has no
     DOI of its own yet.

4. **Metadata/archive gaps.** No cookbook-specific **Zenodo DOI** (see above) and **no GitHub
   release** were found. Cutting a release and minting a Zenodo DOI for this repo (replacing the
   template's `475509405` badge) satisfies the archive rows of the criteria. The `README.md` also
   carries no status/DOI/Binder badges — adding the standard row is a nice-to-have.

## What was verified

- **Each of the seven pip deps against conda-forge** via `api.anaconda.org` — results in the table
  above; `openvisuspy` and `intake-nexgddp` return 404 (keep in pip).
- **The single pin** `python=3.12` and the absence of a justifying comment — read from the current
  `environment.yml`.
- **No Sphinx cruft:** `myst.yml` present, no `sphinx-*` deps, no `conf.py` / `_config.yml` / `_toc.yml`.
- **DOI/release:** `how-to-cite.md` reuses the template's Zenodo ID `475509405`; no repo-specific DOI
  or GitHub release found. **ORCID present** for the lead author in `CITATION.cff`.
- **All notebook kernelspecs are `python3`** (checked every `**/*.ipynb`), so no latent kernel time-bomb.
- **Not verified:** whether OpenVisus/openvisuspy require exactly Python 3.12, and whether the
  conda-forge `OpenVisus` build is interchangeable with the PyPI one — those are the author's call.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
