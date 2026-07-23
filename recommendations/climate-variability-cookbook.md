# climate-variability-cookbook — Recommendations

Live outcome: **ran with errors**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/climate-variability-cookbook.md) · [Repository](https://github.com/ProjectPythia/climate-variability-cookbook)

Static tier `healthy`. **The book builds and runs; the one failure was a transient outage of an external catalog server, not a cookbook defect.**

## What this failure is

`notebooks/cesm2-lens2-aws.ipynb` failed with:

```
ClientResponseError: 503, message='first byte timeout',
url='https://raw.githubusercontent.com/NCAR/cesm2-le-aws/main/intake-catalogs/aws-cesm2-le.json'
```

The notebook opens the NCAR CESM2-LENS intake-esm catalog hosted on GitHub raw. A `503 first byte
timeout` is the server failing to start the response — a transient availability blip, not a broken URL
or wrong code.

**Verified reachable now:** a fresh `GET` of that catalog URL returns **HTTP 200** — the outage has
cleared, so a re-run should pass. The most useful confirmation is a live re-check; this is a good
candidate for one.

## Secondary — resilience (optional, worth considering)

The failure is external, but the cookbook can be made less fragile to these blips:

- **Cache the catalog / pin a stable location.** `raw.githubusercontent.com` is rate-limited and
  occasionally slow; if the CESM2-LENS catalog is also published on a CDN or object store, preferring
  that reduces exposure to GitHub-raw hiccups.
- No code change is required for correctness — this is purely about robustness under a flaky upstream.

## What was verified

- **The 503 was on the GitHub-raw catalog URL**, read from the traceback; a single external error, no
  other cells failing for code reasons.
- **The URL returns HTTP 200 now** (fresh `curl`), so the failure was transient.
- **Not verified with a live re-check yet** — a re-run against binder.projectpythia.org would confirm
  the notebook now completes end-to-end.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with a live re-run and the community, not an applied change.*
