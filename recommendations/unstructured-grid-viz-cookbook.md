# unstructured-grid-viz-cookbook — Recommendations

Live outcome: **build failed** (30m 00s — hit the timeout). [← All recommendations](../recommendations.md) · [Live check](../reports/live/unstructured-grid-viz-cookbook.md) · [Repository](https://github.com/ProjectPythia/unstructured-grid-viz-cookbook)

Static tier `healthy`. **The environment is fast and healthy; the 30-minute timeout was not a dependency problem.**

## What this failure is not

Reproduced locally with `mamba`:

- `mamba env create --dry-run` **solves in ~15 seconds** (368 packages, 312 MB).
- A full `mamba env create` **builds end-to-end in ~52 seconds**, exit 0, including the pip step.

An environment that resolves in 15 s and builds in under a minute did not cause a 30-minute build
timeout. The most likely culprit is infrastructure — a slow or stalled repo2docker/image-push on
BinderHub, of exactly the kind seen elsewhere in these checks. (During the local build one package,
`panel-core`, even returned a transient partial-download that auto-retried — the same flakiness that
can compound into a timeout on a shared builder.)

**First action: re-run the live check.** It will very likely build well within the limit.

## Durable improvements (worth doing regardless)

Even though the env is healthy, three items reduce risk and align with the
[criteria](../docs/criteria.md):

1. **Remove `pathlib`.** This is the obsolete PyPI/conda backport pinned at `1.0.1` — a package that
   *shadows the Python standard library's own `pathlib`*. `pathlib` has been in the stdlib since
   Python 3.4; the backport is unnecessary on every supported interpreter and is a well-known trap
   that can cause subtle import breakage. Nothing needs it. Delete the line.

2. **Remove `sphinx-pythia-theme`.** Dead doc-build cruft from the Sphinx era — the cookbook builds
   with `jupyter-book`/`mystmd`. It bloats the image for no runtime purpose.

3. **Move `antimeridian` from pip to conda.** It is packaged on conda-forge (`0.4.8`), so the entire
   `pip:` block can go, and the build no longer needs pip at all.

```diff
   numpy
-  - pathlib
   - pip
   - pre_commit
   - pyarrow
   - pytest
   - pytest-cov
   - requests
   - scikit-learn
   - scipy
   - shapely
   - spatialpandas
-  - sphinx-pythia-theme
   - uxarray
   - xarray
+  - antimeridian
-  - pip:
-      - antimeridian
```

## What was verified

- **Env solves in ~15 s and builds in ~52 s locally** (`mamba`, exit 0) — not the cause of the
  30-minute timeout.
- **`pathlib` on conda-forge/PyPI is the `1.0.1` stdlib backport**, confirmed by querying both
  indices; it is safe to remove.
- **`antimeridian` is on conda-forge** (`0.4.8`), so it can move out of pip.
- **Not verified:** the exact reason the Binder build reached 30 minutes (no access to that build's
  full logs). The local evidence says the environment is not responsible.

## Secondary

- `pre_commit`, `pytest`, and `pytest-cov` are developer tooling in the runtime env; move them to a
  dev environment to slim the image further.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm in a real build and open with the
community, not an applied change.*
