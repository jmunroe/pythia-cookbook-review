# feature-tracking-cookbook — Recommendations

Live outcome: **ran clean**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/feature-tracking-cookbook.md) · [Repository](https://github.com/ProjectPythia/feature-tracking-cookbook)

Static tier `healthy`. **Builds and runs clean — the items below are minor housekeeping toward the [publication criteria](../docs/criteria.md), not failures.**

This cookbook is in good shape: DOI, release, ORCIDs, and `CITATION.cff` are all present, and every
notebook carries the standard `python3` kernelspec. Three small items remain.

## Housekeeping

1. **Document or relax the one undocumented pin.** `environment.yml` carries two pins, only one of
   which is explained:

   ```
   - python >= 3.13
   - matplotlib < 3.11  # Temporary pin because of a colorbar bug
   ```

   The `matplotlib < 3.11` ceiling is exactly what the community asks for — a pin **with a comment
   saying why**. The `python >= 3.13` floor is undocumented, and it is an aggressive one (it demands
   the newest Python). Either add a one-line comment on why 3.13 is required, or relax it to a milder
   floor / drop it if the notebooks do not actually need 3.13:

   ```diff
   -  - python >= 3.13
   +  - python >= 3.10   # or keep the floor WITH a comment on why 3.13 is needed
   ```

2. **Move the one pip dependency to conda.** `environment.yml` installs `pelicanfs` via pip:

   ```
   - pip:
     - pelicanfs
   ```

   `pelicanfs` is packaged on conda-forge (latest `1.3.0`), so it can move up into the conda
   dependency list and the `pip:` block can be dropped:

   ```diff
   -  - pip
   -  - pip:
   -    - pelicanfs
   +  - pelicanfs
   ```

3. **Fix the leftover template link in `myst.yml`.** The Binder config still points at the template
   repository:

   ```yaml
   jupyter:
       binder:
         url: https://binder.projectpythia.org
         repo: projectpythia/cookbook-template
   ```

   Update `repo` to this cookbook so Binder launches from the right source:

   ```diff
   -        repo: projectpythia/cookbook-template
   +        repo: projectpythia/feature-tracking-cookbook
   ```

## What was verified

- **The two pins** (`python >= 3.13` undocumented, `matplotlib < 3.11` documented) — read from the
  current `environment.yml`.
- **`pelicanfs` is on conda-forge** (`latest_version 1.3.0`, conda-forge API) → safe to move to conda.
- **The `repo: projectpythia/cookbook-template` binder link** in `myst.yml`. (The
  `find: "ProjectPythia/cookbook-template"` string in `.github/workflows/trigger-replace-links.yaml`
  is the standard link-replacement workflow, not a stray content link — leave it.)
- **DOI, release, ORCIDs, and `CITATION.cff` are all present** (`doi: .../zenodo.20753356` in
  `myst.yml`, release tag `v2026.07.09`, ORCIDs on every author, exported `CITATION.cff`).
- **All 13 notebooks carry the standard `python3` kernelspec** (glob over `**/*.ipynb`).
- **Not verified:** whether the notebooks actually require `python >= 3.13` — that is the author's
  call; the recommendation is to document the reason or confirm it can float.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
