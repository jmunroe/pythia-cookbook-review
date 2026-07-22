# physical-oceanography-cookbook

Live outcome: **ran with errors**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/physical-oceanography-cookbook)

Run 2026-07-22 20:28:31 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [physical-oceanography-cookbook](https://github.com/ProjectPythia/physical-oceanography-cookbook) at ref [`main`](https://github.com/ProjectPythia/physical-oceanography-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **ran with errors** |
| Static tier | `incubating` |
| Time to a ready session | 6m 09s (fresh build) |
| Build succeeded | yes |
| Notebook execution | 1m 16s |
| Build command exit code | 0 (zero despite cell errors) |
| Notebooks ran clean | no |
| Execution cache | **reused — timing is not execution** |
| Peak memory (pss) | 1.32 GB |
| Pod memory limit | 8.59 GB |
| Peak as share of limit | 15.3% |
| Peak rss (upper bound, shared pages double-counted) | 1.66 GB |
| Errors raised | 5 |

| Notebook | Execute + render |
|---|---|
| [`notebooks/notebook-template.ipynb`](https://github.com/ProjectPythia/physical-oceanography-cookbook/blob/main/notebooks/notebook-template.ipynb) | 1.67s |
| [`notebooks/04_eccov4.ipynb`](https://github.com/ProjectPythia/physical-oceanography-cookbook/blob/main/notebooks/04_eccov4.ipynb) | 43s |
| [`notebooks/05_gulf_stream_currents.ipynb`](https://github.com/ProjectPythia/physical-oceanography-cookbook/blob/main/notebooks/05_gulf_stream_currents.ipynb) | 43s |
| [`notebooks/01_sea-surface-height.ipynb`](https://github.com/ProjectPythia/physical-oceanography-cookbook/blob/main/notebooks/01_sea-surface-height.ipynb) | 47s |
| [`notebooks/03_cesm_MOM6.ipynb`](https://github.com/ProjectPythia/physical-oceanography-cookbook/blob/main/notebooks/03_cesm_MOM6.ipynb) | 48s |
| [`notebooks/02_along_track.ipynb`](https://github.com/ProjectPythia/physical-oceanography-cookbook/blob/main/notebooks/02_along_track.ipynb) | 49s |

Executed 6 notebook(s) from the project toc: [`notebooks/01_sea-surface-height.ipynb`](https://github.com/ProjectPythia/physical-oceanography-cookbook/blob/main/notebooks/01_sea-surface-height.ipynb), [`notebooks/02_along_track.ipynb`](https://github.com/ProjectPythia/physical-oceanography-cookbook/blob/main/notebooks/02_along_track.ipynb), [`notebooks/03_cesm_MOM6.ipynb`](https://github.com/ProjectPythia/physical-oceanography-cookbook/blob/main/notebooks/03_cesm_MOM6.ipynb), [`notebooks/04_eccov4.ipynb`](https://github.com/ProjectPythia/physical-oceanography-cookbook/blob/main/notebooks/04_eccov4.ipynb), [`notebooks/05_gulf_stream_currents.ipynb`](https://github.com/ProjectPythia/physical-oceanography-cookbook/blob/main/notebooks/05_gulf_stream_currents.ipynb), [`notebooks/notebook-template.ipynb`](https://github.com/ProjectPythia/physical-oceanography-cookbook/blob/main/notebooks/notebook-template.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/physical-oceanography-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Errors

**`ValueError`** — Bad Request: https://storage.googleapis.com/download/storage/v1/b/pangeo-cesm-mom6/o/.zmetadata?alt=media
User project specified in the request is invalid.

in `site/content/notebooks.cesm-mom6.json`

```
------------------------------------------------------...
```

**`ValueError`** — Bad Request: https://storage.googleapis.com/download/storage/v1/b/pangeo-cnes/o/alti%2Fj3%2F.zmetadata?alt=media
User project specified in the request is invalid.

in `site/content/notebooks.along-track.json`

```
------------------------------------------------------...
```

**`ValueError`** — Bad Request: https://storage.googleapis.com/download/storage/v1/b/pangeo-cmems-duacs/o/.zmetadata?alt=media
User project specified in the request is invalid.

in `site/content/notebooks.sea-surface-height.json`

```
------------------------------------------------------...
```

**`ValueError`** — Bad Request: https://storage.googleapis.com/download/storage/v1/b/pangeo-ecco-eccov4r3/o/eccov4r3%2F.zmetadata?alt=media
User project specified in the request is invalid.

in `site/content/notebooks.eccov4.json`

```
------------------------------------------------------...
```

**`ValueError`** — Bad Request: https://storage.googleapis.com/download/storage/v1/b/pangeo-cmems-duacs/o/.zmetadata?alt=media
User project specified in the request is invalid.

in `site/content/notebooks.gulf-stream-currents.json`

```
------------------------------------------------------...
```

