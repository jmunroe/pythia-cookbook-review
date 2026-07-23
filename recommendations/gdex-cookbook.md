# gdex-cookbook — Recommendations

Live outcome: **execution failed** (kernel killed). [← All recommendations](../recommendations.md) · [Live check](../reports/live/gdex-cookbook.md) · [Repository](https://github.com/ProjectPythia/gdex-cookbook)

Static tier `healthy`. **The build works; a Dask cluster asks for more than twice the pod's memory and the kernel is OOM-killed.**

## The one change that matters

**Size the `LocalCluster` to the pod.** Several workflow notebooks create:

```python
cluster = LocalCluster(n_workers=4, memory_limit="4GiB")   # conus404, jra3q, na-cordex
cluster = LocalCluster(n_workers=5, memory_limit="4GiB")   # cesm2_lens
```

`n_workers=5 × memory_limit="4GiB"` tells Dask it may use **20 GiB** — on a pod whose hard limit is
**8.6 GB**. The workers grow into memory that is not there, the cgroup OOM-killer terminates the
process, and MyST records the kernel vanishing:

```
Connection lost, reconnecting in 0 seconds.
Session not found: session_id='…'
Canceled future for execute_request message before replies were done
```

(peak sampled at **7.94 GB of 8.59 GB**, and the true peak at the moment of the kill is higher —
the sampler reads every 3 s and misses the spike.)

Bring the total worker budget under the pod limit, leaving headroom for the kernel and OS:

```diff
- cluster = LocalCluster(n_workers=5, memory_limit="4GiB")
+ cluster = LocalCluster(n_workers=2, threads_per_worker=2, memory_limit="3GiB")
```

Two workers × 3 GiB = 6 GiB leaves ~2.5 GB for the kernel and data buffers. The notebooks still
demonstrate distributed Dask — they just stop over-committing a shared learner pod.

## What was verified

- **Root cause identified:** the workflow notebooks request 16–20 GiB of Dask worker memory on an
  8.6 GB pod; the live check shows the kernel-death signature (`Connection lost` / `Session not
  found` / `Canceled future … before replies were done`) at 7.94 GB sampled.
- **Not verified end-to-end:** a clean run after resizing — the right worker/memory numbers may need
  one tuning pass, and some kerchunk/OPeNDAP data loads may still be heavy. A live re-run after the
  change is the way to confirm, and to check whether any single `.load()` also needs subsetting.

## Secondary

- Notebooks that call `.load()` on a full field (e.g. `ds['co2vmr'].load()`,
  `ds_load = xr.open_dataset(OPeNDAP_URL).isel(time=0).load()`) should select the region/time of
  interest before loading, so the resize has room to work.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with a live re-run and open with the
community, not an applied change.*
