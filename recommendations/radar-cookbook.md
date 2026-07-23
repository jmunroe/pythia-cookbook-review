# radar-cookbook — Recommendations

Live outcome: **ran with errors**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/radar-cookbook.md) · [Repository](https://github.com/ProjectPythia/radar-cookbook)

Static tier `healthy`. **The book builds and runs; two notebooks point at a retired NEXRAD S3 bucket, and one has a transposed array exposed by a library upgrade.**

## The one change that matters: the NEXRAD bucket moved

Two notebooks fail with `PermissionError` (`Forbidden` / `Access Denied`) reading NEXRAD Level 2 data:

- `notebooks/example-workflows/echo_top_height.ipynb`
- `notebooks/example-workflows/moore-oklahoma-tornado.ipynb`

Both read from `s3://noaa-nexrad-level2/…`. NSF Unidata/NOAA **deprecated that bucket on 2025-09-01**
and moved the archive to **`unidata-nexrad-level2`** (same key layout). The old bucket now refuses all
anonymous access — this is a retired data source, **not** a credentials gap (these notebooks never
touch ARM, and no AWS auth would help).

The fix is a one-line bucket rename in each notebook:

```diff
- aws_nexrad_level2_file = "s3://noaa-nexrad-level2/2022/03/22/KHGX/KHGX20220322_120125_V06"
+ aws_nexrad_level2_file = "s3://unidata-nexrad-level2/2022/03/22/KHGX/KHGX20220322_120125_V06"
```
```diff
- files = sorted(fs.glob("s3://noaa-nexrad-level2/2013/05/20/KTLX/KTLX20130520_20*"))
+ files = sorted(fs.glob("s3://unidata-nexrad-level2/2013/05/20/KTLX/KTLX20130520_20*"))
```

The existing `anon=True` is already correct for the new bucket, and files there are now `.gz`-suffixed
— the `*` glob still matches and Py-ART reads gzip transparently, so no other edit is needed.

## Secondary: transposed `pts` in the fastbarnes notebook

`notebooks/example-workflows/fastbarnes_interpolation_rhi.ipynb` fails with:

```
RuntimeError: Barnes interpolation supports only sample points in dimensions 1, 2 or 3
```

`fastbarnes.interpolation.barnes()` documents its `pts` argument as shape `(N, M)` (N points × M
dims) and validates `dim = pts.shape[1]`. In `grid_rhi()` the array is built transposed — `(2, N)` —
so `pts.shape[1]` becomes N (thousands of gates) and trips the guard. `fast-barnes-py` is unpinned and
resolved to **v2.0.0**, which added this strict check; v1.0.0 (what the notebook was written against)
had no guard and tolerated the malformed input — the array was always wrong-shaped.

```diff
- res_field[:,:,j] = barnes(np.asarray([rg_loc.ravel(), radar.gate_altitude['data'].ravel()]),
+ res_field[:,:,j] = barnes(np.asarray([radar.gate_altitude['data'].ravel(), rg_loc.ravel()]).T,
                            data.ravel(), 100, np.asarray([0,0]), 100,
                            (len(z_pts), len(rng_pts)), method=method, ...)
```

`.T` clears the error; the columns are also reordered to (altitude, range) to match the grid's
`size=(len(z_pts), len(rng_pts))` axis order. Prefer this over pinning `fast-barnes-py==1.0.0` (which
would also contradict the [avoid-pins guidance](../docs/criteria.md)).

## What was verified

- **The new bucket works anonymously, the old one doesn't** — verified by direct request: anonymous
  HEAD on `s3://unidata-nexrad-level2/2022/03/22/KHGX/KHGX20220322_120125_V06` → HTTP 200; the old
  bucket → 403; anonymous ListObjectsV2 on the `unidata-nexrad-level2` KTLX prefix → 200 with matching
  `.gz` keys. Deprecation date from the NSF Unidata announcement.
- **The fastbarnes shape bug** — both v1.0.0 and v2.0.0 docstrings define `pts` as N×M; the installed
  v2.0.0 contains the guard at `interpolation.py:113–115`; `fast-barnes-py` is unpinned in the pip
  block.
- **The two PermissionError notebooks never use ARM** — the injected ARM creds (`env_injection.ok`)
  are relevant only to the fastbarnes notebook, whose ARM download actually succeeded.
- **Not verified:** the exact column ordering (altitude-vs-range) is read from the surrounding grid
  definition, not runtime-confirmed — validate the numerical result by running the notebook. Also
  note `echo_top_height` installs `eth_radar` from unpinned `git+…main`, a separate fragility worth
  pinning.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with the community, not an applied change.*
