# BiasCorrectionCrowdsourcedData-cookbook — Recommendations

Live outcome: **ran clean**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/BiasCorrectionCrowdsourcedData-cookbook.md) · [Repository](https://github.com/ProjectPythia/BiasCorrectionCrowdsourcedData-cookbook)

Static tier `healthy`. **Builds and runs clean — the items below are minor housekeeping toward the [publication criteria](../docs/criteria.md), not failures.**

This cookbook runs clean and is in reasonable shape: conda-forge only, no pip, no Sphinx cruft, a clean
`CITATION.cff` with an ORCID. The remaining items are one undocumented pin, the template links, the
missing DOI/release, and one leftover template notebook with a non-standard kernelspec.

## Housekeeping

1. **Document or relax the Python pin.** `environment.yml` pins the interpreter minor version, with no
   comment:

   ```
   - python=3.11
   ```

   The community asks that pins be avoided except where needed, and **documented** where they remain.
   If a specific dependency requires 3.11, add a one-line comment saying so; otherwise relax it (e.g. a
   floor `python>=3.11`, or drop it) so the environment can track newer interpreters:

   ```diff
   -  - python=3.11
   +  - python>=3.11   # or drop, unless a dependency needs exactly 3.11 — then say which
   ```

2. **Replace the template links.** The repo still points at `cookbook-template`:
   - `myst.yml` — `title: Project Pythia Cookbook Template`, `github: .../cookbook-template`, and the
     Binder `repo: projectpythia/cookbook-template`.
   - `README.md` — the nightly-build badge and the contributors image both target
     `ProjectPythia/cookbook-template`.
   - `notebooks/how-to-cite.md` — links the source to `ProjectPythia/cookbook-template`.

   Update these to this cookbook's own repo.

3. **Add a real Zenodo DOI and a GitHub release.** The DOI badge in `README.md` and `how-to-cite.md`
   points at Zenodo record `475509405`, which is the **cookbook-template's** DOI, not this cookbook's.
   There are no release tags. Cut a release and mint a per-cookbook DOI, then update the badge.

4. **Normalize (or remove) the leftover template notebook's kernelspec.** One notebook carries a
   non-standard kernelspec that will fail to execute if it ever enters the executed toc:

   ```
   notebooks/template_createnewIPYNB.ipynb  ->  kernelspec.name = "biascorr-cookbook-dev"
   ```

   This is a template scaffolding notebook (alongside `notebook-template.ipynb` and
   `notebook-template2.ipynb`) and is not in the toc, so it is a latent time-bomb rather than a live
   failure. Either delete these template leftovers, or normalize the kernelspec to the standard:

   ```json
   {"name": "python3", "display_name": "Python 3 (ipykernel)", "language": "python"}
   ```

## What was verified

- **The single pin** `python=3.11`, undocumented, read from the current `environment.yml`.
- **No pip dependencies** — nothing to move to conda.
- **No Sphinx deps or files** — `myst.yml` is present; nothing to remove.
- **Template links** in `myst.yml`, `README.md`, and `how-to-cite.md` (grep).
- **DOI badge `475509405` is the template's**, not this cookbook's; no release tags (`git tag` empty).
- **`CITATION.cff` is clean and contains an ORCID** — no metadata gap there beyond the DOI/release.
- **Kernelspecs** (glob over `**/*.ipynb`): all `python3` except
  `notebooks/template_createnewIPYNB.ipynb` (`biascorr-cookbook-dev`), which confirms the prior sweep's
  finding.
- **Not verified:** whether any dependency actually requires Python 3.11 — that is the author's call.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
