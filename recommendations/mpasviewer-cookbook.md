# mpasviewer-cookbook — Recommendations

Live outcome: **ran with errors**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/mpasviewer-cookbook.md) · [Repository](https://github.com/ProjectPythia/mpasviewer-cookbook)

Static tier `incubating`. **The book builds and runs; the one failure was a transient outage of the GDEX THREDDS server, not a cookbook defect.**

## What this failure is

`notebooks/remote-out-hurricane-investigation.ipynb` failed with:

```
ClientResponseError: 503, message='Service Temporarily Unavailable',
url='https://tds.gdex.ucar.edu/thredds/catalog/files/d010077/native_diag/catalog.html'
```

The notebook reads MPAS output from NCAR's GDEX THREDDS data server. A `503 Service Temporarily
Unavailable` is a server-side outage, not a code or URL error.

**Verified reachable now:** a fresh `GET` of that THREDDS catalog returns **HTTP 200** — the outage
has cleared, so a re-run should pass. A live re-check would confirm.

## Secondary

- The failure is external; no code change is required for correctness. If the GDEX THREDDS endpoint
  proves persistently flaky, consider caching the small subset the notebook needs or documenting the
  data dependency so a reader hitting the same 503 knows it is upstream.
- Five notebooks (`cesm_mpas_remap.ipynb`, `plot_mpas_quiver_overlay_slp.ipynb`, `plot_mpas_ts.ipynb`,
  `plot_mpas_vertical_section.ipynb`, `plot_mpas_zonalAvg.ipynb`) carry a non-standard
  `mpasviewer-cookbook-dev` kernelspec instead of the standard `python3`. That is latent today (they
  are not in the executed build), but if any is added to the toc it will fail immediately with
  "kernel is not available." Normalize them to `{"name":"python3", …}` pre-emptively.

## What was verified

- **The 503 was on the GDEX THREDDS catalog URL**, read from the traceback; a single external error.
- **The URL returns HTTP 200 now** (fresh `curl`), so the failure was transient.
- **Not verified with a live re-check yet** — a re-run would confirm the notebook now completes.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with a live re-run and the community, not an applied change.*
