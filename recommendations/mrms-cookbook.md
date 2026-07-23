# mrms-cookbook — Recommendations

Live outcome: **build failed** (spawn timeout). [← All recommendations](../recommendations.md) · [Live check](../reports/live/mrms-cookbook.md) · [Repository](https://github.com/ProjectPythia/mrms-cookbook)

Static tier `incubating`. **This was a server-spawn timeout on a cached image, not a build error — most likely transient.**

## What this failure actually is

The image was already built and cached (`Container image … already present on machine`); the failure
was the notebook **server not responding within 120 seconds** of the pod starting, twice:

```
Spawn failed: Server at http://…:8888/user/projectpythia-mrms-cookbook-…/api didn't respond in 120 seconds
```

That is a launch/startup timeout on shared BinderHub capacity, not a dependency or image-build
problem. The environment itself is fine — `mamba env create --dry-run` resolves it cleanly (431
packages, 116 MB, no conflict).

**First action: re-run the live check.** A spawn timeout on shared infrastructure is the textbook
case for a retry.

## The one durable cleanup: drop `conda` from the runtime env

`environment.yml` lists `conda` **twice** (lines 18 and 20), which pulls the entire package-manager
stack — `conda`, `conda-libmamba-solver`, `libmamba`, `libmambapy` — *into the learner's runtime
environment*:

```diff
   - cartopy
   - numpy
   - s3fs
   - fsspec
   - cfgrib
   - matplotlib
-  - conda
   - ipykernel
-  - conda
   - ipywidgets
```

A cookbook environment does not need a package manager inside it — no notebook imports `conda` or
shells out to it (confirmed by scanning all 6 notebooks). Removing both lines slims the image, which
can only help a slow spawn, and eliminates a confusing duplicate. This is the clearest concrete
improvement; it will not by itself have caused the timeout, but a leaner image starts faster.

## What was verified

- **Env solves cleanly** with `mamba` (431 packages, 116 MB, no conflict) — the image build is not
  the problem.
- **`conda` is listed twice** (lines 18, 20) and **no notebook uses it** (import scan of all 6
  notebooks).
- **Not verified:** the spawn timeout itself, which depends on live BinderHub scheduling and cannot
  be reproduced locally. The evidence (cached image + server-response timeout) points to transient
  infrastructure.

## Secondary

- The `pyviz` channel is listed but the dependencies all resolve from conda-forge; confirm it is
  still needed, and drop it if not, to keep the solve simple.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm by re-running the live check, not an
applied change.*
