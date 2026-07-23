# api-cookbook — Recommendations

Live outcome: **ran with errors**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/api-cookbook.md) · [Repository](https://github.com/ProjectPythia/api-cookbook)

Static tier `healthy`. **The book builds and runs; one notebook can't import `pyaqsapi` because it's installed from an unpinned Git source that doesn't yield an importable module.**

## The one change that matters

`notebooks/example-workflows/air-quality-system-api.ipynb` fails at its first cell:

```
ModuleNotFoundError: No module named 'pyaqsapi'
```

`pyaqsapi` is **not** missing from `environment.yml` — it is declared, but only as an unpinned Git
source build:

```yaml
  - pip:
      - git+https://github.com/USEPA/pyaqsapi.git
```

The build log even shows it "resolving" to `pyaqsapi 1.0.2`, yet `import pyaqsapi` fails at runtime —
the classic failure mode of an sdist/Git source install that registers distribution metadata without
placing an importable package (PyPI ships no wheel for pyaqsapi, so pip builds from source). The fix
is to use the prebuilt conda-forge package instead:

```diff
   - dask
+  - pyaqsapi
-  - pip:
-      - git+https://github.com/USEPA/pyaqsapi.git
   - mystmd
```

`pyaqsapi` is on conda-forge as `1.0.2`, `noarch`, requiring `python>=3.10` — compatible with this
image's Python 3.10, and it removes the fragile source build entirely (the `pip:` block existed only
for this one entry).

## What was verified

- **The failing import** (`import pyaqsapi as aqs`, cell `In[1]`) and error, from the notebook and
  live record.
- **`pyaqsapi` is declared via `git+…`** in `environment.yml`'s pip block (not missing), and the build
  `exit_code` was 0 with `pyaqsapi 1.0.2 pypi_0` in the conda list — yet the import fails.
- **`pyaqsapi 1.0.2` is on conda-forge** (`noarch`, `python>=3.10`) and on PyPI (**sdist only, no
  wheel** — hence source builds).
- **The other three notebooks executed cleanly** using conda-forge packages that are present,
  confirming the kernel/env is otherwise correct and `pyaqsapi` is the single broken dependency.
- **Not verified:** the exact reason the source build produced no importable module (would need an env
  rebuild). The conda-forge fix sidesteps the cause regardless.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
