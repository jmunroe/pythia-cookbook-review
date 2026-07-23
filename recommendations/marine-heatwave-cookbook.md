# marine-heatwave-cookbook — Recommendations

Live outcome: **ran with errors**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/marine-heatwave-cookbook.md) · [Repository](https://github.com/ProjectPythia/marine-heatwave-cookbook)

Static tier `healthy`. **The book builds and runs; the one failure was a mid-stream interruption of a remote OPeNDAP download, not a cookbook defect.**

## What this failure is

`notebooks/foundation/mhw_observation_myst.ipynb` failed at cell `In[9]`:

```python
ds_mon_anom = (ds_mon_crop.groupby('time.month') - ds_mon_climo).compute()
```
```
ChunkedEncodingError: Response ended prematurely
```

The dataset is NOAA OISST v2, opened lazily over OPeNDAP:

```python
opendap_mon_url = "https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.mon.mean.nc"
ds_mon = xr.open_dataset(opendap_mon_url, engine='pydap', chunks={...})
```

`.compute()` is where the lazy data is actually streamed, and `ChunkedEncodingError: Response ended
prematurely` means the HTTP response from NOAA's PSL THREDDS/OPeNDAP server was cut off mid-transfer —
a transient network/server interruption, not a code error or a wrong URL.

**A re-run is the right first step**, and a live re-check would confirm the notebook now completes.

## Secondary — resilience against OPeNDAP flakiness (optional)

Streaming a full field over OPeNDAP in one `.compute()` is exactly what a premature-response error
hits. Without changing the science, the notebook can be made sturdier:

- **Subset before `.compute()`** (region/time already cropped upstream — materialize the smallest array
  the analysis needs) so each request is smaller and less likely to be dropped.
- **Consider a retry** around the OPeNDAP read, or a cached/local copy of the small monthly-mean field,
  if PSL's server proves persistently flaky.

## What was verified

- **The failing cell** (`.compute()` on the OISST anomaly) and the **NOAA PSL OPeNDAP URL** it streams,
  read from the notebook; a single error, transient in nature (`Response ended prematurely`).
- **Not verified with a live re-check yet** — a re-run would confirm end-to-end completion. (The PSL
  OPeNDAP endpoint's transient behavior can't be usefully probed with a simple `curl`, unlike the
  plain-HTTP catalog outages elsewhere in this tier.)

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with a live re-run and the community, not an applied change.*
