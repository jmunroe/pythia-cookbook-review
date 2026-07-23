# gridding-cookbook — Recommendations

Live outcome: **ran with errors**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/gridding-cookbook.md) · [Repository](https://github.com/ProjectPythia/gridding-cookbook)

Static tier `healthy`. **The book builds and runs; one cell opens a bundled data file with the wrong relative path.**

## The one change that matters

`notebooks/pyresample_intro.ipynb` fails with:

```
FileNotFoundError: [Errno 2] No such file or directory: '/home/jovyan/notebooks/data/onestorm.nc'
```

This is **not** missing data — `data/onestorm.nc` is a real 39 MB file committed to the repo. It is a
relative-path bug. Under `myst build --execute` the working directory is `notebooks/`, so the correct
path is `../data/onestorm.nc`. The failing cell drops the `../`:

```diff
- area_def, cf_info = load_cf_area('data/onestorm.nc', variable='visible', x='x', y='y')
+ area_def, cf_info = load_cf_area('../data/onestorm.nc', variable='visible', x='x', y='y')
```

An earlier cell in the same notebook already opens the file correctly as `'../data/onestorm.nc'` and
succeeds, so this is simply an inconsistency in one cell.

## What was verified

- **`data/onestorm.nc` is present in the repo** (39 MB HDF5/NetCDF, not an LFS pointer).
- **The earlier `xr.open_dataset('../data/onestorm.nc')` cell succeeded** in the same run, and the
  sibling `xESMF_introduction.ipynb` references `../data/onestorm.nc` correctly and ran clean.
- **The cwd-to-traceback resolution matches exactly:** cwd `/home/jovyan/notebooks/` + `data/onestorm.nc`
  → the reported missing path; the file actually lives at `/home/jovyan/data/onestorm.nc`.
- Fully verified against the repo and the captured traceback; the fix is a one-token relative-path
  correction.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
