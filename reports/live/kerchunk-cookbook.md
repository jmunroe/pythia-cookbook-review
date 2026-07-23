# kerchunk-cookbook

Live outcome: **build failed**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/kerchunk-cookbook)

Run 2026-07-23 00:57:11 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [kerchunk-cookbook](https://github.com/ProjectPythia/kerchunk-cookbook) at ref [`main`](https://github.com/ProjectPythia/kerchunk-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **build failed** |
| Static tier | `healthy` |
| Time to a ready session | 9m 28s (fresh build) |
| Build succeeded | no |
| Resource metrics | unavailable: unknown |
| Errors raised | 0 |

Executed 12 notebook(s) from the project toc: [`notebooks/advanced/Parquet_Reference_Storage.ipynb`](https://github.com/ProjectPythia/kerchunk-cookbook/blob/main/notebooks/advanced/Parquet_Reference_Storage.ipynb), [`notebooks/advanced/appending.ipynb`](https://github.com/ProjectPythia/kerchunk-cookbook/blob/main/notebooks/advanced/appending.ipynb), [`notebooks/foundations/01_kerchunk_basics.ipynb`](https://github.com/ProjectPythia/kerchunk-cookbook/blob/main/notebooks/foundations/01_kerchunk_basics.ipynb), [`notebooks/foundations/02_kerchunk_multi_file.ipynb`](https://github.com/ProjectPythia/kerchunk-cookbook/blob/main/notebooks/foundations/02_kerchunk_multi_file.ipynb), [`notebooks/foundations/03_kerchunk_dask.ipynb`](https://github.com/ProjectPythia/kerchunk-cookbook/blob/main/notebooks/foundations/03_kerchunk_dask.ipynb), [`notebooks/generating_references/GRIB2.ipynb`](https://github.com/ProjectPythia/kerchunk-cookbook/blob/main/notebooks/generating_references/GRIB2.ipynb), [`notebooks/generating_references/GeoTIFF.ipynb`](https://github.com/ProjectPythia/kerchunk-cookbook/blob/main/notebooks/generating_references/GeoTIFF.ipynb), [`notebooks/generating_references/NetCDF.ipynb`](https://github.com/ProjectPythia/kerchunk-cookbook/blob/main/notebooks/generating_references/NetCDF.ipynb), [`notebooks/using_references/Datatree.ipynb`](https://github.com/ProjectPythia/kerchunk-cookbook/blob/main/notebooks/using_references/Datatree.ipynb), [`notebooks/using_references/Hvplot_Datashader.ipynb`](https://github.com/ProjectPythia/kerchunk-cookbook/blob/main/notebooks/using_references/Hvplot_Datashader.ipynb), [`notebooks/using_references/Xarray.ipynb`](https://github.com/ProjectPythia/kerchunk-cookbook/blob/main/notebooks/using_references/Xarray.ipynb), [`notebooks/using_references/Xrefcoord.ipynb`](https://github.com/ProjectPythia/kerchunk-cookbook/blob/main/notebooks/using_references/Xrefcoord.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/kerchunk-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Build log (tail)

```
[  552.57s] #20 560.8 Linking libarrow-dataset-24.0.0-h635bf11_9_cpu
[  552.57s] #20 560.8 Linking aiosignal-1.4.0-pyhd8ed1ab_0
[  552.57s] #20 560.8 Linking distributed-2026.7.1-pyhc364b38_0
[  552.57s] #20 560.8 Linking identify-2.6.19-pyhd8ed1ab_0
[  552.71s] #20 561.1 Linking tifffile-2020.6.3-py_0
[  552.89s] #20 561.1 Linking h5netcdf-1.8.1-pyhd8ed1ab_0
[  552.89s] #20 561.1 Linking pre-commit-4.6.1-pyha770c72_0
[  552.91s] #20 561.3 Linking jupyter_bokeh-4.1.0-pyhcf101f3_0
[  553.02s] #20 561.3 Linking dask-2026.7.1-pyhc364b38_0
[  553.02s] #20 561.3 Linking virtualizarr-1.3.0-pyhd8ed1ab_0
[  553.02s] #20 561.3 Linking datashader-0.19.1-pyhd8ed1ab_0
[  553.02s] #20 561.3 Linking cfgrib-0.9.15.1-pyhd8ed1ab_0
[  553.02s] #20 561.3 Linking panel-material-ui-0.14.0-pyhd8ed1ab_0
[  553.15s] #20 561.4 Linking aiohttp-3.14.2-py310h31b6992_0
[  553.15s] #20 561.5
[  553.28s] #20 561.7 warning  libmamba You are using 'pip' as an additional package manager.
[  553.43s] #20 561.7
[  566.57s] #20 575.4 critical libmamba pip failed to update packages
[  567.29s] #20 ERROR: process "/bin/sh -c TIMEFORMAT='time: %3R' bash -c 'time ${MAMBA_EXE} env update -p ${NB_PYTHON_PREFIX} --file \"environment.yml\" && time ${MAMBA_EXE} clean --all -f -y && ${MAMBA_EXE} list -p ${NB_PYTHON_PREFIX} '" did not complete successfully: exit code: 1
[  567.95s] ------
[  567.95s] 561.5
[  567.95s] 561.7     Be aware that packages installed with 'pip' are managed independently from 'conda-forge' channel.
[  567.95s] 561.7
[  567.95s] 561.7 Updating pip packages: git+https://github.com/carbonplan/xrefcoord.git, git+https://github.com/fsspec/kerchunk
[  567.99s] ERROR: failed to solve: process "/bin/sh -c TIMEFORMAT='time: %3R' bash -c 'time ${MAMBA_EXE} env update -p ${NB_PYTHON_PREFIX} --file \"environment.yml\" && time ${MAMBA_EXE} clean --all -f -y && ${MAMBA_EXE} list -p ${NB_PYTHON_PREFIX} '" did not complete successfully: exit code: 1
```

