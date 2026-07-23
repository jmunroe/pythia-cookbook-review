# wavelet-cookbook — Recommendations

Live outcome: **ran clean**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/wavelet-cookbook.md) · [Repository](https://github.com/ProjectPythia/wavelet-cookbook)

Static tier `healthy`. **Builds and runs clean — the items below are minor housekeeping toward the [publication criteria](../docs/criteria.md), not failures.**

This cookbook is in good shape on metadata: DOI present (badge `815311051`), three GitHub releases (latest
`v2026.03.30`), an ORCID-bearing `CITATION.cff`, all six notebooks on the standard `python3` kernelspec, and
no template links (the only `cookbook-template` string is the find-target in the standard
`trigger-replace-links.yaml` workflow). The one real item is leftover Sphinx-era build dependencies.

## Housekeeping

1. **Remove the dead Sphinx build dependencies.** `environment.yml` still lists the pre-MyST toolchain even
   though the repo now builds with mystmd (`myst.yml` is present and `mystmd` is already in the environment):

   ```diff
      dependencies:
   -    - jupyter-book
        - jupyterlab
        - geocat-datafiles
   -    - sphinx-pythia-theme
        - numpy
        ...
        - mystmd
   ```

   `sphinx-pythia-theme` and `jupyter-book` are the old Jupyter Book / Sphinx stack; with the MyST build they
   are never invoked and only bloat the solve. (`nodejs` is likewise a Sphinx/Jupyter-Book-era leftover —
   mystmd bundles its own Node runtime — so it can usually go too; confirm nothing else in the build calls it
   before removing.)

2. **(Minor) Rename the environment.** The env is named `cookbook-dev`, the generic template default. Renaming
   it to `wavelet-cookbook` avoids collisions with other cookbooks' dev environments. Purely cosmetic.

## What was verified

- **The Sphinx dependencies** `sphinx-pythia-theme` and `jupyter-book` (plus `nodejs`) — read from the current
  `environment.yml`; `myst.yml` present and `mystmd` in the environment, confirming the build no longer uses
  the Sphinx stack (so these are dead cruft).
- **No pip dependencies and no version pins** in `environment.yml`.
- **DOI badge, three GitHub releases (latest `v2026.03.30`), and an ORCID** in `CITATION.cff` — confirmed
  present (README badge, `gh api` releases, `CITATION.cff`).
- **All 6 notebooks use `python3` kernelspec**; no leftover `conf.py` / `_config.yml` / `_toc.yml`.
- **Not verified:** whether any part of the build still shells out to `nodejs` independently of mystmd — hence
  the "confirm before removing" note on that one line.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
