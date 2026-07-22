# landsat-ml-cookbook

Live outcome: **ran with errors**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/landsat-ml-cookbook)

Run 2026-07-21 19:29:05 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [landsat-ml-cookbook](https://github.com/ProjectPythia/landsat-ml-cookbook) at ref [`main`](https://github.com/ProjectPythia/landsat-ml-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **ran with errors** |
| Static tier | `stale` |
| Time to a ready session | 7m 49s (fresh build) |
| Build succeeded | yes |
| Notebook execution | 34.69s |
| Build command exit code | 0 (zero despite cell errors) |
| Notebooks ran clean | no |
| Execution cache | **reused — timing is not execution** |
| Peak memory (pss) | 0.95 GB |
| Pod memory limit | 8.59 GB |
| Peak as share of limit | 11.0% |
| Peak rss (upper bound, shared pages double-counted) | 1.16 GB |
| Errors raised | 3 |

| Notebook | Execute + render |
|---|---|
| [`notebooks/0.0_Intro_Landsat.ipynb`](https://github.com/ProjectPythia/landsat-ml-cookbook/blob/main/notebooks/0.0_Intro_Landsat.ipynb) | 0.03s |
| [`notebooks/2.0_Spectral_Clustering_PC.ipynb`](https://github.com/ProjectPythia/landsat-ml-cookbook/blob/main/notebooks/2.0_Spectral_Clustering_PC.ipynb) | 7.56s |
| [`notebooks/1.1_Data_Ingestion-General.ipynb`](https://github.com/ProjectPythia/landsat-ml-cookbook/blob/main/notebooks/1.1_Data_Ingestion-General.ipynb) | 10s |
| [`notebooks/1.0_Data_Ingestion-Geospatial.ipynb`](https://github.com/ProjectPythia/landsat-ml-cookbook/blob/main/notebooks/1.0_Data_Ingestion-Geospatial.ipynb) | 21s |

Executed 4 notebook(s) from the project toc: [`notebooks/0.0_Intro_Landsat.ipynb`](https://github.com/ProjectPythia/landsat-ml-cookbook/blob/main/notebooks/0.0_Intro_Landsat.ipynb), [`notebooks/1.0_Data_Ingestion-Geospatial.ipynb`](https://github.com/ProjectPythia/landsat-ml-cookbook/blob/main/notebooks/1.0_Data_Ingestion-Geospatial.ipynb), [`notebooks/1.1_Data_Ingestion-General.ipynb`](https://github.com/ProjectPythia/landsat-ml-cookbook/blob/main/notebooks/1.1_Data_Ingestion-General.ipynb), [`notebooks/2.0_Spectral_Clustering_PC.ipynb`](https://github.com/ProjectPythia/landsat-ml-cookbook/blob/main/notebooks/2.0_Spectral_Clustering_PC.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/landsat-ml-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Errors

**`ImportError`** — cannot import name 'collections_to_dsk' from 'dask.base' (/srv/conda/envs/notebook/lib/python3.10/site-packages/dask/base.py)

in `html/notebooks.spectral-clustering-pc.json`

```
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
Cell In[1], line 7
      5 import pystac_client
      6 import xarray as xr
----> 7 from dask.distributed import Client
      8 from pystac.extensions.eo import EOExtension as eo
      9 from dask_ml.cluster import SpectralClustering

File /srv/conda/envs/notebook/lib/python3.10/site-packages/dask/distributed.py:11
      3 _import_error_message = (
      4     "dask.distributed is not installed.\n\n"
      5     "Please either conda or pip install distributed:\n\n"
      6     "  conda install dask distributed             # either conda install\n"
      7     '  python -m pip install "dask[distributed]" --upgrade    # or pip install'
      8 )
     10 try:
---> 11     from distributed import *  # noqa: F403
     12 except ImportError as e:
     13     if e.msg == "No module named 'distributed'":

File /srv/conda/envs/notebook/lib/python3.10/site-packages/distributed/__init__.py:23
     20 from dask.config import config  # type: ignore
     22 from distributed._version import get_versions
---> 23 from distributed.actor import Actor, 
```

**`ClientPayloadError`** — 400, message:
  Can not decode content-encoding: br

in `html/notebooks.data-ingestion-general.json`

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
File /srv/conda/envs/notebook/lib/python3.10/site-packages/aiohttp/http_parser.py:1197, in DeflateBuffer.feed_data(self, chunk, size)
   1196 try:
-> 1197     chunk = self.decompressor.decompress_sync(chunk, max_length=max_length)
   1198 except Exception:

File /srv/conda/envs/notebook/lib/python3.10/site-packages/aiohttp/compression_utils.py:371, in BrotliDecompressor.decompress_sync(self, data, max_length)
    370     else:
--> 371         result = cast(bytes, self._obj.process(data, max_length))
    372 # Only way to know that brotli has no further data is checking we get no output

TypeError: process() takes exactly 1 argument (2 given)

During handling of the above exception, another exception occurred:

ContentEncodingError                      Traceback (most recent call last)
File /srv/conda/envs/notebook/lib/python3.10/site-packages/aiohttp/_http_parser.pyx:894, in aiohttp._http_parser.cb_on_body()

File /srv/conda/envs/notebook/lib/python3.10/site-packages/aiohttp/http_parser.py:1199, in DeflateBuffer.feed_data(self, chun
```

**`KeyError`** — 'proj:epsg'

in `html/notebooks.data-ingestion-geospatial.json`

```
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
Cell In[18], line 1
----> 1 da.attrs["crs"] = f"epsg:{selected_item.properties['proj:epsg']}"
      2 da.attrs["crs"]

KeyError: 'proj:epsg'
```

