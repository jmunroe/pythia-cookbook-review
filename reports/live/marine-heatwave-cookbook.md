# marine-heatwave-cookbook

Live outcome: **build failed**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/marine-heatwave-cookbook)

Run 2026-07-22 15:56:41 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [marine-heatwave-cookbook](https://github.com/ProjectPythia/marine-heatwave-cookbook) at ref [`main`](https://github.com/ProjectPythia/marine-heatwave-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **build failed** |
| Static tier | `incubating` |
| Time to a ready session | 11m 25s (fresh build) |
| Build succeeded | no |
| Resource metrics | unavailable: unknown |
| Errors raised | 0 |

Executed 1 notebook(s) from the project toc: [`notebooks/foundation/mhw_observation_myst.ipynb`](https://github.com/ProjectPythia/marine-heatwave-cookbook/blob/main/notebooks/foundation/mhw_observation_myst.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/marine-heatwave-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Build log (tail)

```
[  267.11s] #6 214.7 W: Failed to fetch http://security.ubuntu.com/ubuntu/dists/noble-security/multiverse/binary-amd64/Packages  Connection failed [IP: 91.189.92.22 80]
[  457.99s] #6 390.9 debconf: delaying package configuration, since apt-utils is not installed
[  460.67s] 
[  460.67s] #7 [ 3/19] RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen &&     locale-gen
[  462.13s] #7 0.250   en_US.UTF-8... done
[  462.29s] #7 1.492 Generation complete.
[  462.49s] 
[  462.49s] #8 [ 4/19] RUN if getent group 1000; then       GROUP_1000="$(getent group 1000 | cut -d: -f1)";       if [ "$GROUP_1000" != "jovyan" ]; then         groupmod --new-name jovyan "$GROUP_1000";       fi;     else       groupadd --gid 1000 jovyan;     fi
[  462.66s] #8 0.312 ubuntu:x:1000:
[  462.98s] 
[  462.98s] #9 [ 5/19] RUN if id 1000; then       USER_1000="$(id 1000 -un)";       if [ "$USER_1000" != "jovyan" ]; then         usermod --home "/home/jovyan" --login "jovyan" --move-home "$USER_1000";       fi;     else       useradd         --comment "Default user"         --create-home         --gid 1000         --no-log-init         --shell /bin/bash         --uid 1000         jovyan;     fi
[  463.16s] #9 0.304 uid=1000(ubuntu) gid=1000(jovyan) groups=1000(jovyan),4(adm),20(dialout),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev)
[  463.54s] #9 DONE 0.7s
[  684.56s] #10 204.0 W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/noble/InRelease  Connection failed [IP: 91.189.92.23 80]
[  684.68s] #10 204.0 E: Package 'gettext-base' has no installation candidate
[  684.80s] ------
[  684.80s]  > [ 6/19] RUN apt-get -qq update &&     apt-get -qq install --yes --no-install-recommends        gettext-base        less        unzip        > /dev/null &&     apt-get -qq purge &&     apt-get -qq clean &&     rm -rf /var/lib/apt/lists/*:
[  684.80s] 204.0 W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/noble-backports/InRelease  Could not connect to archive.ubuntu.com:80 (185.125.190.83), connection timed out Could not connect to archive.ubuntu.com:80 (91.189.92.24), connection timed out Could not connect to archive.ubuntu.com:80 (185.125.190.81), connection timed out Could not connect to archive.ubuntu.com:80 (91.189.92.23), connection timed out Could not connect to archive.ubuntu.com:80 (185.125.190.82), connection timed out Could not connect to archive.ubuntu.com:80 (91.189.92.22), connection timed out [IP: 91.189.92.22 80]
[  684.80s] 204.0 E: Package 'gettext-base' has no installation candidate
[  684.80s]   57 | >>> RUN apt-get -qq update && \
[  684.80s]   58 | >>>     apt-get -qq install --yes --no-install-recommends \
[  684.80s]   59 | >>>        gettext-base \
[  684.84s]   61 | >>>        unzip \
[  684.84s]   62 | >>>        > /dev/null && \
[  684.84s]   63 | >>>     apt-get -qq purge && \
```

