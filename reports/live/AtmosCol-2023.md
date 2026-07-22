# AtmosCol-2023

Live outcome: **build failed**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/AtmosCol-2023)

Run 2026-07-22 09:00:35 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [AtmosCol-2023](https://github.com/ProjectPythia/AtmosCol-2023) at ref [`main`](https://github.com/ProjectPythia/AtmosCol-2023/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **build failed** |
| Static tier | `incubating` |
| Time to a ready session | 1m 36s (fresh build) |
| Build succeeded | no |
| Resource metrics | unavailable: unknown |
| Errors raised | 0 |

Executed 17 notebook(s) from the project toc: [`notebooks/1.fundamentos/1.0.Introduccion-JupyterLab.ipynb`](https://github.com/ProjectPythia/AtmosCol-2023/blob/main/notebooks/1.fundamentos/1.0.Introduccion-JupyterLab.ipynb), [`notebooks/1.fundamentos/1.1.Fundamentos-python.ipynb`](https://github.com/ProjectPythia/AtmosCol-2023/blob/main/notebooks/1.fundamentos/1.1.Fundamentos-python.ipynb), [`notebooks/1.fundamentos/1.2.Introduccion-Numpy.ipynb`](https://github.com/ProjectPythia/AtmosCol-2023/blob/main/notebooks/1.fundamentos/1.2.Introduccion-Numpy.ipynb), [`notebooks/1.fundamentos/1.3.Introduccion-Pandas.ipynb`](https://github.com/ProjectPythia/AtmosCol-2023/blob/main/notebooks/1.fundamentos/1.3.Introduccion-Pandas.ipynb), [`notebooks/1.fundamentos/1.4.Introduccion-Xarray.ipynb`](https://github.com/ProjectPythia/AtmosCol-2023/blob/main/notebooks/1.fundamentos/1.4.Introduccion-Xarray.ipynb), [`notebooks/1.fundamentos/1.5.Introduccion-Radar.ipynb`](https://github.com/ProjectPythia/AtmosCol-2023/blob/main/notebooks/1.fundamentos/1.5.Introduccion-Radar.ipynb), [`notebooks/1.fundamentos/1.6.Exploracion-NetCDF-GRIB.ipynb`](https://github.com/ProjectPythia/AtmosCol-2023/blob/main/notebooks/1.fundamentos/1.6.Exploracion-NetCDF-GRIB.ipynb), [`notebooks/1.fundamentos/1.7.Introduccion-ARCO.ipynb`](https://github.com/ProjectPythia/AtmosCol-2023/blob/main/notebooks/1.fundamentos/1.7.Introduccion-ARCO.ipynb), [`notebooks/1.fundamentos/1.8.Formato-Zarr.ipynb`](https://github.com/ProjectPythia/AtmosCol-2023/blob/main/notebooks/1.fundamentos/1.8.Formato-Zarr.ipynb), [`notebooks/2.acceso-datos/2.1.Estaciones.ipynb`](https://github.com/ProjectPythia/AtmosCol-2023/blob/main/notebooks/2.acceso-datos/2.1.Estaciones.ipynb), [`notebooks/2.acceso-datos/2.2.Radares.ipynb`](https://github.com/ProjectPythia/AtmosCol-2023/blob/main/notebooks/2.acceso-datos/2.2.Radares.ipynb), [`notebooks/2.acceso-datos/2.3.GFS.ipynb`](https://github.com/ProjectPythia/AtmosCol-2023/blob/main/notebooks/2.acceso-datos/2.3.GFS.ipynb), [`notebooks/3.Aplicaciones/3.1.ENSO.ipynb`](https://github.com/ProjectPythia/AtmosCol-2023/blob/main/notebooks/3.Aplicaciones/3.1.ENSO.ipynb), [`notebooks/3.Aplicaciones/3.2.Global-Mean-SST.ipynb`](https://github.com/ProjectPythia/AtmosCol-2023/blob/main/notebooks/3.Aplicaciones/3.2.Global-Mean-SST.ipynb), [`notebooks/3.Aplicaciones/3.3.ERA5.ipynb`](https://github.com/ProjectPythia/AtmosCol-2023/blob/main/notebooks/3.Aplicaciones/3.3.ERA5.ipynb), [`notebooks/3.Aplicaciones/3.4.QVPs.ipynb`](https://github.com/ProjectPythia/AtmosCol-2023/blob/main/notebooks/3.Aplicaciones/3.4.QVPs.ipynb), [`notebooks/3.Aplicaciones/3.5.QPE.ipynb`](https://github.com/ProjectPythia/AtmosCol-2023/blob/main/notebooks/3.Aplicaciones/3.5.QPE.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/AtmosCol-2023/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Build log (tail)

```
[   93.16s] #20 72.76 Linking jupyterlab_server-2.27.3-pyhd8ed1ab_1
[   93.61s] #20 72.76 Linking notebook-shim-0.2.4-pyhd8ed1ab_1
[   93.61s] #20 72.76 Linking setuptools-80.9.0-pyhff2d567_0
[   93.61s] #20 72.80 Linking jupyterlab-4.4.9-pyhd8ed1ab_0
[   94.16s] #20 73.32 Linking wheel-0.45.1-pyhd8ed1ab_1
[   94.17s] #20 73.77 warning  libmamba You are using 'pip' as an additional package manager.
[   94.32s] #20 73.77
[   94.90s] #20 74.50   error: subprocess-exited-with-error
[   95.02s] #20 74.50 ERROR: Failed to build 'git+https://github.com/aladinor/raw2zarr.git' when git clone --filter=blob:none --quiet https://github.com/aladinor/raw2zarr.git /tmp/pip-req-build-aksj1m81
[   95.20s] #20 74.65 time: 74.394
[   96.16s] ------
[   96.16s] 74.50   │ exit code: 128
[   96.16s] 74.50   ╰─> [1 lines of output]
[   96.16s] 74.50       fatal: could not read Username for 'https://github.com': terminal prompts disabled
[   96.16s] 74.50       [end of output]
[   96.16s] 74.50
[   96.16s] 74.50   note: This error originates from a subprocess, and is likely not a problem with pip.
[   96.16s] Dockerfile:131
[   96.16s] --------------------
[   96.16s]  130 |     USER ${NB_USER}
[   96.16s]  131 | >>> RUN TIMEFORMAT='time: %3R' \
[   96.16s]  132 | >>> bash -c 'time ${MAMBA_EXE} env update -p ${NB_PYTHON_PREFIX} --file "environment.yml" && \
[   96.16s]  136 |
[   96.16s] --------------------
[   96.16s] ERROR: failed to solve: process "/bin/sh -c TIMEFORMAT='time: %3R' bash -c 'time ${MAMBA_EXE} env update -p ${NB_PYTHON_PREFIX} --file \"environment.yml\" && time ${MAMBA_EXE} clean --all -f -y && ${MAMBA_EXE} list -p ${NB_PYTHON_PREFIX} '" did not complete successfully: exit code: 1
```

