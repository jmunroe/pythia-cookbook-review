# kerchunk-cookbook — Recommendations

Live outcome: **build failed**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/kerchunk-cookbook.md) · [Repository](https://github.com/ProjectPythia/kerchunk-cookbook)

Static tier `healthy` — a build fix is very likely all this cookbook needs.

## The one change that matters

**Install `kerchunk` from conda-forge instead of pinning `git+https://github.com/fsspec/kerchunk`.**
The git pin is what breaks the build, and it points at a package that is now identical to the
released version anyway.

The build fails at the pip step:

```
Updating pip packages: git+https://github.com/carbonplan/xrefcoord.git, git+https://github.com/fsspec/kerchunk
critical libmamba pip failed to update packages
ERROR: process "... env update ... --file environment.yml ..." exit code: 1
```

### Root cause (reproduced)

Installing each git pin in turn against the build's Python:

- `git+https://github.com/carbonplan/xrefcoord.git` — installs cleanly.
- `git+https://github.com/fsspec/kerchunk` — **fails**:

  ```
  Because the current Python version (3.10.x) does not satisfy Python>=3.11
  and kerchunk==0.2.10 depends on Python>=3.11, ... your requirements are unsatisfiable.
  ```

The conda solve produced a **Python 3.10** environment (the build log links `aiohttp…py310`,
`virtualizarr-1.3.0`, and friends). Then pip tried to add `kerchunk` from `main`, whose current
`0.2.10` requires **Python ≥ 3.11**. Two-phase resolution — conda first, pip second — let the
mismatch through: nothing told conda that a later step would need 3.11.

Nothing in the conda dependencies actually *requires* 3.10; several (`virtualizarr`, and `kerchunk`
itself) want 3.11+. The env simply settled on an older, mutually-consistent generation because no
dependency pushed it forward.

### Recommended diff

`kerchunk` is on conda-forge at the same `0.2.10` as `main`, and it carries the `python >=3.11`
constraint. Moving it into the conda dependency list makes that constraint part of the *single*
conda solve, which then selects Python ≥ 3.11 and a consistent modern generation up front:

```diff
   - xarray>=2024.10.0
   - zarr
+  - kerchunk>=0.2.10
   - sphinx-pythia-theme
   - pip:
       - git+https://github.com/carbonplan/xrefcoord.git
-      - git+https://github.com/fsspec/kerchunk
   - mystmd
```

`xrefcoord` stays a git install because it is published on neither PyPI nor conda-forge; it is
pure-Python and installs fine on 3.11. `git` stays in the deps for that one install.

If the cookbook genuinely depends on unreleased kerchunk behaviour (it almost certainly does not —
`main` and the release are the same version), the alternative is to keep the git pin but add
`python>=3.11` to the conda deps so the solve targets a compatible interpreter. Moving to the
conda-forge release is the cleaner fix.

## What was verified

- **Root cause reproduced** by installing each git pin separately on Python 3.10: `xrefcoord`
  succeeds, `kerchunk` fails with the `python>=3.11` conflict quoted above.
- **The fix's mechanism is confirmed:** conda-forge `kerchunk` `0.2.10`, `0.2.9`, and `0.2.8` all
  declare `python >=3.11`, so making it a conda dependency forces the interpreter up to a version
  that satisfies it.
- **Not verified:** a full conda build of the edited file (no conda/mamba on this machine), and
  whether the newer package generation that Python 3.11+ pulls in changes any notebook output.
  Confirm with one real Binder build and a notebook execution pass.

## Secondary (lower priority, not required to build)

- **`sphinx-pythia-theme`** (a conda dependency here) is the old Sphinx doc theme. This cookbook
  builds its site with `mystmd`, so the theme is unused; drop it to shrink the image. It does not
  break the solve (`noarch`, `python >=3.9`), which is why it is secondary.
- **`mamba`** as a runtime dependency is unusual — a learner's notebook environment does not need a
  package manager inside it, and it drags in a heavy `libmamba`/`libsolv` stack. Consider removing
  it unless a notebook actually shells out to `mamba`.
- **`zarr` v2 vs v3:** `xrefcoord` expects zarr v2 while modern `kerchunk`/`virtualizarr` move
  toward v3. The conda solve pins `zarr`, so pip should not downgrade it, but watch for a zarr-major
  clash when the env is rebuilt on 3.11.

---
*Agent-assisted analysis, 2026-07-22. A proposal to confirm in a real build and open with the
community, not an applied change.*
