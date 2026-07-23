# CFC-extreme-weather-cookbook

Live outcome: **ran with errors**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/CFC-extreme-weather-cookbook)

Run 2026-07-23 00:33:02 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [CFC-extreme-weather-cookbook](https://github.com/ProjectPythia/CFC-extreme-weather-cookbook) at ref [`main`](https://github.com/ProjectPythia/CFC-extreme-weather-cookbook/tree/main).

:::{warning} Cached image
BinderHub reused an existing image, so the 9m 18s is a pod launch and image pull. It does **not** test whether `environment.yml` still solves.
:::

| Measure | Value |
|---|---|
| Live outcome | **ran with errors** |
| Static tier | `incubating` |
| Time to a ready session | 9m 18s (cached image) |
| Build succeeded | yes |
| Notebook execution | 2m 51s |
| Build command exit code | 0 (zero despite cell errors) |
| Notebooks ran clean | no |
| Execution cache | **reused — timing is not execution** |
| Peak memory (pss) | 0.84 GB |
| Pod memory limit | 8.59 GB |
| Peak as share of limit | 9.8% |
| Peak rss (upper bound, shared pages double-counted) | 1.02 GB |
| Errors raised | 2 |

| Notebook | Execute + render |
|---|---|
| [`notebooks/cfc-atm.ipynb`](https://github.com/ProjectPythia/CFC-extreme-weather-cookbook/blob/main/notebooks/cfc-atm.ipynb) | 6.21s |

Executed 2 notebook(s) from the project toc: [`notebooks/cfc-atm.ipynb`](https://github.com/ProjectPythia/CFC-extreme-weather-cookbook/blob/main/notebooks/cfc-atm.ipynb), [`notebooks/cfc-ocean.ipynb`](https://github.com/ProjectPythia/CFC-extreme-weather-cookbook/blob/main/notebooks/cfc-ocean.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/CFC-extreme-weather-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Errors

**`ModuleNotFoundError`** — No module named 'xgcm.autogenerate'

in `site/content/notebooks.cfc-atm.json`

```
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[4], line 16
     14 from xgcm import Grid
     15 import xgcm 
---> 16 from xgcm.autogenerate import generate_grid_ds
     18 from cartopy.mpl.geoaxes import GeoAxes
     19 import matplotlib.ticker as mticker

ModuleNotFoundError: No module named 'xgcm.autogenerate'
```

**`TypeError`** — Regions.mask() got an unexpected keyword argument 'lon_name'

in `site/content/notebooks.cfc-ocean.json`

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[11], line 1
----> 1 basin_mask = merged_mask(basins, ds[['lat', 'lon']])

File /srv/conda/envs/notebook/lib/python3.10/site-packages/xmip/regionmask.py:188, in merged_mask(basins, ds, lon_name, lat_name, merge_dict, verbose)
    137 def merged_mask(
    138     basins, ds, lon_name="lon", lat_name="lat", merge_dict=None, verbose=False
    139 ):
    140     """Combine geographical basins (from regionmask) to larger ocean basins.
    141 
    142     Parameters
   (...)
    186 
    187     """
--> 188     mask = basins.mask(ds, lon_name=lon_name, lat_name=lat_name)
    190     if merge_dict is None:
    191         merge_dict = _default_merge_dict()

TypeError: Regions.mask() got an unexpected keyword argument 'lon_name'
```

