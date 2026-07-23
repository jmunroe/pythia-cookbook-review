# eo-datascience-cookbook — Recommendations

Live outcome: **build failed**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/eo-datascience-cookbook.md) · [Repository](https://github.com/ProjectPythia/eo-datascience-cookbook)

Static tier `healthy`. **The environment builds end-to-end locally — conda *and* every pip package — so the failure was most likely transient, aggravated by a slow, oversized pip step.**

## What was reproduced

Rebuilt the full environment locally with `mamba`:

- **Conda solve succeeds** — `mamba env create --dry-run` resolves cleanly (595 packages, 407 MB).
- **The pip step succeeds too.** Reproducing Binder's exact `mamba env update … --file
  environment.yml` runs the `pip:` block and installs everything — `ascat`, `pdbufr`, `pynetcf`,
  `pyswi`, `python-dotenv`, `python-gitlab`, `pyviz_comms==3.0.4`, and the local `envrs` package
  (built from `notebooks/courses/environmental-remote-sensing`). Exit 0; all of them import in the
  finished environment.

So nothing in the environment is actually broken. The build log tail stops right after conda linking
with only the generic `docker buildx … exit status 1` and **no pip error** — consistent with a
transient failure (network, or a registry push) during or just after the long pip step, not a
dependency conflict.

## The durable fix: shrink and speed up the pip step

The pip block is the slow, fragile part of this build — pip resolving `ascat`, `pynetcf`, `pyswi`,
and `pdbufr` pulls a heavy scientific stack (`pyresample`, `pint`, …) and builds a wheel, taking
several minutes. Most of it doesn't need to be pip at all. **Four of the seven pip packages are on
conda-forge:**

| pip package | conda-forge | action |
|---|---|---|
| `pdbufr` | 0.14.2 | move to conda deps |
| `python-dotenv` | 1.2.2 | move to conda deps |
| `python-gitlab` | 8.4.0 | move to conda deps |
| `pyviz_comms==3.0.4` | 3.0.6 | move to conda deps (and drop the exact pin) |
| `ascat` | — | keep in pip (not packaged) |
| `pynetcf` | — | keep in pip (not packaged) |
| `pyswi` | — | keep in pip (not packaged) |
| `notebooks/courses/environmental-remote-sensing` (`envrs`) | — | keep in pip (local package) |

Moving those four to the conda dependency list leaves pip with only the three genuinely pip-only TU
Wien packages plus the local one — a smaller, faster, more reliable pip step, and better alignment
with the [criteria](../docs/criteria.md)'s "prefer conda-forge over pip."

**First action, though: re-run the live check** — the env builds locally, so a retry may simply pass.

## Secondary

- **Slim the runtime environment.** It mixes a developer toolchain into the learner env: `black`,
  `flake8-nb`, `isort`, `nbqa`, `nbstripout`, `pre-commit` (twice — also in pip), `pytest`, and
  `mamba`. None are needed to *run* the notebooks; move them to a dev environment to cut solve time
  and image size.
- **Drop stale exact pins.** `importlib-metadata==4.13.0` is very old (current 8.x) and a frequent
  conflict source; `jupyter==1.1.1`, `jupyterlab==4.2.5`, `jupyterlab_server==2.27.3`,
  `jupyterlab_widgets==3.0.13`, and `pyviz_comms==3.0.4` pin the whole Jupyter stack to exact
  versions. Float these unless a reason is documented.
- **Pre-MyST leftover.** The repo carries both `_config.yml` (Sphinx era) and `myst.yml`; remove the
  stale `_config.yml` — one of the cross-cutting [gaps](../reports/gaps.md).

## What was verified

- Full env builds locally with `mamba` — conda solve + the complete pip step (exit 0); all pip
  packages import.
- Four of the seven pip packages confirmed present on conda-forge (versions above).
- **Not verified:** the exact trigger of the Binder failure — it does not reproduce locally, which
  itself points to transient infrastructure. Confirm with a re-run.

---
*Agent-assisted analysis, updated 2026-07-23 with a full local rebuild (supersedes the earlier
partial note). A proposal to confirm in a real build and open with the community, not an applied
change.*
