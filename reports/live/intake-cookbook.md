# intake-cookbook

Live outcome: **ran with errors**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/intake-cookbook)

Run 2026-07-22 03:08:29 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [intake-cookbook](https://github.com/ProjectPythia/intake-cookbook) at ref [`main`](https://github.com/ProjectPythia/intake-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **ran with errors** |
| Static tier | `degraded` |
| Time to a ready session | 8m 29s (fresh build) |
| Build succeeded | yes |
| Notebook execution | 20.27s |
| Build command exit code | 0 (zero despite cell errors) |
| Notebooks ran clean | no |
| Execution cache | **reused — timing is not execution** |
| Peak memory (pss) | 0.50 GB |
| Pod memory limit | 8.59 GB |
| Peak as share of limit | 5.9% |
| Peak rss (upper bound, shared pages double-counted) | 0.59 GB |
| Errors raised | 2 |

| Notebook | Execute + render |
|---|---|
| [`notebooks/creating_catalogs.ipynb`](https://github.com/ProjectPythia/intake-cookbook/blob/main/notebooks/creating_catalogs.ipynb) | 5.1s |
| [`notebooks/intake_introduction.ipynb`](https://github.com/ProjectPythia/intake-cookbook/blob/main/notebooks/intake_introduction.ipynb) | 5.71s |

Executed 2 notebook(s) from the project toc: [`notebooks/creating_catalogs.ipynb`](https://github.com/ProjectPythia/intake-cookbook/blob/main/notebooks/creating_catalogs.ipynb), [`notebooks/intake_introduction.ipynb`](https://github.com/ProjectPythia/intake-cookbook/blob/main/notebooks/intake_introduction.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/intake-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Errors

**`AttributeError`** — 'ZarrSource' object has no attribute 'yaml'

in `site/content/notebooks.creating-catalogs.json`

```
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[5], line 1
----> 1 print(source.yaml())

AttributeError: 'ZarrSource' object has no attribute 'yaml'
```

**`AttributeError`** — 'ZarrSource' object has no attribute 'describe'

in `site/content/notebooks.intake-introduction.json`

```
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[5], line 1
----> 1 desc = cat.hrrrzarr.describe()
      2 desc

AttributeError: 'ZarrSource' object has no attribute 'describe'
```

