# hello-pythia-cookbook — Recommendations

Live outcome: **ran clean**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/hello-pythia-cookbook.md) · [Repository](https://github.com/ProjectPythia/hello-pythia-cookbook)

Static tier `healthy`. **Builds and runs clean — the items below are minor housekeeping toward the [publication criteria](../docs/criteria.md), not failures.**

The single notebook runs clean and carries the standard `python3` kernelspec. The main housekeeping
item here is that this cookbook has **not yet been migrated to the MyST build** that the rest of the
gallery uses — it still ships the pre-MyST jupyter-book/Sphinx stack. Because there is no `myst.yml`,
the Sphinx files are the *active* build config, not dead cruft, so this is a migration rather than a
delete.

## Housekeeping

1. **Migrate the build from jupyter-book/Sphinx to mystmd.** There is no `myst.yml`; the repo still
   builds with the legacy stack:

   - `environment.yml` lists `jupyter-book` and `sphinx-pythia-theme` (and no `mystmd`).
   - `_config.yml` and `_toc.yml` (plus `_static/` and `_templates/`) drive a Sphinx build with
     `html_theme: sphinx_pythia_theme`.
   - `_config.yml` still carries the template's title — `title: Project Pythia Cookbook Template`.

   Bringing this cookbook in line with the current gallery means: add a `myst.yml` (extending
   `pythia-config`), swap the environment deps to `mystmd` + `jupyterlab-myst`, and remove the
   now-obsolete `_config.yml`, `_toc.yml`, `_static/`, and `_templates/`:

   ```diff
   -  - jupyter-book
    - jupyterlab
   -  - sphinx-pythia-theme
   +  - mystmd
   +  - jupyterlab-myst
   ```

   (This mirrors the migration already applied to sibling cookbooks such as geosat and
   interactive-sentinel-2, which build from `myst.yml` and keep only `sphinx-pythia-theme` behind as
   removable cruft.)

2. **Add a Zenodo DOI and cut a GitHub release.** The repo has no release tag and no DOI
   (`CITATION.cff` carries no DOI entry). Archiving a tagged release to Zenodo and recording the DOI
   satisfies the archive-and-cite criteria rows.

## What was verified

- **No `myst.yml`; `_config.yml`, `_toc.yml`, `_static/`, `_templates/` all present**, and
  `environment.yml` lists `jupyter-book` + `sphinx-pythia-theme` with no `mystmd` — confirming the
  Sphinx stack is the active build, not dead cruft. `_config.yml` `title` is still
  `Project Pythia Cookbook Template`.
- **No pins and no pip dependencies** in `environment.yml`.
- **No release and no DOI** (no tags on the remote; no DOI in `CITATION.cff`). **ORCID is present**
  for the author.
- **The single notebook `hello-pythia.ipynb` carries the standard `python3` kernelspec** (glob over
  `**/*.ipynb`).
- **Not verified:** the exact shape of a new `myst.yml` — best derived from a migrated sibling
  cookbook; the recommendation is to migrate rather than to delete the active Sphinx config.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
