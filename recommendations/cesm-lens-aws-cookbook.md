# cesm-lens-aws-cookbook — Recommendations

Live outcome: **ran with errors**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/cesm-lens-aws-cookbook.md) · [Repository](https://github.com/ProjectPythia/cesm-lens-aws-cookbook)

Static tier `healthy`. **The book builds and runs; one Dask-heavy notebook loses its workers on a default, machine-sized client.**

## The one change that matters

`notebooks/example-workflows/key-figures.ipynb` fails with `KilledWorker` (and a downstream
`AssertionError` cascading from the same cell). The cluster is created with a bare default:

```python
client = Client()      # cell 12 — implicit LocalCluster, sized to the pod's detected CPU/RAM
```

then a later cell materializes the full 40-member seasonal `TREFHT` field at once:

```python
seasons = seasons.sel(time=slice("1979", "2012")).load()   # cell 66 — KilledWorker here
```

Give the client explicit, pod-appropriate limits so individual workers have enough headroom for the
large `.load()`:

```diff
- client = Client()
+ from dask.distributed import Client, LocalCluster
+ cluster = LocalCluster(n_workers=2, threads_per_worker=2, memory_limit="3GiB")
+ client = Client(cluster)
```

Optionally subset before materializing in cell 66 (later cells only use the first 30 members), so no
single task needs a multi-GB block.

## This is worker mis-sizing, not a pod-wide OOM

The record's sampled **peak was ~3.9 GB of the 8.59 GB pod (≈45 %)** — the pod never filled. That is
the signature of a default `Client()` mis-sizing workers against the container cgroup: workers die
one at a time (each hitting its own nanny/terminate threshold on a too-large chunk) while the pod
aggregate stays low, which is exactly what `KilledWorker` means. An explicit small cluster with
generous per-worker memory is the standard remedy for this signature; simply "adding more RAM" would
not, because the ceiling was never the problem.

## What was verified

- **Bare `client = Client()`** at cell 12 and the failing `.load()` at cell 66 read from the notebook;
  the `AssertionError` (cell 69, `assert len(winter_seasons.time) == 34`) is downstream of cell 66
  never producing its result.
- **Resource facts from the record:** 8.59 GB pod limit, peak ≈3.9 GB (45 %), 143 samples @ 3 s
  (so sub-second spikes are under-counted). `dask` is unpinned (build resolved 2026.7.1).
- **Not verified:** that `LocalCluster(n_workers=2, memory_limit="3GiB")` completes cell 66 without a
  `KilledWorker`, and the exact worker count/per-worker limit the default `Client()` produced on that
  pod — neither is observable without a live re-run. The fix is the correct standard remedy for the
  signature; confirm with a re-check.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with a live re-run and the community, not an applied change.*
