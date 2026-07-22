# mrms-cookbook

Live outcome: **build failed**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/mrms-cookbook)

Run 2026-07-22 22:29:43 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [mrms-cookbook](https://github.com/ProjectPythia/mrms-cookbook) at ref [`main`](https://github.com/ProjectPythia/mrms-cookbook/tree/main).

:::{warning} Cached image
BinderHub reused an existing image, so the 9m 26s is a pod launch and image pull. It does **not** test whether `environment.yml` still solves.
:::

| Measure | Value |
|---|---|
| Live outcome | **build failed** |
| Static tier | `incubating` |
| Time to a ready session | 9m 26s (cached image) |
| Build succeeded | no |
| Resource metrics | unavailable: unknown |
| Errors raised | 0 |

Executed 5 notebook(s) from the project toc: [`notebooks/ch1_Introduction.ipynb`](https://github.com/ProjectPythia/mrms-cookbook/blob/main/notebooks/ch1_Introduction.ipynb), [`notebooks/ch2-mar-2023-tornado_jdh.ipynb`](https://github.com/ProjectPythia/mrms-cookbook/blob/main/notebooks/ch2-mar-2023-tornado_jdh.ipynb), [`notebooks/ch3_TXfloods.ipynb`](https://github.com/ProjectPythia/mrms-cookbook/blob/main/notebooks/ch3_TXfloods.ipynb), [`notebooks/ch4_bnf-mrms-qpe-hourly.ipynb`](https://github.com/ProjectPythia/mrms-cookbook/blob/main/notebooks/ch4_bnf-mrms-qpe-hourly.ipynb), [`notebooks/ch5_realtimeData.ipynb`](https://github.com/ProjectPythia/mrms-cookbook/blob/main/notebooks/ch5_realtimeData.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/mrms-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Build log (tail)

```
[    2.97s] 2026-07-22T22:29:46Z [Normal] Created container: block-nfs-access
[    3.95s] 2026-07-22T22:29:47Z [Normal] Container image "quay.io/imagebuilding-non-gcp-hubs/jetstream2-projectpythia-pythia-binder-projectpythia-2dmrms-2dcookbook-36cd92:ff5211c1b307b3d351142f59277069aa3e1fdec7" already present on machine
[    3.95s] 2026-07-22T22:29:47Z [Normal] Created container: notebook
[  119.69s] Spawn failed: Server at http://172.22.101.219:8888/user/projectpythia-mrms-cookbook-cz9qpip7/api didn't respond in 120 seconds
[  135.39s] Server requested
[  136.39s] 2026-07-22T22:32:04.042518Z [Normal] Successfully assigned binderhub/jupyter-projectpythia-mrms-cookbook-36pc6bma to binder-pythia-cluster-d7vpq4idy5va-user-m3-large-fdpj2-vz8xk
[  138.35s] 2026-07-22T22:32:05Z [Normal] Container image "quay.io/jupyterhub/k8s-network-tools:4.1.0" already present on machine
[  138.35s] 2026-07-22T22:32:05Z [Normal] Created container: block-nfs-access
[  138.35s] 2026-07-22T22:32:06Z [Normal] Started container block-nfs-access
[  139.36s] 2026-07-22T22:32:06Z [Normal] Container image "quay.io/imagebuilding-non-gcp-hubs/jetstream2-projectpythia-pythia-binder-projectpythia-2dmrms-2dcookbook-36cd92:ff5211c1b307b3d351142f59277069aa3e1fdec7" already present on machine
[  139.36s] 2026-07-22T22:32:07Z [Normal] Created container: notebook
[  139.36s] 2026-07-22T22:32:07Z [Normal] Started container notebook
[  262.27s] Server requested
[  263.20s] 2026-07-22T22:34:14.229813Z [Normal] Successfully assigned binderhub/jupyter-projectpythia-mrms-cookbook-ethafrgf to binder-pythia-cluster-d7vpq4idy5va-user-m3-large-fdpj2-vz8xk
[  263.20s] 2026-07-22T22:34:14Z [Normal] Container image "quay.io/jupyterhub/k8s-network-tools:4.3.3" already present on machine
[  263.20s] 2026-07-22T22:34:15Z [Normal] Started container block-cloud-metadata
[  266.11s] 2026-07-22T22:34:17Z [Normal] Container image "quay.io/imagebuilding-non-gcp-hubs/jetstream2-projectpythia-pythia-binder-projectpythia-2dmrms-2dcookbook-36cd92:ff5211c1b307b3d351142f59277069aa3e1fdec7" already present on machine
[  266.11s] 2026-07-22T22:34:17Z [Normal] Created container: notebook
[  266.11s] 2026-07-22T22:34:17Z [Normal] Started container notebook
[  407.50s] Spawn failed: Server at http://172.18.176.82:8888/user/projectpythia-mrms-cookbook-ethafrgf/api didn't respond in 120 seconds
[  423.33s] Server requested
[  424.27s] 2026-07-22T22:37:00.034666Z [Normal] Successfully assigned binderhub/jupyter-projectpythia-mrms-cookbook-oywbrfcp to binder-pythia-cluster-d7vpq4idy5va-user-m3-large-fdpj2-vz8xk
[  425.24s] 2026-07-22T22:37:01Z [Normal] Container image "quay.io/jupyterhub/k8s-network-tools:4.1.0" already present on machine
[  426.21s] 2026-07-22T22:37:02Z [Normal] Container image "quay.io/imagebuilding-non-gcp-hubs/jetstream2-projectpythia-pythia-binder-projectpythia-2dmrms-2dcookbook-36cd92:ff5211c1b307b3d351142f59277069aa3e1fdec7" already present on machine
[  565.85s] Spawn failed: Server at http://172.18.176.83:8888/user/projectpythia-mrms-cookbook-oywbrfcp/api didn't respond in 120 seconds
```

