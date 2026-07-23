# Aerosol-Cloud-Interactions-cookbook — Recommendations

Live outcome: **ran clean**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/Aerosol-Cloud-Interactions-cookbook.md) · [Repository](https://github.com/ProjectPythia/Aerosol-Cloud-Interactions-cookbook)

Static tier `healthy`. **Builds and runs clean — the items below are minor housekeeping toward the [publication criteria](../docs/criteria.md), not failures.**

This cookbook runs clean, but it still carries a fair amount of the template's default scaffolding:
two undocumented exact pins, dead Sphinx-era dependencies, template links throughout, no real
Zenodo DOI or release, and a `CITATION.cff` that does not parse. Kernelspecs are all clean (`python3`).

## Housekeeping

1. **Document or relax the two exact pins.** `environment.yml` hard-pins two packages, with no comment
   explaining why:

   ```
   - intake==0.7.0
   - intake-xarray==0.7.0
   ```

   These are the strongest kind of pin (`==`), and they lag far behind conda-forge (`intake` is at
   `2.0.9`, `intake-xarray` at `2.0.0`). The `intake` catalog API changed substantially between 0.x and
   2.x, so these pins are very likely load-bearing — the notebooks probably use the old API. The
   community asks that pins be **documented**. Add a one-line comment on each explaining the reason
   (e.g. "0.x catalog API"), or confirm the notebooks work against current `intake` and drop them:

   ```diff
   -  - intake==0.7.0
   -  - intake-xarray==0.7.0
   +  - intake==0.7.0        # pinned to 0.x catalog API used by the notebooks — confirm before relaxing
   +  - intake-xarray==0.7.0 # same
   ```

2. **Remove the dead Sphinx-era dependencies.** `environment.yml` lists `sphinx-pythia-theme` and
   `jupyter-book`. The repo builds with MyST (`myst.yml` is present), so these are leftovers from the
   pre-MyST toolchain and are never used. Drop them:

   ```diff
   -  - jupyter-book
   -  - sphinx-pythia-theme
   ```

   (`jupyterlab` is also listed twice — a harmless duplicate that can be collapsed to one line.)

3. **Replace the template links.** The repo still points at `cookbook-template` in several places:
   - `myst.yml` — `title: Project Pythia Cookbook Template`, `github: .../cookbook-template`, and the
     Binder `repo: projectpythia/cookbook-template`.
   - `README.md` — the nightly-build and Binder badges target `ProjectPythia/cookbook-template`.
   - `notebooks/how-to-cite.md` — links the source to `ProjectPythia/cookbook-template`.
   - `CITATION.cff` — a `"Cookbook Template contributors"` entry.

   These should be updated to this cookbook's own repo (`Aerosol-Cloud-Interactions-cookbook`).

4. **Add a real Zenodo DOI and a GitHub release.** The DOI badge in `README.md` and `how-to-cite.md`
   points at Zenodo record `475509405`, which is the **cookbook-template's** DOI, not this cookbook's.
   There are no release tags. Cut a GitHub release and mint a per-cookbook Zenodo DOI, then update the
   badge.

5. **Fix the malformed `CITATION.cff`.** The file does not parse as YAML — the author entries have
   inconsistent indentation (e.g. a `-family-names:` with no space after the dash, and dash columns that
   shift between entries). ORCIDs are present for most authors, but the file as written cannot be
   consumed by citation tooling. Re-indent it so it validates.

## What was verified

- **The two pins** `intake==0.7.0` and `intake-xarray==0.7.0`, undocumented, read from the current
  `environment.yml`; conda-forge latest is `intake 2.0.9` / `intake-xarray 2.0.0`.
- **No pip dependencies** — nothing to move to conda.
- **`sphinx-pythia-theme` and `jupyter-book` are dead** — `myst.yml` is present and is the active build
  config.
- **Template links** in `myst.yml`, `README.md`, `how-to-cite.md`, and `CITATION.cff` (grep).
- **DOI badge `475509405` is the template's**, not this cookbook's; no release tags (`git tag` empty).
- **`CITATION.cff` fails to parse** (YAML load error) but does contain ORCIDs — so the "no ORCID / no
  CITATION" snapshot flags are dropped; the actionable item is the malformed indentation.
- **All notebook kernelspecs are `python3`** (glob over `**/*.ipynb`) — no latent kernelspec issue.
- **Not verified:** whether the notebooks actually require `intake` 0.x — that is the author's call; the
  recommendation is to document the reason or confirm they can float.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
