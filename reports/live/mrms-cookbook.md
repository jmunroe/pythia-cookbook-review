# mrms-cookbook

Live outcome: **build failed**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/mrms-cookbook)

Run 2026-07-23 04:21:57 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [mrms-cookbook](https://github.com/ProjectPythia/mrms-cookbook) at ref [`main`](https://github.com/ProjectPythia/mrms-cookbook/tree/main).

:::{warning} Cached image
BinderHub reused an existing image, so the 10m 45s is a pod launch and image pull. It does **not** test whether `environment.yml` still solves.
:::

| Measure | Value |
|---|---|
| Live outcome | **build failed** |
| Static tier | `incubating` |
| Time to a ready session | 10m 45s (cached image) |
| Build succeeded | no |
| Resource metrics | unavailable: unknown |
| Errors raised | 0 |

Executed 5 notebook(s) from the project toc: [`notebooks/ch1_Introduction.ipynb`](https://github.com/ProjectPythia/mrms-cookbook/blob/main/notebooks/ch1_Introduction.ipynb), [`notebooks/ch2-mar-2023-tornado_jdh.ipynb`](https://github.com/ProjectPythia/mrms-cookbook/blob/main/notebooks/ch2-mar-2023-tornado_jdh.ipynb), [`notebooks/ch3_TXfloods.ipynb`](https://github.com/ProjectPythia/mrms-cookbook/blob/main/notebooks/ch3_TXfloods.ipynb), [`notebooks/ch4_bnf-mrms-qpe-hourly.ipynb`](https://github.com/ProjectPythia/mrms-cookbook/blob/main/notebooks/ch4_bnf-mrms-qpe-hourly.ipynb), [`notebooks/ch5_realtimeData.ipynb`](https://github.com/ProjectPythia/mrms-cookbook/blob/main/notebooks/ch5_realtimeData.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/mrms-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Build log (tail)

```
[  224.99s] 2026-07-23T04:25:45.935280Z [Normal] Successfully assigned binderhub/jupyter-projectpythia-mrms-cookbook-9mku46d1 to binder-pythia-cluster-d7vpq4idy5va-user-m3-large-fdpj2-vx2q7
[  224.99s] 2026-07-23T04:25:46Z [Normal] Container image "quay.io/jupyterhub/k8s-network-tools:4.3.3" already present on machine
[  226.00s] 2026-07-23T04:25:47Z [Normal] Container image "quay.io/jupyterhub/k8s-network-tools:4.1.0" already present on machine
[  227.01s] 2026-07-23T04:25:48Z [Normal] Container image "quay.io/imagebuilding-non-gcp-hubs/jetstream2-projectpythia-pythia-binder-projectpythia-2dmrms-2dcookbook-36cd92:ff5211c1b307b3d351142f59277069aa3e1fdec7" already present on machine
[  227.01s] 2026-07-23T04:25:48Z [Normal] Started container notebook
[  368.38s] Spawn failed: Server at http://172.23.47.212:8888/user/projectpythia-mrms-cookbook-9mku46d1/api didn't respond in 120 seconds
[  376.40s] Server requested
[  377.35s] 2026-07-23T04:28:21.534754Z [Normal] Successfully assigned binderhub/jupyter-projectpythia-mrms-cookbook-reiwv6v8 to binder-pythia-cluster-d7vpq4idy5va-user-m3-large-fdpj2-vx2q7
[  377.35s] 2026-07-23T04:28:22Z [Normal] Container image "quay.io/jupyterhub/k8s-network-tools:4.3.3" already present on machine
[  377.35s] 2026-07-23T04:28:22Z [Normal] Created container: block-cloud-metadata
[  377.35s] 2026-07-23T04:28:22Z [Normal] Started container block-cloud-metadata
[  379.31s] 2026-07-23T04:28:23Z [Normal] Started container block-nfs-access
[  379.31s] 2026-07-23T04:28:24Z [Normal] Container image "quay.io/imagebuilding-non-gcp-hubs/jetstream2-projectpythia-pythia-binder-projectpythia-2dmrms-2dcookbook-36cd92:ff5211c1b307b3d351142f59277069aa3e1fdec7" already present on machine
[  380.29s] 2026-07-23T04:28:24Z [Normal] Created container: notebook
[  380.29s] 2026-07-23T04:28:24Z [Normal] Started container notebook
[  503.16s] Spawn failed: Server at http://172.23.47.213:8888/user/projectpythia-mrms-cookbook-reiwv6v8/api didn't respond in 120 seconds
[  503.16s] Launch attempt 3 failed, retrying...
[  518.42s] 2026-07-23T04:30:45.371171Z [Normal] Successfully assigned binderhub/jupyter-projectpythia-mrms-cookbook-xid4lfn9 to binder-pythia-cluster-d7vpq4idy5va-user-m3-large-fdpj2-vx2q7
[  518.42s] 2026-07-23T04:30:45Z [Normal] Container image "quay.io/jupyterhub/k8s-network-tools:4.3.3" already present on machine
[  518.42s] 2026-07-23T04:30:46Z [Normal] Started container block-cloud-metadata
[  519.40s] 2026-07-23T04:30:46Z [Normal] Container image "quay.io/jupyterhub/k8s-network-tools:4.1.0" already present on machine
[  519.40s] 2026-07-23T04:30:46Z [Normal] Started container block-nfs-access
[  520.38s] 2026-07-23T04:30:47Z [Normal] Created container: notebook
[  520.38s] 2026-07-23T04:30:47Z [Normal] Started container notebook
[  645.24s] Spawn failed: Server at http://172.23.47.214:8888/user/projectpythia-mrms-cookbook-xid4lfn9/api didn't respond in 120 seconds
```

