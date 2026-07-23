# atmos-modeling-cookbook — Recommendations

Live outcome: **ran clean**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/atmos-modeling-cookbook.md) · [Repository](https://github.com/ProjectPythia/atmos-modeling-cookbook)

Static tier `healthy`. **Builds and runs clean — the items below are minor housekeeping toward the [publication criteria](../docs/criteria.md), not failures.**

This cookbook is in good shape: no version pins, conda-forge only, no pip, a customized `myst.yml`, and a
`CITATION.cff` full of ORCIDs. Kernelspecs are all clean (`python3`). The remaining items are one dead
legacy build dependency, a couple of template links, and the missing DOI/release.

## Housekeeping

1. **Remove the dead legacy build dependency.** `environment.yml` lists `jupyter-book` alongside
   `mystmd`. The repo builds with MyST (`myst.yml` is present), so `jupyter-book` is a leftover from the
   pre-MyST toolchain and is never used. Drop it:

   ```diff
   -  - jupyter-book
   ```

2. **Replace the remaining template links.** `myst.yml` is already customized to this cookbook, but a few
   template references remain:
   - `README.md` — the nightly-build and Binder badges target `ProjectPythia/cookbook-template`.
   - `notebooks/how-to-cite.md` — links the source to `ProjectPythia/cookbook-template`.
   - `CITATION.cff` — a `"Cookbook Template contributors"` entry, and the abstract is still the template
     placeholder `"Add a description when done!"`.

   Update these to this cookbook's own repo and fill in the abstract.

3. **Add a real Zenodo DOI and a GitHub release.** The DOI badge in `README.md` and `how-to-cite.md`
   points at Zenodo record `475509405`, which is the **cookbook-template's** DOI, not this cookbook's.
   There are no release tags. Cut a release and mint a per-cookbook DOI, then update the badge.

## What was verified

- **No version pins** in `environment.yml` — nothing to document there.
- **No pip dependencies** — nothing to move to conda.
- **`jupyter-book` is dead** — `myst.yml` is present and is the active build config; `mystmd` is already
  in the environment.
- **Template links**: `myst.yml` is clean (points at `atmos-modeling-cookbook`), but `README.md`,
  `how-to-cite.md`, and a `CITATION.cff` entry still reference `cookbook-template` (grep).
- **DOI badge `475509405` is the template's**, not this cookbook's; no release tags (`git tag` empty).
- **`CITATION.cff` is populated with ORCIDs** — no metadata gap beyond the DOI/release and the
  placeholder abstract.
- **All notebook kernelspecs are `python3`** (glob over `**/*.ipynb`) — no latent kernelspec issue.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
