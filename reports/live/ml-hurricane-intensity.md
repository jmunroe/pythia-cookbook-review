# ml-hurricane-intensity

Live outcome: **build failed**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/ml-hurricane-intensity)

Run 2026-07-22 16:10:13 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [ml-hurricane-intensity](https://github.com/ProjectPythia/ml-hurricane-intensity) at ref [`main`](https://github.com/ProjectPythia/ml-hurricane-intensity/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **build failed** |
| Static tier | `incubating` |
| Time to a ready session | 3m 36s (fresh build) |
| Build succeeded | no |
| Resource metrics | unavailable: unknown |
| Errors raised | 0 |

Executed 3 notebook(s) from the project toc: [`notebooks/Model.ipynb`](https://github.com/ProjectPythia/ml-hurricane-intensity/blob/main/notebooks/Model.ipynb), [`notebooks/era5_preprocessing.ipynb`](https://github.com/ProjectPythia/ml-hurricane-intensity/blob/main/notebooks/era5_preprocessing.ipynb), [`notebooks/ibtrack_preprocessing.ipynb`](https://github.com/ProjectPythia/ml-hurricane-intensity/blob/main/notebooks/ibtrack_preprocessing.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/ml-hurricane-intensity/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Build log (tail)

```
[  108.21s] #10 ...
[  108.76s] #9 transferring context: 2.24GB 10.4s done
[  109.69s] #9 DONE 11.6s
[  109.69s] 
[  215.24s] #10 109.1 W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/noble-updates/InRelease  Could not connect to archive.ubuntu.com:80 (91.189.92.23), connection timed out Could not connect to archive.ubuntu.com:80 (91.189.92.22), connection timed out Could not connect to archive.ubuntu.com:80 (185.125.190.83), connection timed out Could not connect to archive.ubuntu.com:80 (91.189.92.24), connection timed out Could not connect to archive.ubuntu.com:80 (185.125.190.82), connection timed out Could not connect to archive.ubuntu.com:80 (185.125.190.81), connection timed out [IP: 185.125.190.81 80]
[  215.24s] #10 109.1 W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/noble-backports/InRelease  Unable to connect to archive.ubuntu.com:http: [IP: 185.125.190.81 80]
[  215.24s] #10 109.1 W: Failed to fetch http://security.ubuntu.com/ubuntu/dists/noble-security/InRelease  Could not connect to security.ubuntu.com:80 (185.125.190.83), connection timed out Could not connect to security.ubuntu.com:80 (91.189.92.22), connection timed out Could not connect to security.ubuntu.com:80 (91.189.92.24), connection timed out Could not connect to security.ubuntu.com:80 (91.189.92.23), connection timed out Could not connect to security.ubuntu.com:80 (185.125.190.81), connection timed out Could not connect to security.ubuntu.com:80 (185.125.190.82), connection timed out
[  215.24s] #10 109.1 W: Some index files failed to download. They have been ignored, or old ones used instead.
[  215.35s] #10 109.1 E: Package 'gettext-base' has no installation candidate
[  215.35s] #10 ERROR: process "/bin/sh -c apt-get -qq update &&     apt-get -qq install --yes --no-install-recommends        gettext-base        less        unzip        > /dev/null &&     apt-get -qq purge &&     apt-get -qq clean &&     rm -rf /var/lib/apt/lists/*" did not complete successfully: exit code: 100
[  215.54s] ------
[  215.54s] 109.1 W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/noble/InRelease  Connection failed [IP: 185.125.190.81 80]
[  215.54s] 109.1 W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/noble-updates/InRelease  Could not connect to archive.ubuntu.com:80 (91.189.92.23), connection timed out Could not connect to archive.ubuntu.com:80 (91.189.92.22), connection timed out Could not connect to archive.ubuntu.com:80 (185.125.190.83), connection timed out Could not connect to archive.ubuntu.com:80 (91.189.92.24), connection timed out Could not connect to archive.ubuntu.com:80 (185.125.190.82), connection timed out Could not connect to archive.ubuntu.com:80 (185.125.190.81), connection timed out [IP: 185.125.190.81 80]
[  215.54s] 109.1 W: Some index files failed to download. They have been ignored, or old ones used instead.
[  215.54s] 109.1 E: Package 'gettext-base' has no installation candidate
[  215.54s] Dockerfile:57
[  215.54s] --------------------
[  215.58s]   57 | >>> RUN apt-get -qq update && \
[  215.58s]   61 | >>>        unzip \
[  215.58s]   65 | >>>     rm -rf /var/lib/apt/lists/*
[  215.58s]   66 |
[  215.58s] --------------------
[  215.58s] ERROR: failed to solve: process "/bin/sh -c apt-get -qq update &&     apt-get -qq install --yes --no-install-recommends        gettext-base        less        unzip        > /dev/null &&     apt-get -qq purge &&     apt-get -qq clean &&     rm -rf /var/lib/apt/lists/*" did not complete successfully: exit code: 100
[  215.98s] Error during build: Command '['docker', 'buildx', 'build', '--progress', 'plain', '--push', '--build-arg', 'NB_USER=jovyan', '--build-arg', 'NB_UID=1000', '--tag', 'quay.io/imagebuilding-non-gcp-hubs/jetstream2-projectpythia-pythia-binder-projectpythia-2dml-2dhurricane-2dintensity-2bb351:2f121838b7386c35a7aa374ff296cfa746bd81c7', '--platform', 'linux/amd64', '/tmp/tmp5hy6n3xq']' returned non-zero exit status 1.
[  215.98s] Error during build: Command '['docker', 'buildx', 'build', '--progress', 'plain', '--push', '--build-arg', 'NB_USER=jovyan', '--build-arg', 'NB_UID=1000', '--tag', 'quay.io/imagebuilding-non-gcp-hubs/jetstream2-projectpythia-pythia-binder-projectpythia-2dml-2dhurricane-2dintensity-2bb351:2f121838b7386c35a7aa374ff296cfa746bd81c7', '--platform', 'linux/amd64', '/tmp/tmp5hy6n3xq']' returned non-zero exit status 1.
```

