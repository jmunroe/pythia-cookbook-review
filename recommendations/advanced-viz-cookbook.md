# advanced-viz-cookbook — Recommendations

Live outcome: **ran clean**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/advanced-viz-cookbook.md) · [Repository](https://github.com/ProjectPythia/advanced-viz-cookbook)

Static tier `healthy`. **Builds and runs clean — the items below are minor housekeeping toward the [publication criteria](../docs/criteria.md), not failures.**

This cookbook is in good shape: conda-forge only, no pip, DOI and release present, ORCID and citation
present, no template links, no Sphinx cruft. There is one small item.

## Housekeeping

1. **Document or relax the one version pin.** `environment.yml` carries a single undocumented pin:

   ```
   - geocat-viz>=2023.10.0
   ```

   The community asks authors to avoid pins except where needed, and to **document the reason** for the
   ones that remain. This is a lower-bound floor (the mildest kind), so it is likely harmless — but it
   is currently unexplained. Either add a one-line comment saying why the floor is needed (e.g. a
   specific `geocat-viz` feature the notebooks use), or drop it if the notebooks work against the
   current release (`geocat-viz` is at `2025.07.0` on conda-forge):

   ```diff
   -  - geocat-viz>=2023.10.0
   +  - geocat-viz          # or keep the floor WITH a comment on why it's needed
   ```

## What was verified

- **The single pin** `geocat-viz>=2023.10.0` and the absence of comments, pip deps, Sphinx deps, and
  template links — read from the current `environment.yml` and the static audit.
- **DOI, release, ORCID, and citation are all present** (static audit).
- **Not verified:** whether the notebooks actually require `geocat-viz>=2023.10.0` — that is the
  author's call; the recommendation is to document the reason or confirm it can float.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
