# radiative-feedback-cookbook — Recommendations

Live outcome: **execution failed** (30-minute timeout). [← All recommendations](../recommendations.md) · [Live check](../reports/live/radiative-feedback-cookbook.md) · [Repository](https://github.com/ProjectPythia/radiative-feedback-cookbook)

Static tier `incubating`. **The build works; a heavy CMIP6 radiative-kernel notebook does not finish inside the 30-minute execution limit.**

## What this failure is

Execution ran to the **1800-second timeout** with only `README.md` and `how-to-cite.md` built —
none of the content notebooks completed. The two that matter are compute-heavy:

- `notebooks/foundations/climkern-calc.ipynb` (30 cells) — `intake.open_esm_datastore(...)`, the
  `climkern` radiative-kernel package, and `.compute()`.
- `notebooks/foundations/manual-calc.ipynb` (88 cells) — `intake.open_esm_datastore(...)` and
  `.load()` of CMIP6 fields.

(`energy-balance-model.ipynb` is a single trivial cell and is not the problem.) MyST executes the
three in parallel, and computing radiative feedbacks from full CMIP6 output — loading multi-model
fields and running kernel convolutions — simply takes longer than 30 minutes in the pod, or thrashes
memory badly enough to crawl.

## Recommended actions

1. **Shrink the CMIP6 request.** Restrict the `open_esm_datastore` query to the minimum models,
   experiments, and years the narrative needs (often one model is enough to teach the method), and
   select the time/level slice before `.load()` / `.compute()`. This is the biggest single reduction
   in both time and memory.
2. **Chunk and stream.** Ensure the datasets are opened chunked so the kernel convolutions and means
   stream rather than materialising every model at once; if a Dask cluster is used, size it to the
   pod (`LocalCluster(n_workers=2, threads_per_worker=2, memory_limit="3GiB")`).
3. **Confirm the boundary with a re-run.** After subsetting, a live re-run shows whether the run now
   finishes inside the limit — and separates "slow compute" from a possible memory-thrash, which the
   timeout alone cannot distinguish.

## Also: a broken table-of-contents entry

The live check's stderr flagged a concrete config error:

```
⛔️ myst.yml Table of contents entry does not exist: references.md
```

`myst.yml` lists `references.md` (line 29) but the file **does not exist** in the repo. Either add
the references/bibliography page or remove the toc entry. This does not cause the timeout, but it is
a build error worth clearing in the same PR.

## What was verified

- **Execution timed out at 1800s** with no content notebook completing — read from the live check.
- **The heavy notebooks identified:** `climkern-calc.ipynb` and `manual-calc.ipynb` load CMIP6 via
  intake-esm and run `.compute()`/`.load()` radiative-kernel calculations; `energy-balance-model`
  is trivial.
- **`references.md` is missing** but listed in `myst.yml`'s toc (confirmed locally).
- **Not verified:** whether the notebooks are slow vs memory-bound, and how much subsetting is
  enough — a live re-run after the data reduction confirms.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with a live re-run and open with the
community, not an applied change.*
