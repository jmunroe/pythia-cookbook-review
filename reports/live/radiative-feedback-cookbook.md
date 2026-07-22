# radiative-feedback-cookbook

Live outcome: **build failed**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/radiative-feedback-cookbook)

Run 2026-07-22 20:43:19 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [radiative-feedback-cookbook](https://github.com/ProjectPythia/radiative-feedback-cookbook) at ref [`main`](https://github.com/ProjectPythia/radiative-feedback-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **build failed** |
| Static tier | `incubating` |
| Time to a ready session | 1m 03s (fresh build) |
| Build succeeded | no |
| Resource metrics | unavailable: unknown |
| Errors raised | 0 |

Executed 3 notebook(s) from the project toc: [`notebooks/foundations/climkern-calc.ipynb`](https://github.com/ProjectPythia/radiative-feedback-cookbook/blob/main/notebooks/foundations/climkern-calc.ipynb), [`notebooks/foundations/energy-balance-model.ipynb`](https://github.com/ProjectPythia/radiative-feedback-cookbook/blob/main/notebooks/foundations/energy-balance-model.ipynb), [`notebooks/foundations/manual-calc.ipynb`](https://github.com/ProjectPythia/radiative-feedback-cookbook/blob/main/notebooks/foundations/manual-calc.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/radiative-feedback-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Build log (tail)

```
[   56.89s] #20 40.39   - libzlib                                    1.3.1  hb9d3cd8_2               conda-forge      61kB
[   56.89s] #20 40.39   + libzlib                                    1.3.2  h25fd6f3_2               conda-forge      64kB
[   56.89s] #20 40.39   - ncurses                                      6.5  h2d0b736_3               conda-forge     892kB
[   56.89s] #20 40.39   + ncurses                                      6.6  hdb14827_0               conda-forge     919kB
[   56.89s] #20 40.39   - nodejs                                   20.19.5  hf7ee748_0               conda-forge      17MB
[   56.89s] #20 40.39   - psutil                                     7.1.0  py310h7c4b9e2_0          conda-forge     361kB
[   56.89s] #20 40.39   - python_abi                                  3.10  8_cp310                  conda-forge       7kB
[   56.89s] #20 40.39   + python_abi                                  3.14  8_cp314                  conda-forge       7kB
[   56.89s] #20 40.39   - readline                                     8.2  h8c095d6_2               conda-forge     282kB
[   56.89s] #20 40.39   + readline                                     8.3  h853b02a_0               conda-forge     345kB
[   56.89s] #20 40.39   - rpds-py                                   0.27.1  py310hd8f68c5_1          conda-forge     387kB
[   56.89s] #20 40.39   + rpds-py                                 2026.6.3  py314h1bee95f_0          conda-forge     300kB
[   56.89s] #20 40.39   - sqlalchemy                                2.0.44  py310h7c4b9e2_0          conda-forge       3MB
[   56.89s] #20 40.39   + sqlalchemy                                2.0.51  py314h0f05182_0          conda-forge       4MB
[   56.89s] #20 40.39   - tornado                                    6.5.2  py310h7c4b9e2_1          conda-forge     661kB
[   56.89s] #20 40.39   + tornado                                    6.5.7  py314h5bd0f2a_0          conda-forge     918kB
[   56.89s] #20 40.39   - zlib                                       1.3.1  hb9d3cd8_2               conda-forge      92kB
[   56.89s] #20 40.39   + zlib                                       1.3.2  h25fd6f3_2               conda-forge      96kB
[   56.89s] #20 40.39   Total download: 630MB
[   56.89s] #20 40.39
[   56.89s] #20 40.39 ──────────────────────────────────────────────────────────────────────────────────────────────────────
[   56.89s] #20 40.39
[   56.89s] #20 40.39 Confirm changes: [Y/n]
[   56.89s] #20 40.39 Transaction starting
[   63.34s] ERROR: failed to receive status: rpc error: code = Unavailable desc = error reading from server: EOF
```

