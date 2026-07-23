# interactive-sentinel-2-cookbook — Recommendations

Live outcome: **ran clean**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/interactive-sentinel-2-cookbook.md) · [Repository](https://github.com/ProjectPythia/interactive-sentinel-2-cookbook)

Static tier `healthy`. **Builds and runs clean — the items below are minor housekeeping toward the [publication criteria](../docs/criteria.md), not failures.**

This cookbook builds with mystmd (`myst.yml` present), has a release tag, an ORCID, and no pip
dependencies. Three small items remain.

## Housekeeping

1. **Delete the dead Sphinx dependency.** Because the repo now builds with mystmd, the pre-MyST theme
   in `environment.yml` is dead cruft:

   ```
   - sphinx-pythia-theme
   ```

   It is not used by the MyST build. Remove it:

   ```diff
   -  - sphinx-pythia-theme
    - mystmd
   ```

2. **Document or relax the one undocumented pin.** `environment.yml` carries a single pin:

   ```
   - python>=3.9
   ```

   This is a lower-bound floor (the mildest kind) and a loose one, so it is likely harmless — but it is
   unexplained. Either add a one-line comment on why the floor is needed, or drop it if the notebooks
   work against the current Python:

   ```diff
   -  - python>=3.9
   +  - python          # or keep the floor WITH a comment on why it's needed
   ```

3. **Add a Zenodo DOI.** The repo has a release (`v2026.3.30`) but no DOI — `myst.yml` has no `doi:`
   field and `CITATION.cff` carries no DOI entry. Notably `myst.yml` already contains `error_rules`
   suppressing DOI/Zenodo link validation, which suggests a DOI was intended but never minted.
   Archiving the release to Zenodo and recording the DOI satisfies the archive-and-cite criteria rows.

## What was verified

- **`sphinx-pythia-theme` in `environment.yml`, and the presence of `myst.yml`** — confirming the
  Sphinx dep is dead cruft. No leftover `conf.py`/`_config.yml`/`_toc.yml` files exist.
- **The single pin `python>=3.9`** and the absence of comments and pip dependencies — read from the
  current `environment.yml`.
- **Release present but no DOI** (`v2026.3.30` on the remote; no `doi:` in `myst.yml`, no DOI in
  `CITATION.cff`; `myst.yml` `error_rules` pre-suppress DOI validation). **ORCID is present** for the
  author.
- **The notebook `data-intake-ms-planetary-computer.ipynb` carries the standard `python3` kernelspec**
  (its `display_name` reads `is2-cookbook-dev`, which is cosmetic — the `name` is `python3`, so it is
  not a time-bomb).
- **Not verified:** whether the notebooks actually require `python>=3.9` — the author's call; the
  recommendation is to document the reason or confirm it can float.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
