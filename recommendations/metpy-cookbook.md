# metpy-cookbook — Recommendations

Live outcome: **ran with errors**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/metpy-cookbook.md) · [Repository](https://github.com/ProjectPythia/metpy-cookbook)

Static tier `healthy`. **The book builds and runs; five notebooks fail on one Python-version-sensitive import, and two more hit an external data server.**

## The one change that matters

Five notebooks fail at their **first cell** with:

```
ImportError: cannot import name 'UTC' from 'datetime'
```

`datetime.UTC` is a Python **3.11** alias; the Binder image resolved to **Python 3.10** (every
traceback frame is under `/srv/conda/envs/notebook/lib/python3.10/…`), so the import never succeeds
and the whole notebook is dead on arrival.

The portable fix is a two-line code change per notebook — use the pre-3.11 spelling, which also works
on 3.11+:

```diff
- from datetime import datetime, UTC
+ from datetime import datetime, timezone
...
- dt = datetime.now(UTC)
+ dt = datetime.now(timezone.utc)
```

Apply to all five affected notebooks:

- `notebooks/specialty/Smoothing_Contours.ipynb`
- `notebooks/synoptic/250hPa_Hemispheric_Plot.ipynb`
- `notebooks/synoptic/Wind_Shear_Vectors_Example.ipynb`
- `notebooks/synoptic/Upperair_Obs.ipynb`
- `notebooks/skewt/Sounding_Plotter.ipynb`

This is preferred over pinning `python>=3.11` in `environment.yml`: it adds no version constraint
(in keeping with Pythia's [avoid-pins guidance](../docs/criteria.md)), and it makes the notebooks
correct on every supported interpreter rather than depending on the image resolving to 3.11.

## What was verified

- **The five `UTC` ImportErrors and their exact lines** (`from datetime import datetime, UTC` +
  `datetime.now(UTC)`) read from the notebooks by grep; the live record captured **seven** errors —
  these five plus the two below.
- **The image ran Python 3.10** — confirmed from the traceback frame paths; `environment.yml` pins
  no Python version and the repo carries no `runtime.txt`/`binder/` config, so it takes repo2docker's
  default.
- **`datetime.timezone.utc` works on 3.10+** and `datetime.UTC` was introduced in 3.11 — language
  history, so the fix is certain.
- **Not verified:** the exact `metpy`/`siphon` versions (truncated from the build log). The fix does
  not depend on them.

## Secondary — an external data server, not a cookbook defect

Two notebooks fail on **HTTP errors from the University of Wyoming upper-air archive**
(`weather.arcc.uwyo.edu`), not on anything in the cookbook:

- `notebooks/specialty/Observational_Data_Cross_Section.ipynb` — `WyomingUpperAir.request_data(...)`
  for 2019 station DNR.
- `notebooks/skewt/Skew-T_Analysis.ipynb` — `WyomingUpperAir.request_data(...)` for 2016 station MPX.

Both request well-past historical soundings that should exist, so this reads as a server-side
availability problem rather than a clean transient blip. **No code change fixes it**; a re-run may
pass if the service recovers. Worth flagging upstream as a flaky external dependency (Siphon's
Wyoming endpoint), but it is outside the cookbook's control.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
