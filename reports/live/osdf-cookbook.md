# osdf-cookbook

Live outcome: **build failed**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/osdf-cookbook)

Run 2026-07-22 23:29:07 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [osdf-cookbook](https://github.com/ProjectPythia/osdf-cookbook) at ref [`main`](https://github.com/ProjectPythia/osdf-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **build failed** |
| Static tier | `healthy` |
| Time to a ready session | 1m 44s (fresh build) |
| Build succeeded | no |
| Resource metrics | unavailable: unknown |
| Errors raised | 0 |

Executed 15 notebook(s) from the project toc: [`notebooks/01_osdf_intro.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/01_osdf_intro.ipynb), [`notebooks/01_pelicanfs.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/01_pelicanfs.ipynb), [`notebooks/02_cesm2_oceanheat.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/02_cesm2_oceanheat.ipynb), [`notebooks/02_cmip6_gmst.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/02_cmip6_gmst.ipynb), [`notebooks/02_ncar_intro.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/02_ncar_intro.ipynb), [`notebooks/03_EnviStor_Foundations.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/03_EnviStor_Foundations.ipynb), [`notebooks/03_EnviStor_Technical.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/03_EnviStor_Technical.ipynb), [`notebooks/04_SonarAI_Foundations.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/04_SonarAI_Foundations.ipynb), [`notebooks/04_SonarAI_Technical.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/04_SonarAI_Technical.ipynb), [`notebooks/05_PyCoGSS_Foundations.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/05_PyCoGSS_Foundations.ipynb), [`notebooks/05_PyCoGSS_SpectralChange_PFS.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/05_PyCoGSS_SpectralChange_PFS.ipynb), [`notebooks/06_atmosphere_llc2160_visualization.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/06_atmosphere_llc2160_visualization.ipynb), [`notebooks/06_introduction_to_NSDF_OpenVISUS.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/06_introduction_to_NSDF_OpenVISUS.ipynb), [`notebooks/06_ocean_llc2160_visualization.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/06_ocean_llc2160_visualization.ipynb), [`notebooks/06_ocean_llc4320_visualization.ipynb`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/notebooks/06_ocean_llc4320_visualization.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/osdf-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Build log (tail)

```
[  101.80s] #20 52.64 Linking fasteners-0.20-pyhd8ed1ab_0
[  101.80s] #20 52.65 Linking narwhals-2.24.0-pyhcf101f3_0
[  101.80s] #20 52.66 Linking cachetools-5.5.2-pyhd8ed1ab_0
[  101.80s] #20 52.66 Linking markdown-3.10.2-pyhcf101f3_0
[  101.80s] #20 52.67 Linking param-2.4.1-pyhc455866_0
[  101.80s] #20 52.68 Linking uc-micro-py-2.0.0-pyhcf101f3_0
[  101.90s] #20 52.74 Linking scitokens-1.9.7-pyhcf101f3_0
[  101.90s] #20 52.76 Linking zict-3.0.0-pyhd8ed1ab_1
[  101.90s] #20 52.77 Linking jmespath-1.1.0-pyhcf101f3_1
[  101.90s] #20 52.77 Linking filetype-1.2.0-pyhd8ed1ab_0
[  101.90s] #20 52.83 Linking et_xmlfile-2.0.0-pyhd8ed1ab_1
[  102.50s] #20 52.84 Linking pyshp-2.3.1-pyhd8ed1ab_1
[  102.72s] #20 53.45 Linking python-multipart-0.0.32-pyhcf101f3_0
[  102.72s] #20 53.49 Linking cattrs-26.1.0-pyhcf101f3_1
[  102.75s] #20 53.50 Linking font-ttf-source-code-pro-2.038-h77eed37_0
[  102.75s] #20 53.53 Linking plotly-6.9.0-pyhd8ed1ab_0
[  102.91s] #20 53.87 Linking folium-0.20.0-pyhd8ed1ab_0
[  103.30s] #20 53.89 Linking partd-1.4.2-pyhd8ed1ab_0
[  103.30s] #20 53.89 Linking botocore-1.43.53-pyhd8ed1ab_0
[  103.56s] #20 54.44 Linking snuggs-1.4.7-pyhd8ed1ab_2
[  103.73s] #20 54.54 Linking boto3-1.43.53-pyhd8ed1ab_0
[  103.73s] #20 54.55 Linking python-fasthtml-0.14.9-pyhc364b38_0
[  104.00s] ERROR: failed to receive status: rpc error: code = Unavailable desc = error reading from server: EOF
[  104.04s] Error during build: Command '['docker', 'buildx', 'build', '--progress', 'plain', '--push', '--build-arg', 'NB_USER=jovyan', '--build-arg', 'NB_UID=1000', '--tag', 'quay.io/imagebuilding-non-gcp-hubs/jetstream2-projectpythia-pythia-binder-projectpythia-2dosdf-2dcookbook-252aff:3130487ab6e3ede78eebfb6a04f0fb4a9af7a253', '--platform', 'linux/amd64', '/tmp/tmpedwgpdi4']' returned non-zero exit status 1.
[  104.04s] Error during build: Command '['docker', 'buildx', 'build', '--progress', 'plain', '--push', '--build-arg', 'NB_USER=jovyan', '--build-arg', 'NB_UID=1000', '--tag', 'quay.io/imagebuilding-non-gcp-hubs/jetstream2-projectpythia-pythia-binder-projectpythia-2dosdf-2dcookbook-252aff:3130487ab6e3ede78eebfb6a04f0fb4a9af7a253', '--platform', 'linux/amd64', '/tmp/tmpedwgpdi4']' returned non-zero exit status 1.
```

