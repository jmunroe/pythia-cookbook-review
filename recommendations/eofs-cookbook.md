# eofs-cookbook — Recommendations

Live outcome: **ran clean**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/eofs-cookbook.md) · [Repository](https://github.com/ProjectPythia/eofs-cookbook)

Static tier `healthy`. **Builds and runs clean, and there is nothing to change** — this page is a
clean bill of health against the [publication criteria](../docs/criteria.md), recorded so the review
covers this cookbook explicitly rather than by omission.

This is a model cookbook. Every mechanical criterion is already met:

- **Environment** — single `conda-forge` channel, no pip dependencies, **no version pins at all**,
  no Sphinx-era packages. This is exactly the floating, conda-forge-only environment the community
  asks for, and it solved and ran green.
- **Metadata** — DOI, release `v2026.3.30`, ORCID, citation, license, real title and abstract,
  thumbnail, and real gallery tags are all present.
- **Notebooks** — all four carry the standard `python3` kernelspec, so there is no latent
  execution time-bomb; no template links remain.
- **Live check** — build and execution both exit 0, three toc notebooks, peak 1.43 GB (17% of the
  8.6 GB limit), 2026-07-21 snapshot.

The only items left are the three the community reserves for human judgment — geoscience relevance,
narrative flow, and metadata *appropriateness* (as opposed to mere presence). Those are deliberately
out of scope for these automated recommendation pages; they live in the human-written
[notes](https://github.com/jmunroe/pythia-cookbook-review/tree/main/notes).

## What was verified

- **The environment is clean** — `conda-forge` only, `pip_dep_count: 0`, `pinned_count: 0`, no
  `sphinx_deps` — read from the current `environment.yml` and the static audit.
- **Metadata is complete** — DOI, release, ORCID, citation, license, real title/abstract, thumbnail,
  real tags (static audit).
- **All four notebooks carry standard `python3` kernelspecs** (scanned all `*.ipynb`).
- **The live check ran clean** — build and execution both exit 0; 2026-07-21 snapshot.
- **Not verified (by design):** the three human-judgment criteria above.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
