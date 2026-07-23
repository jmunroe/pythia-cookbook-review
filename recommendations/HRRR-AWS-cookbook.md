# HRRR-AWS-cookbook — Recommendations

Live outcome: **ran clean**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/HRRR-AWS-cookbook.md) · [Repository](https://github.com/ProjectPythia/HRRR-AWS-cookbook)

Static tier `healthy`. **Builds and runs clean — the one item below is minor housekeeping toward the [publication criteria](../docs/criteria.md), not a failure.**

This cookbook is in good shape and close to a model of the criteria: conda-forge only, no pip, no
version pins, no Sphinx cruft, no template links. DOI, release, ORCID, citation, license, thumbnail
and real tags are all present, and the single notebook ran clean on Binder in ~28 s at 7% of the
memory limit. There is one small item.

## Housekeeping

1. **Drop the leftover `jupyter-book` dependency.** `environment.yml` still lists the classic
   (Sphinx-based) `jupyter-book` build tool alongside `mystmd`:

   ```
   - jupyter-book
   ```

   Pythia's cookbooks now build with `mystmd` — the repo carries a `myst.yml` and its nightly builds
   green through `cookbook-actions`. The classic `jupyter-book` package is the modern analog of the
   already-flagged Sphinx-era dead weight: it is no longer part of the build and only adds solve time
   and surface area to the environment. Remove it unless a notebook actually imports it:

   ```diff
   -  - jupyter-book
   ```

## What was verified

- **The environment is clean** — single `conda-forge` channel, `pip_dep_count: 0`, `pinned_count: 0`,
  no `sphinx_deps`, no template links — read from the current `environment.yml` and the static audit.
- **Metadata is complete** — DOI, release `v2026.3.30`, ORCID, citation, license, thumbnail, real
  tags (static audit).
- **The notebooks carry standard `python3` kernelspecs** (scanned all `*.ipynb`) — no latent
  execution time-bomb.
- **The live check ran clean** — build and execution both exit 0, one toc notebook, peak 0.62 GB
  (7% of the 8.6 GB limit); 2026-07-21 snapshot.
- **Not verified:** whether anything imports `jupyter-book`. It is almost certainly unused now that
  the build is MyST, but confirm with a quick import scan before removing.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
