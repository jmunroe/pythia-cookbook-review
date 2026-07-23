# eo-datascience-cookbook — Recommendations

Live outcome: **build failed**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/eo-datascience-cookbook.md) · [Repository](https://github.com/ProjectPythia/eo-datascience-cookbook)

Static tier `healthy`. **Partial recommendation** — the failure was *not* reproduced from the
captured log, so the top items below are the direction to take rather than a single confirmed diff.

## What this failure is *not*

The build log tail stops right after conda finishes linking (`odc-stac`, `six`) with only the
generic `docker buildx … exit status 1`; the specific error is not in the captured tail. Two obvious
suspects were checked and cleared:

- **The local package installs fine.** `environment.yml` pip-installs a relative path,
  `notebooks/courses/environmental-remote-sensing` (the `envrs` package, `build-backend =
  "uv_build"`, `requires-python >=3.13`). It builds and installs cleanly on Python 3.13 with **plain
  pip** using build isolation — not just with `uv` — so the unusual `uv_build` backend is not the
  problem.
- **Every pip dependency exists.** `ascat`, `pdbufr`, `pynetcf`, `pyswi`, `python-gitlab`, and
  `pyviz_comms` all resolve on PyPI (HTTP 200). No dead pins here.

So the failure is most likely a **resolution conflict** that only appears once conda's full stack is
in place — something the pip step or the final conda solve hits — and it cannot be pinned down
without a real rebuild.

## Recommended direction

1. **Rebuild once with full logs to capture the actual error.** The single most useful next step is
   a Binder (or local `mamba env create`) build that surfaces the failing line the tail truncated.
   Everything below is a strong prior, not a substitute for that.

2. **Slim the runtime environment.** This `environment.yml` mixes a full developer toolchain into
   the learner's runtime env: `black`, `flake8-nb`, `isort`, `nbqa`, `nbstripout`, `pre-commit`,
   `pytest`, and `mamba`. None are needed to *run* the notebooks; each adds solve constraints and a
   chance of conflict. Move them to a separate dev environment (or drop them) so the runtime env has
   only what the notebooks import. A smaller env is both faster and far less likely to fail to solve.

3. **Drop or refresh the stale exact pins.** Several hard pins look like frozen incidental versions
   rather than deliberate constraints:
   - `importlib-metadata==4.13.0` — very old (current 8.x); a frequent source of conflicts on a
     modern Python 3.13 stack. Float it unless a specific package needs 4.x.
   - `jupyter==1.1.1`, `jupyterlab==4.2.5`, `jupyterlab_server==2.27.3`,
     `jupyterlab_widgets==3.0.13`, `pyviz_comms==3.0.4` — pinning the entire Jupyter stack to exact
     versions invites solver conflicts as conda-forge moves. Float these and pin again only where a
     reason is documented, per the [criteria](../docs/criteria.md).
   - `zarr==2.18.4` holds zarr at v2; confirm whether the notebooks actually require v2 or can move
     to v3, and document the reason if v2 is intentional.

4. **`python==3.13` is aggressive.** It is the newest line and some geospatial wheels lag it. If the
   rebuild shows a package with no 3.13 build, relaxing to `python=3.12` is the quickest unblock.

## Secondary

- **Pre-MyST leftover.** The repo carries both `_config.yml` (Sphinx/jupyter-book era) and
  `myst.yml`. The cookbook builds with `mystmd`, so the stale `_config.yml` should be removed — one
  of the cross-cutting [gaps](../reports/gaps.md) across the collection.

## What was verified

- Local `envrs` package builds and installs under real `pip` on Python 3.13 (build isolation
  fetching `uv_build`). Not the cause.
- All six external pip dependencies resolve on PyPI. Not the cause.
- **Not verified:** the actual failing step — no conda/mamba on this machine, and the log tail does
  not contain the error. A rebuild is required to confirm any fix.

---
*Agent-assisted analysis, 2026-07-22. Partial: verified negatives plus recommended direction;
the fix must be confirmed against a real build that captures the failing line.*
