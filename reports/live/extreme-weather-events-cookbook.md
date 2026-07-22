# extreme-weather-events-cookbook

Live outcome: **build failed**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/extreme-weather-events-cookbook)

Run 2026-07-22 09:44:25 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [extreme-weather-events-cookbook](https://github.com/ProjectPythia/extreme-weather-events-cookbook) at ref [`main`](https://github.com/ProjectPythia/extreme-weather-events-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **build failed** |
| Static tier | `incubating` |
| Time to a ready session | 2m 12s (fresh build) |
| Build succeeded | no |
| Resource metrics | unavailable: unknown |
| Errors raised | 0 |

Executed 0 notebook(s) from the project toc: none. Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/extreme-weather-events-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Build log (tail)

```
[  129.99s] #20 122.7 Linking click-plugins-1.1.1.2-pyhd8ed1ab_0
[  129.99s] #20 122.7 Linking bokeh-3.9.1-pyhd8ed1ab_0
[  129.99s] #20 122.8 Linking snuggs-1.4.7-pyhd8ed1ab_2
[  130.09s] #20 122.9 Linking markdown-it-py-4.2.0-pyhd8ed1ab_0
[  130.09s] #20 122.9 Linking linkify-it-py-2.1.0-pyhcf101f3_0
[  130.09s] #20 122.9 Linking httpcore2-2.3.0-pyhcf101f3_0
[  130.10s] #20 122.9 Linking fonts-conda-forge-1-hc364b38_1
[  130.10s] #20 122.9 Linking dask-core-2026.7.1-pyhc364b38_0
[  130.10s] #20 122.9 Linking fastlite-0.2.3-pyhcf101f3_0
[  130.10s] #20 122.9 Linking mdit-py-plugins-0.6.1-pyhd8ed1ab_0
[  130.10s] #20 123.0 Linking httpx2-2.3.0-pyhcf101f3_0
[  130.20s] #20 123.0 Linking fonts-conda-ecosystem-1-0
[  130.20s] #20 123.0 Linking _python_abi3_support-1.0-hd8ed1ab_3
[  130.20s] #20 123.0 Linking sphinxcontrib-htmlhelp-2.1.0-pyhd8ed1ab_1
[  130.21s] #20 123.0 Linking sphinxcontrib-qthelp-2.0.0-pyhd8ed1ab_1
[  130.21s] #20 123.0 Linking fastprogress-1.1.6-pyhd8ed1ab_0
[  130.21s] #20 123.0 Linking sphinxcontrib-serializinghtml-2.0.0-pyhd8ed1ab_0
[  130.21s] #20 123.0 Linking pydata-sphinx-theme-0.15.4-pyhd8ed1ab_0
[  130.48s] #20 123.1 Linking cytoolz-1.1.0-py310h7c4b9e2_2
[  130.58s] #20 123.4 Linking pandas-2.3.3-py310h0158d43_2
[  130.85s] #20 123.7 Linking fonttools-4.63.0-py310h3406613_0
[  131.28s] #20 124.1 Linking aiohttp-3.14.2-py310h31b6992_0
[  131.39s] #20 124.2 Linking polars-runtime-32-1.43.0-py310h9585f58_0
[  132.21s] Error during build: Command '['docker', 'buildx', 'build', '--progress', 'plain', '--push', '--build-arg', 'NB_USER=jovyan', '--build-arg', 'NB_UID=1000', '--tag', 'quay.io/imagebuilding-non-gcp-hubs/jetstream2-projectpythia-pythia-binder-projectpythia-2dextreme-2dweather-2devents-2dcookbook-ebcc9f:5158f5e3354b04f946e7e9caa2850f76566bc25f', '--platform', 'linux/amd64', '/tmp/tmpag6tk9r4']' returned non-zero exit status 1.
[  132.21s] Error during build: Command '['docker', 'buildx', 'build', '--progress', 'plain', '--push', '--build-arg', 'NB_USER=jovyan', '--build-arg', 'NB_UID=1000', '--tag', 'quay.io/imagebuilding-non-gcp-hubs/jetstream2-projectpythia-pythia-binder-projectpythia-2dextreme-2dweather-2devents-2dcookbook-ebcc9f:5158f5e3354b04f946e7e9caa2850f76566bc25f', '--platform', 'linux/amd64', '/tmp/tmpag6tk9r4']' returned non-zero exit status 1.
```

