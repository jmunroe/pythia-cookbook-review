# CFC-extreme-weather-cookbook

Live outcome: **build failed**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/CFC-extreme-weather-cookbook)

Run 2026-07-22 09:19:53 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [CFC-extreme-weather-cookbook](https://github.com/ProjectPythia/CFC-extreme-weather-cookbook) at ref [`main`](https://github.com/ProjectPythia/CFC-extreme-weather-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **build failed** |
| Static tier | `incubating` |
| Time to a ready session | 1m 18s (fresh build) |
| Build succeeded | no |
| Resource metrics | unavailable: unknown |
| Errors raised | 0 |

Executed 2 notebook(s) from the project toc: [`notebooks/cfc-atm.ipynb`](https://github.com/ProjectPythia/CFC-extreme-weather-cookbook/blob/main/notebooks/cfc-atm.ipynb), [`notebooks/cfc-ocean.ipynb`](https://github.com/ProjectPythia/CFC-extreme-weather-cookbook/blob/main/notebooks/cfc-ocean.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/CFC-extreme-weather-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Build log (tail)

```
[   77.70s] #20 71.38 Linking libcups-2.3.3-hb8b1518_5
[   77.70s] #20 71.39 Linking libzip-1.11.2-h6991a6a_0
[   77.70s] #20 71.40 Linking libpng-1.6.58-h421ea60_0
[   77.80s] #20 71.40 Linking pcre2-10.46-h1321c63_0
[   77.80s] #20 71.43 Linking librttopo-1.1.0-h96cd706_19
[   77.80s] #20 71.46 Linking xorg-libsm-1.2.6-he73a12e_0
[   77.80s] #20 71.46 Linking protobuf-6.31.1-py310ha36e12e_2
[   77.80s] #20 71.48 Linking libprotobuf-6.31.1-hfb7daa7_5
[   77.80s] #20 71.50 Linking google-crc32c-1.8.0-py310hf432777_1
[   77.91s] #20 71.51 Linking libxml2-16-2.15.1-ha9997c6_0
[   77.91s] #20 71.52 Linking blosc-1.21.6-he440d0b_1
[   77.91s] #20 71.52 Linking aws-c-compression-0.3.1-h7e655bb_8
[   77.91s] #20 71.52 Linking aws-checksums-0.2.7-h7e655bb_4
[   77.91s] #20 71.56 Linking libfreetype6-2.14.3-h73754d4_0
[   77.91s] #20 71.56 Linking libglib-2.86.2-h32235b2_0
[   77.91s] #20 71.59 Linking xcb-util-0.4.1-h4f16b4b_2
[   77.91s] #20 71.59 Linking xcb-util-wm-0.4.2-hb711507_0
[   77.91s] #20 71.59 Linking xcb-util-renderutil-0.3.10-hb711507_0
[   78.05s] #20 71.62 Linking openjpeg-2.5.4-h55fea9a_0
[   78.05s] #20 71.62 Linking libopenblas-0.3.33-pthreads_h94d23a6_0
[   78.05s] #20 71.62 Linking libcurl-8.18.0-h4e3cde8_0
[   78.05s] #20 71.63 Linking re2-2025.11.05-h5301d42_0
[   78.05s] #20 71.63 Linking orc-2.2.1-hd747db4_0
[   78.05s] #20 71.63 Linking libxml2-2.15.1-h26afc86_0
[   78.09s] Error during build: Command '['docker', 'buildx', 'build', '--progress', 'plain', '--push', '--build-arg', 'NB_USER=jovyan', '--build-arg', 'NB_UID=1000', '--tag', 'quay.io/imagebuilding-non-gcp-hubs/jetstream2-projectpythia-pythia-binder-projectpythia-2dcfc-2dextreme-2dweather-2dcookbook-f72d8e:82d260434d70eca88a8aa3eea7450d29527f2d51', '--platform', 'linux/amd64', '/tmp/tmps1oyv8jc']' returned non-zero exit status 1.
```

