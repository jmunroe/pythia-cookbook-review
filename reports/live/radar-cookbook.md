# radar-cookbook

Live outcome: **ran with errors**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/radar-cookbook)

Run 2026-07-21 21:46:19 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [radar-cookbook](https://github.com/ProjectPythia/radar-cookbook) at ref [`main`](https://github.com/ProjectPythia/radar-cookbook/tree/main).

:::{warning} Cached image
BinderHub reused an existing image, so the 7.16s is a pod launch and image pull. It does **not** test whether `environment.yml` still solves.
:::

| Measure | Value |
|---|---|
| Live outcome | **ran with errors** |
| Static tier | `stale` |
| Time to a ready session | 7.16s (cached image) |
| Build succeeded | yes |
| Notebook execution | 6m 54s |
| Build command exit code | 0 (zero despite cell errors) |
| Notebooks ran clean | no |
| Execution cache | **reused — timing is not execution** |
| Peak memory (pss) | 7.97 GB |
| Pod memory limit | 8.59 GB |
| Peak as share of limit | 92.7% |
| Peak rss (upper bound, shared pages double-counted) | 16.97 GB |
| Errors raised | 3 |

| Notebook | Execute + render |
|---|---|
| [`notebooks/radar-basics/radar-basics.ipynb`](https://github.com/ProjectPythia/radar-cookbook/blob/main/notebooks/radar-basics/radar-basics.ipynb) | 0.11s |
| [`notebooks/example-workflows/moore-oklahoma-tornado.ipynb`](https://github.com/ProjectPythia/radar-cookbook/blob/main/notebooks/example-workflows/moore-oklahoma-tornado.ipynb) | 9.71s |
| [`notebooks/example-workflows/echo_top_height.ipynb`](https://github.com/ProjectPythia/radar-cookbook/blob/main/notebooks/example-workflows/echo_top_height.ipynb) | 11s |
| [`notebooks/example-workflows/fastbarnes_interpolation_rhi.ipynb`](https://github.com/ProjectPythia/radar-cookbook/blob/main/notebooks/example-workflows/fastbarnes_interpolation_rhi.ipynb) | 13s |
| [`notebooks/foundations/interactive-radar-visualization.ipynb`](https://github.com/ProjectPythia/radar-cookbook/blob/main/notebooks/foundations/interactive-radar-visualization.ipynb) | 27s |

Executed 11 notebook(s) from the project toc: [`notebooks/example-workflows/cacti-data-quality-example.ipynb`](https://github.com/ProjectPythia/radar-cookbook/blob/main/notebooks/example-workflows/cacti-data-quality-example.ipynb), [`notebooks/example-workflows/echo_top_height.ipynb`](https://github.com/ProjectPythia/radar-cookbook/blob/main/notebooks/example-workflows/echo_top_height.ipynb), [`notebooks/example-workflows/fastbarnes_interpolation_rhi.ipynb`](https://github.com/ProjectPythia/radar-cookbook/blob/main/notebooks/example-workflows/fastbarnes_interpolation_rhi.ipynb), [`notebooks/example-workflows/kdp-comparison.ipynb`](https://github.com/ProjectPythia/radar-cookbook/blob/main/notebooks/example-workflows/kdp-comparison.ipynb), [`notebooks/example-workflows/moore-oklahoma-tornado.ipynb`](https://github.com/ProjectPythia/radar-cookbook/blob/main/notebooks/example-workflows/moore-oklahoma-tornado.ipynb), [`notebooks/example-workflows/tracer-example.ipynb`](https://github.com/ProjectPythia/radar-cookbook/blob/main/notebooks/example-workflows/tracer-example.ipynb), [`notebooks/foundations/interactive-radar-visualization.ipynb`](https://github.com/ProjectPythia/radar-cookbook/blob/main/notebooks/foundations/interactive-radar-visualization.ipynb), [`notebooks/foundations/pyart-basics.ipynb`](https://github.com/ProjectPythia/radar-cookbook/blob/main/notebooks/foundations/pyart-basics.ipynb), [`notebooks/foundations/pyart-corrections.ipynb`](https://github.com/ProjectPythia/radar-cookbook/blob/main/notebooks/foundations/pyart-corrections.ipynb), [`notebooks/foundations/pyart-gridding.ipynb`](https://github.com/ProjectPythia/radar-cookbook/blob/main/notebooks/foundations/pyart-gridding.ipynb), [`notebooks/radar-basics/radar-basics.ipynb`](https://github.com/ProjectPythia/radar-cookbook/blob/main/notebooks/radar-basics/radar-basics.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/radar-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Errors

**`PermissionError`** — Forbidden

in `site/content/notebooks.example-workflows.echo-top-height.json`

```
---------------------------------------------------------------------------
ClientError                               Traceback (most recent call last)
File /srv/conda/envs/notebook/lib/python3.12/site-packages/s3fs/core.py:114, in _error_wrapper(func, args, kwargs, retries)
    113 try:
--> 114     return await func(*args, **kwargs)
    115 except S3_RETRYABLE_ERRORS as e:

File /srv/conda/envs/notebook/lib/python3.12/site-packages/aiobotocore/context.py:36, in with_current_context.<locals>.decorator.<locals>.wrapper(*args, **kwargs)
     35     await resolve_awaitable(hook())
---> 36 return await func(*args, **kwargs)

File /srv/conda/envs/notebook/lib/python3.12/site-packages/aiobotocore/client.py:424, in AioBaseClient._make_api_call(self, operation_name, api_params)
    423     error_class = self.exceptions.from_code(error_code)
--> 424     raise error_class(parsed_response, operation_name)
    425 else:

ClientError: An error occurred (403) when calling the HeadObject operation: Forbidden

The above exception was the direct cause of the following exception:

PermissionError                           Traceback (most recent call last)
Cell In[3], line 5
      1 aws_nexrad_level2
```

**`RuntimeError`** — Barnes interpolation supports only sample points in dimensions 1, 2 or 3

in `site/content/notebooks.example-workflows.fastbarnes-interpolation-rhi.json`

```
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
Cell In[8], line 1
----> 1 grid_ds = grid_rhi(radar_file)

Cell In[7], line 63, in grid_rhi(file, z_res, rng_res, z_limits, rng_limits, fields)
     60     data = deepcopy(np.array(radar.fields[fields[j]]['data']))
     61     # data = data.filled(np.nan)
---> 63     res_field[:,:,j] = barnes(np.asarray([rg_loc.ravel(),radar.gate_altitude['data'].ravel()]),
     64                        data.ravel(),
     65                        100,
     66                        np.asarray([0,0]),
     67                        100,
     68                        (len(z_pts),len(rng_pts)),
     69                        method=method,
     70                        num_iter = num_iter,
     71                        min_weight=0.0002
     72                       )
     75 data_dict = {}
     76 for k in range(len(fields)):

File /srv/conda/envs/notebook/lib/python3.12/site-packages/fastbarnes/interpolation.py:115, in barnes(pts, val, sigma, x0, step, size, method, num_iter, max_dist, min_weight)
    113 dim = pts.shape[1]
    114 if dim < 1 or
```

**`PermissionError`** — Access Denied

in `site/content/notebooks.example-workflows.moore-oklahoma-tornado.json`

```
---------------------------------------------------------------------------
ClientError                               Traceback (most recent call last)
File /srv/conda/envs/notebook/lib/python3.12/site-packages/s3fs/core.py:755, in S3FileSystem._lsdir(self, path, refresh, max_items, delimiter, prefix, versions)
    754 files = []
--> 755 async for c in self._iterdir(
    756     bucket,
    757     max_items=max_items,
    758     delimiter=delimiter,
    759     prefix=prefix,
    760     versions=versions,
    761 ):
    762     if c["type"] == "directory":

File /srv/conda/envs/notebook/lib/python3.12/site-packages/s3fs/core.py:805, in S3FileSystem._iterdir(self, bucket, max_items, delimiter, prefix, versions)
    798 it = pag.paginate(
    799     Bucket=bucket,
    800     Prefix=prefix,
   (...)
    803     **self.req_kw,
    804 )
--> 805 async for i in it:
    806     for l in i.get("CommonPrefixes", []):

File /srv/conda/envs/notebook/lib/python3.12/site-packages/aiobotocore/paginate.py:39, in AioPageIterator.__anext__(self)
     38 while True:
---> 39     response = await self._make_request(current_kwargs)
     40     parsed = self._extract_parsed_response(response)

File
```

