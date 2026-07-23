# geostationary-cookbook — Recommendations

Live outcome: **ran with errors**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/geostationary-cookbook.md) · [Repository](https://github.com/ProjectPythia/geostationary-cookbook)

Static tier `incubating`. **The book builds and runs; the true-color composites fail because satpy/pyspectral's Rayleigh-correction LUTs are never provisioned and the lazy download from Zenodo is unreliable.**

## The one change that matters: pre-download the pyspectral LUTs at build time

An earlier live check failed with a Zenodo `504 Gateway Time-out` fetching the pyspectral correction
LUTs. A fresh re-check on **2026-07-23** got past that (the 504 was transient) and revealed the real,
recurring problem in three notebooks:

```
FileNotFoundError: [Errno 2] No such file or directory:
'/home/jovyan/.local/share/pyspectral/rayleigh_only/pyspectral_rayleigh_correction_luts.tgz'
```

The notebooks load satpy `true_color` / `natural_color` composites, which apply Rayleigh correction via
**pyspectral**. pyspectral downloads its correction LUTs from Zenodo *lazily, on first use*, into
`~/.local/share/pyspectral/` — and that download is unreliable inside the Binder build (a 504 one run,
a missing/partial file the next). Because the LUT is never present, every true-color composite fails.

The fix is to **provision the LUTs deterministically at build time** with a `binder/postBuild` script,
so they are baked into the image and runtime never depends on Zenodo:

```bash
#!/bin/bash
# binder/postBuild
set -e
python -c "from pyspectral.utils import download_luts, download_rsr; download_luts(); download_rsr()"
```

This is the canonical way to run satpy/pyspectral in CI. (An early notebook cell calling
`download_luts()` would also work but repeats the fragile download on every run; the postBuild bakes
it in once.)

## What was verified

- **The re-check confirmed the earlier failure was transient** (Zenodo 504 → now past it), and
  surfaced the underlying LUT-provisioning problem in three notebooks (`geosat-abi-goes-east`,
  `geosat-ahi-himawari`, `geosat-ami-gk2a`); build cached, executed clean otherwise (peak 2.6 GB).
- **The failing composites are `true_color`/`natural_color`** (satpy `.load([...])`), which invoke
  pyspectral Rayleigh correction; `satpy` is in `environment.yml` (pyspectral comes transitively).
- **There is no `postBuild`/`binder/` provisioning** in the repo, so the LUTs are only ever fetched
  lazily at runtime.
- **Not verified:** that the postBuild fully populates the exact LUT the composites request in one call
  (pyspectral downloads per aerosol type; `download_luts()` with no args fetches all). A live re-check
  with the postBuild added would confirm end-to-end.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with a live re-run and the community, not an applied change.*
