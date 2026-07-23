# snow-observations-cookbook — Recommendations

Live outcome: **ran clean**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/snow-observations-cookbook.md) · [Repository](https://github.com/ProjectPythia/snow-observations-cookbook)

Static tier `healthy`. **Builds and runs clean — the items below are minor housekeeping toward the [publication criteria](../docs/criteria.md), not failures.**

This cookbook is in good shape on the archive/metadata front: DOI (`10.5281/zenodo.19006079`) and a
GitHub release (`v1.0.0`) are present, the `CITATION.cff` is populated with ORCIDs for many authors, there
are no Sphinx-era files, all ten notebooks carry the standard `python3` kernelspec, and there are no
template links (the only `cookbook-template` string is the find-target inside the standard
`trigger-replace-links.yaml` workflow, which is expected machinery). Two dependency-hygiene items remain.

## Housekeeping

1. **Document or relax the undocumented pins.** `environment.yml` carries two version constraints, neither
   with an explaining comment:

   ```
   - holoviews>=1.15            # conda dep, lower-bound floor
   ...
   pip:
     - uavsar_pytools>=0.7.1, <0.8   # bounded pin
   ```

   The community asks authors to avoid pins except where needed and to **document the reason** for the ones
   that remain. `holoviews>=1.15` is a mild floor and likely harmless; the `uavsar_pytools>=0.7.1, <0.8`
   upper-bound is the more restrictive one and will silently exclude any 0.8+ release. Either add a one-line
   comment on why each bound is needed, or relax it if the notebooks work against the current release:

   ```diff
   -  - holoviews>=1.15
   +  - holoviews          # or keep the floor WITH a comment on why it's needed
   ```

2. **Reconsider the four pip dependencies.** The pip block holds four entries; only one is available on
   conda-forge:

   ```
   pip:
     - git+https://github.com/SnowEx/snowexsql.git@master
     - uavsar_pytools>=0.7.1, <0.8
     - snowmicropyn
     - metloom
   ```

   - `snowexsql` **is** on conda-forge (latest `0.5.0`), but the environment installs it from a moving
     `git@master` ref. If the notebooks do not actually depend on unreleased `master` changes, switch to the
     conda-forge package (`- snowexsql`) for a reproducible, non-moving install; if master *is* required,
     document why next to the git line.
   - `uavsar_pytools`, `snowmicropyn`, and `metloom` are **not** on conda-forge — keep them in pip (pip is a
     flag, not a failure).

## What was verified

- **The two pins** (`holoviews>=1.15`, `uavsar_pytools>=0.7.1, <0.8`) and the absence of comments — read from
  the current `environment.yml`.
- **Each pip dependency against conda-forge** via `api.anaconda.org`: `snowexsql` available (`0.5.0`);
  `uavsar_pytools`, `snowmicropyn`, `metloom` return 404 (not packaged).
- **DOI, GitHub release (`v1.0.0`), and ORCIDs** confirmed present (README badge, `gh api` releases,
  `CITATION.cff`).
- **All 10 notebooks use `python3` kernelspec** and there are no Sphinx-era files (`myst.yml` present).
- **Not verified:** whether the notebooks require the specific version bounds or the `snowexsql` master ref —
  those are the authors' call; the recommendation is to document the reason or confirm each can float.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
