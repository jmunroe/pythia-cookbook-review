# snow-observations-cookbook

Live outcome: **build failed**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/snow-observations-cookbook)

Run 2026-07-22 07:31:54 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [snow-observations-cookbook](https://github.com/ProjectPythia/snow-observations-cookbook) at ref [`main`](https://github.com/ProjectPythia/snow-observations-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **build failed** |
| Static tier | `healthy` |
| Time to a ready session | 1m 03s (fresh build) |
| Build succeeded | no |
| Resource metrics | unavailable: unknown |
| Errors raised | 0 |

Executed 10 notebook(s) from the project toc: [`notebooks/GPR-lidar-tutorial.ipynb`](https://github.com/ProjectPythia/snow-observations-cookbook/blob/main/notebooks/GPR-lidar-tutorial.ipynb), [`notebooks/aviris-ng-tutorial.ipynb`](https://github.com/ProjectPythia/snow-observations-cookbook/blob/main/notebooks/aviris-ng-tutorial.ipynb), [`notebooks/microstructure-tutorial.ipynb`](https://github.com/ProjectPythia/snow-observations-cookbook/blob/main/notebooks/microstructure-tutorial.ipynb), [`notebooks/snotel_data_access.ipynb`](https://github.com/ProjectPythia/snow-observations-cookbook/blob/main/notebooks/snotel_data_access.ipynb), [`notebooks/snowex_data_overview.ipynb`](https://github.com/ProjectPythia/snow-observations-cookbook/blob/main/notebooks/snowex_data_overview.ipynb), [`notebooks/snowexsql-database.ipynb`](https://github.com/ProjectPythia/snow-observations-cookbook/blob/main/notebooks/snowexsql-database.ipynb), [`notebooks/thermal-ir-tutorial.ipynb`](https://github.com/ProjectPythia/snow-observations-cookbook/blob/main/notebooks/thermal-ir-tutorial.ipynb), [`notebooks/timelapse-camera-tutorial.ipynb`](https://github.com/ProjectPythia/snow-observations-cookbook/blob/main/notebooks/timelapse-camera-tutorial.ipynb), [`notebooks/tls_data_access.ipynb`](https://github.com/ProjectPythia/snow-observations-cookbook/blob/main/notebooks/tls_data_access.ipynb), [`notebooks/uavsar-tutorial.ipynb`](https://github.com/ProjectPythia/snow-observations-cookbook/blob/main/notebooks/uavsar-tutorial.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/snow-observations-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Build log (tail)

```
[    1.02s] Waiting for build to start...
[    2.71s] Unknown phase "undefined" from builder
[    2.71s] Cloning into '/tmp/repo2dockerkmyv87bq'...
[   49.83s] Python version unspecified, using current default Python version 3.10. This will change in the future.
[   49.83s] Unknown phase "undefined" from builder
[   49.83s] Unknown phase "undefined" from builder
[   49.83s] Using CondaBuildPack builder
[   55.07s] #1 transferring dockerfile: 5.78kB done
[   55.07s] #1 DONE 0.1s
[   55.07s] 
[   55.07s] #2 [internal] load metadata for docker.io/library/buildpack-deps:24.04
[   55.35s] 
[   55.35s] #3 [internal] load .dockerignore
[   55.35s] #3 transferring context: 2B done
[   55.35s] #4 [ 1/19] FROM docker.io/library/buildpack-deps:24.04@sha256:cfb30ff3856780c63b00ec3ad2e4aed77ae6afce5975ebb8ad9525ec45354e2e
[   55.35s] #5 [internal] load build context
[   62.59s] ERROR: failed to receive status: rpc error: code = Unavailable desc = error reading from server: EOF
```

