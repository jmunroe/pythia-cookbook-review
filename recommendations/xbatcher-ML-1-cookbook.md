# xbatcher-ML-1-cookbook — Recommendations

Live outcome: **ran with errors**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/xbatcher-ML-1-cookbook.md) · [Repository](https://github.com/ProjectPythia/xbatcher-ML-1-cookbook)

Static tier `healthy`. **The book builds and runs; one notebook fails because its CESM-POP data lives in a requester-pays Google Cloud bucket that public CI cannot bill.**

## The one thing that matters: the data needs GCP billing CI can't provide

`notebooks/surface_currents.ipynb` fails with:

```
ValueError: Bad Request: https://storage.googleapis.com/.../pangeo-cesm-pop/o/control%2F.zmetadata?alt=media
User project specified in the request is invalid.
```

The failing notebook `%run`s `surface_currents_prep.ipynb`, which opens the store via the remote
**pangeo-datastore** catalog:

```python
cat = open_catalog("https://raw.githubusercontent.com/pangeo-data/pangeo-datastore/master/intake-catalogs/ocean/CESM_POP.yaml")
ds  = cat["CESM_POP_hires_control"].to_dask()   # urlpath: gs://pangeo-cesm-pop/control, requester_pays: True
```

`gs://pangeo-cesm-pop` is a **requester-pays** bucket: the caller must supply a billable GCP project,
which a public Binder/CI environment does not have, so GCS rejects the request. This is **not** a
stale hardcoded project id to patch — the `requester_pays: True` (no project) setting comes from the
remote catalog, and nothing in the cookbook carries a project id. Confirmed live: anonymous access to
`pangeo-cesm-pop` is refused with the requester-pays message — the bucket is still genuinely
requester-pays, not moved or public.

There is no in-repo one-line fix. Honest options, for discussion with the community:

1. **Mark the notebook as requiring credentials / not CI-executable**, so the green nightly stops
   implying it runs unauthenticated.
2. **Migrate to a public/anonymous copy** of the CESM-POP data if an equivalent exists (not verified)
   — the cleanest outcome, but a real data-sourcing effort.
3. **Supply a GCP billing project + credentials** in the execution environment — not viable for public
   CI.

Removing `requester_pays` is not possible from the cookbook (the catalog lives in the separate,
now-unmaintained pangeo-datastore repo) and would not help — the bucket requires billing regardless.

## What was verified

- **The failing open** (`open_catalog(...CESM_POP.yaml)` → `cat["CESM_POP_hires_control"].to_dask()`)
  in `surface_currents_prep.ipynb`, reached via `%run` from `surface_currents.ipynb` cell 12; the
  catalog entry's `urlpath: gs://pangeo-cesm-pop/control`, `requester_pays: True`.
- **No hardcoded/stale project id** in the cookbook — the setting comes from the remote catalog.
- **The bucket is still requester-pays** — verified live: anonymous access is refused with the
  requester-pays message.
- **Not verified:** whether a drop-in *public* replacement for the CESM-POP control dataset exists
  (none found; not claimed).

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
