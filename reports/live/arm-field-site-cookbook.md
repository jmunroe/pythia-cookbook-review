# arm-field-site-cookbook

Live outcome: **build failed**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/arm-field-site-cookbook)

Run 2026-07-22 08:46:26 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [arm-field-site-cookbook](https://github.com/ProjectPythia/arm-field-site-cookbook) at ref [`main`](https://github.com/ProjectPythia/arm-field-site-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **build failed** |
| Static tier | `incubating` |
| Time to a ready session | 1m 26s (fresh build) |
| Build succeeded | no |
| Resource metrics | unavailable: unknown |
| Errors raised | 0 |

Executed 15 notebook(s) from the project toc: [`foundations/act/ACT-Basics-BNF.ipynb`](https://github.com/ProjectPythia/arm-field-site-cookbook/blob/main/foundations/act/ACT-Basics-BNF.ipynb), [`foundations/act/act-tower-data.ipynb`](https://github.com/ProjectPythia/arm-field-site-cookbook/blob/main/foundations/act/act-tower-data.ipynb), [`foundations/pyart/pyart-basics.ipynb`](https://github.com/ProjectPythia/arm-field-site-cookbook/blob/main/foundations/pyart/pyart-basics.ipynb), [`foundations/pyart/pyart-corrections.ipynb`](https://github.com/ProjectPythia/arm-field-site-cookbook/blob/main/foundations/pyart/pyart-corrections.ipynb), [`foundations/pyart/pyart-gatefilers.ipynb`](https://github.com/ProjectPythia/arm-field-site-cookbook/blob/main/foundations/pyart/pyart-gatefilers.ipynb), [`foundations/pyart/pyart-qpe.ipynb`](https://github.com/ProjectPythia/arm-field-site-cookbook/blob/main/foundations/pyart/pyart-qpe.ipynb), [`foundations/pyart/radars-with-arm.ipynb`](https://github.com/ProjectPythia/arm-field-site-cookbook/blob/main/foundations/pyart/radars-with-arm.ipynb), [`foundations/xarray/dask-xarray-demo.ipynb`](https://github.com/ProjectPythia/arm-field-site-cookbook/blob/main/foundations/xarray/dask-xarray-demo.ipynb), [`foundations/xarray/xarray-intro.ipynb`](https://github.com/ProjectPythia/arm-field-site-cookbook/blob/main/foundations/xarray/xarray-intro.ipynb), [`foundations/xarray/xwrf-xarray-intro.ipynb`](https://github.com/ProjectPythia/arm-field-site-cookbook/blob/main/foundations/xarray/xwrf-xarray-intro.ipynb), [`projects/bnf-2025/acid/ccn-droplet-count.ipynb`](https://github.com/ProjectPythia/arm-field-site-cookbook/blob/main/projects/bnf-2025/acid/ccn-droplet-count.ipynb), [`projects/bnf-2025/acid/optical-properties.ipynb`](https://github.com/ProjectPythia/arm-field-site-cookbook/blob/main/projects/bnf-2025/acid/optical-properties.ipynb), [`projects/bnf-2025/bnf-deep-convection/coldpool-radar-analysis.ipynb`](https://github.com/ProjectPythia/arm-field-site-cookbook/blob/main/projects/bnf-2025/bnf-deep-convection/coldpool-radar-analysis.ipynb), [`projects/bnf-2025/bnf-deep-convection/coldpool-time-series.ipynb`](https://github.com/ProjectPythia/arm-field-site-cookbook/blob/main/projects/bnf-2025/bnf-deep-convection/coldpool-time-series.ipynb), [`projects/bnf-2025/land-atmosphere-interactions/surface-energy-balance-all-sites.ipynb`](https://github.com/ProjectPythia/arm-field-site-cookbook/blob/main/projects/bnf-2025/land-atmosphere-interactions/surface-energy-balance-all-sites.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/arm-field-site-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Build log (tail)

```
[   83.08s] #20 42.52   + libexpat                                   2.8.1  hecca717_1               conda-forge      78kB
[   83.08s] #20 42.52   - libffi                                     3.4.6  h2dba641_1               conda-forge      57kB
[   83.08s] #20 42.52   + libffi                                     3.5.2  h3435931_0               conda-forge      59kB
[   83.08s] #20 42.52   - liblzma                                    5.8.1  hb9d3cd8_2               conda-forge     113kB
[   83.08s] #20 42.52   + liblzma                                    5.8.3  hb03c661_0               conda-forge     113kB
[   83.08s] #20 42.52   - libsodium                                 1.0.20  h4ab18f5_0               conda-forge     206kB
[   83.08s] #20 42.52   - libuuid                                   2.41.2  he9a06e4_0               conda-forge      37kB
[   83.08s] #20 42.52   + libuuid                                   2.42.2  h5347b49_0               conda-forge      40kB
[   83.08s] #20 42.52   - libzlib                                    1.3.1  hb9d3cd8_2               conda-forge      61kB
[   83.08s] #20 42.52   + libzlib                                    1.3.2  h25fd6f3_2               conda-forge      64kB
[   83.08s] #20 42.52   - ncurses                                      6.5  h2d0b736_3               conda-forge     892kB
[   83.08s] #20 42.52   + ncurses                                      6.6  hdb14827_0               conda-forge     919kB
[   83.08s] #20 42.52   - nodejs                                   20.19.5  hf7ee748_0               conda-forge      17MB
[   83.08s] #20 42.52   - zlib                                       1.3.1  hb9d3cd8_2               conda-forge      92kB
[   83.08s] #20 42.52   + zlib                                       1.3.2  h25fd6f3_2               conda-forge      96kB
[   83.08s] #20 42.52
[   83.08s] #20 42.52
[   83.08s] #20 42.52   Upgrade: 17 packages
[   83.08s] #20 42.52 ──────────────────────────────────────────────────────────────────────────────────────────────────────
[   83.08s] #20 42.52
[   83.08s] #20 42.52
[   83.08s] #20 42.53 Confirm changes: [Y/n]
[   83.08s] #20 42.53 Transaction starting
[   86.27s] Error during build: Command '['docker', 'buildx', 'build', '--progress', 'plain', '--push', '--build-arg', 'NB_USER=jovyan', '--build-arg', 'NB_UID=1000', '--tag', 'quay.io/imagebuilding-non-gcp-hubs/jetstream2-projectpythia-pythia-binder-projectpythia-2darm-2dfield-2dsite-2dcookbook-bd3cc2:507972a13ce0642f789ea5864c73ef8c6686bd20', '--platform', 'linux/amd64', '/tmp/tmpzr2puzf9']' returned non-zero exit status 1.
[   86.27s] Error during build: Command '['docker', 'buildx', 'build', '--progress', 'plain', '--push', '--build-arg', 'NB_USER=jovyan', '--build-arg', 'NB_UID=1000', '--tag', 'quay.io/imagebuilding-non-gcp-hubs/jetstream2-projectpythia-pythia-binder-projectpythia-2darm-2dfield-2dsite-2dcookbook-bd3cc2:507972a13ce0642f789ea5864c73ef8c6686bd20', '--platform', 'linux/amd64', '/tmp/tmpzr2puzf9']' returned non-zero exit status 1.
```

