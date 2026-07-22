# mpas-jedi-cookbook

Live outcome: **build failed**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/mpas-jedi-cookbook)

Run 2026-07-22 06:10:47 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [mpas-jedi-cookbook](https://github.com/ProjectPythia/mpas-jedi-cookbook) at ref [`main`](https://github.com/ProjectPythia/mpas-jedi-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **build failed** |
| Static tier | `healthy` |
| Time to a ready session | 2m 45s (fresh build) |
| Build succeeded | no |
| Resource metrics | unavailable: unknown |
| Errors raised | 0 |

Executed 7 notebook(s) from the project toc: [`notebooks/jedi-mpas.ipynb`](https://github.com/ProjectPythia/mpas-jedi-cookbook/blob/main/notebooks/jedi-mpas.ipynb), [`notebooks/jedi-obsSpace.ipynb`](https://github.com/ProjectPythia/mpas-jedi-cookbook/blob/main/notebooks/jedi-obsSpace.ipynb), [`notebooks/mpas-advanced.ipynb`](https://github.com/ProjectPythia/mpas-jedi-cookbook/blob/main/notebooks/mpas-advanced.ipynb), [`notebooks/mpas-basic.ipynb`](https://github.com/ProjectPythia/mpas-jedi-cookbook/blob/main/notebooks/mpas-basic.ipynb), [`notebooks/overview-jedi.ipynb`](https://github.com/ProjectPythia/mpas-jedi-cookbook/blob/main/notebooks/overview-jedi.ipynb), [`notebooks/overview-mpas.ipynb`](https://github.com/ProjectPythia/mpas-jedi-cookbook/blob/main/notebooks/overview-mpas.ipynb), [`notebooks/overview-rrfsv2.ipynb`](https://github.com/ProjectPythia/mpas-jedi-cookbook/blob/main/notebooks/overview-rrfsv2.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/mpas-jedi-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Build log (tail)

```
[  154.75s] #20 42.81   + openssl                                    3.6.3  h35e630c_0               conda-forge       3MB
[  154.75s] #20 42.81   - python                                   3.11.14  hfe2f287_1_cpython       conda-forge      31MB
[  154.75s] #20 42.81   + python                                   3.11.15  h7508c33_1_cpython       conda-forge      31MB
[  154.75s] #20 42.81   - readline                                     8.2  h8c095d6_2               conda-forge     282kB
[  154.75s] #20 42.81   + readline                                     8.3  h853b02a_0               conda-forge     345kB
[  154.75s] #20 42.81   - zlib                                       1.3.1  hb9d3cd8_2               conda-forge      92kB
[  154.75s] #20 42.81   + zlib                                       1.3.2  h25fd6f3_2               conda-forge      96kB
[  154.75s] #20 42.81
[  154.75s] #20 42.81   Summary:
[  154.75s] #20 42.81
[  154.75s] #20 42.81   Install: 283 packages
[  154.75s] #20 42.81   Change: 1 packages
[  154.75s] #20 42.81   Reinstall: 116 packages
[  154.75s] #20 42.81   Upgrade: 17 packages
[  162.76s] #20 51.19 Unlinking liblzma-5.8.1-hb9d3cd8_2
[  163.52s] #20 52.10 Unlinking libexpat-2.7.1-hecca717_0
[  163.63s] #20 52.11 Unlinking libuuid-2.41.2-he9a06e4_0
[  163.63s] #20 52.11 Unlinking openssl-3.5.4-h26f9b46_0
[  163.63s] #20 52.15 Unlinking icu-75.1-he02047a_0
[  163.63s] #20 52.22 Unlinking libsodium-1.0.20-h4ab18f5_0
[  163.83s] #20 52.23 Unlinking zlib-1.3.1-hb9d3cd8_2
[  163.83s] #20 52.23 Unlinking readline-8.2-h8c095d6_2
[  164.08s] #20 52.67 Unlinking zeromq-4.3.5-h387f397_9
[  164.76s] Error during build: Command '['docker', 'buildx', 'build', '--progress', 'plain', '--push', '--build-arg', 'NB_USER=jovyan', '--build-arg', 'NB_UID=1000', '--tag', 'quay.io/imagebuilding-non-gcp-hubs/jetstream2-projectpythia-pythia-binder-projectpythia-2dmpas-2djedi-2dcookbook-e4fd66:887c7a95a571b30d9a894033f1b385006425a2ec', '--platform', 'linux/amd64', '/tmp/tmpn26es4bp']' returned non-zero exit status 1.
[  164.76s] Error during build: Command '['docker', 'buildx', 'build', '--progress', 'plain', '--push', '--build-arg', 'NB_USER=jovyan', '--build-arg', 'NB_UID=1000', '--tag', 'quay.io/imagebuilding-non-gcp-hubs/jetstream2-projectpythia-pythia-binder-projectpythia-2dmpas-2djedi-2dcookbook-e4fd66:887c7a95a571b30d9a894033f1b385006425a2ec', '--platform', 'linux/amd64', '/tmp/tmpn26es4bp']' returned non-zero exit status 1.
```

