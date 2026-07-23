# mrms-cookbook — Recommendations

Live outcome: **build failed** (server never started). [← All recommendations](../recommendations.md) · [Live check](../reports/live/mrms-cookbook.md) · [Repository](https://github.com/ProjectPythia/mrms-cookbook)

Static tier `incubating`. **A live re-check proved this is *not* transient — the notebook server reproducibly fails to start.**

## What the re-check changed

The original run failed at the server-spawn step, which looked like it might be a one-off. I re-ran
the live check on [binder.projectpythia.org](https://binder.projectpythia.org) on 2026-07-23 to find
out. It failed the same way — **and worse: every spawn attempt failed**, across two independent
live checks and multiple retries:

```
Started container notebook
Spawn failed: Server at http://…:8888/user/projectpythia-mrms-cookbook-…/api didn't respond in 120 seconds
Launch attempt 1 failed, retrying...
Spawn failed: … didn't respond in 120 seconds
```

The image is **cached and builds fine**; the pod schedules and the notebook *container starts*. What
fails, every time, is the **Jupyter server inside it becoming responsive within 120 seconds**. That
is a reproducible startup problem in the image, not shared-hub flakiness. So "re-run it" — my first
guess — is wrong: it needs a fix.

## The most likely cause, and the first thing to try

A server that starts but never answers within two minutes usually means a **server extension
hanging or an over-heavy image loading slowly on startup**. The strongest concrete lead is the
environment itself:

- **`conda` is listed twice** in `environment.yml` (lines 18 and 20), dragging the entire
  package-manager stack (`conda`, `conda-libmamba-solver`, `libmamba`, `libmambapy`) into the
  learner's runtime image. A cookbook environment should never contain a package manager — it
  bloats the image and can register startup hooks that slow the server.

```diff
   - matplotlib
-  - conda
   - ipykernel
-  - conda
   - ipywidgets
```

Remove both, then rebuild. If the server still stalls, audit the server extensions the env installs
(`jupyter_bokeh`, `geoviews`/`jupyter-server-proxy` if present) by launching with
`jupyter server --debug` and watching which extension blocks.

## The definitive next diagnostic

The one thing this live check *cannot* see is the server's own startup log inside the pod — which
records exactly what the server was doing when it failed to answer. The maintainers can get it by
launching the cookbook on the hub and reading the pod log (or `jupyter server` output locally in the
built image). That log will name the blocking step directly; the `conda`-removal above is the most
likely fix in the meantime.

## What was verified

- **The spawn failure is reproducible** — all attempts across two live checks (2026-07-22 and
  2026-07-23) failed with "Server … didn't respond in 120 seconds"; the image is cached and builds
  successfully. Recorded in `data/live/mrms-cookbook-2026-07-23T043255Z.json`.
- **`conda` appears twice** in `environment.yml`; the env otherwise solves cleanly (431 packages).
- **No notebook uses `conda`** (scanned all 6).
- **Not verified:** the exact blocking step at server startup (needs the pod's server log), and
  whether removing `conda` alone fixes it. It is the highest-probability first fix.

---
*Agent-assisted analysis, updated 2026-07-23 after a live re-check (supersedes the earlier
"transient, re-run" note). A proposal to confirm with the community, not an applied change.*
