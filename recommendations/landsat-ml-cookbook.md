# landsat-ml-cookbook — Recommendations

Live outcome: **ran with errors**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/landsat-ml-cookbook.md) · [Repository](https://github.com/ProjectPythia/landsat-ml-cookbook)

Static tier `healthy`. **The book builds and runs, but three cells fail — all symptoms of the same condition: the environment is half-frozen to a 2023 stack (heavy pins) while unpinned packages have floated to 2026.**

## The one thing that matters: the env is internally inconsistent

A live re-check on 2026-07-23 (build cached, executed in 173 s, peak 0.9 GB) reproduced three
persistent errors — the same three seen on 2026-07-21, so none is transient. Each is a version
mismatch between a **pinned 2023-era package** and an **unpinned 2026 one**. `environment.yml` carries
heavy pins (`xarray<2023.04`, `jupyter_server<2`, `panel<1.4.0`, `bokeh<3.4.0`, `shapely<2.0.0`) that
hold transitive dependencies old, while `aiohttp`, `pystac`, and the dask stack float to current
releases. The durable fix is a coherent re-pin/rebuild; the three targeted fixes below are the minimal
changes.

## The three fixes

**1. `KeyError: 'proj:epsg'`** — `notebooks/1.0_Data_Ingestion-Geospatial.ipynb`, cell `In[18]`
(same pattern in `2.0_Spectral_Clustering_PC.ipynb` `In[6]`/`In[21]`).

`pystac` is unpinned and floats to ≥1.11, which auto-migrates the STAC projection extension v1→v2 when
deserializing an item — renaming `proj:epsg` (int) to `proj:code` (string `"EPSG:…"`) and deleting
`proj:epsg`. The server still ships v1.0.0 with `proj:epsg`; the rename happens client-side in pystac.
Read `proj:code` (it is already a full `EPSG:` string, so don't re-prefix):

```diff
- da.attrs["crs"] = f"epsg:{selected_item.properties['proj:epsg']}"
+ props = selected_item.properties
+ da.attrs["crs"] = props["proj:code"] if "proj:code" in props else f"epsg:{props['proj:epsg']}"
```

**2. `ClientPayloadError: Can not decode content-encoding: br`** — `notebooks/1.1_Data_Ingestion-General.ipynb`,
cell `In[2]` (the Planetary Computer STAC fetch through `intake`→`fsspec`→`aiohttp`).

`brotli-python` is transitively held **< 1.2.0**, whose `Decompressor.process()` takes one argument,
but current `aiohttp` calls it with two (`data, max_length`) — a hard `TypeError` decoding the brotli
STAC response. Add a floor:

```diff
+  - brotli-python>=1.2.0
```

**3. `ImportError: cannot import name 'collections_to_dsk' from 'dask.base'`** —
`notebooks/2.0_Spectral_Clustering_PC.ipynb`, cell `In[1]` (`from dask.distributed import Client`).

The notebook is innocent — this is `distributed`'s own import failing. `dask.base` dropped
`collections_to_dsk` in 2026.1.0, and the same release dropped `distributed`'s import of it, but the
cached image has a **skewed pair** (a `distributed` still importing the symbol against a `dask-core`
that removed it). `environment.yml` pins nothing on the dask stack. Pin them together (conda recipes
tie the versions, so a matched pair resolves cleanly):

```diff
-  - dask
+  - dask=2024.12.*
+  - distributed=2024.12.*
```

(2024.x still exports `collections_to_dsk`. Letting both float to a matched 2026.x pair also clears
this import, but a 2024.x pair is safer given `dask-ml`'s SpectralClustering may use other legacy-graph
APIs removed in dask ≥2026.)

## What was verified

- **All three errors persist across both checks** (2026-07-21 and 2026-07-23) — not transient.
- **`proj:epsg` — fully reproduced:** pystac 1.15.1 migrates the live PC item to `proj:code` and
  raises the exact `KeyError`; pystac 1.10.1 does not. The value is a full `"EPSG:32611"` string.
- **brotli — verified from source:** Google Brotli's `Decompressor.process()` gained its second arg in
  **1.2.0**; aiohttp's `BrotliDecompressor` calls it with two; `brotli-python` 1.2.0 is on conda-forge.
- **dask — verified from source:** `collections_to_dsk` exists in `dask.base` and `distributed`'s
  imports through 2025.1.0, removed in 2026.1.0; the conda recipe pins `dask-core`↔`distributed`
  together.
- **Not verified:** the exact package versions on the (uninspectable) cached Binder image — the dask
  skew is inferred from the traceback and is consistent with a stale image; and whether dask-ml's
  SpectralClustering has *further* dask≥2026 breakages beyond this import (hence the conservative
  2024.x pin). A rebuild + live re-check would confirm all three end-to-end.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with a live re-run and the community, not an applied change.*
