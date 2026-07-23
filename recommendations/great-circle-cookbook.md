# great-circle-cookbook — Recommendations

Live outcome: **ran with errors**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/great-circle-cookbook.md) · [Repository](https://github.com/ProjectPythia/great-circle-cookbook)

Static tier `healthy`. **The book builds and runs; one notebook uses Python-3.12-only f-string syntax that fails on the image's Python 3.10.**

## The one change that matters

`notebooks/tutorials/1_arc_path.ipynb` fails at parse time with:

```
SyntaxError: f-string: unmatched '['
```

Two lines reuse the `"` quote character *inside* a double-quoted f-string:

```python
print(f"Boulder latitude: {location_df.loc["boulder", "latitude"]}")
print(f"Boulder longitude: {location_df.loc["boulder", "longitude"]}")
```

Nested same-quote reuse in f-strings was only legalized by **PEP 701 in Python 3.12**. The Binder
image resolved to **Python 3.10** (`environment.yml` pins no Python version), where the parser closes
the string at `loc[` and chokes on the bracket — a hard `SyntaxError` that kills the whole notebook.

The portable fix is to use single quotes for the inner index keys — valid on every Python version:

```diff
-print(f"Boulder latitude: {location_df.loc["boulder", "latitude"]}")
-print(f"Boulder longitude: {location_df.loc["boulder", "longitude"]}")
+print(f"Boulder latitude: {location_df.loc['boulder', 'latitude']}")
+print(f"Boulder longitude: {location_df.loc['boulder', 'longitude']}")
```

Only these two lines are affected; every other `.loc[..., "latitude"]` in the notebook sits outside an
f-string and is fine. This is preferred over pinning `python>=3.12`, which adds a discouraged pin and
masks that the notebook was authored on 3.12 only.

## What was verified

- **The offending literal** at lines 157–158 of `1_arc_path.ipynb` (cell `In[4]`), read by grep; the
  captured traceback's caret is on the inner `[`.
- **The syntax is PEP 701-only** — `ast.parse` of the line succeeds on Python 3.12.3 locally; the
  construct is invalid pre-3.12.
- **The image ran Python 3.10** (py310 build strings throughout the build log); `environment.yml` does
  not pin Python.
- **Not verified:** the `SyntaxError` was not reproduced against a live 3.10 interpreter (none
  available locally) — but the PEP 701 semantics plus the matching traceback make the diagnosis
  certain. Note the file is `1_arc_path.ipynb` (the URL slug drops the `1_`).

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
