# cmip6-cookbook — Recommendations

Live outcome: **execution failed** (kernel lost). [← All recommendations](../recommendations.md) · [Live check](../reports/live/cmip6-cookbook.md) · [Repository](https://github.com/ProjectPythia/cmip6-cookbook)

Static tier `healthy`. **The build works; the kernel dropped mid-execution under heavy Dask/CMIP6 loads.**

## What this failure is

Execution stopped after 41.57s with the kernel-connection-lost signature and **no cell error**:

```
Connection lost, reconnecting in 0 seconds.  (repeated)
Canceled future for execute_request message before replies were done
```

Sampled peak memory was **7.32 GB of 8.59 GB (85 %)**. Because the sampler reads every 3 s and the
kernel died between samples, the true peak is higher — the most likely cause is an **OOM kill** while
loading full CMIP6 fields, though at 85 % a transient hub/worker drop cannot be fully ruled out (see
"confirm" below).

## Where the memory goes

The example-workflow notebooks open CMIP6 Zarr stores and materialise large fields with a **default**
Dask client:

- `client = Client()` (`ecs-cmip6.ipynb`, `precip-freq.ipynb`) — no worker or memory cap, sized to
  the node rather than the 8.6 GB pod.
- `ds_abrupt.compute()`, `ta_timeseries.load()`, `cmip6em_ohutcr = ds_out_regrid.mean(dim='model').load()`
  — each pulls a full multi-model field into memory.

## Recommended actions

1. **Give the Dask client pod-sized limits** instead of defaults:

   ```diff
   - client = Client()
   + client = Client(n_workers=2, threads_per_worker=2, memory_limit="3GiB")
   ```

2. **Reduce fields before `.load()`/`.compute()`** — select the time slice, level, or model subset
   the plot actually uses before materialising, so the regrid/mean does not hold every model at once.

3. **Confirm OOM vs transient with a re-run.** At 85 % sampled, one live re-run will disambiguate: a
   recurrence at the same point is an OOM to fix with the above; a clean pass means the first run hit
   a transient worker drop. This is a good candidate for a re-check.

## What was verified

- **Kernel-lost signature and 85 % sampled peak** read from the live check; 0 cell errors, exit 1.
- **Default `Client()` and full-field `.load()`/`.compute()`** present in the example-workflow
  notebooks.
- **Not verified:** whether the peak truly exceeds the limit (sampler undercount) — a re-run
  confirms. The client-sizing change is worthwhile regardless.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with a live re-run and open with the
community, not an applied change.*
