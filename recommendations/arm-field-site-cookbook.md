# arm-field-site-cookbook — Recommendations

Live outcome: **build failed**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/arm-field-site-cookbook.md) · [Repository](https://github.com/ProjectPythia/arm-field-site-cookbook)

Static tier `incubating`. The environment is not broken — it is **oversized**, and that is what makes the build fragile.

## The one change that matters

**Remove the heavy machine-learning packages nothing in the cookbook imports:** `tensorflow`,
`tensorflow-probability`, `jaxopt`, `pydda`, `tobac`, and the build-only `cookiecutter`. They inflate
the image to **489 packages / ~4 GB**, and a 4 GB pull is exactly the kind of build that dies on a
transient download or a resource limit — which is what the 2m 18s failure was.

### The environment solves; the size is the problem

Rebuilt locally with `mamba`:

- `mamba env create --dry-run` on the current `environment.yml` **solves cleanly** — no conflict,
  no missing package. It plans **489 packages, ~4 GB** to download.
- A real `mamba env create` downloads and links those packages successfully on this machine.

So the Binder failure was not a dependency error. It was the fragility of building a 4 GB image:
the log ends right after `mamba` prints its download plan, consistent with a transient failure part
way through pulling ~4 GB of packages (`tensorflow` and `pydda`, which itself pulls in TensorFlow
*and* JAX, account for most of it).

### Most of that weight is never used

Scanning the code cells of all 16 notebooks for imports:

| Imported by notebooks | Never imported |
|---|---|
| `pyart` (7), `act` (6), `xradar` (5), `xwrf` (2) | `tensorflow`, `tensorflow-probability`, `jaxopt`, `jax`, `pydda`, `tobac`, `cookiecutter` |

The cookbook teaches ARM field-site data access with Py-ART, ACT, xradar, and xwrf. The entire ML
stack is dead weight — likely copied from a template or left over from a planned notebook that was
never added.

### Recommended diff

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

`act-atmos` provides the `act` import and `arm_pyart` provides `pyart`, so every package a notebook
actually uses is retained. Removing top-level packages that nothing else depends on cannot break the
solve — the remaining packages already resolved together inside the 489-package solve above.

If a future notebook is planned to use `pydda` or TensorFlow, re-add just that one when the notebook
lands, rather than carrying the whole ML stack now (*useful, not finished* — an absent future
feature is fine; a 4 GB build that fails is not).

## What was verified

- **Current env solves and builds locally** with `mamba` (489 packages, ~4 GB) — the failure is not
  a dependency conflict.
- **Import scan** of all 16 notebooks confirms `tensorflow`, `tensorflow-probability`, `jaxopt`,
  `jax`, `pydda`, `tobac`, and `cookiecutter` are never imported, while `pyart`, `act`, `xradar`,
  and `xwrf` are.
- **Trimmed env solves too:** `mamba env create --dry-run` on the proposed diff resolves to **389
  packages** (100 fewer), and drops the multi-gigabyte TensorFlow/JAX/pyDDA packages that dominate
  the ~4 GB download.
- **Not fully verified:** a full end-to-end build of the trimmed env on Binder plus a notebook
  execution pass. The solve is confirmed; confirm the fresh-download size reduction and clean
  execution on a real build.

## Secondary

- **Re-running the current env may also succeed**, since the failure was transient — but trimming is
  the durable fix that stops it recurring and makes the launch button fast.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm in a real build and open with the
community, not an applied change.*
