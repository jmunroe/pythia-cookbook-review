# dask-cookbook — Recommendations

Live outcome: **execution failed** (kernel killed). [← All recommendations](../recommendations.md) · [Live check](../reports/live/dask-cookbook.md) · [Repository](https://github.com/ProjectPythia/dask-cookbook)

Static tier `healthy`. **The build works; the Dask demos out-grow the 8.6 GB pod and the kernel is OOM-killed.** There is some irony in *the* Dask cookbook being the one that runs out of memory.

## What this failure is

Peak memory reached **8.23 GB of 8.59 GB (96 %)** and the kernel died mid-execution — the live
check shows the tell-tale sequence:

```
Connection lost, reconnecting in 0 seconds.
Session not found: session_id='…'
Canceled future for execute_request message before replies were done
```

That is an OOM kill, not a cell exception (`0 errors raised`, exit 1). Two things combine:

1. **Default clusters.** `client = Client()` / `cluster = LocalCluster()` size themselves to the
   machine Dask *sees* — on an 8-core node that is several workers with no memory cap, which
   collectively assume far more RAM than the 8.6 GB pod actually has.
2. **A large demo array.** `04-dask-cluster.ipynb` builds
   `da.random.normal(10, 0.1, size=(20_000, 20_000), chunks=(2000, 2000))` — a **3.2 GB** array —
   and calls `.compute()`, which must also hold results and intermediates.

## Recommended actions

1. **Pin the cluster to the pod.** Give every `LocalCluster()` explicit, pod-sized limits:

   ```diff
   - cluster = LocalCluster()
   + cluster = LocalCluster(n_workers=2, threads_per_worker=2, memory_limit="3GiB")
   ```

   This is also better *teaching*: a cookbook about Dask should model choosing worker and memory
   settings deliberately, not accept machine defaults that break on a shared hub.

2. **Keep the big-array demo, size it honestly.** `20_000 × 20_000` float64 is 3.2 GB before any
   computation. Either shrink it (e.g. `10_000 × 10_000` = 0.8 GB) or make the point that it is
   deliberately larger than memory and compute a *reduction* (`.mean().compute()`) rather than
   materialising the whole result.

3. **Avoid `.compute()` on a full result** where a reduction or a `.persist()` of a chunked subset
   makes the same pedagogical point within the pod budget.

## What was verified

- **Kernel OOM-kill confirmed** from the live check: 8.23 GB of 8.59 GB, `Connection lost` /
  `Session not found` / `Canceled future … before replies were done`, 0 cell errors.
- **The 3.2 GB demo array and default cluster** are present in the notebooks (`04-dask-cluster.ipynb`,
  `02`/`03` `LocalCluster()`).
- **Not verified end-to-end:** the exact worker/memory numbers that clear the pod — one tuning pass
  on a live re-run will confirm.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with a live re-run and open with the
community, not an applied change.*
