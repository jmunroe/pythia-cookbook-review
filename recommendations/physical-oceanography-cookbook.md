# physical-oceanography-cookbook — Recommendations

Live outcome: **ran with errors**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/physical-oceanography-cookbook.md) · [Repository](https://github.com/ProjectPythia/physical-oceanography-cookbook)

Static tier `healthy`. **The book builds and runs; five notebooks fail because their data lives in requester-pays Google Cloud buckets that public CI cannot bill.**

## The one thing that matters: the data needs GCP billing CI can't provide

Five notebooks fail with variants of:

```
ValueError: Bad Request: https://storage.googleapis.com/.../pangeo-.../o/.zmetadata?alt=media
User project specified in the request is invalid.
```

Each opens a `gs://pangeo-*` store through the remote **pangeo-datastore** intake catalogs, whose
entries set `storage_options: {requester_pays: True}` with **no project id**:

| notebook | catalog entry | bucket |
|---|---|---|
| `01_sea-surface-height.ipynb` | `sea_surface_height` | `gs://pangeo-cmems-duacs` |
| `02_along_track.ipynb` | `j3` | `gs://pangeo-cnes` |
| `03_cesm_MOM6.ipynb` | `cesm_mom6_example` | `gs://pangeo-cesm-mom6` |
| `04_eccov4.ipynb` | `ECCOv4r3` | `gs://pangeo-ecco-eccov4r3` |
| `05_gulf_stream_currents.ipynb` | `sea_surface_height` | `gs://pangeo-cmems-duacs` |

These are **requester-pays** buckets: the caller must supply a billable GCP project, which a public
Binder/CI environment does not have, so GCS rejects the request. This is **not** a stale hardcoded
project id to patch — there is no project id anywhere in the cookbook to fix (notebook 05 even carries
a markdown cell telling users to set up their *own* GCP billing). Confirmed live: anonymous requests
to all five buckets return *"Bucket is a requester pays bucket but no user project provided"* — they
are still genuinely requester-pays, not moved or made public.

There is no in-repo one-line fix. Honest options, for discussion with the community:

1. **Mark these notebooks as requiring credentials / not CI-executable** (e.g. exclude from the
   executed build), so the green nightly stops implying they run unauthenticated.
2. **Migrate to a public/anonymous copy** of each dataset if an equivalent exists (not verified to
   exist) — the cleanest outcome, but a real data-sourcing effort.
3. **Supply a GCP billing project + credentials** in the execution environment — not viable for
   public CI, and it moves cost onto whoever runs the book.

Removing `requester_pays` is not possible from the cookbook (the catalog lives in the separate,
now-unmaintained pangeo-datastore repo) and would not help — the buckets require billing regardless.

## What was verified

- **All five failing open calls** (`open_catalog(...)` → `cat[...].to_dask()`) and their target
  buckets, read from the notebooks and tracebacks; the record captured 4 of the 5 (the 5th,
  `gulf-stream-currents`, reuses `pangeo-cmems-duacs`).
- **No hardcoded/stale project id** exists in the notebooks — the `requester_pays: True` (no project)
  setting comes from the remote pangeo-datastore catalog YAMLs (fetched and confirmed).
- **The buckets are still requester-pays** — verified live: anonymous access is refused with the
  requester-pays message.
- **Not verified:** whether a drop-in *public* replacement dataset exists for any of these (none
  found; not claimed).

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
