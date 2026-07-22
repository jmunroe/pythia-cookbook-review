# cesm-lens-aws-cookbook

Live outcome: **ran with errors**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/cesm-lens-aws-cookbook)

Run 2026-07-22 03:35:26 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [cesm-lens-aws-cookbook](https://github.com/ProjectPythia/cesm-lens-aws-cookbook) at ref [`main`](https://github.com/ProjectPythia/cesm-lens-aws-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **ran with errors** |
| Static tier | `healthy` |
| Time to a ready session | 329.75s (fresh build) |
| Build succeeded | yes |
| Notebook execution | 463.46s |
| Build command exit code | 0 (zero despite cell errors) |
| Notebooks ran clean | no |
| Execution cache | **reused — timing is not execution** |
| Peak memory (pss) | 3.90 GB |
| Pod memory limit | 8.59 GB |
| Peak as share of limit | 45.5% |
| Peak rss (upper bound, shared pages double-counted) | 4.23 GB |
| Errors raised | 2 |

| Notebook | Execute + render |
|---|---|
| [`notebooks/foundations/enhanced-catalog.ipynb`](https://github.com/ProjectPythia/cesm-lens-aws-cookbook/blob/main/notebooks/foundations/enhanced-catalog.ipynb) | 6.52s |

Executed 2 notebook(s) from the project toc: [`notebooks/example-workflows/key-figures.ipynb`](https://github.com/ProjectPythia/cesm-lens-aws-cookbook/blob/main/notebooks/example-workflows/key-figures.ipynb), [`notebooks/foundations/enhanced-catalog.ipynb`](https://github.com/ProjectPythia/cesm-lens-aws-cookbook/blob/main/notebooks/foundations/enhanced-catalog.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/cesm-lens-aws-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Errors

**`KilledWorker`** — Attempted to run task 'finalize-hlgfinalizecompute-ac2f174f63514bf1bef758c1756814a9' on 4 different workers, but all those workers died while running it. The last worker that attempt to run the task was tcp://127.0.0.1:37493. Inspecting worker logs is often a good next step to diagnose what went wrong. For more information see https://distributed.dask.org/en/stable/killed.html.

in `site/content/notebooks.example-workflows.key-figures.json`

```
---------------------------------------------------------------------------
KilledWorker                              Traceback (most recent call last)
File <timed exec>:5

File /srv/conda/envs/notebook/lib/python3.14/site-packages/xarray/core/dataarray.py:1180, in DataArray.load(self, **kwargs)
   1150 def load(self, **kwargs) -> Self:
   1151     """Trigger loading data into memory and return this dataarray.
   1152 
   1153     Data will be computed and/or loaded from disk or a remote source.
   (...)
   1178     Variable.load
   1179     """
-> 1180     ds = self._to_temp_dataset().load(**kwargs)
   1181     new = self._from_temp_dataset(ds)
   1182     self._variable = new._variable

File /srv/conda/envs/notebook/lib/python3.14/site-packages/xarray/core/dataset.py:569, in Dataset.load(self, **kwargs)
    566 chunkmanager = get_chunked_array_type(*chunked_data.values())
    568 # evaluate all the chunked arrays simultaneously
--> 569 evaluated_data: tuple[np.ndarray[Any, Any], ...] = chunkmanager.compute(
    570     *chunked_data.values(), **kwargs
    571 )
    573 for k, data in zip(chunked_data, evaluated_data, strict=False):
    574     self.variables[k].data = data

File 
```

**`AssertionError`** — 

in `site/content/notebooks.example-workflows.key-figures.json`

```
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
Cell In[30], line 1
----> 1 assert len(winter_seasons.time) == 34

AssertionError: 
```

