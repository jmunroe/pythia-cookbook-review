# bayesian-mcmc-cookbook — Recommendations

Live outcome: **ran clean**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/bayesian-mcmc-cookbook.md) · [Repository](https://github.com/ProjectPythia/bayesian-mcmc-cookbook)

Static tier `healthy`. **Builds and runs clean — the items below are minor housekeeping toward the [publication criteria](../docs/criteria.md), not failures.**

This cookbook is effectively pristine on the code side: `environment.yml` is conda-forge only with
**no version pins, no pip deps, and no Sphinx cruft**; it already builds with MyST (`myst.yml`
present); all five notebooks carry the standard `python3` kernelspec; and there are no leftover
template links (the only `cookbook-template` string is the expected `find:` pattern inside
`.github/workflows/trigger-replace-links.yaml`, which is standard machinery, not a stray link).
`CITATION.cff` is present and includes an ORCID. The only open items are archival metadata.

## Housekeeping

1. **Mint a Zenodo DOI.** The README has no DOI badge and `CITATION.cff` carries no DOI identifier.
   The publication criteria ask for a citable archive. Enable the Zenodo–GitHub integration for the
   repo so future releases are archived and a DOI is issued, then add the DOI badge to the README.

2. **Cut a tagged GitHub release.** The repo has no releases (no tags). A tagged release gives the
   Zenodo integration something to archive and provides a stable citation point. These two items go
   together: create the release, and Zenodo mints the DOI.

## What was verified

- **`environment.yml`** — read from the current clone: conda-forge only, no pins, no pip section, no
  `sphinx-*` deps.
- **MyST build** — `myst.yml` present; no `_config.yml` / `_toc.yml` / `_static` / `_templates`.
- **Kernelspecs** — all 5 notebooks under `notebooks/` are `python3`.
- **Template links** — none beyond the standard `trigger-replace-links.yaml` machinery.
- **Metadata** — `CITATION.cff` present with ORCID; **no Zenodo DOI** and **no GitHub release**.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
