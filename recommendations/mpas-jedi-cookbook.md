# mpas-jedi-cookbook — Recommendations

Live outcome: **ran clean**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/mpas-jedi-cookbook.md) · [Repository](https://github.com/ProjectPythia/mpas-jedi-cookbook)

Static tier `healthy`. **Builds and runs clean — the items below are minor housekeeping toward the [publication criteria](../docs/criteria.md), not failures.**

This cookbook is in good shape: it builds with mystmd (`myst.yml` present), has release tags, ORCIDs
on every author, a `CITATION.cff`, no pip dependencies, and no Sphinx cruft. Every notebook carries
the standard `python3` kernelspec. Two small items remain.

## Housekeeping

1. **Document or relax the one exact pin.** `environment.yml` carries a single pin:

   ```
   - python=3.11
   ```

   This is an **exact** pin (the strongest kind — it locks Python to 3.11 and blocks 3.12/3.13), and
   it is undocumented. The community asks authors to avoid pins except where needed, and to document
   the reason for any that remain. Either add a one-line comment on why 3.11 specifically is required
   (e.g. a dependency such as `uxarray` that lagged newer Python), or relax it to a floor if the
   notebooks work against newer releases:

   ```diff
   -  - python=3.11
   +  - python>=3.11    # or keep it exact WITH a comment on why 3.11 is required
   ```

2. **Add a Zenodo DOI.** The repo has release tags (`v0.1.0`, `0.1.1`) but no DOI — `myst.yml` has no
   `doi:` field and `CITATION.cff` carries no DOI entry. Archiving a release to Zenodo and recording
   the DOI satisfies the archive-and-cite criteria rows.

## What was verified

- **The single pin `python=3.11`** (exact) and the absence of comments, pip dependencies, and Sphinx
  deps — read from the current `environment.yml`.
- **Builds with mystmd** (`myst.yml` present); no leftover `conf.py`/`_config.yml`/`_toc.yml` files.
- **Release present but no DOI** (`v0.1.0` and `0.1.1` on the remote; no `doi:` in `myst.yml`, no DOI
  in `CITATION.cff`). **ORCIDs are present** for all authors, and `CITATION.cff` exists.
- **All nine notebooks carry the standard `python3` kernelspec** (glob over `**/*.ipynb`).
- **Not verified:** whether the notebooks actually require Python 3.11 exactly — the author's call;
  the recommendation is to document the reason or relax to a floor.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
