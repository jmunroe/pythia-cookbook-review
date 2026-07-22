# unstructured-grid-viz-cookbook

Live outcome: **build failed**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/unstructured-grid-viz-cookbook)

Run 2026-07-22 07:33:23 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [unstructured-grid-viz-cookbook](https://github.com/ProjectPythia/unstructured-grid-viz-cookbook) at ref [`main`](https://github.com/ProjectPythia/unstructured-grid-viz-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **build failed** |
| Static tier | `healthy` |
| Time to a ready session | 30m 00s (fresh build) |
| Build succeeded | no |
| Resource metrics | unavailable: unknown |
| Errors raised | 0 |

Executed 20 notebook(s) from the project toc: [`notebooks/01-foundations/plotting-libs.ipynb`](https://github.com/ProjectPythia/unstructured-grid-viz-cookbook/blob/main/notebooks/01-foundations/plotting-libs.ipynb), [`notebooks/01-foundations/rendering-techniques.ipynb`](https://github.com/ProjectPythia/unstructured-grid-viz-cookbook/blob/main/notebooks/01-foundations/rendering-techniques.ipynb), [`notebooks/01-foundations/unstructured-grids.ipynb`](https://github.com/ProjectPythia/unstructured-grid-viz-cookbook/blob/main/notebooks/01-foundations/unstructured-grids.ipynb), [`notebooks/02-intro-to-uxarray/grid.ipynb`](https://github.com/ProjectPythia/unstructured-grid-viz-cookbook/blob/main/notebooks/02-intro-to-uxarray/grid.ipynb), [`notebooks/02-intro-to-uxarray/overview.ipynb`](https://github.com/ProjectPythia/unstructured-grid-viz-cookbook/blob/main/notebooks/02-intro-to-uxarray/overview.ipynb), [`notebooks/02-intro-to-uxarray/selection.ipynb`](https://github.com/ProjectPythia/unstructured-grid-viz-cookbook/blob/main/notebooks/02-intro-to-uxarray/selection.ipynb), [`notebooks/02-intro-to-uxarray/uxds-uxda.ipynb`](https://github.com/ProjectPythia/unstructured-grid-viz-cookbook/blob/main/notebooks/02-intro-to-uxarray/uxds-uxda.ipynb), [`notebooks/03-plotting-with-uxarray/compare-xarray.ipynb`](https://github.com/ProjectPythia/unstructured-grid-viz-cookbook/blob/main/notebooks/03-plotting-with-uxarray/compare-xarray.ipynb), [`notebooks/03-plotting-with-uxarray/customization.ipynb`](https://github.com/ProjectPythia/unstructured-grid-viz-cookbook/blob/main/notebooks/03-plotting-with-uxarray/customization.ipynb), [`notebooks/03-plotting-with-uxarray/data-viz.ipynb`](https://github.com/ProjectPythia/unstructured-grid-viz-cookbook/blob/main/notebooks/03-plotting-with-uxarray/data-viz.ipynb), [`notebooks/03-plotting-with-uxarray/geo.ipynb`](https://github.com/ProjectPythia/unstructured-grid-viz-cookbook/blob/main/notebooks/03-plotting-with-uxarray/geo.ipynb), [`notebooks/03-plotting-with-uxarray/grid-viz.ipynb`](https://github.com/ProjectPythia/unstructured-grid-viz-cookbook/blob/main/notebooks/03-plotting-with-uxarray/grid-viz.ipynb), [`notebooks/03-plotting-with-uxarray/high-res.ipynb`](https://github.com/ProjectPythia/unstructured-grid-viz-cookbook/blob/main/notebooks/03-plotting-with-uxarray/high-res.ipynb), [`notebooks/04-recipes/e3sm.ipynb`](https://github.com/ProjectPythia/unstructured-grid-viz-cookbook/blob/main/notebooks/04-recipes/e3sm.ipynb), [`notebooks/04-recipes/mpas-atmo.ipynb`](https://github.com/ProjectPythia/unstructured-grid-viz-cookbook/blob/main/notebooks/04-recipes/mpas-atmo.ipynb), [`notebooks/04-recipes/mpas-ocean.ipynb`](https://github.com/ProjectPythia/unstructured-grid-viz-cookbook/blob/main/notebooks/04-recipes/mpas-ocean.ipynb), [`notebooks/04-recipes/mpas-regional.ipynb`](https://github.com/ProjectPythia/unstructured-grid-viz-cookbook/blob/main/notebooks/04-recipes/mpas-regional.ipynb), [`notebooks/05-viz-packages/datashader.ipynb`](https://github.com/ProjectPythia/unstructured-grid-viz-cookbook/blob/main/notebooks/05-viz-packages/datashader.ipynb), [`notebooks/05-viz-packages/lonboard.ipynb`](https://github.com/ProjectPythia/unstructured-grid-viz-cookbook/blob/main/notebooks/05-viz-packages/lonboard.ipynb), [`notebooks/05-viz-packages/matplotlib.ipynb`](https://github.com/ProjectPythia/unstructured-grid-viz-cookbook/blob/main/notebooks/05-viz-packages/matplotlib.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/unstructured-grid-viz-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Build log (tail)

```
[  373.11s] #14 29.66   tk                             8.6.13          noxft_hd72426e_102  conda-forge
[  373.11s] #14 29.66   tomli                          2.3.0           pyhcf101f3_0        conda-forge
[  373.11s] #14 29.66   typing_utils                   0.1.0           pyhd8ed1ab_1        conda-forge
[  373.11s] #14 29.66   tzdata                         2025b           h78e105d_0          conda-forge
[  373.11s] #14 29.66   uri-template                   1.3.0           pyhd8ed1ab_1        conda-forge
[  373.16s] #14 29.66   websocket-client               1.9.0           pyhd8ed1ab_0        conda-forge
[  373.16s] #14 29.66   wheel                          0.45.1          pyhd8ed1ab_1        conda-forge
[  373.16s] #14 29.66   widgetsnbextension             4.0.14          pyhd8ed1ab_0        conda-forge
[  373.16s] #14 29.66   yaml                           0.2.5           h280c20c_3          conda-forge
[  373.16s] #14 29.66   zeromq                         4.3.5           h387f397_9          conda-forge
[  373.16s] #14 29.66   zipp                           3.23.0          pyhd8ed1ab_0        conda-forge
[  373.16s] #14 29.66   zlib                           1.3.1           hb9d3cd8_2          conda-forge
[  373.16s] #14 29.66   zstandard                      0.25.0          py310h139afa4_0     conda-forge
[  373.16s] #14 29.66   zstd                           1.5.7           hb8e6e7a_2          conda-forge
[  373.48s] #14 30.09 time: 29.821
[  374.93s] 
[  374.93s] #15 [11/19] RUN mkdir -p /srv/npm && chown -R jovyan:jovyan /srv/npm
[  375.14s] #15 DONE 0.4s
[  375.50s] #16 DONE 0.4s
[  375.78s] 
[  375.78s] #18 [14/19] RUN chown jovyan:jovyan /home/jovyan
[  376.03s] #18 DONE 0.4s
[  376.32s] 
[  376.32s] #20 [16/19] RUN TIMEFORMAT='time: %3R' bash -c 'time ${MAMBA_EXE} env update -p ${NB_PYTHON_PREFIX} --file "environment.yml" && time ${MAMBA_EXE} clean --all -f -y && ${MAMBA_EXE} list -p ${NB_PYTHON_PREFIX} '
[  391.24s] #20 15.08
```

