# ml-hurricane-intensity

Live outcome: **build failed**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/ml-hurricane-intensity)

Run 2026-07-23 21:34:04 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [ml-hurricane-intensity](https://github.com/ProjectPythia/ml-hurricane-intensity) at ref [`main`](https://github.com/ProjectPythia/ml-hurricane-intensity/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **build failed** |
| Static tier | `incubating` |
| Time to a ready session | 4m 09s (fresh build) |
| Build succeeded | no |
| Resource metrics | unavailable: unknown |
| Errors raised | 0 |

Executed 3 notebook(s) from the project toc: [`notebooks/Model.ipynb`](https://github.com/ProjectPythia/ml-hurricane-intensity/blob/main/notebooks/Model.ipynb), [`notebooks/era5_preprocessing.ipynb`](https://github.com/ProjectPythia/ml-hurricane-intensity/blob/main/notebooks/era5_preprocessing.ipynb), [`notebooks/ibtrack_preprocessing.ipynb`](https://github.com/ProjectPythia/ml-hurricane-intensity/blob/main/notebooks/ibtrack_preprocessing.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/ml-hurricane-intensity/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Build log (tail)

```
[  235.14s] #4 sha256:76a991c6bfc1738367d1f726699924445e25d762cea07820a5069de2e0ffb806 13.58MB / 13.58MB 0.2s done
[  235.24s] #4 sha256:992bb70ed221ae6468bafbde091d782eb827cfa9afae6267256a2d2737b8619f 47.77MB / 47.77MB 0.4s done
[  235.24s] #4 sha256:13f2c3e911f50d01ad2d490a0fa0c8921ce491b3365589e1fe21c2a07de011c3 41.54MB / 185.48MB 0.5s
[  235.36s] #4 sha256:13f2c3e911f50d01ad2d490a0fa0c8921ce491b3365589e1fe21c2a07de011c3 71.71MB / 185.48MB 0.6s
[  235.60s] #4 sha256:13f2c3e911f50d01ad2d490a0fa0c8921ce491b3365589e1fe21c2a07de011c3 134.22MB / 185.48MB 0.8s
[  235.80s] #4 sha256:13f2c3e911f50d01ad2d490a0fa0c8921ce491b3365589e1fe21c2a07de011c3 185.48MB / 185.48MB 1.0s
[  236.15s] #4 extracting sha256:ca2678b20700c15185707964d9211b1a6406196114bf675f568b6025d37b3888 1.0s done
[  238.99s] #4 extracting sha256:992bb70ed221ae6468bafbde091d782eb827cfa9afae6267256a2d2737b8619f 1.9s done
[  244.13s] #4 extracting sha256:13f2c3e911f50d01ad2d490a0fa0c8921ce491b3365589e1fe21c2a07de011c3 5.1s
[  244.66s] 
[  244.77s] #5 ...
[  244.77s] #4 [ 1/19] FROM docker.io/library/buildpack-deps:24.04@sha256:cfb30ff3856780c63b00ec3ad2e4aed77ae6afce5975ebb8ad9525ec45354e2e
[  245.69s] 
[  245.69s] #5 [internal] load build context
[  245.69s] #5 transferring context: 2.24GB 10.9s done
[  245.69s] #4 [ 1/19] FROM docker.io/library/buildpack-deps:24.04@sha256:cfb30ff3856780c63b00ec3ad2e4aed77ae6afce5975ebb8ad9525ec45354e2e
[  249.34s] /home/jmunroe/.nvm/versions/node/v22.22.0/lib/node_modules/binderbot/dist/main.cjs:4283
[  249.34s]         logError(data.message.trimEnd());
[  249.34s]                               ^
[  249.34s] 
[  249.34s] TypeError: Cannot read properties of undefined (reading 'trimEnd')
[  249.34s]     at _Command.startSession (/home/jmunroe/.nvm/versions/node/v22.22.0/lib/node_modules/binderbot/dist/main.cjs:4283:31)
[  249.34s]     at process.processTicksAndRejections (node:internal/process/task_queues:105:5)
[  249.34s] 
[  249.34s] Node.js v22.22.0
```

