# mrms-cookbook

Live outcome: **build failed**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/mrms-cookbook)

Run 2026-07-22 16:15:30 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [mrms-cookbook](https://github.com/ProjectPythia/mrms-cookbook) at ref [`main`](https://github.com/ProjectPythia/mrms-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **build failed** |
| Static tier | `incubating` |
| Time to a ready session | 3m 13s (fresh build) |
| Build succeeded | no |
| Resource metrics | unavailable: unknown |
| Errors raised | 0 |

Executed 5 notebook(s) from the project toc: [`notebooks/ch1_Introduction.ipynb`](https://github.com/ProjectPythia/mrms-cookbook/blob/main/notebooks/ch1_Introduction.ipynb), [`notebooks/ch2-mar-2023-tornado_jdh.ipynb`](https://github.com/ProjectPythia/mrms-cookbook/blob/main/notebooks/ch2-mar-2023-tornado_jdh.ipynb), [`notebooks/ch3_TXfloods.ipynb`](https://github.com/ProjectPythia/mrms-cookbook/blob/main/notebooks/ch3_TXfloods.ipynb), [`notebooks/ch4_bnf-mrms-qpe-hourly.ipynb`](https://github.com/ProjectPythia/mrms-cookbook/blob/main/notebooks/ch4_bnf-mrms-qpe-hourly.ipynb), [`notebooks/ch5_realtimeData.ipynb`](https://github.com/ProjectPythia/mrms-cookbook/blob/main/notebooks/ch5_realtimeData.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/mrms-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Build log (tail)

```
[  107.78s] 
[  107.78s] #3 DONE 0.1s
[  107.95s] #4 DONE 0.0s
[  107.95s] #5 CACHED
[  107.95s] 
[  107.95s] #7 [ 4/19] RUN if getent group 1000; then       GROUP_1000="$(getent group 1000 | cut -d: -f1)";       if [ "$GROUP_1000" != "jovyan" ]; then         groupmod --new-name jovyan "$GROUP_1000";       fi;     else       groupadd --gid 1000 jovyan;     fi
[  107.99s] 
[  107.99s] #9 [internal] load build context
[  111.44s] #9 transferring context: 691.80MB 3.3s done
[  111.44s] #9 DONE 3.4s
[  111.44s] 
[  111.44s] #10 [ 6/19] RUN apt-get -qq update &&     apt-get -qq install --yes --no-install-recommends        gettext-base        less        unzip        > /dev/null &&     apt-get -qq purge &&     apt-get -qq clean &&     rm -rf /var/lib/apt/lists/*
[  192.67s] #10 78.35 E: Package 'gettext-base' has no installation candidate
[  192.83s] 78.35 E: Package 'gettext-base' has no installation candidate
[  192.83s] ------
[  192.84s]   61 | >>>        unzip \
[  192.84s]   62 | >>>        > /dev/null && \
[  192.84s]   63 | >>>     apt-get -qq purge && \
[  192.84s]   64 | >>>     apt-get -qq clean && \
[  192.84s]   65 | >>>     rm -rf /var/lib/apt/lists/*
[  192.84s]   66 |
[  192.84s] --------------------
[  192.84s] ERROR: failed to solve: process "/bin/sh -c apt-get -qq update &&     apt-get -qq install --yes --no-install-recommends        gettext-base        less        unzip        > /dev/null &&     apt-get -qq purge &&     apt-get -qq clean &&     rm -rf /var/lib/apt/lists/*" did not complete successfully: exit code: 100
[  192.99s] Error during build: Command '['docker', 'buildx', 'build', '--progress', 'plain', '--push', '--build-arg', 'NB_USER=jovyan', '--build-arg', 'NB_UID=1000', '--tag', 'quay.io/imagebuilding-non-gcp-hubs/jetstream2-projectpythia-pythia-binder-projectpythia-2dmrms-2dcookbook-36cd92:ff5211c1b307b3d351142f59277069aa3e1fdec7', '--platform', 'linux/amd64', '/tmp/tmp95fxz_vb']' returned non-zero exit status 1.
[  192.99s] Error during build: Command '['docker', 'buildx', 'build', '--progress', 'plain', '--push', '--build-arg', 'NB_USER=jovyan', '--build-arg', 'NB_UID=1000', '--tag', 'quay.io/imagebuilding-non-gcp-hubs/jetstream2-projectpythia-pythia-binder-projectpythia-2dmrms-2dcookbook-36cd92:ff5211c1b307b3d351142f59277069aa3e1fdec7', '--platform', 'linux/amd64', '/tmp/tmp95fxz_vb']' returned non-zero exit status 1.
```

