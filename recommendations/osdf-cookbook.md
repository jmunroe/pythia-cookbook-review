# osdf-cookbook — Recommendations

Live outcome: was **build failed**; on a fresh live re-check it **built clean and ran with errors** (4). [← All recommendations](../recommendations.md) · [Live check](../reports/live/osdf-cookbook.md) · [Repository](https://github.com/ProjectPythia/osdf-cookbook)

Static tier `healthy`. **A live re-run confirmed the build failure was transient — and surfaced the real problem underneath it.**

## The build failure was transient — confirmed by re-running

The original failure was a registry transport error (`rpc … Unavailable … EOF`) during
`docker buildx --push`. I re-ran the live check against
[binder.projectpythia.org](https://binder.projectpythia.org) on 2026-07-23:

- **Fresh image built successfully** (~15 min), including the exact push step that failed before.
- Peak memory a comfortable **5.27 GB of 8.59 GB**.

So there is nothing to fix in the environment build. **But the re-run got far enough to execute the
notebooks, and that is where the actual issues are.**

## The real issue: 4 notebook execution errors

With the build working, `myst build --execute` ran and **4 cells raised**:

| Notebook | Error | Cause |
|---|---|---|
| `notebooks/01_pelicanfs.ipynb` | `AttributeError` | `intake.open_esm_datastore()` → intake-esm pydantic validation |
| `notebooks/02_cesm2_oceanheat.ipynb` | `AttributeError` | same |
| `notebooks/02_cmip6_gmst.ipynb` | `AttributeError` | same |
| `notebooks/03_EnviStor_Technical.ipynb` | `NoAvailableSource` | intake source with no available backend |

### 1. Three notebooks fail inside intake-esm (the one change that matters)

All three `AttributeError`s share a traceback that ends in intake-esm, not in the notebook:

```
col = intake.open_esm_datastore(cat_url)
  File .../intake_esm/core.py:113, in esm_datastore.__init__
  File .../intake_esm/cat.py:243, in ESMCatalogModel.load  ->  cls.model_validate(data)
  File .../intake_esm/cat.py:72,  in Assets._validate...
AttributeError: 'pydantic_core._pydantic_core.ValidationInfo' object has no attribute 'format'
```

This is an intake-esm ↔ pydantic incompatibility: intake-esm's `@model_validator` receives a
pydantic `ValidationInfo` where its code expects a field, and dies. The environment **pins
`intake-esm=2025.2.3`**, which freezes intake-esm at an old release while conda is free to resolve
any pydantic — and the specific pair the hub's solve produced is broken.

**Recommended fix: drop the `intake-esm=2025.2.3` pin** (and let conda co-resolve a matching
intake-esm/pydantic), or bump it to the current release:

```diff
-  - intake-esm=2025.2.3
+  - intake-esm>=2025.12
```

The catalog itself is fine and the current release reads it: with `intake-esm==2025.12.12`,
`intake.open_esm_datastore('https://data.gdex.ucar.edu/d850001/catalogs/cmip6-osdf-zarr.json')`
opens **522,217 rows** cleanly. (The bug does *not* reproduce in a clean env across pydantic
2.6–2.13 with `intake-esm==2025.2.3`, which is exactly why the fix is to stop pinning the old
version and let the solver pick a coherent set rather than to chase one pydantic number.)

### 2. `03_EnviStor_Technical.ipynb` — `NoAvailableSource`

A separate failure: an intake source with no available backend — typically a missing driver
(e.g. `intake-xarray`/zarr not registered for that source) or a moved/renamed EnviStor dataset.
Open the notebook, identify the source it requests, and confirm the driver is installed and the URL
still resolves. Investigate after the intake-esm fix, since three of four errors are the same root
cause.

## What was verified

- **Live re-check (2026-07-23): fresh build succeeded**, image pushed, notebooks executed, peak 5.27
  GB — the transient EOF is gone. Recorded in `data/live/osdf-cookbook-2026-07-23T041124Z.json`.
- **Four execution errors captured with tracebacks;** three trace into `intake_esm/cat.py` at
  `open_esm_datastore`, one is `NoAvailableSource`.
- **The catalog reads cleanly on the current intake-esm** (`2025.12.12`, 522,217 rows) — so the fix
  is a version bump, not a data problem.
- **Not verified:** a full green re-run after unpinning intake-esm (worth one more live check once
  the pin is changed), and the exact `NoAvailableSource` source in notebook 03.

## Secondary env hygiene

- **Move `rioxarray` from pip to conda** (packaged on conda-forge). Keep `OpenVisus`, `openvisuspy`,
  `import-ipynb` in pip.
- **Document the remaining pins** — `pelicanfs=1.2.1`, `zarr=2.18.1` (holds zarr at v2),
  `igwn-auth-utils=1.4.0` — or float them. The intake-esm pin above is the one that actually breaks
  a notebook.

---
*Agent-assisted analysis, updated 2026-07-23 after a live re-check (supersedes the earlier
"re-run, transient" note). A proposal to confirm with one more build and open with the community,
not an applied change.*
