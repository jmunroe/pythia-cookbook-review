# unstructured-grid-viz-cookbook — Recommendations

Live outcome: **ran with errors** (after re-check — the earlier build timeout was transient). [← All recommendations](../recommendations.md) · [Live check](../reports/live/unstructured-grid-viz-cookbook.md) · [Repository](https://github.com/ProjectPythia/unstructured-grid-viz-cookbook)

Static tier `healthy`. **The build timeout was transient; on re-check the book builds and runs, and one notebook fails on an unloaded plotting extension.**

## The earlier timeout was transient — confirmed

An earlier live check hit the 30-minute build timeout. A fresh re-check on **2026-07-23** built the
image cleanly (**593 s fresh build**, then **207 s execution**, peak 6.0 GB of the 8.59 GB pod) — so
the timeout was infrastructure, not the environment, exactly as the local `mamba` reproduction
predicted (solves in ~15 s, builds in ~52 s locally). No environment change is needed for the build.

## The one thing that matters: load a plotting extension in `selection.ipynb`

With the build working, the re-check surfaced a single real execution error, in
`notebooks/02-intro-to-uxarray/selection.ipynb` (cell `In[2]`):

```
ValueError: No plotting extension is currently loaded. Ensure you load a plotting extension with
hv.extension or import it explicitly from holoviews.plotting before applying any options.
```

The cell builds its map features *before* it draws any uxarray plot:

```python
features = gf.coastline(projection=ccrs.PlateCarree(), ...) * gf.states(...)   # <- fails here
...
uxda.plot(rasterize=True, ...) * features
```

`gf.coastline(...)` applies HoloViews `.opts()` internally (`geoviews … Feature.__call__ → .opts()`),
and that runs first — before `uxda.plot()` (which is what normally auto-loads the Bokeh backend on its
first call). The notebook imports `geoviews.feature as gf` but never calls `gv.extension('bokeh')`, so
at that first `.opts()` no backend is loaded. Sibling notebooks avoid this only by accident of
ordering (their first plotting op is `uxda.plot()`).

The fix is to load the extension explicitly at the top of the notebook — the canonical HoloViews/
GeoViews idiom and exactly what the error asks for:

```diff
  import cartopy.crs as ccrs
  import geoviews.feature as gf
+ import geoviews as gv
  import uxarray as ux
+
+ gv.extension("bokeh")
```

(`hv.extension("bokeh")` is equivalent.) This makes the notebook robust regardless of which plotting
call comes first, and is worth adding to any notebook here that mixes bare `geoviews` features with
uxarray plots.

## Durable improvements (worth doing regardless)

Even though the env is healthy, three items reduce risk and align with the
[criteria](../docs/criteria.md):

1. **Remove `pathlib`.** This is the obsolete PyPI/conda backport pinned at `1.0.1` — a package that
   *shadows the Python standard library's own `pathlib`*. `pathlib` has been in the stdlib since
   Python 3.4; the backport is unnecessary on every supported interpreter and is a well-known trap
   that can cause subtle import breakage. Nothing needs it. Delete the line.

2. **Remove `sphinx-pythia-theme`.** Dead doc-build cruft from the Sphinx era — the cookbook builds
   with `jupyter-book`/`mystmd`. It bloats the image for no runtime purpose.

3. **Move `antimeridian` from pip to conda.** It is packaged on conda-forge (`0.4.8`), so the entire
   `pip:` block can go, and the build no longer needs pip at all.

```diff
   numpy
-  - pathlib
   - pip
   - pre_commit
   - pyarrow
   - pytest
   - pytest-cov
   - requests
   - scikit-learn
   - scipy
   - shapely
   - spatialpandas
-  - sphinx-pythia-theme
   - uxarray
   - xarray
+  - antimeridian
-  - pip:
-      - antimeridian
```

## What was verified

- **The build timeout was transient — verified by re-check.** A live re-check on 2026-07-23 built the
  fresh image (593 s) and executed all 20 notebooks (207 s, peak 6.0 GB), so the environment is not
  responsible. Local `mamba` also solves in ~15 s and builds in ~52 s (exit 0).
- **The `selection.ipynb` error and its cause** read from the re-check record: the failing cell is
  `In[2]`, and the traceback is `geoviews … Feature.__call__ → .opts()` raising before any backend is
  loaded; the notebook has no `gv.extension`/`hv.extension`/`import hvplot` call.
- **`pathlib` on conda-forge/PyPI is the `1.0.1` stdlib backport**, confirmed by querying both
  indices; it is safe to remove. **`antimeridian` is on conda-forge** (`0.4.8`), so it can move out
  of pip.
- **Not verified:** that adding `gv.extension("bokeh")` alone clears the error end-to-end (not
  re-run with the edit) — but it is the direct, documented remedy for this exact message.

## Secondary

- `pre_commit`, `pytest`, and `pytest-cov` are developer tooling in the runtime env; move them to a
  dev environment to slim the image further.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm in a real build and open with the
community, not an applied change.*
