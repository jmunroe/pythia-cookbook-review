# sklearn-argo-cookbook — Recommendations

Live outcome: **execution failed** (out of memory). [← All recommendations](../recommendations.md) · [Live check](../reports/live/sklearn-argo-cookbook.md) · [Repository](https://github.com/ProjectPythia/sklearn-argo-cookbook)

Static tier `incubating`. The build is fine; a notebook **runs the pod out of memory** during a long (9m 22s) execution.

## What this failure is

The image builds, but `myst build --execute` fails with peak memory at **8.61 GB — 100.2 % of the
8.6 GB pod limit**, over a 9m 22s run, with **zero errors raised** and exit code 1. That is an
out-of-memory kill, not a code exception. The overshoot is only two tenths of a percent, so a modest
reduction in one peak allocation brings the whole run back under the limit.

## Where the memory goes

The heavy work is loading Argo BGC profiles with `argopy` and then flattening them into a pandas
DataFrame — a shape change that multiplies memory:

- `sklearn-regression.ipynb` and `argo-access.ipynb`: `f.region(BOX).load()` pulls a whole
  lat/lon/time box of synthetic BGC profiles into memory, then
  `ds.argo.point2profile()` → `argodat = argodat.to_dataframe().reset_index()` expands the gridded
  dataset into a long-format table (one row per level per profile) — the single most memory-hungry
  step in the cookbook.
- The regression notebook additionally runs a `hyperopt` search over GAM/regression models, which
  keeps arrays and fitted models resident during the search — plausibly what pushes the run over the
  edge, and what makes it take 9 minutes.

Each notebook runs in its own kernel, so the 8.61 GB peak is inside **one** of them — almost
certainly `sklearn-regression.ipynb`.

## Recommended actions (highest-leverage first)

1. **Shrink the `region(BOX)` request.** Narrow the lat/lon box and/or the date range so fewer
   profiles load. For a teaching notebook a smaller region illustrates the method just as well and is
   the biggest single memory (and time) saving.
2. **Avoid the full `to_dataframe()` expansion.** Select the variables and levels actually used
   *before* flattening, or work with the xarray dataset directly and only convert the subset that
   feeds `scikit-learn`. The long-format table is where memory multiplies.
3. **Bound the `hyperopt` search.** Reduce `max_evals`, and `del` large intermediates and fitted
   trial models between evaluations so they don't accumulate during the search.
4. **Confirm the culprit.** Run `sklearn-regression.ipynb` with a memory profile to see the peak;
   the fix then needs to touch only that notebook.

## What was verified

- **Peak memory 8.61 GB = 100.2 % of the 8.6 GB limit**, 9m 22s, execution failed with zero errors
  raised — read from the [live check](../reports/live/sklearn-argo-cookbook.md); the signature of an
  OOM kill.
- **Not verified:** which notebook holds the peak and the exact GB each change saves — pinpointing
  needs a per-notebook memory profile (offered as a targeted follow-up). The direction is robust
  because the overshoot is marginal.

## Secondary (env hygiene)

- **Remove `sphinx-pythia-theme`** — dead Sphinx-era doc cruft; the cookbook builds with
  `jupyter-book`/`mystmd`.
- **`python=3.9` is very old** (end-of-life). Once the memory fix lands, try relaxing toward a
  current Python so the scientific stack is not held back; test the notebooks, since `argopy` and
  `scikit-learn` have both moved on since 3.9.
- **Move `matplotlib-label-lines` consideration aside** — the only genuinely pip-only packages are
  `argovisHelpers` and `matplotlib-label-lines`; the rest already come from conda-forge, which is
  good.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm by profiling the peak notebook and
open with the community, not an applied change.*
