# mpasviewer-cookbook

Live outcome: **build failed**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/mpasviewer-cookbook)

Run 2026-07-22 16:14:27 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [mpasviewer-cookbook](https://github.com/ProjectPythia/mpasviewer-cookbook) at ref [`main`](https://github.com/ProjectPythia/mpasviewer-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **build failed** |
| Static tier | `incubating` |
| Time to a ready session | 26.52s (fresh build) |
| Build succeeded | no |
| Resource metrics | unavailable: unknown |
| Errors raised | 0 |

Executed 4 notebook(s) from the project toc: [`notebooks/20_remote_out_hurricane_investigation.ipynb`](https://github.com/ProjectPythia/mpasviewer-cookbook/blob/main/notebooks/20_remote_out_hurricane_investigation.ipynb), [`notebooks/Hurricane_Ida_Pt2.ipynb`](https://github.com/ProjectPythia/mpasviewer-cookbook/blob/main/notebooks/Hurricane_Ida_Pt2.ipynb), [`notebooks/convective-environments.ipynb`](https://github.com/ProjectPythia/mpasviewer-cookbook/blob/main/notebooks/convective-environments.ipynb), [`notebooks/introduction.ipynb`](https://github.com/ProjectPythia/mpasviewer-cookbook/blob/main/notebooks/introduction.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/mpasviewer-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Build log (tail)

```
[   19.29s] HEAD is now at 21f9d885 added example anim
[   19.50s] Building conda environment for python=3.10
[   19.50s] Unknown phase "undefined" from builder
[   19.50s] Using CondaBuildPack builder
[   20.60s] #3 transferring context: 2B done
[   20.60s] #3 DONE 0.1s
[   20.60s] 
[   20.60s] #5 [internal] load build context
[   20.92s] #5 transferring context: 58.45MB 0.3s done
[   21.14s] 
[   21.14s] #6 [ 5/19] RUN if id 1000; then       USER_1000="$(id 1000 -un)";       if [ "$USER_1000" != "jovyan" ]; then         usermod --home "/home/jovyan" --login "jovyan" --move-home "$USER_1000";       fi;     else       useradd         --comment "Default user"         --create-home         --gid 1000         --no-log-init         --shell /bin/bash         --uid 1000         jovyan;     fi
[   21.14s] #6 CACHED
[   21.14s] #7 CACHED
[   21.14s] #8 CACHED
[   21.15s] 
[   21.19s] #10 [ 9/19] COPY --chown=1000:1000 build_script_files/-2fopt-2fvenv-2flib-2fpython3-2e12-2fsite-2dpackages-2frepo2docker-2fbuildpacks-2fconda-2finstall-2dbase-2denv-2ebash-637204 /tmp/install-base-env.bash
[   21.19s] 
[   21.19s] #15 CACHED
[   21.19s] #16 [ 7/19] COPY --chown=1000:1000 build_script_files/-2fopt-2fvenv-2flib-2fpython3-2e12-2fsite-2dpackages-2frepo2docker-2fbuildpacks-2fconda-2factivate-2dconda-2esh-e67d51 /etc/profile.d/activate-conda.sh
[   21.19s] #16 CACHED
[   21.47s] #19 DONE 0.5s
[   21.65s] #20 [16/19] RUN TIMEFORMAT='time: %3R' bash -c 'time ${MAMBA_EXE} env update -p ${NB_PYTHON_PREFIX} --file "environment.yml" && time ${MAMBA_EXE} clean --all -f -y && ${MAMBA_EXE} list -p ${NB_PYTHON_PREFIX} '
[   26.49s] ERROR: failed to receive status: rpc error: code = Unavailable desc = error reading from server: EOF
[   26.52s] Error during build: Command '['docker', 'buildx', 'build', '--progress', 'plain', '--push', '--build-arg', 'NB_USER=jovyan', '--build-arg', 'NB_UID=1000', '--tag', 'quay.io/imagebuilding-non-gcp-hubs/jetstream2-projectpythia-pythia-binder-projectpythia-2dmpasviewer-2dcookbook-9a297b:21f9d885a68ce3636285d6f72f238ffa34554008', '--platform', 'linux/amd64', '/tmp/tmpj7vow4dd']' returned non-zero exit status 1.
[   26.52s] Error during build: Command '['docker', 'buildx', 'build', '--progress', 'plain', '--push', '--build-arg', 'NB_USER=jovyan', '--build-arg', 'NB_UID=1000', '--tag', 'quay.io/imagebuilding-non-gcp-hubs/jetstream2-projectpythia-pythia-binder-projectpythia-2dmpasviewer-2dcookbook-9a297b:21f9d885a68ce3636285d6f72f238ffa34554008', '--platform', 'linux/amd64', '/tmp/tmpj7vow4dd']' returned non-zero exit status 1.
```

