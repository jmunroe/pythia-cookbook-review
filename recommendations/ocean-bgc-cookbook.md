# ocean-bgc-cookbook — Recommendations

Live outcome: **execution failed** (kernel lost). [← All recommendations](../recommendations.md) · [Live check](../reports/live/ocean-bgc-cookbook.md) · [Repository](https://github.com/ProjectPythia/ocean-bgc-cookbook)

Static tier `healthy`. **The build works; the kernel dropped mid-execution loading large CESM ocean-BGC datasets.**

## What this failure is

Execution stopped after 49.4s with the kernel-connection-lost signature and **no cell error**:

```
Connection lost, reconnecting in 0 seconds.  (repeated)
Canceled future for execute_request message before replies were done
```

Sampled peak was **7.47 GB of 8.59 GB (87 %)**; the true peak at the moment of the kill is higher.
The likely cause is an **OOM kill** while opening and reducing multi-file CESM output, with a
transient worker drop as a less-likely alternative at 87 % (confirm with a re-run).

## Where the memory goes

Every analysis notebook follows the same shape:

```python
cluster = LocalCluster()                       # default, machine-sized
ds = xr.open_mfdataset(fileset, data_vars="minimal", coords="minimal", compat="override", ...)
ds_glb = global_mean(ds, ds_grid, variables, normalize=False).compute()
```

`LocalCluster()` with no cap plus a multi-file `open_mfdataset` global-mean `.compute()` over full
CESM fields is what pushes the pod to its ceiling.

## Recommended actions

1. **Cap the cluster to the pod:**

   ```diff
   - cluster = LocalCluster()
   + cluster = LocalCluster(n_workers=2, threads_per_worker=2, memory_limit="3GiB")
   ```

2. **Chunk and subset before the global mean.** Ensure `open_mfdataset` is chunked (time and/or
   basin) so the `global_mean(...).compute()` streams rather than materialising the whole stack, and
   select the variables/time range each figure needs before reducing.

3. **Confirm OOM vs transient with a re-run** — at 87 % sampled, one live re-check tells you whether
   the kill recurs (OOM, fix as above) or the first run hit a transient worker drop.

## What was verified

- **Kernel-lost signature and 87 % sampled peak** read from the live check; 0 cell errors, exit 1.
- **Default `LocalCluster()` and multi-file `open_mfdataset(...).compute()`** present across the
  `ocn-*` notebooks.
- **Not verified:** whether the peak exceeds the limit (sampler undercount) — a re-run confirms; the
  cluster-cap and chunking are worthwhile regardless.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with a live re-run and open with the
community, not an applied change.*
