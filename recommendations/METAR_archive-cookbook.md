# METAR_archive-cookbook — Recommendations

Live outcome: **ran clean**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/METAR_archive-cookbook.md) · [Repository](https://github.com/ProjectPythia/METAR_archive-cookbook)

Static tier `healthy`. **Builds and runs clean — the items below are minor housekeeping toward the [publication criteria](../docs/criteria.md), not failures.**

This cookbook runs clean and its `myst.yml` and `CITATION.cff` are already well customized (real title,
authors, and repo). The remaining items are two undocumented pins, a lone template badge, the missing
DOI/release, and two scratch notebooks carrying non-standard kernelspecs.

## Housekeeping

1. **Document or relax the two version pins.** `environment.yml` carries two undocumented constraints:

   ```
   - python>=3.14
   - matplotlib<3.11
   ```

   `python>=3.14` is an unusually aggressive floor — it requires the newest interpreter and will exclude
   anyone on 3.12/3.13. `matplotlib<3.11` is an upper cap that actively excludes the current conda-forge
   release (`matplotlib` is at `3.11.1`). Both are the kind of pin the community asks to see documented.
   Add a one-line comment on each explaining the reason (e.g. a 3.14-only feature; a matplotlib 3.11
   incompatibility), or relax them if they are not actually needed:

   ```diff
   -  - python>=3.14
   -  - matplotlib<3.11
   +  - python>=3.14     # why is 3.14 required? document, or lower the floor
   +  - matplotlib<3.11  # what breaks on 3.11? document, or drop the cap
   ```

   (Minor, out of the pin family: `vim` is listed as a dependency — a text editor is unusual in a
   runtime environment and is likely a stray addition worth removing.)

2. **Replace the remaining template link.** `myst.yml` is already customized to this cookbook, but
   `README.md` still targets `ProjectPythia/cookbook-template` in the nightly-build badge, and
   `notebooks/how-to-cite.md` links the source to `cookbook-template`. `CITATION.cff` also keeps a
   `"Cookbook Template contributors"` entry. Update these to this cookbook's own repo.

3. **Add a real Zenodo DOI and a GitHub release.** The DOI badge in `README.md` and `how-to-cite.md`
   points at Zenodo record `475509405`, which is the **cookbook-template's** DOI, not this cookbook's.
   There are no release tags. Cut a release and mint a per-cookbook DOI, then update the badge.

4. **Normalize (or remove) the two scratch-notebook kernelspecs.** Two notebooks under `notebooks/scratch/`
   carry non-standard kernelspecs that will fail to execute if they ever enter the executed toc:

   ```
   notebooks/scratch/MetarParquetDuckDB.ipynb  ->  kernelspec.name = "jan25"
   notebooks/scratch/MetarParquetViz.ipynb     ->  kernelspec.name = "jan26"
   ```

   They are not in the toc today, so this is a latent time-bomb rather than a live failure. Either delete
   the `scratch/` directory, or normalize the kernelspec to the standard:

   ```json
   {"name": "python3", "display_name": "Python 3 (ipykernel)", "language": "python"}
   ```

## What was verified

- **The two pins** `python>=3.14` and `matplotlib<3.11`, undocumented, read from the current
  `environment.yml`; conda-forge latest `matplotlib` is `3.11.1`, so the cap excludes the current
  release. The stray `vim` dependency was also confirmed in the file.
- **No pip dependencies** — nothing to move to conda.
- **No Sphinx deps or files** — `myst.yml` is present and customized; nothing to remove.
- **Template links**: `myst.yml` is clean, but `README.md`, `how-to-cite.md`, and a `CITATION.cff`
  entry still reference `cookbook-template` (grep).
- **DOI badge `475509405` is the template's**, not this cookbook's; no release tags (`git tag` empty).
- **`CITATION.cff` / `authors.yml` are well populated with ORCIDs** — no metadata gap beyond DOI/release.
- **Kernelspecs** (glob over `**/*.ipynb`): all `python3` except the two `notebooks/scratch/` notebooks
  (`jan25`, `jan26`), confirming the prior sweep's finding.
- **Not verified:** whether the notebooks actually require Python 3.14 or break under matplotlib 3.11 —
  that is the author's call.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
