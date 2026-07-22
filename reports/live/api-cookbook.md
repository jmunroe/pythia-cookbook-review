# api-cookbook

Live outcome: **ran with errors**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/api-cookbook)

Run 2026-07-22 08:39:10 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [api-cookbook](https://github.com/ProjectPythia/api-cookbook) at ref [`main`](https://github.com/ProjectPythia/api-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **ran with errors** |
| Static tier | `incubating` |
| Time to a ready session | 6m 33s (fresh build) |
| Build succeeded | yes |
| Notebook execution | 22.02s |
| Build command exit code | 0 (zero despite cell errors) |
| Notebooks ran clean | no |
| Execution cache | **reused — timing is not execution** |
| Peak memory (pss) | 0.97 GB |
| Pod memory limit | 8.59 GB |
| Peak as share of limit | 11.3% |
| Peak rss (upper bound, shared pages double-counted) | 1.23 GB |
| Errors raised | 1 |

| Notebook | Execute + render |
|---|---|
| [`notebooks/example-workflows/cneos-fireball.ipynb`](https://github.com/ProjectPythia/api-cookbook/blob/main/notebooks/example-workflows/cneos-fireball.ipynb) | 5.61s |
| [`notebooks/example-workflows/air-quality-system-api.ipynb`](https://github.com/ProjectPythia/api-cookbook/blob/main/notebooks/example-workflows/air-quality-system-api.ipynb) | 5.83s |
| [`notebooks/example-workflows/wfm-cloud-water.ipynb`](https://github.com/ProjectPythia/api-cookbook/blob/main/notebooks/example-workflows/wfm-cloud-water.ipynb) | 6.08s |
| [`notebooks/api-foundations/api-basics.ipynb`](https://github.com/ProjectPythia/api-cookbook/blob/main/notebooks/api-foundations/api-basics.ipynb) | 7.06s |
| [`notebooks/example-workflows/earthaccess-sla-sss.ipynb`](https://github.com/ProjectPythia/api-cookbook/blob/main/notebooks/example-workflows/earthaccess-sla-sss.ipynb) | 13s |

Executed 5 notebook(s) from the project toc: [`notebooks/api-foundations/api-basics.ipynb`](https://github.com/ProjectPythia/api-cookbook/blob/main/notebooks/api-foundations/api-basics.ipynb), [`notebooks/example-workflows/air-quality-system-api.ipynb`](https://github.com/ProjectPythia/api-cookbook/blob/main/notebooks/example-workflows/air-quality-system-api.ipynb), [`notebooks/example-workflows/cneos-fireball.ipynb`](https://github.com/ProjectPythia/api-cookbook/blob/main/notebooks/example-workflows/cneos-fireball.ipynb), [`notebooks/example-workflows/earthaccess-sla-sss.ipynb`](https://github.com/ProjectPythia/api-cookbook/blob/main/notebooks/example-workflows/earthaccess-sla-sss.ipynb), [`notebooks/example-workflows/wfm-cloud-water.ipynb`](https://github.com/ProjectPythia/api-cookbook/blob/main/notebooks/example-workflows/wfm-cloud-water.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/api-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Errors

**`ModuleNotFoundError`** — No module named 'pyaqsapi'

in `site/content/notebooks.example-workflows.air-quality-system-api.json`

```
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[1], line 8
      6 import numpy as np
      7 import os
----> 8 import pyaqsapi as aqs

ModuleNotFoundError: No module named 'pyaqsapi'
```

