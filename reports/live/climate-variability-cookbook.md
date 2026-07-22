# climate-variability-cookbook

Live outcome: **ran with errors**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/climate-variability-cookbook)

Run 2026-07-22 09:21:45 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [climate-variability-cookbook](https://github.com/ProjectPythia/climate-variability-cookbook) at ref [`main`](https://github.com/ProjectPythia/climate-variability-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **ran with errors** |
| Static tier | `incubating` |
| Time to a ready session | 6m 22s (fresh build) |
| Build succeeded | yes |
| Notebook execution | 42.27s |
| Build command exit code | 0 (zero despite cell errors) |
| Notebooks ran clean | no |
| Execution cache | **reused — timing is not execution** |
| Peak memory (pss) | 0.34 GB |
| Pod memory limit | 8.59 GB |
| Peak as share of limit | 4.0% |
| Peak rss (upper bound, shared pages double-counted) | 0.36 GB |
| Errors raised | 1 |

| Notebook | Execute + render |
|---|---|
| [`notebooks/CESM2_LENS2_AWS.ipynb`](https://github.com/ProjectPythia/climate-variability-cookbook/blob/main/notebooks/CESM2_LENS2_AWS.ipynb) | 35s |

Executed 1 notebook(s) from the project toc: [`notebooks/CESM2_LENS2_AWS.ipynb`](https://github.com/ProjectPythia/climate-variability-cookbook/blob/main/notebooks/CESM2_LENS2_AWS.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/climate-variability-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Errors

**`ClientResponseError`** — 503, message='first byte timeout', url='https://raw.githubusercontent.com/NCAR/cesm2-le-aws/main/intake-catalogs/aws-cesm2-le.json'

in `site/content/notebooks.cesm2-lens2-aws.json`

```
---------------------------------------------------------------------------
ClientResponseError                       Traceback (most recent call last)
Cell In[2], line 1
----> 1 catalog = intake.open_esm_datastore(
      2     'https://raw.githubusercontent.com/NCAR/cesm2-le-aws/main/intake-catalogs/aws-cesm2-le.json'
      3 )
      4 catalog

File /srv/conda/envs/notebook/lib/python3.10/site-packages/intake_esm/core.py:124, in esm_datastore.__init__(self, obj, progressbar, sep, registry, read_csv_kwargs, columns_with_iterables, storage_options, threaded, **intake_kwargs)
    122     self.esmcat = ESMCatalogModel.from_dict(obj)
    123 else:
--> 124     self.esmcat = ESMCatalogModel.load(
    125         obj, storage_options=self.storage_options, read_csv_kwargs=read_csv_kwargs
    126     )
    128 self.derivedcat = registry or default_registry
    129 self._entries = {}

File /srv/conda/envs/notebook/lib/python3.10/site-packages/intake_esm/cat.py:252, in ESMCatalogModel.load(cls, json_file, storage_options, read_csv_kwargs)
    249 _mapper = fsspec.get_mapper(json_file, **storage_options)
    251 with fsspec.open(json_file, **storage_options) as fobj:
--> 252     data = json.lo
```

