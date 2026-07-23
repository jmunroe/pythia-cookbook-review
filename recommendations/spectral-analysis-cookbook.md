# spectral-analysis-cookbook — Recommendations

Live outcome: **execution failed** (out of memory). [← All recommendations](../recommendations.md) · [Live check](../reports/live/spectral-analysis-cookbook.md) · [Repository](https://github.com/ProjectPythia/spectral-analysis-cookbook)

Static tier `incubating`. The build is fine; a notebook is **running the pod out of memory**.

## What this failure is

The image builds, but `myst build --execute` fails with peak memory at **8.61 GB — 100.2 % of the
8.6 GB pod limit**. That is an out-of-memory kill, not a code error (`Errors raised: 0`, exit code
1). The learner's kernel dies partway through and the published page truncates.

The overshoot is **tiny** — two tenths of a percent. A modest reduction in a single peak allocation
is enough to bring the whole run back under the limit. This is a good-news finding: the cookbook is
one careful notebook away from green.

## Where the memory goes

The env is well-kept (documented pins, conda-forge-first) — the issue is entirely in how a few
notebooks handle full gridded fields. The recurring pattern is **materialising an entire daily
field into a dense NumPy array**, then building a second large matrix from it:

- `field_3d = olr_noaa['olr'].values` / `.load()` on full daily OLR and NCEP-NCAR uwind fields
  (`08`, `09`, `11`, `12`, `14`) — each pulls a multi-decade daily grid fully into RAM.
- `data_2d = olr.olr.values.reshape(n_time, -1)` and the **lagged EEOF matrix**
  `np.zeros((n_time - lag_step*max_lag, n_space*(max_lag+1)))` in `10.extended-eofs.ipynb` — a dense
  `float64` design matrix that can dominate memory.
- `14.ml-application.ipynb` calls `.load()` on both `olr_daily_ds` and `uwind_daily_ds` in the same
  kernel.

Each notebook runs in its own kernel, so the 8.61 GB peak lives inside **one** of them — most likely
`10`, `11`, or `14` — rather than accumulating across the book.

## Recommended actions (highest-leverage first)

1. **Subset before you materialise.** Apply the `.sel(time=…, lat=…, lon=…)` domain *before* calling
   `.values` / `.load()`, so only the region actually analysed is pulled into RAM. Several notebooks
   already select a band or period later — moving that selection ahead of the full-field load is the
   single biggest win.
2. **Use `float32`.** These are geophysical fields; double precision is rarely needed. Casting the
   large arrays and design matrices (`.astype("float32")`, already used for *outputs* in `10`) halves
   their footprint — on its own more than enough to clear a 0.2 % overshoot.
3. **Free intermediates.** After building a derived matrix, `del` the full-field array (and the
   reshaped copy) so two multi-gigabyte objects don't coexist at the peak.
4. **Confirm the culprit.** Run notebooks `10`, `11`, and `14` individually with a memory profile to
   identify which one peaks; the fix then needs to touch only that notebook.

## What was verified

- **Peak memory 8.61 GB = 100.2 % of the 8.6 GB limit**, execution failed with zero errors raised —
  read from the [live check](../reports/live/spectral-analysis-cookbook.md); this is the signature of
  an OOM kill.
- **The environment is healthy** — documented pins (`python<3.12` for TensorFlow, `matplotlib<3.11`
  for a colorbar bug), conda-forge-first, no dead dependencies.
- **Not verified:** which notebook holds the peak, and the exact GB each fix saves. Pinpointing needs
  a per-notebook memory profile (offered as a targeted follow-up); the direction above is robust
  because the overshoot is marginal.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm by profiling the peak notebook and
open with the community, not an applied change.*
