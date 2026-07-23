# vapor-python-cookbook — Recommendations

Live outcome: **ran with errors** (15 cells). [← All recommendations](../recommendations.md) · [Live check](../reports/live/vapor-python-cookbook.md) · [Repository](https://github.com/ProjectPythia/vapor-python-cookbook)

Static tier `incubating`. **The wrong environment file is being built — the one Binder builds has no scientific stack at all, so every notebook dies at its first import.**

## The one change that matters: build the vapor environment

Almost every notebook fails at its first cell with `No module named 'numpy'` / `'matplotlib'` /
`'xarray'` / `'vapor'`. That is not a broken kernel — it is a **near-empty environment**. The cookbook
ships **two** environment files, and Binder builds the wrong one:

- **`environment.yml`** (what Binder actually builds) is a generic docs template:
  `jupyter-book, jupyterlab, jupyter_server, sphinx-pythia-theme, mystmd` — **no numpy, matplotlib,
  xarray, or vapor**.
- **`vapor_environment.yml`** (the real, intended env, never activated) has `ncar-vapor::vapor` plus
  the jupyter stack.

The build succeeds (exit 0) but installs a docs-only env, so the notebooks — whose kernel correctly
points at that single built env — have nothing to import.

The fix is to make the built `environment.yml` the vapor one (merge `vapor_environment.yml` into it, or
replace it), so `ncar-vapor::vapor` and its scientific dependencies are installed:

```yaml
# environment.yml
name: vapor-python-cookbook
channels:
  - conda-forge
  - ncar-vapor
dependencies:
  - ncar-vapor::vapor
  - jupyter-book
  - jupyterlab
  - jupyter_server
  - mystmd
```

`ncar-vapor::vapor` is a valid, installable spec (the `ncar-vapor` channel has `vapor` up to 3.10.0,
`linux-64`), and it pulls numpy/matplotlib/xarray transitively — resolving 14 of the 15 errors.

## What was verified

- **The build solved exactly the docs-only `environment.yml`** (jupyter-book / sphinx-pythia-theme /
  mystmd), from the build log; it succeeded (`failed: false`, exit 0) with no scientific packages.
- **Both env files' contents** read from the repo; `vapor_environment.yml` is the real one and is never
  built.
- **All 16 notebooks use the standard `kernelspec.name: python3`** — this is *not* a kernelspec
  problem (only cosmetic `display_name` values differ).
- **`vapor` availability:** absent on conda-forge; the PyPI `vapor` is an unrelated package; **present
  on the `ncar-vapor` channel** (`vapor` ≤3.10.0, linux-64) — so `ncar-vapor::vapor` is correct.
- **Not verified:** that `ncar-vapor::vapor` co-solves cleanly with current conda-forge jupyter-book/
  mystmd (no solve run), and that numpy/matplotlib/xarray are strictly transitive deps of that vapor
  build (inferred from the env file listing no explicit scientific deps). A local solve + live re-check
  would confirm.

## Secondary — one independent, external failure

`xarray_example.ipynb` fails separately with an `SSLError` downloading
`data.rda.ucar.edu/ds897.7/Katrina.zip` in its first cell — an external/transient HTTPS issue at RDA,
not an environment problem. It needs a retry or a different data source, independent of the env fix
above.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with a live re-run and the community, not an applied change.*
