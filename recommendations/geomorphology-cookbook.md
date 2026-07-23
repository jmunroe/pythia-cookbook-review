# geomorphology-cookbook — Recommendations

Live outcome: **ran with errors**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/geomorphology-cookbook.md) · [Repository](https://github.com/ProjectPythia/geomorphology-cookbook)

Static tier `healthy`. **The book builds and runs; a single interactive JupyterGIS cell is missing the `skip-execution` tag its siblings all carry.**

## The one change that matters

`notebooks/jupytergis-showcase.ipynb` fails with:

```
NameError: name 'doc' is not defined
```

at the cell:

```python
doc.sidecar(title="Seabed Morphology", anchor="split-right")
```

`doc` is created one cell earlier by `doc = GISDocument()`, which **is** tagged `skip-execution` —
because these JupyterGIS cells open a live JupyterLab sidecar widget that cannot render in a headless
`myst build --execute`. Of the notebook's interactive GIS cells, five carry `skip-execution`; this one
`doc.sidecar(...)` cell was left untagged, so MyST ran it against a namespace where `doc` was never
bound.

The fix is to add the tag so this cell matches its five siblings:

```diff
- "tags": []
+ "tags": ["skip-execution"]
```

on the `doc.sidecar(title="Seabed Morphology", …)` cell. **Do not** "fix" it by defining `doc` and
executing — the cell is an interactive-widget demo that can never run headlessly; skipping is exactly
what the rest of the notebook already does.

## What was verified

- **The five `skip-execution` tags and the one untagged `doc.sidecar` cell** read directly from the
  notebook JSON; the `NameError` from the live record.
- **Execution-count proof:** the failure is `In[8]`. Cells 1–7 run as In[1]–In[7], the tagged
  `doc = GISDocument()` consumes no count (skipped), so `doc.sidecar` runs as In[8] — confirming the
  definition cell was skipped while this one ran. (If `skip-execution` were being ignored,
  `doc = GISDocument()` would have been In[8] and `doc` would exist.)
- **`jupytergis` is present and unpinned** (resolved 0.15.0) — not an environment problem.
- **Not verified:** the fix was not re-run through `myst build --execute`; the conclusion rests on the
  execution-count inference (strong and internally consistent). A live re-check would confirm the
  notebook builds clean with the tag added.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
