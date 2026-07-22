# ERA5_interactive-cookbook

Live outcome: **ran with errors**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/ERA5_interactive-cookbook)

Run 2026-07-22 04:25:49 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [ERA5_interactive-cookbook](https://github.com/ProjectPythia/ERA5_interactive-cookbook) at ref [`main`](https://github.com/ProjectPythia/ERA5_interactive-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **ran with errors** |
| Static tier | `healthy` |
| Time to a ready session | 421.62s (fresh build) |
| Build succeeded | yes |
| Notebook execution | 738.69s |
| Build command exit code | 0 (zero despite cell errors) |
| Notebooks ran clean | no |
| Execution cache | **reused — timing is not execution** |
| Peak memory (pss) | 2.23 GB |
| Pod memory limit | 8.59 GB |
| Peak as share of limit | 25.9% |
| Peak rss (upper bound, shared pages double-counted) | 2.69 GB |
| Errors raised | 1 |

| Notebook | Execute + render |
|---|---|
| [`notebooks/05_data_preprocessing.ipynb`](https://github.com/ProjectPythia/ERA5_interactive-cookbook/blob/main/notebooks/05_data_preprocessing.ipynb) | 11.0s |
| [`notebooks/06_era5_anomaly.ipynb`](https://github.com/ProjectPythia/ERA5_interactive-cookbook/blob/main/notebooks/06_era5_anomaly.ipynb) | 19.0s |
| [`notebooks/04_dashboard.ipynb`](https://github.com/ProjectPythia/ERA5_interactive-cookbook/blob/main/notebooks/04_dashboard.ipynb) | 22.0s |
| [`notebooks/03_hvplot.ipynb`](https://github.com/ProjectPythia/ERA5_interactive-cookbook/blob/main/notebooks/03_hvplot.ipynb) | 35.0s |

Executed 6 notebook(s) from the project toc: [`notebooks/01BasicVisualization.ipynb`](https://github.com/ProjectPythia/ERA5_interactive-cookbook/blob/main/notebooks/01BasicVisualization.ipynb), [`notebooks/02InteractiveVisualization.ipynb`](https://github.com/ProjectPythia/ERA5_interactive-cookbook/blob/main/notebooks/02InteractiveVisualization.ipynb), [`notebooks/03_hvplot.ipynb`](https://github.com/ProjectPythia/ERA5_interactive-cookbook/blob/main/notebooks/03_hvplot.ipynb), [`notebooks/04_dashboard.ipynb`](https://github.com/ProjectPythia/ERA5_interactive-cookbook/blob/main/notebooks/04_dashboard.ipynb), [`notebooks/05_data_preprocessing.ipynb`](https://github.com/ProjectPythia/ERA5_interactive-cookbook/blob/main/notebooks/05_data_preprocessing.ipynb), [`notebooks/06_era5_anomaly.ipynb`](https://github.com/ProjectPythia/ERA5_interactive-cookbook/blob/main/notebooks/06_era5_anomaly.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/ERA5_interactive-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Errors

**`AttributeError`** — 'pydantic_core._pydantic_core.ValidationInfo' object has no attribute 'format'

in `site/content/notebooks.data-preprocessing.json`

```
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[10], line 1
----> 1 era5_cat = intake.open_esm_datastore(era5_catalog)
      2 era5_cat

File /srv/conda/envs/notebook/lib/python3.10/site-packages/intake_esm/core.py:113, in esm_datastore.__init__(self, obj, progressbar, sep, registry, read_csv_kwargs, columns_with_iterables, storage_options, **intake_kwargs)
    111     self.esmcat = ESMCatalogModel.from_dict(obj)
    112 else:
--> 113     self.esmcat = ESMCatalogModel.load(
    114         obj, storage_options=self.storage_options, read_csv_kwargs=read_csv_kwargs
    115     )
    117 self.derivedcat = registry or default_registry
    118 self._entries = {}

File /srv/conda/envs/notebook/lib/python3.10/site-packages/intake_esm/cat.py:243, in ESMCatalogModel.load(cls, json_file, storage_options, read_csv_kwargs)
    241 if 'last_updated' not in data:
    242     data['last_updated'] = None
--> 243 cat = cls.model_validate(data)
    244 if cat.catalog_file:
    245     if _mapper.fs.exists(cat.catalog_file):

    [... skipping hidden 1 frame]

File /srv/conda/envs/notebook/
```

