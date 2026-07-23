# thermodynamic-budgets — Recommendations

Live outcome: **ran clean**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/thermodynamic-budgets.md) · [Repository](https://github.com/ProjectPythia/thermodynamic-budgets)

Static tier `healthy`. **Builds and runs clean — the items below are minor housekeeping toward the [publication criteria](../docs/criteria.md), not failures.**

The notebooks build and run, use the standard `python3` kernelspec, and there are no Sphinx-era files.
However this repo still carries a fair amount of un-customized template scaffolding, and it has no GitHub
release and no genuine Zenodo DOI. Three items below.

## Housekeeping

1. **Move the one pip dependency to conda.** `environment.yml` installs a single package via pip that **is**
   available on conda-forge (`xarray-regrid`, latest `0.4.2`):

   ```diff
      dependencies:
        ...
   -    - pip
   -    - pip:
   -      - xarray-regrid
   +    - xarray-regrid
   ```

   Installing it from conda-forge keeps the whole environment on one solver and drops the pip stage entirely.

2. **Replace the leftover template links.** Several references still point at `cookbook-template` instead of
   this repository:

   - `README.md` — the nightly-build and Binder badges both target
     `ProjectPythia/cookbook-template/...`, and the boilerplate line *"See the Cookbook Contributor's Guide
     for step-by-step instructions on how to create your new Cookbook…"* is template text that should be
     removed from a published cookbook.
   - `myst.yml` — `jupyter.binder.repo: projectpythia/cookbook-template` should be
     `projectpythia/thermodynamic-budgets`.
   - `CITATION.cff` — the organizational author is still `"Cookbook Template contributors"`; update it to the
     Thermodynamic Budgets contributors.

3. **Add a GitHub release and a real Zenodo DOI.** The repo has **zero** GitHub releases. The DOI badge in
   `README.md` (`zenodo.org/badge/475509405.svg`) is **not** this cookbook's DOI — badge id `475509405` is
   the GitHub repo id of `cookbook-template`, whereas `thermodynamic-budgets` is repo id `1032750558`. So the
   badge is another leftover template link masquerading as a DOI. Cut a GitHub release, enable the Zenodo
   integration for *this* repo, and replace the badge with the resulting DOI.

## What was verified

- **The single pip dep** `xarray-regrid` against conda-forge (`api.anaconda.org`): available, latest `0.4.2`.
- **Template links** located by grep in `README.md`, `myst.yml`, and `CITATION.cff`; the `cookbook-template`
  string in `.github/workflows/trigger-replace-links.yaml` is the expected find-target, not a stray link.
- **No GitHub releases** (`gh api repos/ProjectPythia/thermodynamic-budgets/releases` → 0) and the README DOI
  badge id resolves to `cookbook-template`, not this repo (`gh api` id comparison).
- **Both notebooks use `python3` kernelspec**, `myst.yml` is present (no Sphinx cruft), and there are no
  version pins in the conda dependency list.
- **Not verified:** whether the authors intend a Zenodo archive — the recommendation flags the objective gap
  (no release, no repo-specific DOI); creating one is their call.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
