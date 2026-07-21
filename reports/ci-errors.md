# Green nightlies with failing notebooks

Generated from `ci-errors-2026-07-21.json` (collected 2026-07-21). Do not edit — regenerate with `python scripts/ci_errors.py && python scripts/report_ci.py`.

:::{danger} A passing badge does not mean the notebooks ran
**12 of 30 gallery cookbooks** had at least one notebook raise an exception during their most recent nightly build — and the build reported **success** anyway.
:::

## Why this happens

`myst build --execute` exits 0 when a cell raises. The exception is captured into the page and the build carries on, so the workflow — whose health is the command's exit status — goes green, the book deploys, and the gallery card says passing.

MyST logs each failure like this:

```
⛔️ notebooks/01-easygems.ipynb An exception occurred during code execution, halting further execution
```

Note **halting further execution**: every cell after the failure is skipped, so the published page is silently truncated. A learner sees a lesson that stops partway, or a traceback where a figure should be.

This is measured from Project Pythia's own CI logs, not from a reproduction — there is no environment confound. See [the method](../docs/live-assessment.md).

## Affected cookbooks

| Cookbook | Notebooks raising | Gallery says | Nightly run |
|---|---|---|---|
| [vapor-python-cookbook](https://github.com/ProjectPythia/vapor-python-cookbook) | **15** | ✅ passing | [success](https://github.com/ProjectPythia/vapor-python-cookbook/actions/runs/29794132854) |
| [kerchunk-cookbook](https://github.com/ProjectPythia/kerchunk-cookbook) | **10** | ✅ passing | [success](https://github.com/ProjectPythia/kerchunk-cookbook/actions/runs/29794780631) |
| [ocean-bgc-cookbook](https://github.com/ProjectPythia/ocean-bgc-cookbook) | **7** | ✅ passing | [success](https://github.com/ProjectPythia/ocean-bgc-cookbook/actions/runs/29792982708) |
| [metpy-cookbook](https://github.com/ProjectPythia/metpy-cookbook) | **4** | ✅ passing | [success](https://github.com/ProjectPythia/metpy-cookbook/actions/runs/29795223462) |
| [healpix-cookbook](https://github.com/ProjectPythia/healpix-cookbook) | **3** | ✅ passing | [success](https://github.com/ProjectPythia/healpix-cookbook/actions/runs/29797074376) |
| [osdf-cookbook](https://github.com/ProjectPythia/osdf-cookbook) | **3** | ✅ passing | [success](https://github.com/ProjectPythia/osdf-cookbook/actions/runs/29796824021) |
| [gdex-cookbook](https://github.com/ProjectPythia/gdex-cookbook) | **2** | ✅ passing | [success](https://github.com/ProjectPythia/gdex-cookbook/actions/runs/29794709429) |
| [ERA5_interactive-cookbook](https://github.com/ProjectPythia/ERA5_interactive-cookbook) | **1** | ✅ passing | [success](https://github.com/ProjectPythia/ERA5_interactive-cookbook/actions/runs/29798652074) |
| [interactive-sentinel-2-cookbook](https://github.com/ProjectPythia/interactive-sentinel-2-cookbook) | **1** | ✅ passing | [success](https://github.com/ProjectPythia/interactive-sentinel-2-cookbook/actions/runs/29795000748) |
| [advanced-viz-cookbook](https://github.com/ProjectPythia/advanced-viz-cookbook) | **1** | ✅ passing | [success](https://github.com/ProjectPythia/advanced-viz-cookbook/actions/runs/29795781034) |
| [unstructured-grid-viz-cookbook](https://github.com/ProjectPythia/unstructured-grid-viz-cookbook) | **1** | ✅ passing | [success](https://github.com/ProjectPythia/unstructured-grid-viz-cookbook/actions/runs/29795188896) |
| [eo-datascience-cookbook](https://github.com/ProjectPythia/eo-datascience-cookbook) | **1** | ✅ passing | [success](https://github.com/ProjectPythia/eo-datascience-cookbook/actions/runs/29798721119) |

## Detail

### vapor-python-cookbook

- [`notebooks/AGU_2023_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/AGU_2023_example.ipynb) — `ModuleNotFoundError`
- [`notebooks/animation_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/animation_example.ipynb)
- [`notebooks/annotation_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/annotation_example.ipynb)
- [`notebooks/camera_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/camera_example.ipynb)
- [`notebooks/cloudfield_visualizer.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/cloudfield_visualizer.ipynb) — `ModuleNotFoundError`
- [`notebooks/custom_images_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/custom_images_example.ipynb)
- [`notebooks/dataset_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/dataset_example.ipynb)
- [`notebooks/flow_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/flow_example.ipynb)
- [`notebooks/keyframing_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/keyframing_example.ipynb) — `ModuleNotFoundError`
- [`notebooks/numpy_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/numpy_example.ipynb) — `ModuleNotFoundError`
- [`notebooks/quickstart.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/quickstart.ipynb) — `ModuleNotFoundError`
- [`notebooks/transfer_function_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/transfer_function_example.ipynb)
- [`notebooks/visualizer_widget_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/visualizer_widget_example.ipynb) — `ModuleNotFoundError`
- [`notebooks/workflow_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/workflow_example.ipynb) — `ModuleNotFoundError`
- [`notebooks/xarray_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/xarray_example.ipynb) — `SSLCertVerificationError`

### kerchunk-cookbook

- [`notebooks/advanced/Parquet_Reference_Storage.ipynb`](https://github.com/ProjectPythia/kerchunk-cookbook/blob/main/notebooks/advanced/Parquet_Reference_Storage.ipynb)
- [`notebooks/advanced/appending.ipynb`](https://github.com/ProjectPythia/kerchunk-cookbook/blob/main/notebooks/advanced/appending.ipynb)
- [`notebooks/foundations/01_kerchunk_basics.ipynb`](https://github.com/ProjectPythia/kerchunk-cookbook/blob/main/notebooks/foundations/01_kerchunk_basics.ipynb) — `TypeError`
- [`notebooks/foundations/02_kerchunk_multi_file.ipynb`](https://github.com/ProjectPythia/kerchunk-cookbook/blob/main/notebooks/foundations/02_kerchunk_multi_file.ipynb)
- [`notebooks/foundations/03_kerchunk_dask.ipynb`](https://github.com/ProjectPythia/kerchunk-cookbook/blob/main/notebooks/foundations/03_kerchunk_dask.ipynb)
- [`notebooks/generating_references/GRIB2.ipynb`](https://github.com/ProjectPythia/kerchunk-cookbook/blob/main/notebooks/generating_references/GRIB2.ipynb)
- [`notebooks/generating_references/GeoTIFF.ipynb`](https://github.com/ProjectPythia/kerchunk-cookbook/blob/main/notebooks/generating_references/GeoTIFF.ipynb)
- [`notebooks/generating_references/NetCDF.ipynb`](https://github.com/ProjectPythia/kerchunk-cookbook/blob/main/notebooks/generating_references/NetCDF.ipynb)
- [`notebooks/using_references/Datatree.ipynb`](https://github.com/ProjectPythia/kerchunk-cookbook/blob/main/notebooks/using_references/Datatree.ipynb)
- [`notebooks/using_references/Xarray.ipynb`](https://github.com/ProjectPythia/kerchunk-cookbook/blob/main/notebooks/using_references/Xarray.ipynb)

### ocean-bgc-cookbook

- [`notebooks/ocn-carbonfluxes.ipynb`](https://github.com/ProjectPythia/ocean-bgc-cookbook/blob/main/notebooks/ocn-carbonfluxes.ipynb) — `ModuleNotFoundError`
- [`notebooks/ocn-iron.ipynb`](https://github.com/ProjectPythia/ocean-bgc-cookbook/blob/main/notebooks/ocn-iron.ipynb) — `ModuleNotFoundError`
- [`notebooks/ocn-macronuts.ipynb`](https://github.com/ProjectPythia/ocean-bgc-cookbook/blob/main/notebooks/ocn-macronuts.ipynb) — `ModuleNotFoundError`
- [`notebooks/ocn-phyto-biomass.ipynb`](https://github.com/ProjectPythia/ocean-bgc-cookbook/blob/main/notebooks/ocn-phyto-biomass.ipynb) — `ModuleNotFoundError`
- [`notebooks/ocn-phyto-lims.ipynb`](https://github.com/ProjectPythia/ocean-bgc-cookbook/blob/main/notebooks/ocn-phyto-lims.ipynb) — `ModuleNotFoundError`
- [`notebooks/ocn-tracer-views.ipynb`](https://github.com/ProjectPythia/ocean-bgc-cookbook/blob/main/notebooks/ocn-tracer-views.ipynb)
- [`notebooks/ocn-zoo.ipynb`](https://github.com/ProjectPythia/ocean-bgc-cookbook/blob/main/notebooks/ocn-zoo.ipynb) — `ModuleNotFoundError`

### metpy-cookbook

- [`notebooks/skewt/Skew-T_Analysis.ipynb`](https://github.com/ProjectPythia/metpy-cookbook/blob/main/notebooks/skewt/Skew-T_Analysis.ipynb)
- [`notebooks/skewt/Sounding_Plotter.ipynb`](https://github.com/ProjectPythia/metpy-cookbook/blob/main/notebooks/skewt/Sounding_Plotter.ipynb)
- [`notebooks/specialty/Observational_Data_Cross_Section.ipynb`](https://github.com/ProjectPythia/metpy-cookbook/blob/main/notebooks/specialty/Observational_Data_Cross_Section.ipynb) — `HTTPError`
- [`notebooks/synoptic/250hPa_Hemispheric_Plot.ipynb`](https://github.com/ProjectPythia/metpy-cookbook/blob/main/notebooks/synoptic/250hPa_Hemispheric_Plot.ipynb) — `AttributeError`

### healpix-cookbook

- [`notebooks/01-easygems.ipynb`](https://github.com/ProjectPythia/healpix-cookbook/blob/main/notebooks/01-easygems.ipynb) — `GroupNotFoundError`
- [`notebooks/02-uxarray.ipynb`](https://github.com/ProjectPythia/healpix-cookbook/blob/main/notebooks/02-uxarray.ipynb) — `GroupNotFoundError`
- [`notebooks/03-uxarray-advanced.ipynb`](https://github.com/ProjectPythia/healpix-cookbook/blob/main/notebooks/03-uxarray-advanced.ipynb) — `GroupNotFoundError`

### osdf-cookbook

- [`notebooks/01_pelicanfs.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/01_pelicanfs.ipynb) — `HTTPError`
- [`notebooks/03_EnviStor_Technical.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/03_EnviStor_Technical.ipynb)
- [`notebooks/04_SonarAI_Technical.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/04_SonarAI_Technical.ipynb)

### gdex-cookbook

- [`notebooks/workflows/data_fusion.ipynb`](https://github.com/ProjectPythia/gdex-cookbook/blob/main/notebooks/workflows/data_fusion.ipynb)
- [`notebooks/workflows/na-cordex.ipynb`](https://github.com/ProjectPythia/gdex-cookbook/blob/main/notebooks/workflows/na-cordex.ipynb)

### ERA5_interactive-cookbook

- [`notebooks/06_era5_anomaly.ipynb`](https://github.com/ProjectPythia/ERA5_interactive-cookbook/blob/main/notebooks/06_era5_anomaly.ipynb)

### interactive-sentinel-2-cookbook

- [`notebooks/data-intake-ms-planetary-computer.ipynb`](https://github.com/ProjectPythia/interactive-sentinel-2-cookbook/blob/main/notebooks/data-intake-ms-planetary-computer.ipynb) — `HTTPError`

### advanced-viz-cookbook

- [`notebooks/6-spaghetti.ipynb`](https://github.com/ProjectPythia/advanced-viz-cookbook/blob/main/notebooks/6-spaghetti.ipynb) — `ModuleNotFoundError`

### unstructured-grid-viz-cookbook

- [`notebooks/04-recipes/mpas-atmo.ipynb`](https://github.com/ProjectPythia/unstructured-grid-viz-cookbook/blob/main/notebooks/04-recipes/mpas-atmo.ipynb) — `ValueError`

### eo-datascience-cookbook

- [`notebooks/courses/microwave-remote-sensing/unit_03/09_in_class_exercise.ipynb`](https://github.com/ProjectPythia/eo-datascience-cookbook/blob/main/notebooks/courses/microwave-remote-sensing/unit_03/09_in_class_exercise.ipynb) — `AttributeError`

## Cookbooks whose latest nightly showed no execution errors

`cesm-lens-aws-cookbook`, `cmip6-cookbook`, `HRRR-AWS-cookbook`, `landsat-ml-cookbook`, `xbatcher-ML-1-cookbook`, `dask-cookbook`, `web-map-feature-services-cookbook`, `gridding-cookbook`, `na-cordex-viz-cookbook`, `eofs-cookbook`, `paleoPCA-cookbook`, `esgf-cookbook`, `wavelet-cookbook`, `snow-observations-cookbook`, `feature-tracking-cookbook`, `mpas-jedi-cookbook`

## What to do with this

This is a finding about the **shared build configuration**, not about any one cookbook. MyST supports `error_rules`, so failing the build on execution errors looks like a one-place change in [`cookbook-actions`](https://github.com/ProjectPythia/cookbook-actions) or the shared [`pythia-config`](https://github.com/ProjectPythia/pythia-config).

Worth raising with the Pythia maintainers before acting: turning this on would flip a large fraction of the gallery red overnight, which is a decision for the community rather than a fix to land unannounced. The counts above are the argument for making it, and the list is the work it implies.

