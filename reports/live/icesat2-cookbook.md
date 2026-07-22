# icesat2-cookbook

Live outcome: **ran with errors**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/icesat2-cookbook)

Run 2026-07-22 10:34:53 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [icesat2-cookbook](https://github.com/ProjectPythia/icesat2-cookbook) at ref [`main`](https://github.com/ProjectPythia/icesat2-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **ran with errors** |
| Static tier | `incubating` |
| Time to a ready session | 12m 10s (fresh build) |
| Build succeeded | yes |
| Notebook execution | 1m 04s |
| Build command exit code | 0 (zero despite cell errors) |
| Notebooks ran clean | no |
| Execution cache | **reused — timing is not execution** |
| Peak memory (pss) | 1.84 GB |
| Pod memory limit | 8.59 GB |
| Peak as share of limit | 21.4% |
| Peak rss (upper bound, shared pages double-counted) | 1.86 GB |
| Errors raised | 2 |

| Notebook | Execute + render |
|---|---|
| [`notebooks/governance.ipynb`](https://github.com/ProjectPythia/icesat2-cookbook/blob/main/notebooks/governance.ipynb) | 0.12s |
| [`notebooks/contributing.ipynb`](https://github.com/ProjectPythia/icesat2-cookbook/blob/main/notebooks/contributing.ipynb) | 0.12s |
| [`notebooks/engagement.ipynb`](https://github.com/ProjectPythia/icesat2-cookbook/blob/main/notebooks/engagement.ipynb) | 0.12s |
| [`notebooks/visualization.ipynb`](https://github.com/ProjectPythia/icesat2-cookbook/blob/main/notebooks/visualization.ipynb) | 0.16s |
| [`notebooks/mission-overview.ipynb`](https://github.com/ProjectPythia/icesat2-cookbook/blob/main/notebooks/mission-overview.ipynb) | 1.58s |
| [`notebooks/land-ice.ipynb`](https://github.com/ProjectPythia/icesat2-cookbook/blob/main/notebooks/land-ice.ipynb) | 9.23s |
| [`notebooks/geospatial-transforms.ipynb`](https://github.com/ProjectPythia/icesat2-cookbook/blob/main/notebooks/geospatial-transforms.ipynb) | 40s |
| [`notebooks/filtering.ipynb`](https://github.com/ProjectPythia/icesat2-cookbook/blob/main/notebooks/filtering.ipynb) | 52s |

Executed 9 notebook(s) from the project toc: [`notebooks/contributing.ipynb`](https://github.com/ProjectPythia/icesat2-cookbook/blob/main/notebooks/contributing.ipynb), [`notebooks/engagement.ipynb`](https://github.com/ProjectPythia/icesat2-cookbook/blob/main/notebooks/engagement.ipynb), [`notebooks/filtering.ipynb`](https://github.com/ProjectPythia/icesat2-cookbook/blob/main/notebooks/filtering.ipynb), [`notebooks/geospatial-transforms.ipynb`](https://github.com/ProjectPythia/icesat2-cookbook/blob/main/notebooks/geospatial-transforms.ipynb), [`notebooks/governance.ipynb`](https://github.com/ProjectPythia/icesat2-cookbook/blob/main/notebooks/governance.ipynb), [`notebooks/land-ice.ipynb`](https://github.com/ProjectPythia/icesat2-cookbook/blob/main/notebooks/land-ice.ipynb), [`notebooks/mission-overview.ipynb`](https://github.com/ProjectPythia/icesat2-cookbook/blob/main/notebooks/mission-overview.ipynb), [`notebooks/snowdepth.ipynb`](https://github.com/ProjectPythia/icesat2-cookbook/blob/main/notebooks/snowdepth.ipynb), [`notebooks/visualization.ipynb`](https://github.com/ProjectPythia/icesat2-cookbook/blob/main/notebooks/visualization.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/icesat2-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Errors

**`IndexError`** — list index out of range

in `site/content/notebooks.geospatial-transforms.json`

```
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
Cell In[31], line 8
      6 # read multiple HDF5 groups and merge into a dataset
      7 groups = ['gt1l/land_ice_segments', 'gt1l/land_ice_segments/dem']
----> 8 ds = xr.merge([xr.open_dataset(buffers[0], group=g) for g in groups])
      9 # inspect ATL06 data for beam group
     10 ds

Cell In[31], line 8, in <listcomp>(.0)
      6 # read multiple HDF5 groups and merge into a dataset
      7 groups = ['gt1l/land_ice_segments', 'gt1l/land_ice_segments/dem']
----> 8 ds = xr.merge([xr.open_dataset(buffers[0], group=g) for g in groups])
      9 # inspect ATL06 data for beam group
     10 ds

IndexError: list index out of range
```

**`AttributeError`** — The geopandas.dataset has been deprecated and was removed in GeoPandas 1.0. You can get the original 'naturalearth_lowres' data from https://www.naturalearthdata.com/downloads/110m-cultural-vectors/.

in `site/content/notebooks.land-ice.json`

```
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
File /srv/conda/envs/notebook/lib/python3.10/site-packages/icepyx/core/query.py:1135, in Query.visualize_spatial_extent(self)
   1134 try:
-> 1135     import geoviews as gv
   1136     from shapely.geometry import Polygon  # noqa: F401

ModuleNotFoundError: No module named 'geoviews'

During handling of the above exception, another exception occurred:

AttributeError                            Traceback (most recent call last)
Cell In[3], line 1
----> 1 region_a.visualize_spatial_extent()

File /srv/conda/envs/notebook/lib/python3.10/site-packages/icepyx/core/query.py:1145, in Query.visualize_spatial_extent(self)
   1142     return tile * bbox_poly
   1144 except ImportError:
-> 1145     world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
   1146     f, ax = plt.subplots(1, figsize=(12, 6))
   1147     world.plot(ax=ax, facecolor="lightgray", edgecolor="gray")

File /srv/conda/envs/notebook/lib/python3.10/site-packages/geopandas/datasets/__init__.py:18, in get_path(dataset)
     12 error_msg = (
     13     "The geop
```

