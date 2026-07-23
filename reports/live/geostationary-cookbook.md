# geostationary-cookbook

Live outcome: **ran with errors**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/geostationary-cookbook)

Run 2026-07-23 14:29:19 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [geostationary-cookbook](https://github.com/ProjectPythia/geostationary-cookbook) at ref [`main`](https://github.com/ProjectPythia/geostationary-cookbook/tree/main).

:::{warning} Cached image
BinderHub reused an existing image, so the 4m 59s is a pod launch and image pull. It does **not** test whether `environment.yml` still solves.
:::

| Measure | Value |
|---|---|
| Live outcome | **ran with errors** |
| Static tier | `incubating` |
| Time to a ready session | 4m 59s (cached image) |
| Build succeeded | yes |
| Notebook execution | 2m 04s |
| Build command exit code | 0 (zero despite cell errors) |
| Notebooks ran clean | no |
| Execution cache | **reused — timing is not execution** |
| Peak memory (pss) | 2.60 GB |
| Pod memory limit | 8.59 GB |
| Peak as share of limit | 30.3% |
| Peak rss (upper bound, shared pages double-counted) | 2.73 GB |
| Errors raised | 3 |

| Notebook | Execute + render |
|---|---|
| [`notebooks/notebook-template.ipynb`](https://github.com/ProjectPythia/geostationary-cookbook/blob/main/notebooks/notebook-template.ipynb) | 2.09s |
| [`notebooks/01_geosat_ABI_GOES_east.ipynb`](https://github.com/ProjectPythia/geostationary-cookbook/blob/main/notebooks/01_geosat_ABI_GOES_east.ipynb) | 28s |
| [`notebooks/02_geosat_ABI_GOES_west.ipynb`](https://github.com/ProjectPythia/geostationary-cookbook/blob/main/notebooks/02_geosat_ABI_GOES_west.ipynb) | 30s |
| [`notebooks/03_geosat_AHI_HIMAWARI.ipynb`](https://github.com/ProjectPythia/geostationary-cookbook/blob/main/notebooks/03_geosat_AHI_HIMAWARI.ipynb) | 31s |
| [`notebooks/04_geosat_AMI_GK2A.ipynb`](https://github.com/ProjectPythia/geostationary-cookbook/blob/main/notebooks/04_geosat_AMI_GK2A.ipynb) | 32s |
| [`notebooks/00_geosat_explaining_steps.ipynb`](https://github.com/ProjectPythia/geostationary-cookbook/blob/main/notebooks/00_geosat_explaining_steps.ipynb) | 57s |
| [`notebooks/01_geosat_GOESR.ipynb`](https://github.com/ProjectPythia/geostationary-cookbook/blob/main/notebooks/01_geosat_GOESR.ipynb) | 1m 00s |

Executed 8 notebook(s) from the project toc: [`notebooks/00_geosat_explaining_steps.ipynb`](https://github.com/ProjectPythia/geostationary-cookbook/blob/main/notebooks/00_geosat_explaining_steps.ipynb), [`notebooks/01_geosat_ABI_GOES_east.ipynb`](https://github.com/ProjectPythia/geostationary-cookbook/blob/main/notebooks/01_geosat_ABI_GOES_east.ipynb), [`notebooks/01_geosat_GOESR.ipynb`](https://github.com/ProjectPythia/geostationary-cookbook/blob/main/notebooks/01_geosat_GOESR.ipynb), [`notebooks/02_geosat_ABI_GOES_west.ipynb`](https://github.com/ProjectPythia/geostationary-cookbook/blob/main/notebooks/02_geosat_ABI_GOES_west.ipynb), [`notebooks/03_geosat_AHI_HIMAWARI.ipynb`](https://github.com/ProjectPythia/geostationary-cookbook/blob/main/notebooks/03_geosat_AHI_HIMAWARI.ipynb), [`notebooks/04_geosat_AMI_GK2A.ipynb`](https://github.com/ProjectPythia/geostationary-cookbook/blob/main/notebooks/04_geosat_AMI_GK2A.ipynb), [`notebooks/99_auxiliar_dowloading.ipynb`](https://github.com/ProjectPythia/geostationary-cookbook/blob/main/notebooks/99_auxiliar_dowloading.ipynb), [`notebooks/notebook-template.ipynb`](https://github.com/ProjectPythia/geostationary-cookbook/blob/main/notebooks/notebook-template.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/geostationary-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Errors

**`FileNotFoundError`** — [Errno 2] No such file or directory: '/home/jovyan/.local/share/pyspectral/rayleigh_only/pyspectral_rayleigh_correction_luts.tgz'

in `site/content/notebooks.geosat-abi-goes-east.json`

```
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
Cell In[16], line 1
----> 1 lscn.load(['true_color'])
      3 ### Uncomment to show it
      4 #lscn.show('true_color')

File /srv/conda/envs/notebook/lib/python3.10/site-packages/satpy/scene.py:1484, in Scene.load(self, wishlist, calibration, resolution, polarization, level, modifiers, generate, unload, **kwargs)
   1482 self._read_datasets_from_storage(**kwargs)
   1483 if generate:
-> 1484     self.generate_possible_composites(unload)

File /srv/conda/envs/notebook/lib/python3.10/site-packages/satpy/scene.py:1547, in Scene.generate_possible_composites(self, unload)
   1540 def generate_possible_composites(self, unload):
   1541     """See which composites can be generated and generate them.
   1542 
   1543     Args:
   1544         unload (bool): if the dependencies of the composites
   1545                        should be unloaded after successful generation.
   1546     """
-> 1547     keepables = self._generate_composites_from_loaded_datasets()
   1549     if self.missing_datasets:
   1550         self._remove_failed_dataset
```

**`FileNotFoundError`** — [Errno 2] No such file or directory: '/home/jovyan/.local/share/pyspectral/rayleigh_only/pyspectral_rayleigh_correction_luts.tgz'

in `site/content/notebooks.geosat-ahi-himawari.json`

```
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
Cell In[14], line 1
----> 1 lscn.load(['true_color'])
      3 ### Uncomment to show it
      4 #lscn.show('true_color')

File /srv/conda/envs/notebook/lib/python3.10/site-packages/satpy/scene.py:1484, in Scene.load(self, wishlist, calibration, resolution, polarization, level, modifiers, generate, unload, **kwargs)
   1482 self._read_datasets_from_storage(**kwargs)
   1483 if generate:
-> 1484     self.generate_possible_composites(unload)

File /srv/conda/envs/notebook/lib/python3.10/site-packages/satpy/scene.py:1547, in Scene.generate_possible_composites(self, unload)
   1540 def generate_possible_composites(self, unload):
   1541     """See which composites can be generated and generate them.
   1542 
   1543     Args:
   1544         unload (bool): if the dependencies of the composites
   1545                        should be unloaded after successful generation.
   1546     """
-> 1547     keepables = self._generate_composites_from_loaded_datasets()
   1549     if self.missing_datasets:
   1550         self._remove_failed_dataset
```

**`FileNotFoundError`** — [Errno 2] No such file or directory: '/home/jovyan/.local/share/pyspectral/rayleigh_only/pyspectral_rayleigh_correction_luts.tgz'

in `site/content/notebooks.geosat-ami-gk2a.json`

```
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
Cell In[14], line 1
----> 1 lscn.load(['true_color'])
      3 ### Uncomment to show it
      4 #lscn.show('true_color')

File /srv/conda/envs/notebook/lib/python3.10/site-packages/satpy/scene.py:1484, in Scene.load(self, wishlist, calibration, resolution, polarization, level, modifiers, generate, unload, **kwargs)
   1482 self._read_datasets_from_storage(**kwargs)
   1483 if generate:
-> 1484     self.generate_possible_composites(unload)

File /srv/conda/envs/notebook/lib/python3.10/site-packages/satpy/scene.py:1547, in Scene.generate_possible_composites(self, unload)
   1540 def generate_possible_composites(self, unload):
   1541     """See which composites can be generated and generate them.
   1542 
   1543     Args:
   1544         unload (bool): if the dependencies of the composites
   1545                        should be unloaded after successful generation.
   1546     """
-> 1547     keepables = self._generate_composites_from_loaded_datasets()
   1549     if self.missing_datasets:
   1550         self._remove_failed_dataset
```

