# ml-hurricane-intensity

Live outcome: **build failed**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/ml-hurricane-intensity)

Run 2026-07-22 22:03:34 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [ml-hurricane-intensity](https://github.com/ProjectPythia/ml-hurricane-intensity) at ref [`main`](https://github.com/ProjectPythia/ml-hurricane-intensity/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **build failed** |
| Static tier | `incubating` |
| Time to a ready session | 5m 28s (fresh build) |
| Build succeeded | no |
| Resource metrics | unavailable: unknown |
| Errors raised | 0 |

Executed 3 notebook(s) from the project toc: [`notebooks/Model.ipynb`](https://github.com/ProjectPythia/ml-hurricane-intensity/blob/main/notebooks/Model.ipynb), [`notebooks/era5_preprocessing.ipynb`](https://github.com/ProjectPythia/ml-hurricane-intensity/blob/main/notebooks/era5_preprocessing.ipynb), [`notebooks/ibtrack_preprocessing.ipynb`](https://github.com/ProjectPythia/ml-hurricane-intensity/blob/main/notebooks/ibtrack_preprocessing.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/ml-hurricane-intensity/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Build log (tail)

```
[  325.35s] #20 232.3   + krb5                                  1.22.2  hbde042b_1               conda-forge       1MB
[  325.35s] #20 232.3   - libexpat                               2.7.1  hecca717_0               conda-forge      75kB
[  325.35s] #20 232.3   - libsodium                             1.0.20  h4ab18f5_0               conda-forge     206kB
[  325.35s] #20 232.3   + libsodium                             1.0.22  h280c20c_1               conda-forge     269kB
[  325.35s] #20 232.3   - libsqlite                             3.50.4  h0c1763c_0               conda-forge     933kB
[  325.35s] #20 232.3   - libuuid                               2.41.2  he9a06e4_0               conda-forge      37kB
[  325.35s] #20 232.3   + libuuid                               2.42.2  h5347b49_0               conda-forge      40kB
[  325.35s] #20 232.3   - libzlib                                1.3.1  hb9d3cd8_2               conda-forge      61kB
[  325.35s] #20 232.3   + nodejs                                26.0.0  he4ff34a_0               conda-forge      19MB
[  325.35s] #20 232.3   - openssl                                3.5.4  h26f9b46_0               conda-forge       3MB
[  325.35s] #20 232.3   + openssl                                3.6.3  h35e630c_0               conda-forge       3MB
[  325.35s] #20 232.3   + zlib                                   1.3.2  h25fd6f3_2               conda-forge      96kB
[  325.35s] #20 232.3
[  325.35s] #20 232.3   Summary:
[  325.35s] #20 232.3
[  325.35s] #20 232.3   Install: 235 packages
[  325.35s] #20 232.3   Change: 1 packages
[  325.35s] #20 232.3   Upgrade: 11 packages
[  325.35s] #20 232.3   Total download: 897MB
[  325.35s] #20 232.3
[  325.35s] #20 232.3 ──────────────────────────────────────────────────────────────────────────────────────────────────
[  325.35s] #20 232.3
[  325.35s] #20 232.3
[  328.23s] Error during build: Command '['docker', 'buildx', 'build', '--progress', 'plain', '--push', '--build-arg', 'NB_USER=jovyan', '--build-arg', 'NB_UID=1000', '--tag', 'quay.io/imagebuilding-non-gcp-hubs/jetstream2-projectpythia-pythia-binder-projectpythia-2dml-2dhurricane-2dintensity-2bb351:2f121838b7386c35a7aa374ff296cfa746bd81c7', '--platform', 'linux/amd64', '/tmp/tmpu1frekhl']' returned non-zero exit status 1.
[  328.23s] Error during build: Command '['docker', 'buildx', 'build', '--progress', 'plain', '--push', '--build-arg', 'NB_USER=jovyan', '--build-arg', 'NB_UID=1000', '--tag', 'quay.io/imagebuilding-non-gcp-hubs/jetstream2-projectpythia-pythia-binder-projectpythia-2dml-2dhurricane-2dintensity-2bb351:2f121838b7386c35a7aa374ff296cfa746bd81c7', '--platform', 'linux/amd64', '/tmp/tmpu1frekhl']' returned non-zero exit status 1.
```

