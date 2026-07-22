# osdf-cookbook

Live outcome: **build failed**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/osdf-cookbook)

Run 2026-07-22 07:19:35 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [osdf-cookbook](https://github.com/ProjectPythia/osdf-cookbook) at ref [`main`](https://github.com/ProjectPythia/osdf-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **build failed** |
| Static tier | `healthy` |
| Time to a ready session | 1m 49s (fresh build) |
| Build succeeded | no |
| Resource metrics | unavailable: unknown |
| Errors raised | 0 |

Executed 15 notebook(s) from the project toc: [`notebooks/01_osdf_intro.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/01_osdf_intro.ipynb), [`notebooks/01_pelicanfs.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/01_pelicanfs.ipynb), [`notebooks/02_cesm2_oceanheat.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/02_cesm2_oceanheat.ipynb), [`notebooks/02_cmip6_gmst.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/02_cmip6_gmst.ipynb), [`notebooks/02_ncar_intro.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/02_ncar_intro.ipynb), [`notebooks/03_EnviStor_Foundations.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/03_EnviStor_Foundations.ipynb), [`notebooks/03_EnviStor_Technical.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/03_EnviStor_Technical.ipynb), [`notebooks/04_SonarAI_Foundations.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/04_SonarAI_Foundations.ipynb), [`notebooks/04_SonarAI_Technical.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/04_SonarAI_Technical.ipynb), [`notebooks/05_PyCoGSS_Foundations.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/05_PyCoGSS_Foundations.ipynb), [`notebooks/05_PyCoGSS_SpectralChange_PFS.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/05_PyCoGSS_SpectralChange_PFS.ipynb), [`notebooks/06_atmosphere_llc2160_visualization.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/06_atmosphere_llc2160_visualization.ipynb), [`notebooks/06_introduction_to_NSDF_OpenVISUS.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/06_introduction_to_NSDF_OpenVISUS.ipynb), [`notebooks/06_ocean_llc2160_visualization.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/06_ocean_llc2160_visualization.ipynb), [`notebooks/06_ocean_llc4320_visualization.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/06_ocean_llc4320_visualization.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Build log (tail)

```
[  106.53s] #20 43.74   + xorg-libxrender                       0.9.12  hb9d3cd8_0               conda-forge      33kB
[  106.53s] #20 43.74   + xorg-libxtst                           1.2.5  hb9d3cd8_3               conda-forge      33kB
[  106.53s] #20 43.74   + xorg-libxxf86vm                        1.1.7  hb03c661_0               conda-forge      19kB
[  106.53s] #20 43.74   + xyzservices                         2026.3.0  pyhd8ed1ab_0             conda-forge      52kB
[  106.53s] #20 43.74   + yarl                                  1.24.5  py312h8a5da7c_0          conda-forge     171kB
[  106.53s] #20 43.74   + zarr                                  2.18.1  pyhd8ed1ab_0             conda-forge     160kB
[  106.53s] #20 43.74   + zict                                   3.0.0  pyhd8ed1ab_1             conda-forge      36kB
[  106.53s] #20 43.74   + zlib-ng                                2.3.3  hceb46e0_1               conda-forge     123kB
[  106.53s] #20 43.74
[  106.53s] #20 43.74   Upgrade:
[  106.53s] #20 43.74 ──────────────────────────────────────────────────────────────────────────────────────────────────
[  106.53s] #20 43.74
[  106.53s] #20 43.74   - libsqlite                             3.50.4  h0c1763c_0               conda-forge     933kB
[  106.53s] #20 43.74   + libsqlite                             3.53.3  h0c1763c_0               conda-forge     962kB
[  106.53s] #20 43.74   - libzlib                                1.3.1  hb9d3cd8_2               conda-forge      61kB
[  106.53s] #20 43.74   + libzlib                                1.3.2  h25fd6f3_2               conda-forge      64kB
[  106.53s] #20 43.74   - zlib                                   1.3.1  hb9d3cd8_2               conda-forge      92kB
[  106.53s] #20 43.74   + zlib                                   1.3.2  h25fd6f3_2               conda-forge      96kB
[  106.53s] #20 43.74
[  106.53s] #20 43.74   Downgrade:
[  106.53s] #20 43.74 ──────────────────────────────────────────────────────────────────────────────────────────────────
[  106.53s] #20 43.74
[  106.53s] #20 43.74   - pytz                                  2025.2  pyhd8ed1ab_0             conda-forge     189kB
[  106.53s] #20 43.74   + pytz                                  2024.1  pyhd8ed1ab_0             conda-forge     189kB
[  108.67s] ERROR: failed to receive status: rpc error: code = Unavailable desc = error reading from server: EOF
```

