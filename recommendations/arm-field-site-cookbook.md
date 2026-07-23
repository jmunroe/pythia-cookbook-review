# arm-field-site-cookbook — Recommendations

Live outcome: **execution failed** (build now succeeds). [← All recommendations](../recommendations.md) · [Live check](../reports/live/arm-field-site-cookbook.md) · [Repository](https://github.com/ProjectPythia/arm-field-site-cookbook)

Static tier `incubating`. **A live re-check on 2026-07-23 built the image successfully for the first
time — so the build failure was the transient/oversized-image fragility described below, not a broken
environment. With the build out of the way, the real blocker is now visible: execution fails
immediately on a non-standard kernel.**

## The one change that matters

**Reset the notebook kernelspecs to the standard `python3`.** The re-check's build finished (exit 0,
~22 min) and then execution failed in **13 seconds with zero cells run**:

```
The 'conda-base-py' kernel is not available. Please pick another suitable kernel instead, or install that kernel.
```

Four notebooks were saved on an author's JupyterHub and carry that hub's kernel name in their
metadata, which does not exist in the Binder image:

- `foundations/xarray/dask-xarray-demo.ipynb`
- `foundations/pyart/pyart-basics.ipynb`
- `projects/bnf-2025/bnf-deep-convection/coldpool-radar-analysis.ipynb`
- `projects/bnf-2025/bnf-deep-convection/coldpool-time-series.ipynb`

`myst build --execute` — the same command Pythia's nightly uses — aborts the whole run at the first
one. Rewrite each notebook's `metadata.kernelspec` to the standard:

```json
{"display_name": "Python 3 (ipykernel)", "language": "python", "name": "python3"}
```

(`jupyter nbconvert --to notebook --inplace` after setting the kernel, or a one-line `jq`/script over
the four files, does it.) This is the single change that takes the cookbook from *cannot execute at
all* to *runs*.

## Secondary

1. **Fix the broken table-of-contents entry.** `myst.yml` line 25 lists
   `foundations/pyart/pyart-gatefilers.ipynb`, but the file is spelled
   `pyart-gatefil**t**ers.ipynb`. MyST logged `Table of contents entry does not exist` and dropped it,
   so that notebook is silently missing from the built book:

   ```diff
   -            - file: foundations/pyart/pyart-gatefilers.ipynb
   +            - file: foundations/pyart/pyart-gatefilters.ipynb
   ```

   (The same `toc` block also drew `missing required key: children` schema warnings and an ignored
   `binder` key — worth a tidy pass while in there.)

2. **Trim the oversized environment — the durable build fix.** The build now succeeds, but it took
   ~22 minutes because the env is **489 packages / ~4 GB**, most of it a machine-learning stack no
   notebook imports. Removing it makes the launch button fast and the build far less likely to fail
   the next time the registry hiccups. Verified locally (`mamba`): the current env solves cleanly
   (489 pkgs) and an import scan of all 16 notebooks shows `tensorflow`, `tensorflow-probability`,
   `jaxopt`, `jax`, `pydda`, `tobac`, and `cookiecutter` are **never imported**, while `pyart`,
   `act`, `xradar`, and `xwrf` are:

   ```diff
    dependencies:
      - python=3.11
      - mystmd
   -  - cookiecutter
      - act-atmos
      - jupyterlab
      - arm_pyart
      - cartopy
      - matplotlib
   -  - pydda
   -  - jaxopt
   -  - tensorflow>=2.6
      - xradar
   -  - tensorflow-probability>=0.24
      - xwrf
   -  - tobac
      - plotly
   ```

   The trimmed env solves to **389 packages** (100 fewer) and drops the multi-gigabyte TensorFlow/JAX/
   pyDDA download. Re-add a single package only if a future notebook needs it.

## What was verified

- **Build now succeeds on Binder** — 2026-07-23 live re-check, exit 0, image not cached, ~1340 s.
  The earlier "build failed" was the fragility of pulling a ~4 GB image, not a dependency conflict.
- **Execution fails immediately** on the `conda-base-py` kernel — reproduced on that same live run
  (13.45 s, 0 cells executed). The four affected notebooks were confirmed by scanning every
  `*.ipynb`'s kernelspec on the clone.
- **The toc typo is real** — `myst.yml` references `pyart-gatefilers.ipynb`; the file on disk is
  `pyart-gatefilters.ipynb`.
- **The env trim is safe** — current env solves (489 pkgs), trimmed env solves (389 pkgs), and the
  removed packages are unimported across all 16 notebooks (local `mamba` + import scan).
- **Not verified:** a full clean execution pass *after* the kernelspec fix — the ARM credential
  injection worked on the re-check, but the run never reached a data-access cell because the kernel
  error aborted it first. Fix the kernelspecs and re-run to see what, if anything, lies behind them.

---
*Agent-assisted analysis, updated 2026-07-23 after a live re-check that built the image and exposed
the kernelspec blocker (supersedes the earlier build-failure note). A proposal to confirm in a real
build and open with the community, not an applied change.*
