# extreme-weather-events-cookbook — Recommendations

Live outcome: **ran clean**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/extreme-weather-events-cookbook.md) · [Repository](https://github.com/ProjectPythia/extreme-weather-events-cookbook)

Static tier `healthy`. **Builds and runs clean — the items below are minor housekeeping toward the [publication criteria](../docs/criteria.md), not failures.**

This cookbook runs clean but is still on the **legacy Jupyter Book / Sphinx build**: there is no
`myst.yml`, and it builds from `_config.yml` + `_toc.yml` (with `_static/` and `_templates/`) using
`html_theme: sphinx_pythia_theme`. So `sphinx-pythia-theme` / `jupyter-book` in `environment.yml` are
load-bearing here, not dead cruft, until the cookbook migrates to MyST. There are also two
undocumented version pins, several latent kernelspec issues, and template placeholders left in the
toc.

## Housekeeping

1. **Document (or retire) the two version pins.** `environment.yml` carries two exact pins with no
   comment:

   ```
   - intake==0.7.0
   - intake-xarray==0.7.0
   ```

   These are far behind conda-forge (`intake` is at `2.0.9`, `intake-xarray` at `2.0.0`), and the 2.x
   series has a breaking API change — so the pins are probably deliberate, holding the notebooks on
   the old `intake` catalog API. The community asks that pins be **documented**: add a one-line
   comment explaining why 0.7.0 is required, or migrate the notebooks to the intake 2.x API and drop
   the pins. Do not remove them blindly.

2. **Migrate to the MyST build (mystmd).** As with other legacy cookbooks, add a `myst.yml`, then
   remove the now-dead `_config.yml`, `_toc.yml`, `_static/`, `_templates/`, and drop `jupyter-book` +
   `sphinx-pythia-theme` from `environment.yml`. Do the migration first; the deletions follow.

3. **Clear the template placeholders in the toc.** `_toc.yml` still publishes the template stub and an
   unfilled caption:

   ```
   - caption: Introduction
       - file: notebooks/notebook-template     # leftover template notebook
   - caption: <Second Chapter Name>            # unfilled placeholder caption
   ```

   Drop `notebooks/notebook-template` from the toc (and the file) and give the chapter a real caption.
   This folds naturally into the MyST migration above.

4. **Normalize non-standard / missing kernelspecs (latent).** Six notebooks do not use the standard
   `python3` kernel:

   ```
   notebooks/Reihaneh.ipynb            (no kernelspec at all)
   notebooks/conus_max_temps.ipynb     name=2025-digital-earths-global-hackathon
   notebooks/sa_max_temps.ipynb        name=2025-digital-earths-global-hackathon
   notebooks/sa_precip.ipynb           name=2025-digital-earths-global-hackathon
   notebooks/test_visualization.ipynb  name=2025-digital-earths-global-hackathon
   notebooks/precip-lat_time.ipynb     name=myhackathon
   ```

   None are in the executed `_toc.yml` today, so they did not affect this run — but any of them is a
   time-bomb if it enters the executed toc. Reset each to:

   ```json
   {"name": "python3", "display_name": "Python 3 (ipykernel)", "language": "python"}
   ```

5. **Fill in the ORCIDs and cut a release.** `CITATION.cff` has placeholder ORCIDs
   (`xxxx-xxxx-xxxx-xxxx`, `yyyy-yyyy-yyyy-yyyy`) — replace them with real ones. The README has a
   Zenodo DOI badge but the repo has **no GitHub release/tag**; tag one so the archive matches the
   citation.

## What was verified

- **Legacy build** — no `myst.yml`; `_config.yml` sets `html_theme: sphinx_pythia_theme`; `_toc.yml`,
  `_static/`, `_templates/` present.
- **`environment.yml`** — conda-forge only, includes `jupyter-book` + `sphinx-pythia-theme`; two exact
  pins `intake==0.7.0` and `intake-xarray==0.7.0`; no pip section. conda-forge latest confirmed
  `intake` 2.0.9 / `intake-xarray` 2.0.0.
- **Toc** — `_toc.yml` includes `notebooks/notebook-template` and the caption `<Second Chapter Name>`.
- **Kernelspecs** — 6 notebooks non-standard/missing (listed above); none currently in the executed
  toc (which runs `precip-2d`, `precip-PDF`, `notebook-template`, all `python3`).
- **Template links** — README badges already point at the correct repo (no stray links there).
- **Metadata** — Zenodo DOI badge present; ORCIDs are placeholders; **no GitHub release**.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
