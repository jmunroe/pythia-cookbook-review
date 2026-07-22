# mpasviewer-cookbook

Live outcome: **ran with errors**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/mpasviewer-cookbook)

Run 2026-07-22 23:18:45 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [mpasviewer-cookbook](https://github.com/ProjectPythia/mpasviewer-cookbook) at ref [`main`](https://github.com/ProjectPythia/mpasviewer-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **ran with errors** |
| Static tier | `incubating` |
| Time to a ready session | 6m 40s (fresh build) |
| Build succeeded | yes |
| Notebook execution | 3m 06s |
| Build command exit code | 0 (zero despite cell errors) |
| Notebooks ran clean | no |
| Execution cache | **reused — timing is not execution** |
| Peak memory (pss) | 1.78 GB |
| Pod memory limit | 8.59 GB |
| Peak as share of limit | 20.7% |
| Peak rss (upper bound, shared pages double-counted) | 1.90 GB |
| Errors raised | 1 |

| Notebook | Execute + render |
|---|---|
| [`notebooks/introduction.ipynb`](https://github.com/ProjectPythia/mpasviewer-cookbook/blob/main/notebooks/introduction.ipynb) | 0.04s |
| [`notebooks/20_remote_out_hurricane_investigation.ipynb`](https://github.com/ProjectPythia/mpasviewer-cookbook/blob/main/notebooks/20_remote_out_hurricane_investigation.ipynb) | 4.44s |

Executed 4 notebook(s) from the project toc: [`notebooks/20_remote_out_hurricane_investigation.ipynb`](https://github.com/ProjectPythia/mpasviewer-cookbook/blob/main/notebooks/20_remote_out_hurricane_investigation.ipynb), [`notebooks/Hurricane_Ida_Pt2.ipynb`](https://github.com/ProjectPythia/mpasviewer-cookbook/blob/main/notebooks/Hurricane_Ida_Pt2.ipynb), [`notebooks/convective-environments.ipynb`](https://github.com/ProjectPythia/mpasviewer-cookbook/blob/main/notebooks/convective-environments.ipynb), [`notebooks/introduction.ipynb`](https://github.com/ProjectPythia/mpasviewer-cookbook/blob/main/notebooks/introduction.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/mpasviewer-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Errors

**`ClientResponseError`** — 503, message='Service Temporarily Unavailable', url='https://tds.gdex.ucar.edu/thredds/catalog/files/d010077/native_diag/catalog.html'

in `site/content/notebooks.remote-out-hurricane-investigation.json`

```
---------------------------------------------------------------------------
ClientResponseError                       Traceback (most recent call last)
Cell In[4], line 3
      1 url_thredds = "https://tds.gdex.ucar.edu/thredds/catalog/files/d010077/native_diag/catalog.html"
      2 inidt = datetime(2017, 9, 20, 0); enddt = datetime(2017, 9, 20, 12)
----> 3 list_files = scvtmesh.get_thredds_list(url_thredds, date_start=inidt, date_end=enddt)

File /srv/conda/envs/notebook/lib/python3.14/site-packages/mpasviewer/main.py:827, in scvtmesh.get_thredds_list(url_thredds, date_start, date_end)
    825 def get_thredds_list(url_thredds, date_start=None, date_end=None):
    826     fs = fsspec.filesystem("https")
--> 827     files_metadata = fs.ls(url_thredds)
    829     file_urls = [file["name"] for file in files_metadata]
    831     file_nms = [os.path.basename(f) for f in file_urls] 

File /srv/conda/envs/notebook/lib/python3.14/site-packages/fsspec/asyn.py:118, in sync_wrapper.<locals>.wrapper(*args, **kwargs)
    115 @functools.wraps(func)
    116 def wrapper(*args, **kwargs):
    117     self = obj or args[0]
--> 118     return sync(self.loop, func, *args, **kwargs)

File /srv/conda/
```

