# great-circle-cookbook

Live outcome: **build failed**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/great-circle-cookbook)

Run 2026-07-22 10:13:31 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [great-circle-cookbook](https://github.com/ProjectPythia/great-circle-cookbook) at ref [`main`](https://github.com/ProjectPythia/great-circle-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **build failed** |
| Static tier | `incubating` |
| Time to a ready session | 1m 34s (fresh build) |
| Build succeeded | no |
| Resource metrics | unavailable: unknown |
| Errors raised | 0 |

Executed 8 notebook(s) from the project toc: [`notebooks/foundations/1_terminology.ipynb`](https://github.com/ProjectPythia/great-circle-cookbook/blob/main/notebooks/foundations/1_terminology.ipynb), [`notebooks/foundations/2_coordinates.ipynb`](https://github.com/ProjectPythia/great-circle-cookbook/blob/main/notebooks/foundations/2_coordinates.ipynb), [`notebooks/tutorials/1_arc_path.ipynb`](https://github.com/ProjectPythia/great-circle-cookbook/blob/main/notebooks/tutorials/1_arc_path.ipynb), [`notebooks/tutorials/2_arc_to_point.ipynb`](https://github.com/ProjectPythia/great-circle-cookbook/blob/main/notebooks/tutorials/2_arc_to_point.ipynb), [`notebooks/tutorials/3_parallels_max_min.ipynb`](https://github.com/ProjectPythia/great-circle-cookbook/blob/main/notebooks/tutorials/3_parallels_max_min.ipynb), [`notebooks/tutorials/4_path_intersection.ipynb`](https://github.com/ProjectPythia/great-circle-cookbook/blob/main/notebooks/tutorials/4_path_intersection.ipynb), [`notebooks/tutorials/5_angles.ipynb`](https://github.com/ProjectPythia/great-circle-cookbook/blob/main/notebooks/tutorials/5_angles.ipynb), [`notebooks/tutorials/6_polygon_area.ipynb`](https://github.com/ProjectPythia/great-circle-cookbook/blob/main/notebooks/tutorials/6_polygon_area.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/great-circle-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Build log (tail)

```
[   90.20s] #20 75.32   + pixman                                          0.46.4  h54a6638_2               conda-forge     376kB
[   90.20s] #20 75.32   + qhull                                           2020.2  h434a139_5               conda-forge     553kB
[   90.20s] #20 75.32   + qt6-main                                         6.9.3  h5c1c036_1               conda-forge      55MB
[   90.20s] #20 75.32   + re2                                         2025.11.05  h5301d42_0               conda-forge      27kB
[   90.20s] #20 75.32   + retrying                                         1.4.2  pyhe01879c_0             conda-forge      21kB
[   90.20s] #20 75.32   + s2n                                              1.6.0  h8399546_1               conda-forge     394kB
[   90.20s] #20 75.32   + scikit-learn                                     1.7.2  py310h228f341_0          conda-forge       8MB
[   90.20s] #20 75.32   + scipy                                           1.15.2  py310h1d65ade_0          conda-forge      16MB
[   90.20s] #20 75.32   + shapely                                          2.1.2  py310hc8bbb35_2          conda-forge     540kB
[   90.20s] #20 75.32   + snappy                                           1.2.2  h03e3b7b_1               conda-forge      46kB
[   90.20s] #20 75.32   + sortedcontainers                                 2.4.0  pyhd8ed1ab_1             conda-forge      29kB
[   90.20s] #20 75.32   + spatialpandas                                    0.5.0  pyhd8ed1ab_0             conda-forge      81kB
[   90.20s] #20 75.32   + wayland                                         1.24.0  hd6090a7_1               conda-forge     330kB
[   90.20s] #20 75.32   + xorg-libx11                                     1.8.13  he1eb515_0               conda-forge     840kB
[   90.20s] #20 75.32   + xorg-libxau                                     1.0.12  hb03c661_1               conda-forge      15kB
[   90.20s] #20 75.32   + xorg-libxcomposite                               0.4.7  hb03c661_0               conda-forge      14kB
[   90.20s] #20 75.32   + xorg-libxtst                                     1.2.5  hb9d3cd8_3               conda-forge      33kB
[   90.20s] #20 75.32   + xorg-libxxf86vm                                  1.1.7  hb03c661_0               conda-forge      19kB
[   90.20s] #20 75.32   + xyzservices                                   2026.3.0  pyhd8ed1ab_0             conda-forge      52kB
[   90.20s] #20 75.32   Summary:
[   90.20s] #20 75.32
[   90.20s] #20 75.32   Install: 236 packages
[   90.20s] #20 75.32   Upgrade: 2 packages
[   90.20s] #20 75.32
[   94.06s] ERROR: failed to receive status: rpc error: code = Unavailable desc = error reading from server: EOF
```

