# CFC-extreme-weather-cookbook — Recommendations

Live outcome: **ran with errors**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/CFC-extreme-weather-cookbook.md) · [Repository](https://github.com/ProjectPythia/CFC-extreme-weather-cookbook)

Static tier `healthy`. **The book builds and runs; two notebooks break on API removals in unpinned dependencies (xgcm and regionmask).**

## The one change that matters

Two independent version-drift failures, one per notebook:

```
ModuleNotFoundError: No module named 'xgcm.autogenerate'                        # cfc-atm.ipynb
TypeError: Regions.mask() got an unexpected keyword argument 'lon_name'         # cfc-ocean.ipynb
```

Both `xgcm` and `regionmask` are unpinned in `environment.yml`, so each floated to a release that
removed the API in use. The two fixes are different in kind:

**1. xgcm — delete the dead import (a code change, because the module is truly gone).**
`xgcm.autogenerate` was removed in xgcm 0.9.0 (env resolved 0.10.1). But `cfc-atm.ipynb` only
*imports* `generate_grid_ds` — it never calls it. Delete the line:

```diff
- from xgcm.autogenerate import generate_grid_ds
```

The sibling `from xgcm import Grid` still works and stays.

**2. regionmask — pin `<0.13` (the broken call is inside xmip, not the notebook).**
`Regions.mask()` dropped the `lon_name=`/`lat_name=` kwargs in regionmask 0.13.0 (env resolved
0.13.0). The notebook's `merged_mask(basins, ds[['lat','lon']])` is correct — the failing call is
inside `xmip.regionmask.merged_mask`, which still passes those kwargs, and no released xmip fixes it.
So hold regionmask back:

```diff
- regionmask
+ regionmask <0.13   # xmip 0.7.2 still passes lon_name/lat_name, removed in regionmask 0.13.0
```

`regionmask ==0.12.1` matches a commented `# !pip install -q regionmask==0.12.1` breadcrumb the
author already left in `cfc-atm.ipynb`.

## What was verified

- **Both tracebacks and exact lines:** `from xgcm.autogenerate import generate_grid_ds`
  (`cfc-atm.ipynb`, and grep confirms `generate_grid_ds` is never used); `merged_mask(basins,
  ds[['lat','lon']])` (`cfc-ocean.ipynb`), with the actual `lon_name=` call inside `xmip/regionmask.py`.
- **The API-removal versions,** from each project's changelog: xgcm `autogenerate` removed in 0.9.0
  (last present 0.8.1); regionmask `lon_name`/`lat_name` deprecated 0.10.0, removed 0.13.0 (last
  accepting them 0.12.1). Current conda-forge: xgcm 0.10.1, regionmask 0.13.0, xmip 0.7.2.
- **xmip 0.7.2 `main` still passes `lon_name`** at `regionmask.py:188` — so bumping xmip is not an
  option; the regionmask pin is the proportionate fix.
- **Not verified:** a local co-solve of the pins (regionmask 0.12.1 + xmip 0.7.2 is a known-compatible
  pairing that predates the 0.13 removal), and whether `cfc-ocean.ipynb` has downstream cells that
  break after the mask cell — the live run halted at these two errors.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
