# intake-cookbook — Recommendations

Live outcome: **ran with errors**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/intake-cookbook.md) · [Repository](https://github.com/ProjectPythia/intake-cookbook)

Static tier `healthy`. **The book builds and runs; two notebooks break because Binder installed the rewritten intake 2.x, which dropped the classic catalog API this tutorial teaches.**

## The one change that matters

Two cells fail with:

```
AttributeError: 'ZarrSource' object has no attribute 'yaml'      # creating_catalogs.ipynb
AttributeError: 'ZarrSource' object has no attribute 'describe'  # intake_introduction.ipynb
```

`environment.yml` leaves both `intake` and `intake-xarray` **unpinned**, so the solver takes the
current **2.x** line (Binder installed `intake 2.0.9` + `intake-xarray 2.0.0`). Intake 2.x is the
"take2" rewrite: it kept enough of a shim to *open* the classic `catalog.yml`, but removed the
source-object introspection methods (`.yaml()`, `.describe()`) that are the very subject of this
cookbook. The broken `ZarrSource` comes from **intake-xarray**, so both packages must be pinned.

```diff
-  - intake
-  - intake-xarray
+  - intake>=0.6,<2      # classic API: intake 2.x dropped Source.yaml()/.describe()
+  - intake-xarray<2     # ZarrSource introspection lives here; must match intake <2
```

`<2` resolves to `0.7.0` for both — the last classic-API release, which is the stack this cookbook's
`catalog.yml` (classic `driver:`/`{{ CATALOG_DIR }}` format) was written against.

Pinning core `intake` alone is not enough: intake-xarray 2.0.0 would still install and still lack the
methods. Both pins are load-bearing and carry a documented reason, consistent with Pythia's
[pinning guidance](../docs/criteria.md).

## What was verified

- **Both tracebacks and their exact lines** — `print(source.yaml())` (`creating_catalogs.ipynb`,
  also used in three later cells) and `cat.hrrrzarr.describe()` (`intake_introduction.ipynb`) —
  read from the notebooks.
- **Binder installed intake 2.0.9 + intake-xarray 2.0.0**, from the build package list; both are
  unpinned in `environment.yml`. Neither package has a 1.x series (conda-forge jumps 0.7.0 → 2.0.0),
  so `<2` == 0.7.0.
- **The fix restores the API — reproduced locally.** `uv pip install 'intake<2' 'intake-xarray<2'`
  installs `0.7.0`/`0.7.0`, and `intake_xarray.xzarr.ZarrSource` has both `yaml` and `describe`
  attributes (`hasattr` → `True` for both). The earlier classic calls in the notebooks
  (`open_zarr`, `read`, `open_catalog`) already ran under 2.x, so `<2` fixes the two failing cells
  without disturbing the rest.
- **Not verified:** a full end-to-end notebook execution under the pinned stack (only the missing
  attributes were confirmed present). The `intake-markdown 0.0.2` pip driver is a classic-API driver
  and pairs correctly with `<2`.

## Secondary — consider whether to teach 2.x eventually

The pin is the right *minimal* fix: this cookbook's whole subject is the classic catalog-authoring
workflow, so migrating the notebooks and `catalog.yml` to the intake 2.x data/reader model is a
substantial content rewrite, not a bug fix. Worth raising with the community as a longer-term
question — but not something to bundle into the fix that gets the book green again.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
