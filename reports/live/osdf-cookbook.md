# osdf-cookbook

Live outcome: **ran with errors**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/osdf-cookbook)

Run 2026-07-23 03:52:28 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [osdf-cookbook](https://github.com/ProjectPythia/osdf-cookbook) at ref [`main`](https://github.com/ProjectPythia/osdf-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **ran with errors** |
| Static tier | `healthy` |
| Time to a ready session | 15m 09s (fresh build) |
| Build succeeded | yes |
| Notebook execution | 3m 26s |
| Build command exit code | 0 (zero despite cell errors) |
| Notebooks ran clean | no |
| Execution cache | **reused — timing is not execution** |
| Peak memory (pss) | 5.27 GB |
| Pod memory limit | 8.59 GB |
| Peak as share of limit | 61.4% |
| Peak rss (upper bound, shared pages double-counted) | 5.40 GB |
| Errors raised | 4 |

| Notebook | Execute + render |
|---|---|
| [`notebooks/02_ncar_intro.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/02_ncar_intro.ipynb) | 0.13s |
| [`notebooks/03_EnviStor_Foundations.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/03_EnviStor_Foundations.ipynb) | 0.13s |
| [`notebooks/06_introduction_to_NSDF_OpenVISUS.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/06_introduction_to_NSDF_OpenVISUS.ipynb) | 0.1s |
| [`notebooks/05_PyCoGSS_Foundations.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/05_PyCoGSS_Foundations.ipynb) | 0.96s |
| [`notebooks/04_SonarAI_Foundations.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/04_SonarAI_Foundations.ipynb) | 4.46s |
| [`notebooks/01_osdf_intro.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/01_osdf_intro.ipynb) | 6.69s |
| [`notebooks/06_atmosphere_llc2160_visualization.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/06_atmosphere_llc2160_visualization.ipynb) | 11s |
| [`notebooks/02_cmip6_gmst.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/02_cmip6_gmst.ipynb) | 15s |
| [`notebooks/02_cesm2_oceanheat.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/02_cesm2_oceanheat.ipynb) | 15s |
| [`notebooks/03_EnviStor_Technical.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/03_EnviStor_Technical.ipynb) | 16s |
| [`notebooks/01_pelicanfs.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/01_pelicanfs.ipynb) | 22s |
| [`notebooks/06_ocean_llc2160_visualization.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/06_ocean_llc2160_visualization.ipynb) | 23s |
| [`notebooks/06_ocean_llc4320_visualization.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/06_ocean_llc4320_visualization.ipynb) | 47s |

Executed 15 notebook(s) from the project toc: [`notebooks/01_osdf_intro.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/01_osdf_intro.ipynb), [`notebooks/01_pelicanfs.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/01_pelicanfs.ipynb), [`notebooks/02_cesm2_oceanheat.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/02_cesm2_oceanheat.ipynb), [`notebooks/02_cmip6_gmst.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/02_cmip6_gmst.ipynb), [`notebooks/02_ncar_intro.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/02_ncar_intro.ipynb), [`notebooks/03_EnviStor_Foundations.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/03_EnviStor_Foundations.ipynb), [`notebooks/03_EnviStor_Technical.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/03_EnviStor_Technical.ipynb), [`notebooks/04_SonarAI_Foundations.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/04_SonarAI_Foundations.ipynb), [`notebooks/04_SonarAI_Technical.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/04_SonarAI_Technical.ipynb), [`notebooks/05_PyCoGSS_Foundations.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/05_PyCoGSS_Foundations.ipynb), [`notebooks/05_PyCoGSS_SpectralChange_PFS.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/05_PyCoGSS_SpectralChange_PFS.ipynb), [`notebooks/06_atmosphere_llc2160_visualization.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/06_atmosphere_llc2160_visualization.ipynb), [`notebooks/06_introduction_to_NSDF_OpenVISUS.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/06_introduction_to_NSDF_OpenVISUS.ipynb), [`notebooks/06_ocean_llc2160_visualization.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/06_ocean_llc2160_visualization.ipynb), [`notebooks/06_ocean_llc4320_visualization.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/06_ocean_llc4320_visualization.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Errors

**`AttributeError`** — 'pydantic_core._pydantic_core.ValidationInfo' object has no attribute 'format'

in `site/content/notebooks.cesm2-oceanheat.json`

```
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[5], line 1
----> 1 col = intake.open_esm_datastore(cat_url)
      2 col

File /srv/conda/envs/notebook/lib/python3.12/site-packages/intake_esm/core.py:113, in esm_datastore.__init__(self, obj, progressbar, sep, registry, read_csv_kwargs, columns_with_iterables, storage_options, **intake_kwargs)
    111     self.esmcat = ESMCatalogModel.from_dict(obj)
    112 else:
--> 113     self.esmcat = ESMCatalogModel.load(
    114         obj, storage_options=self.storage_options, read_csv_kwargs=read_csv_kwargs
    115     )
    117 self.derivedcat = registry or default_registry
    118 self._entries = {}

File /srv/conda/envs/notebook/lib/python3.12/site-packages/intake_esm/cat.py:243, in ESMCatalogModel.load(cls, json_file, storage_options, read_csv_kwargs)
    241 if 'last_updated' not in data:
    242     data['last_updated'] = None
--> 243 cat = cls.model_validate(data)
    244 if cat.catalog_file:
    245     if _mapper.fs.exists(cat.catalog_file):

    [... skipping hidden 1 frame]

File /srv/conda/envs/notebook/lib/python3.12/s
```

**`AttributeError`** — 'pydantic_core._pydantic_core.ValidationInfo' object has no attribute 'format'

in `site/content/notebooks.pelicanfs.json`

```
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[5], line 4
      1 gdex_url    =  'https://data.gdex.ucar.edu/'
      2 cat_url     = gdex_url +  'd850001/catalogs/osdf/cmip6-aws/cmip6-osdf-zarr.json'
----> 4 col = intake.open_esm_datastore(cat_url)
      6 expts = ['historical']
      8 query = dict(
      9     experiment_id=expts,
     10     table_id='Amon',
   (...)     13     #activity_id = 'CMIP',
     14 )

File /srv/conda/envs/notebook/lib/python3.12/site-packages/intake_esm/core.py:113, in esm_datastore.__init__(self, obj, progressbar, sep, registry, read_csv_kwargs, columns_with_iterables, storage_options, **intake_kwargs)
    111     self.esmcat = ESMCatalogModel.from_dict(obj)
    112 else:
--> 113     self.esmcat = ESMCatalogModel.load(
    114         obj, storage_options=self.storage_options, read_csv_kwargs=read_csv_kwargs
    115     )
    117 self.derivedcat = registry or default_registry
    118 self._entries = {}

File /srv/conda/envs/notebook/lib/python3.12/site-packages/intake_esm/cat.py:243, in ESMCatalogModel.load(cls, json_file, storage_options, 
```

**`NoAvailableSource`** — 

in `site/content/notebooks.envistor-technical.json`

```
---------------------------------------------------------------------------
NoAvailableSource                         Traceback (most recent call last)
Cell In[2], line 2
      1 pelfs = OSDFFileSystem()
----> 2 file_buoy1 = pelfs.cat('/envistor/CREST_Buoy_2_NW_Biscayne_Bay_-_S_of_Biscayne_Canal_082720-112221.xlsx')
      3 file_buoy2 = pelfs.cat('/envistor/CREST_Buoy_3_Haulover_Inlet_100518_-_073020_updated.xlsx')
      4 file_buoy3 = pelfs.cat('/envistor/CREST_Buoy_3-2_Little_River_042121-050624.xlsx')

File /srv/conda/envs/notebook/lib/python3.12/site-packages/fsspec/asyn.py:118, in sync_wrapper.<locals>.wrapper(*args, **kwargs)
    115 @functools.wraps(func)
    116 def wrapper(*args, **kwargs):
    117     self = obj or args[0]
--> 118     return sync(self.loop, func, *args, **kwargs)

File /srv/conda/envs/notebook/lib/python3.12/site-packages/fsspec/asyn.py:103, in sync(loop, func, timeout, *args, **kwargs)
    101     raise FSTimeoutError from return_result
    102 elif isinstance(return_result, BaseException):
--> 103     raise return_result
    104 else:
    105     return return_result

File /srv/conda/envs/notebook/lib/python3.12/site-packages/fsspec/asyn.py:56, in _runn
```

**`AttributeError`** — 'pydantic_core._pydantic_core.ValidationInfo' object has no attribute 'format'

in `site/content/notebooks.cmip6-gmst.json`

```
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[5], line 1
----> 1 col = intake.open_esm_datastore(cat_url)
      2 col

File /srv/conda/envs/notebook/lib/python3.12/site-packages/intake_esm/core.py:113, in esm_datastore.__init__(self, obj, progressbar, sep, registry, read_csv_kwargs, columns_with_iterables, storage_options, **intake_kwargs)
    111     self.esmcat = ESMCatalogModel.from_dict(obj)
    112 else:
--> 113     self.esmcat = ESMCatalogModel.load(
    114         obj, storage_options=self.storage_options, read_csv_kwargs=read_csv_kwargs
    115     )
    117 self.derivedcat = registry or default_registry
    118 self._entries = {}

File /srv/conda/envs/notebook/lib/python3.12/site-packages/intake_esm/cat.py:243, in ESMCatalogModel.load(cls, json_file, storage_options, read_csv_kwargs)
    241 if 'last_updated' not in data:
    242     data['last_updated'] = None
--> 243 cat = cls.model_validate(data)
    244 if cat.catalog_file:
    245     if _mapper.fs.exists(cat.catalog_file):

    [... skipping hidden 1 frame]

File /srv/conda/envs/notebook/lib/python3.12/s
```

