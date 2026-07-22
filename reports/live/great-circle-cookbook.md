# great-circle-cookbook

Live outcome: **ran with errors**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/great-circle-cookbook)

Run 2026-07-22 22:40:11 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [great-circle-cookbook](https://github.com/ProjectPythia/great-circle-cookbook) at ref [`main`](https://github.com/ProjectPythia/great-circle-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **ran with errors** |
| Static tier | `incubating` |
| Time to a ready session | 14m 50s (fresh build) |
| Build succeeded | yes |
| Notebook execution | 31.37s |
| Build command exit code | 0 (zero despite cell errors) |
| Notebooks ran clean | no |
| Execution cache | **reused — timing is not execution** |
| Peak memory (pss) | 1.12 GB |
| Pod memory limit | 8.59 GB |
| Peak as share of limit | 13.0% |
| Peak rss (upper bound, shared pages double-counted) | 1.60 GB |
| Errors raised | 1 |

| Notebook | Execute + render |
|---|---|
| [`notebooks/foundations/1_terminology.ipynb`](https://github.com/ProjectPythia/great-circle-cookbook/blob/main/notebooks/foundations/1_terminology.ipynb) | 4.71s |
| [`notebooks/tutorials/4_path_intersection.ipynb`](https://github.com/ProjectPythia/great-circle-cookbook/blob/main/notebooks/tutorials/4_path_intersection.ipynb) | 5.42s |
| [`notebooks/tutorials/1_arc_path.ipynb`](https://github.com/ProjectPythia/great-circle-cookbook/blob/main/notebooks/tutorials/1_arc_path.ipynb) | 6.17s |
| [`notebooks/tutorials/5_angles.ipynb`](https://github.com/ProjectPythia/great-circle-cookbook/blob/main/notebooks/tutorials/5_angles.ipynb) | 6.77s |
| [`notebooks/tutorials/3_parallels_max_min.ipynb`](https://github.com/ProjectPythia/great-circle-cookbook/blob/main/notebooks/tutorials/3_parallels_max_min.ipynb) | 8.39s |
| [`notebooks/foundations/2_coordinates.ipynb`](https://github.com/ProjectPythia/great-circle-cookbook/blob/main/notebooks/foundations/2_coordinates.ipynb) | 8.97s |
| [`notebooks/tutorials/6_polygon_area.ipynb`](https://github.com/ProjectPythia/great-circle-cookbook/blob/main/notebooks/tutorials/6_polygon_area.ipynb) | 10s |
| [`notebooks/tutorials/2_arc_to_point.ipynb`](https://github.com/ProjectPythia/great-circle-cookbook/blob/main/notebooks/tutorials/2_arc_to_point.ipynb) | 16s |

Executed 8 notebook(s) from the project toc: [`notebooks/foundations/1_terminology.ipynb`](https://github.com/ProjectPythia/great-circle-cookbook/blob/main/notebooks/foundations/1_terminology.ipynb), [`notebooks/foundations/2_coordinates.ipynb`](https://github.com/ProjectPythia/great-circle-cookbook/blob/main/notebooks/foundations/2_coordinates.ipynb), [`notebooks/tutorials/1_arc_path.ipynb`](https://github.com/ProjectPythia/great-circle-cookbook/blob/main/notebooks/tutorials/1_arc_path.ipynb), [`notebooks/tutorials/2_arc_to_point.ipynb`](https://github.com/ProjectPythia/great-circle-cookbook/blob/main/notebooks/tutorials/2_arc_to_point.ipynb), [`notebooks/tutorials/3_parallels_max_min.ipynb`](https://github.com/ProjectPythia/great-circle-cookbook/blob/main/notebooks/tutorials/3_parallels_max_min.ipynb), [`notebooks/tutorials/4_path_intersection.ipynb`](https://github.com/ProjectPythia/great-circle-cookbook/blob/main/notebooks/tutorials/4_path_intersection.ipynb), [`notebooks/tutorials/5_angles.ipynb`](https://github.com/ProjectPythia/great-circle-cookbook/blob/main/notebooks/tutorials/5_angles.ipynb), [`notebooks/tutorials/6_polygon_area.ipynb`](https://github.com/ProjectPythia/great-circle-cookbook/blob/main/notebooks/tutorials/6_polygon_area.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/great-circle-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Errors

**`SyntaxError`** — f-string: unmatched '[' (3216377505.py, line 1)

in `site/content/notebooks.tutorials.arc-path.json`

```
  Cell In[4], line 1
    print(f"Boulder latitude: {location_df.loc["boulder", "latitude"]}")
                                                ^
SyntaxError: f-string: unmatched '['

```

