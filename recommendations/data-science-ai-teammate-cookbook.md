# data-science-ai-teammate-cookbook — Recommendations

Live outcome: **ran clean**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/data-science-ai-teammate-cookbook.md) · [Repository](https://github.com/ProjectPythia/data-science-ai-teammate-cookbook)

Static tier `healthy`. **Builds and runs clean — the items below are minor housekeeping toward the [publication criteria](../docs/criteria.md), not failures.**

This cookbook is on the MyST build (`myst.yml` present) and its `environment.yml` is clean:
conda-forge only, **no pins, no pip deps, no Sphinx cruft**. All notebooks carry the standard
`python3` kernelspec. A Zenodo DOI is present. The open items are leftover template links and a
GitHub release.

## Housekeeping

1. **Fix the template links.** The repo still points at the template in four places:

   ```
   myst.yml:7    github: https://github.com/projectpythia/cookbook-template
   myst.yml:32   repo: projectpythia/cookbook-template        # thebe/binder config
   README.md:25  .../ProjectPythia/cookbook-template/actions/workflows/nightly-build.yaml...
   README.md:26  .../v2/gh/ProjectPythia/cookbook-template/main?labpath=notebooks
   ```

   Repoint all four to `ProjectPythia/data-science-ai-teammate-cookbook`. (The `cookbook-template`
   string in `.github/workflows/trigger-replace-links.yaml` is the standard `find:` pattern — leave
   it.)

2. **Cut a tagged GitHub release.** A Zenodo DOI badge is present in the README, but the repo has no
   release/tag. Tag a release so the archived version matches the citation.

3. **(Minor) Check one ORCID entry in `CITATION.cff`.** The first author's ORCID is stored as
   `https://orcid.org/my-orcid?orcid=0009-0009-9651-341X` — a copied "my-orcid" URL rather than the
   canonical `https://orcid.org/0009-0009-9651-341X` form. Replace it with the plain ORCID URL. The
   remaining ORCIDs are well-formed.

## What was verified

- **`environment.yml`** — read from the current clone: conda-forge only, no pins, no pip section, no
  `sphinx-*` deps.
- **MyST build** — `myst.yml` present; no `_config.yml` / `_toc.yml`.
- **Kernelspecs** — all notebooks under `notebooks/` are `python3`. (A leftover
  `notebooks/notebook-template.ipynb` exists but is not in the `myst.yml` toc, so it is harmless.)
- **Template links** — `myst.yml` lines 7 and 32, README lines 25–26.
- **Metadata** — Zenodo DOI present; ORCIDs present (one malformed as noted); **no GitHub release**.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
