# uxarray-vorticity-cookbook — Recommendations

Live outcome: **ran with errors**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/uxarray-vorticity-cookbook.md) · [Repository](https://github.com/ProjectPythia/uxarray-vorticity-cookbook)

Static tier `incubating`. **The book builds and runs; the one notebook reads the author's private local data by hardcoded macOS path, so it cannot execute anywhere else.**

## The one thing that matters: the data isn't in the repo

`notebooks/mpas_vorticity.ipynb` fails with:

```
FileNotFoundError: [Errno 2] No such file or directory:
'/Users/Shared/JohnsData/MPAS/dymond_1_Falko/120km/x1.40962.grid.nc'
```

The cell hardcodes absolute paths on the author's Mac:

```python
grid_path = "/Users/Shared/JohnsData/MPAS/dymond_1_Falko/120km/x1.40962.grid.nc"
data_path = "/Users/Shared/JohnsData/MPAS/dymond_1_Falko/120km/diag.2016-08-20_00.00.00.nc"
uxds = ux.open_dataset(grid_path, data_path)
```

Neither file is in the repo, and there is **no download logic anywhere** (no `data/` dir, no `.nc`
files, and grep for `pooch`/`wget`/`curl`/`urlretrieve`/`http`/`s3`/`intake` finds nothing).
`environment.yml` installs only `uxarray`, `netcdf4`, and plotting libraries — no data-fetch tooling.
This is the author's private MPAS model output, so the notebook can run **only** on their machine.

There is no one-line fix; this needs data to be made available. In order of preference:

1. **Host the two sample files** (the grid + the `diag` field file with `u10`/`v10`) on a public store
   — Pythia's OSN/S3 example-data bucket is the usual home — and add a `pooch` download cell that
   replaces the hardcoded paths. This is the fix that makes the cookbook reproducible.
2. **Swap to a public equivalent.** `x1.40962.grid.nc` is the standard MPAS-A quasi-uniform 40962-cell
   (~120 km) mesh, which has public counterparts (e.g. UXarray's test mesh files). The **grid** is
   replaceable, but the `diag.*.nc` field file carrying `u10`/`v10` is model output with no obvious
   public drop-in — so the vorticity computation would still need a substitute dataset.

Option 1 is the clean path and keeps the intended science; option 2 risks changing what the notebook
teaches.

## What was verified

- **The hardcoded absolute paths** in cell 3 and the `ux.open_dataset(grid_path, data_path)` call,
  read from the notebook; the grid file is the one that raised `FileNotFoundError`.
- **No data or download machinery in the repo** — confirmed by listing and grepping the clone;
  `environment.yml` carries no fetch tooling.
- **Not verified:** the availability of a *specific* public replacement — the note that UXarray ships
  test MPAS meshes and that a Pythia-hosted equivalent could exist is knowledge-based, not
  network-checked. The core diagnosis (private hardcoded data, unreproducible as-is) is certain.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
