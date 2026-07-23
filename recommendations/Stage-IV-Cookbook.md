# Stage-IV-Cookbook — Recommendations

Live outcome: **ran clean**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/Stage-IV-Cookbook.md) · [Repository](https://github.com/ProjectPythia/Stage-IV-Cookbook)

Static tier `healthy`. **Builds and runs clean — the items below are minor housekeeping toward the [publication criteria](../docs/criteria.md), not failures.**

The notebooks execute cleanly, but this cookbook stands out from its ran-clean peers: it has **not been
migrated to MyST**. There is no `myst.yml`; instead the repo still carries the full pre-MyST Jupyter Book
stack (`_config.yml`, `_toc.yml`, `_static/`, `_templates/`, plus `jupyter-book` and `sphinx-pythia-theme`
in the environment). Its `CITATION.cff` and `_config.yml` also still carry the template's placeholder
title and abstract. Kernelspecs are clean (`name: python3`).

## Housekeeping

1. **Migrate the build to MyST — the Sphinx/Jupyter Book files here are still *active*, not dead cruft.**
   Unlike the other ran-clean cookbooks, this repo has no `myst.yml`. It still relies on the legacy
   Jupyter Book toolchain:
   - `environment.yml` — `jupyter-book` and `sphinx-pythia-theme`.
   - repo root — `_config.yml`, `_toc.yml`, `_static/` (`custom.css`, `footer-logo-nsf.png`),
     `_templates/` (`footer-extra.html`).

   The current ProjectPythia build path is MyST (`mystmd` + `myst.yml`), so this cookbook should be
   migrated: add a `myst.yml` (title, authors, toc, Binder repo), then remove `_config.yml`, `_toc.yml`,
   `_static/`, `_templates/`, and swap `jupyter-book`/`sphinx-pythia-theme` out of `environment.yml` for
   `mystmd`/`jupyterlab-myst`. Because these files are the active config today, do **not** simply delete
   them without adding the MyST replacement first.

2. **Document or relax the Python cap.** `environment.yml` carries one undocumented pin:

   ```
   - python<3.12
   ```

   This is an upper cap that excludes Python 3.12+. The community asks that pins be documented. Add a
   one-line comment on what needs the cap, or relax it if the notebooks run on newer interpreters:

   ```diff
   -  - python<3.12
   +  - python<3.12   # what requires <3.12? document, or drop the cap
   ```

3. **Replace the template links and placeholder metadata.** The repo still carries the template defaults:
   - `README.md` — the nightly-build and Binder badges target `ProjectPythia/cookbook-template`.
   - `_config.yml` — `title: Project Pythia Cookbook Template`.
   - `CITATION.cff` — `title: "Cookbook Template"`, `abstract: "A sample cookbook description."`, and a
     `"Cookbook Template contributors"` entry.
   - `notebooks/how-to-cite.md` — links the source to `ProjectPythia/cookbook-template`.

   Update these to this cookbook's own repo and real title. (The `CITATION.cff` author ORCIDs are already
   populated.)

4. **Add a real Zenodo DOI and a GitHub release.** The DOI badge in `README.md` and `how-to-cite.md`
   points at Zenodo record `475509405`, which is the **cookbook-template's** DOI, not this cookbook's.
   There are no release tags. Cut a release and mint a per-cookbook DOI, then update the badge.

## What was verified

- **No `myst.yml`** — confirmed absent; the active build config is `_config.yml` + `_toc.yml`, and
  `environment.yml` still lists `jupyter-book` and `sphinx-pythia-theme`. The `_static/` and
  `_templates/` directories are present. So the "leftover pre-MyST files" are in fact the live build
  system, and the recommendation is to migrate, not merely delete.
- **The single pin** `python<3.12`, undocumented, read from the current `environment.yml`.
- **No pip dependencies** — nothing to move to conda.
- **Template links / placeholders** in `README.md`, `_config.yml`, `CITATION.cff`, and `how-to-cite.md`
  (grep). ORCIDs are present in `CITATION.cff`.
- **DOI badge `475509405` is the template's**, not this cookbook's; no release tags (`git tag` empty).
- **All notebook kernelspecs are `python3`** (glob over `**/*.ipynb`) — no latent kernelspec issue.
- **Not verified:** whether anything actually requires Python <3.12 — that is the author's call.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
