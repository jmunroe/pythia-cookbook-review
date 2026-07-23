# icesat2-cookbook — Recommendations

Live outcome: **ran with errors**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/icesat2-cookbook.md) · [Repository](https://github.com/ProjectPythia/icesat2-cookbook)

Static tier `healthy`. **The book builds and runs; one notebook needs a missing optional dependency, the other needs Earthdata credentials the headless check can't provide.**

## The one change that matters

`notebooks/land-ice.ipynb` fails on:

```
AttributeError: The geopandas.dataset has been deprecated and was removed in GeoPandas 1.0.
```

This is **not** the cookbook's own code — it is inside `icepyx`. `region_a.visualize_spatial_extent()`
tries `import geoviews` first and, because **geoviews is absent from `environment.yml`**, falls into
its `except ImportError` branch, which calls the removed `gpd.datasets.get_path("naturalearth_lowres")`
(deleted in GeoPandas 1.0, and `geopandas` floats unpinned to 1.x here).

The fix is to add the missing optional dependency so icepyx takes its primary, working path:

```diff
 dependencies:
   - geodatasets
+  - geoviews
```

With geoviews present, `visualize_spatial_extent()` never reaches the deprecated GeoPandas fallback.
This is better than pinning `geopandas<1.0` (a version-pin smell that leaves the real gap — the
missing viz dependency — in place).

## What was verified

- **Both tracebacks and source cells** read from the notebooks.
- **The deprecated call lives in icepyx** (`icepyx/core/query.py`
  `gpd.datasets.get_path("naturalearth_lowres")`), reached only because `import geoviews` raised.
- **geoviews is absent** from `environment.yml` (0 occurrences); **geopandas is unpinned** (build
  resolved shapely 2.1.2 / pyogrio 0.11.0, consistent with GeoPandas ≥1.0); **geodatasets is already
  present** and on conda-forge.
- **Not verified:** that geoviews alone fully satisfies icepyx's viz path (it may also want `bokeh`,
  though the conda-forge geoviews package normally pulls its own viz stack) — confirm in a re-run.

## Secondary — the second failure is a credentials gap, not a bug

`notebooks/geospatial-transforms.ipynb` fails with `IndexError: list index out of range` at
`xr.open_dataset(buffers[0], …)`. The chain: Earthdata Login has no credentials in the headless
Binder build (`env_injection.attempted = false`), the auth cell swallows the failure and sets
`granules = None`, `earthaccess.download(None)` returns an empty list, and the next cell indexes
`buffers[0]` on it. The merge logic itself is correct — it only fails because there is nothing to
download without authentication.

Two options, both a design choice rather than a bug fix:

1. **Guard the download/read cell** so it no-ops when `granules` is falsy (`if granules:` before the
   download + merge), letting the notebook render cleanly without credentials; or
2. **Accept that these data-access cells require authenticated execution** and cannot pass an
   unauthenticated live check.

This is the same Earthdata-Login-in-CI pattern seen elsewhere in these cookbooks; worth deciding on
a consistent convention with the community.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
