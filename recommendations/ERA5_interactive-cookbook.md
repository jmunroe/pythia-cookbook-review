# ERA5_interactive-cookbook — Recommendations

Live outcome: **ran with errors**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/ERA5_interactive-cookbook.md) · [Repository](https://github.com/ProjectPythia/ERA5_interactive-cookbook)

Static tier `healthy`. **The book builds and runs; one notebook fails opening its intake-esm catalog because a pinned old `intake-esm` co-solved with a newer pydantic.**

## The one change that matters

`notebooks/05_data_preprocessing.ipynb` fails at:

```python
era5_cat = intake.open_esm_datastore(era5_catalog)
```
```
AttributeError: 'pydantic_core._pydantic_core.ValidationInfo' object has no attribute 'format'
```

`environment.yml` pins `intake-esm=2025.2.3`, but pydantic is unpinned and solved to 2.12.2. That old
intake-esm's `@pydantic.model_validator(mode='after')` (`intake_esm/cat.py:72`) is written against an
earlier pydantic calling convention and receives a `ValidationInfo` where it expects the model, so
catalog opening dies. This is the **same intake-esm × pydantic incompatibility** already diagnosed in
the [osdf cookbook](osdf-cookbook.md) — the fix is to stop pinning the stale intake-esm:

```diff
-  - intake=2.0.8
-  - intake-esm=2025.2.3
+  - intake
+  - intake-esm
```

Or, if a floating env is undesired, the conservative bump `intake-esm>=2025.12.12` (a recent release
that opens catalogs cleanly). Unpinning is preferred and matches Pythia's
[avoid-pins guidance](../docs/criteria.md); the `intake` pin is not implicated in this traceback but
is worth unpinning for the same reason.

## What was verified

- **The full traceback** terminates in `intake_esm/cat.py:72` at catalog open, at the exact call
  `intake.open_esm_datastore('https://data.gdex.ucar.edu/d633000/catalogs/d633000-https.json')`.
- **The pins:** `intake-esm=2025.2.3` and `intake=2.0.8` in `environment.yml`, pydantic unpinned; the
  build solved pydantic 2.12.2 / pydantic-core 2.41.4 with intake-esm 2025.2.3.
- **`intake-esm 2025.12.12` exists on conda-forge** (releases after the pin: 2025.7.9, 2025.12.12).
- **Not verified in a fresh solve:** that 2025.12.12 specifically opens *this* GDEX catalog against
  pydantic 2.12.x — this rests on the osdf precedent (same signature, same fix). A local solve + cell
  re-run would close the loop; a live re-check would confirm end-to-end.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
