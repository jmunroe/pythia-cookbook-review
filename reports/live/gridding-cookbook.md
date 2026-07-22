# gridding-cookbook

Live outcome: **ran with errors**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/gridding-cookbook)

Run 2026-07-22 05:03:54 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [gridding-cookbook](https://github.com/ProjectPythia/gridding-cookbook) at ref [`main`](https://github.com/ProjectPythia/gridding-cookbook/tree/main).

:::{warning} Cached image
BinderHub reused an existing image, so the 419.87s is a pod launch and image pull. It does **not** test whether `environment.yml` still solves.
:::

| Measure | Value |
|---|---|
| Live outcome | **ran with errors** |
| Static tier | `healthy` |
| Time to a ready session | 419.87s (cached image) |
| Build succeeded | yes |
| Notebook execution | 58.63s |
| Build command exit code | 0 (zero despite cell errors) |
| Notebooks ran clean | no |
| Execution cache | **reused — timing is not execution** |
| Peak memory (pss) | 3.73 GB |
| Pod memory limit | 8.59 GB |
| Peak as share of limit | 43.4% |
| Peak rss (upper bound, shared pages double-counted) | 3.74 GB |
| Errors raised | 1 |

| Notebook | Execute + render |
|---|---|
| [`notebooks/pyresample_intro.ipynb`](https://github.com/ProjectPythia/gridding-cookbook/blob/main/notebooks/pyresample_intro.ipynb) | 10.0s |
| [`notebooks/verde_intro.ipynb`](https://github.com/ProjectPythia/gridding-cookbook/blob/main/notebooks/verde_intro.ipynb) | 11.0s |
| [`notebooks/xESMF_introduction.ipynb`](https://github.com/ProjectPythia/gridding-cookbook/blob/main/notebooks/xESMF_introduction.ipynb) | 49.0s |

Executed 3 notebook(s) from the project toc: [`notebooks/pyresample_intro.ipynb`](https://github.com/ProjectPythia/gridding-cookbook/blob/main/notebooks/pyresample_intro.ipynb), [`notebooks/verde_intro.ipynb`](https://github.com/ProjectPythia/gridding-cookbook/blob/main/notebooks/verde_intro.ipynb), [`notebooks/xESMF_introduction.ipynb`](https://github.com/ProjectPythia/gridding-cookbook/blob/main/notebooks/xESMF_introduction.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/gridding-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Errors

**`FileNotFoundError`** — [Errno 2] No such file or directory: '/home/jovyan/notebooks/data/onestorm.nc'

in `site/content/notebooks.pyresample-intro.json`

```
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
File /srv/conda/envs/notebook/lib/python3.10/site-packages/xarray/backends/file_manager.py:211, in CachingFileManager._acquire_with_cache_info(self, needs_lock)
    210 try:
--> 211     file = self._cache[self._key]
    212 except KeyError:

File /srv/conda/envs/notebook/lib/python3.10/site-packages/xarray/backends/lru_cache.py:56, in LRUCache.__getitem__(self, key)
     55 with self._lock:
---> 56     value = self._cache[key]
     57     self._cache.move_to_end(key)

KeyError: [<class 'netCDF4._netCDF4.Dataset'>, ('/home/jovyan/notebooks/data/onestorm.nc',), 'r', (('clobber', True), ('diskless', False), ('format', 'NETCDF4'), ('persist', False)), 'f8fe2efb-1989-46f0-9437-8982235d3130']

During handling of the above exception, another exception occurred:

FileNotFoundError                         Traceback (most recent call last)
Cell In[6], line 1
----> 1 area_def, cf_info = load_cf_area('data/onestorm.nc', variable='visible', x='x', y='y')

File /srv/conda/envs/notebook/lib/python3.10/site-packages/pyresample/utils/cf.py:444, in l
```

