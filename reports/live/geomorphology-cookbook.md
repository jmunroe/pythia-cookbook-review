# geomorphology-cookbook

Live outcome: **ran with errors**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/geomorphology-cookbook)

Run 2026-07-22 09:47:07 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [geomorphology-cookbook](https://github.com/ProjectPythia/geomorphology-cookbook) at ref [`main`](https://github.com/ProjectPythia/geomorphology-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **ran with errors** |
| Static tier | `incubating` |
| Time to a ready session | 475.51s (fresh build) |
| Build succeeded | yes |
| Notebook execution | 141.74s |
| Build command exit code | 0 (zero despite cell errors) |
| Notebooks ran clean | no |
| Execution cache | **reused — timing is not execution** |
| Peak memory (pss) | 2.27 GB |
| Pod memory limit | 8.59 GB |
| Peak as share of limit | 26.4% |
| Peak rss (upper bound, shared pages double-counted) | 2.52 GB |
| Errors raised | 1 |

| Notebook | Execute + render |
|---|---|
| [`notebooks/seabed-morphology.ipynb`](https://github.com/ProjectPythia/geomorphology-cookbook/blob/main/notebooks/seabed-morphology.ipynb) | 1.44s |
| [`notebooks/DataStory.ipynb`](https://github.com/ProjectPythia/geomorphology-cookbook/blob/main/notebooks/DataStory.ipynb) | 2.87s |
| [`notebooks/Openness_Closeness_Explainer.ipynb`](https://github.com/ProjectPythia/geomorphology-cookbook/blob/main/notebooks/Openness_Closeness_Explainer.ipynb) | 4.83s |
| [`notebooks/Metadata.ipynb`](https://github.com/ProjectPythia/geomorphology-cookbook/blob/main/notebooks/Metadata.ipynb) | 6.74s |
| [`notebooks/Polygonization.ipynb`](https://github.com/ProjectPythia/geomorphology-cookbook/blob/main/notebooks/Polygonization.ipynb) | 10.0s |
| [`notebooks/rasterviz-intro.ipynb`](https://github.com/ProjectPythia/geomorphology-cookbook/blob/main/notebooks/rasterviz-intro.ipynb) | 16.0s |
| [`notebooks/jupytergis-showcase.ipynb`](https://github.com/ProjectPythia/geomorphology-cookbook/blob/main/notebooks/jupytergis-showcase.ipynb) | 45.0s |
| [`notebooks/Topographic-Positioning-Index-Methods.ipynb`](https://github.com/ProjectPythia/geomorphology-cookbook/blob/main/notebooks/Topographic-Positioning-Index-Methods.ipynb) | 53.0s |

Executed 9 notebook(s) from the project toc: [`notebooks/DataStory.ipynb`](https://github.com/ProjectPythia/geomorphology-cookbook/blob/main/notebooks/DataStory.ipynb), [`notebooks/Metadata.ipynb`](https://github.com/ProjectPythia/geomorphology-cookbook/blob/main/notebooks/Metadata.ipynb), [`notebooks/Openness_Closeness_Computation.ipynb`](https://github.com/ProjectPythia/geomorphology-cookbook/blob/main/notebooks/Openness_Closeness_Computation.ipynb), [`notebooks/Openness_Closeness_Explainer.ipynb`](https://github.com/ProjectPythia/geomorphology-cookbook/blob/main/notebooks/Openness_Closeness_Explainer.ipynb), [`notebooks/Polygonization.ipynb`](https://github.com/ProjectPythia/geomorphology-cookbook/blob/main/notebooks/Polygonization.ipynb), [`notebooks/Topographic-Positioning-Index-Methods.ipynb`](https://github.com/ProjectPythia/geomorphology-cookbook/blob/main/notebooks/Topographic-Positioning-Index-Methods.ipynb), [`notebooks/jupytergis-showcase.ipynb`](https://github.com/ProjectPythia/geomorphology-cookbook/blob/main/notebooks/jupytergis-showcase.ipynb), [`notebooks/rasterviz-intro.ipynb`](https://github.com/ProjectPythia/geomorphology-cookbook/blob/main/notebooks/rasterviz-intro.ipynb), [`notebooks/seabed-morphology.ipynb`](https://github.com/ProjectPythia/geomorphology-cookbook/blob/main/notebooks/seabed-morphology.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/geomorphology-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Errors

**`NameError`** — name 'doc' is not defined

in `site/content/notebooks.jupytergis-showcase.json`

```
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[8], line 1
----> 1 doc.sidecar(title="Seabed Morphology", anchor="split-right")

NameError: name 'doc' is not defined
```

