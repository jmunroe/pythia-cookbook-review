# web-map-feature-services-cookbook — Recommendations

Live outcome: **ran clean**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/web-map-feature-services-cookbook.md) · [Repository](https://github.com/ProjectPythia/web-map-feature-services-cookbook)

Static tier `healthy`. **Builds and runs clean — the items below are minor housekeeping toward the [publication criteria](../docs/criteria.md), not failures.**

This cookbook is effectively pristine on the substantive criteria: `environment.yml` is conda-forge only with
no version pins and no pip block, DOI present (badge `653301659`), two GitHub releases (latest `v2026.3.30`),
an ORCID-bearing `CITATION.cff`, all four notebooks on the standard `python3` kernelspec, and no Sphinx-era
files. Only one leftover template link remains.

## Housekeeping

1. **Fix the one leftover template link.** The Binder badge in `README.md` still points at the template repo:

   ```diff
   -[![Binder](https://binder.projectpythia.org/badge_logo.svg)](https://binder.projectpythia.org/v2/gh/ProjectPythia/cookbook-template/main?labpath=notebooks)
   +[![Binder](https://binder.projectpythia.org/badge_logo.svg)](https://binder.projectpythia.org/v2/gh/ProjectPythia/web-map-feature-services-cookbook/main?labpath=notebooks)
   ```

   Everything else already references the real repo — `myst.yml` `github:` is correct and the DOI/nightly-build
   badges point at this repository. (The `cookbook-template` string in `.github/workflows/replace-links.yaml`
   is the expected find-target of the link-replacement workflow, not a stray link.)

2. **(Minor) Rename the environment.** The env is named `web-map-feature-services-cookbook-dev`; the `-dev`
   suffix is the template default. Trimming it to `web-map-feature-services-cookbook` is purely cosmetic.

## What was verified

- **The one template link** — the `README.md` Binder badge targeting `ProjectPythia/cookbook-template` —
  located by grep across `README.md`, `myst.yml`, and `.github/`; no other stray `cookbook-template` links.
- **`environment.yml` is conda-forge only, no pins, no pip block** — read directly.
- **DOI badge, two GitHub releases (latest `v2026.3.30`), and an ORCID** in `CITATION.cff` — confirmed present
  (README badge, `gh api` releases, `CITATION.cff`).
- **All 4 notebooks use `python3` kernelspec**; `myst.yml` present, no Sphinx cruft.
- **Not verified:** nothing material outstanding — the cookbook is essentially publication-ready aside from
  the single Binder badge URL.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
