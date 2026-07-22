# metpy-cookbook

Live outcome: **build failed**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/metpy-cookbook)

Run 2026-07-22 05:43:30 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [metpy-cookbook](https://github.com/ProjectPythia/metpy-cookbook) at ref [`main`](https://github.com/ProjectPythia/metpy-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **build failed** |
| Static tier | `healthy` |
| Time to a ready session | 10m 53s (fresh build) |
| Build succeeded | no |
| Resource metrics | unavailable: unknown |
| Errors raised | 0 |

Executed 0 notebook(s) from the project toc: none. Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/metpy-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Build log (tail)

```
[  649.43s] #20 66.19 Linking libspatialite-5.1.0-h2eee824_16
[  649.43s] #20 66.19 Linking fonttools-4.63.0-py310h3406613_0
[  649.57s] #20 66.26 Linking xorg-libxtst-1.2.5-hb9d3cd8_3
[  649.57s] #20 66.26 Linking libvulkan-loader-1.4.341.0-h5279c79_0
[  649.57s] #20 66.27 Linking numpy-2.2.6-py310hefbff90_0
[  649.57s] #20 66.40 Linking libclang13-22.1.8-default_h9692865_3
[  649.69s] #20 66.40 Linking libgdal-core-3.11.4-hed660dc_1
[  649.69s] #20 66.52 Linking cairo-1.18.4-h3394656_0
[  649.85s] #20 66.55 Linking contourpy-1.3.2-py310h3788b33_0
[  649.85s] #20 66.56 Linking scipy-1.15.2-py310h1d65ade_0
[  649.85s] #20 66.67 Linking pandas-2.3.3-py310h0158d43_2
[  650.10s] #20 66.93 Linking pyogrio-0.11.1-py310h460ceab_1
[  650.28s] #20 66.94 Linking harfbuzz-12.2.0-h15599e2_0
[  650.46s] #20 67.30 Linking qt6-main-6.9.3-h5c1c036_1
[  652.25s] #20 69.00 Linking pyside6-6.9.3-py310h2007e60_2
[  652.25s] #20 69.04 Linking matplotlib-3.10.9-py310hff52083_0
[  652.25s] #20 69.04 Linking folium-0.20.0-pyhd8ed1ab_0
[  652.41s] #20 69.09 Linking metpy-1.7.1-pyhd8ed1ab_0
[  652.47s] #20 69.31
[  652.61s] #20 69.37 time: 69.092
[  652.61s] #20 69.39 Collect information..
[  652.61s] #20 69.39 Cleaning index cache..
[  652.61s] ERROR: failed to receive status: rpc error: code = Unavailable desc = error reading from server: EOF
[  652.82s] Error during build: Command '['docker', 'buildx', 'build', '--progress', 'plain', '--push', '--build-arg', 'NB_USER=jovyan', '--build-arg', 'NB_UID=1000', '--tag', 'quay.io/imagebuilding-non-gcp-hubs/jetstream2-projectpythia-pythia-binder-projectpythia-2dmetpy-2dcookbook-dde93e:1012228e2e3f73485b9177884e8228c912a10231', '--platform', 'linux/amd64', '/tmp/tmpekj2wdqk']' returned non-zero exit status 1.
[  652.82s] Error during build: Command '['docker', 'buildx', 'build', '--progress', 'plain', '--push', '--build-arg', 'NB_USER=jovyan', '--build-arg', 'NB_UID=1000', '--tag', 'quay.io/imagebuilding-non-gcp-hubs/jetstream2-projectpythia-pythia-binder-projectpythia-2dmetpy-2dcookbook-dde93e:1012228e2e3f73485b9177884e8228c912a10231', '--platform', 'linux/amd64', '/tmp/tmpekj2wdqk']' returned non-zero exit status 1.
```

