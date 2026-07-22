# METAR_archive-cookbook

Live outcome: **build failed**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/METAR_archive-cookbook)

Run 2026-07-22 16:07:53 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [METAR_archive-cookbook](https://github.com/ProjectPythia/METAR_archive-cookbook) at ref [`main`](https://github.com/ProjectPythia/METAR_archive-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **build failed** |
| Static tier | `incubating` |
| Time to a ready session | 1m 56s (fresh build) |
| Build succeeded | no |
| Resource metrics | unavailable: unknown |
| Errors raised | 0 |

Executed 9 notebook(s) from the project toc: [`notebooks/AI_Assistant.ipynb`](https://github.com/ProjectPythia/METAR_archive-cookbook/blob/main/notebooks/AI_Assistant.ipynb), [`notebooks/Dataset_Restructuring.ipynb`](https://github.com/ProjectPythia/METAR_archive-cookbook/blob/main/notebooks/Dataset_Restructuring.ipynb), [`notebooks/Geopandas_Visualization.ipynb`](https://github.com/ProjectPythia/METAR_archive-cookbook/blob/main/notebooks/Geopandas_Visualization.ipynb), [`notebooks/Lonboard_Visualization.ipynb`](https://github.com/ProjectPythia/METAR_archive-cookbook/blob/main/notebooks/Lonboard_Visualization.ipynb), [`notebooks/MetPy_METAR_Map.ipynb`](https://github.com/ProjectPythia/METAR_archive-cookbook/blob/main/notebooks/MetPy_METAR_Map.ipynb), [`notebooks/Temperature.ipynb`](https://github.com/ProjectPythia/METAR_archive-cookbook/blob/main/notebooks/Temperature.ipynb), [`notebooks/local_statistics.ipynb`](https://github.com/ProjectPythia/METAR_archive-cookbook/blob/main/notebooks/local_statistics.ipynb), [`notebooks/primer.ipynb`](https://github.com/ProjectPythia/METAR_archive-cookbook/blob/main/notebooks/primer.ipynb), [`notebooks/reanalysis_comparison.ipynb`](https://github.com/ProjectPythia/METAR_archive-cookbook/blob/main/notebooks/reanalysis_comparison.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/METAR_archive-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Build log (tail)

```
[  115.12s] #10 80.15 W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/noble/multiverse/binary-amd64/Packages  Could not connect to archive.ubuntu.com:80 (185.125.190.81), connection timed out Could not connect to archive.ubuntu.com:80 (185.125.190.82), connection timed out Could not connect to archive.ubuntu.com:80 (185.125.190.83), connection timed out Could not connect to archive.ubuntu.com:80 (91.189.92.23), connection timed out Could not connect to archive.ubuntu.com:80 (91.189.92.22), connection timed out Could not connect to archive.ubuntu.com:80 (91.189.92.24), connection timed out [IP: 91.189.92.24 80]
[  115.13s] #10 80.15 W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/noble/main/binary-amd64/Packages  Unable to connect to archive.ubuntu.com:http: [IP: 91.189.92.24 80]
[  115.13s] #10 80.15 W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/noble/universe/binary-amd64/Packages  Unable to connect to archive.ubuntu.com:http: [IP: 91.189.92.24 80]
[  115.27s] #10 80.29 E: Package 'gettext-base' has no installation candidate
[  115.51s] ------
[  115.51s]  > [ 6/19] RUN apt-get -qq update &&     apt-get -qq install --yes --no-install-recommends        gettext-base        less        unzip        > /dev/null &&     apt-get -qq purge &&     apt-get -qq clean &&     rm -rf /var/lib/apt/lists/*:
[  115.51s] 80.15 W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/noble/restricted/binary-amd64/Packages  Unable to connect to archive.ubuntu.com:http: [IP: 91.189.92.24 80]
[  115.52s] 80.15 W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/noble-backports/main/binary-amd64/Packages  Unable to connect to archive.ubuntu.com:http: [IP: 91.189.92.24 80]
[  115.52s] 80.29 E: Package 'gettext-base' has no installation candidate
[  115.52s] ------
[  115.52s] Dockerfile:57
[  115.52s] --------------------
[  115.52s]   56 |     # If install fails for some reason, errors will still be printed
[  115.52s]   57 | >>> RUN apt-get -qq update && \
[  115.52s]   58 | >>>     apt-get -qq install --yes --no-install-recommends \
[  115.52s]   59 | >>>        gettext-base \
[  115.52s]   60 | >>>        less \
[  115.52s]   61 | >>>        unzip \
[  115.52s]   62 | >>>        > /dev/null && \
[  115.52s]   63 | >>>     apt-get -qq purge && \
[  115.52s]   64 | >>>     apt-get -qq clean && \
[  115.52s]   65 | >>>     rm -rf /var/lib/apt/lists/*
[  115.52s]   66 |
[  115.52s] --------------------
[  115.52s] ERROR: failed to solve: process "/bin/sh -c apt-get -qq update &&     apt-get -qq install --yes --no-install-recommends        gettext-base        less        unzip        > /dev/null &&     apt-get -qq purge &&     apt-get -qq clean &&     rm -rf /var/lib/apt/lists/*" did not complete successfully: exit code: 100
```

