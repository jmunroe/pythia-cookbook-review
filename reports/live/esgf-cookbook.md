# esgf-cookbook

Live outcome: **build failed**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/esgf-cookbook)

Run 2026-07-21 19:13:12 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [esgf-cookbook](https://github.com/ProjectPythia/esgf-cookbook) at ref [`main`](https://github.com/ProjectPythia/esgf-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **build failed** |
| Static tier | `stale` |
| Time to a ready session | 416.52s (fresh build) |
| Build succeeded | no |
| Resource metrics | unavailable: unknown |
| Errors raised | 0 |

Executed 7 notebook(s) from the project toc: [`notebooks/complex-search.ipynb`](https://github.com/ProjectPythia/esgf-cookbook/blob/main/notebooks/complex-search.ipynb), [`notebooks/complex-search2-and-analysis.ipynb`](https://github.com/ProjectPythia/esgf-cookbook/blob/main/notebooks/complex-search2-and-analysis.ipynb), [`notebooks/ex-regrid-plot.ipynb`](https://github.com/ProjectPythia/esgf-cookbook/blob/main/notebooks/ex-regrid-plot.ipynb), [`notebooks/intro-search.ipynb`](https://github.com/ProjectPythia/esgf-cookbook/blob/main/notebooks/intro-search.ipynb), [`notebooks/rooki.ipynb`](https://github.com/ProjectPythia/esgf-cookbook/blob/main/notebooks/rooki.ipynb), [`notebooks/rooki_enso_nonlinear.ipynb`](https://github.com/ProjectPythia/esgf-cookbook/blob/main/notebooks/rooki_enso_nonlinear.ipynb), [`notebooks/use-intake-esgf-with-rooki.ipynb`](https://github.com/ProjectPythia/esgf-cookbook/blob/main/notebooks/use-intake-esgf-with-rooki.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/esgf-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Build log (tail)

```
[  409.91s] #20 81.75 Linking jupyterlab_pygments-0.3.0-pyhd8ed1ab_2
[  409.91s] #20 81.75 Linking mistune-3.1.4-pyhcf101f3_0
[  409.91s] #20 81.77 Linking nbformat-5.10.4-pyhd8ed1ab_1
[  409.91s] #20 81.77 Linking pandocfilters-1.5.0-pyhd8ed1ab_0
[  409.91s] #20 81.78 Linking nbconvert-core-7.16.6-pyh29332c3_0
[  410.11s] #20 81.80 Linking jupyter_server-2.17.0-pyhcf101f3_0
[  410.11s] #20 81.84 Linking pamela-1.2.0-pyhd8ed1ab_1
[  410.11s] #20 81.84 Linking typing-inspection-0.4.2-pyhd8ed1ab_0
[  410.11s] #20 81.84 Linking pydantic-2.12.2-pyh3cfb1c2_0
[  410.64s] #20 82.54 Linking jupyterlab_server-2.27.3-pyhd8ed1ab_1
[  410.77s] #20 82.66 Linking notebook-7.4.7-pyhd8ed1ab_0
[  410.96s] #20 82.70 Linking wheel-0.45.1-pyhd8ed1ab_1
[  411.13s] #20 83.03 warning  libmamba You are using 'pip' as an additional package manager.
[  411.29s] #20 83.04
[  411.29s] #20 83.04 Updating pip packages: sphinx-pythia-theme, sphinx==4.5.0, sphinxcontrib-applehelp<1.0.7, sphinxcontrib-devhelp<1.0.5, sphinxcontrib-htmlhelp<2.0.4, sphinxcontrib-qthelp<1.0.6, sphinxcontrib-serializinghtml<1.1.9, pydata-sphinx-theme<=0.8, docutils==0.16, git+https://github.com/esgf2-us/intake-esgf
[  415.39s] #20 87.30 critical libmamba pip failed to update packages
[  416.32s] #20 ERROR: process "/bin/sh -c TIMEFORMAT='time: %3R' bash -c 'time ${MAMBA_EXE} env update -p ${NB_PYTHON_PREFIX} --file \"environment.yml\" && time ${MAMBA_EXE} clean --all -f -y && ${MAMBA_EXE} list -p ${NB_PYTHON_PREFIX} '" did not complete successfully: exit code: 1
[  416.46s] 82.86
[  416.46s] Dockerfile:131
[  416.46s] --------------------
[  416.52s]  134 | >>> ${MAMBA_EXE} list -p ${NB_PYTHON_PREFIX} \
[  416.52s]  135 | >>> '
[  416.52s]  136 |
[  416.52s] Error during build: Command '['docker', 'buildx', 'build', '--progress', 'plain', '--push', '--build-arg', 'NB_USER=jovyan', '--build-arg', 'NB_UID=1000', '--tag', 'quay.io/imagebuilding-non-gcp-hubs/jetstream2-projectpythia-pythia-binder-projectpythia-2desgf-2dcookbook-523f4c:fb5ed9a2491993e7383e5fe0cc9a7ed76c5c3c3e', '--platform', 'linux/amd64', '/tmp/tmpmzhuo8oz']' returned non-zero exit status 1.
[  416.52s] Error during build: Command '['docker', 'buildx', 'build', '--progress', 'plain', '--push', '--build-arg', 'NB_USER=jovyan', '--build-arg', 'NB_UID=1000', '--tag', 'quay.io/imagebuilding-non-gcp-hubs/jetstream2-projectpythia-pythia-binder-projectpythia-2desgf-2dcookbook-523f4c:fb5ed9a2491993e7383e5fe0cc9a7ed76c5c3c3e', '--platform', 'linux/amd64', '/tmp/tmpmzhuo8oz']' returned non-zero exit status 1.
```

