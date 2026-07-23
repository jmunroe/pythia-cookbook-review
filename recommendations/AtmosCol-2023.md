# AtmosCol-2023 — Recommendations

Live outcome: **build failed**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/AtmosCol-2023.md) · [Repository](https://github.com/ProjectPythia/AtmosCol-2023)

Static tier `incubating`. A single dead dependency is blocking the entire build.

## The one change that matters

**Remove the `git+https://github.com/aladinor/raw2zarr.git` pip line from `environment.yml`.** That
repository no longer exists, and no notebook actually imports the package — so one broken URL is
taking the whole cookbook down with it.

The build fails during the pip step:

```
fatal: could not read Username for 'https://github.com': terminal prompts disabled
  exit code: 128
ERROR: failed to solve: process "... env update ... --file environment.yml ..." exit code: 1
```

That "could not read Username" is GitHub's 404 in disguise: for a repository that is deleted,
renamed, or made private, an unauthenticated `https` fetch is answered as if it needed a login, so
git stops to prompt for credentials — and in a non-interactive build, prompts are disabled, so it
dies. Confirmed directly:

```
$ git ls-remote https://github.com/aladinor/raw2zarr.git
remote: Repository not found.
```

The `aladinor` account still exists; only the `raw2zarr` repo is gone. It is on neither PyPI nor
conda-forge, and the only other `raw2zarr` on GitHub (`juanbarmo10/raw2zarr`) is an unrelated 2023
fork.

### It is safe to remove — nothing runs it

Across all notebooks, `raw2zarr` appears **only in prose and one commented-out path**, never in an
executed cell:

- `notebooks/2.acceso-datos/2.2.Radares.ipynb` — a markdown sentence describing the library.
- `notebooks/3.Aplicaciones/3.5.QPE.ipynb` — a markdown bullet, plus a commented-out local
  `.../raw2zarr/zarr/Guaviare.zarr` path inside one code cell.

No cell does `import raw2zarr`. Removing the pin unblocks the build with no effect on any code that
executes.

### Recommended diff

```diff
       - xmip
       - sodapy
       - pydap
-      - git+https://github.com/aladinor/raw2zarr.git
```

## What was verified

- **Root cause confirmed:** `git ls-remote` on the pinned URL returns `Repository not found`, and
  the repo's GitHub page returns HTTP 404. This is exactly the failure the build log shows.
- **Safe to drop:** a scan of every notebook's code cells finds no `import raw2zarr` — the only
  code-cell reference is a commented-out path.
- **The remaining pip pins resolve:** `icechunk`, `arraylake`, `xmip`, `sodapy`, and `pydap` are all
  live on PyPI.
- **Not verified:** a full conda build (no conda/mamba here). The change deletes one unused,
  unreachable dependency, so the risk is minimal; confirm with one Binder build.

## Secondary (lower priority, not required to build)

- **Content gap.** `2.2.Radares.ipynb` tells learners they will read RAWDSX2 radar data "using the
  `raw2zarr` library," but that library is neither installed nor used. Either restore a working
  source for it (ask the author where `raw2zarr` moved) and add a real worked example, or soften the
  narrative so it does not promise a tool the cookbook cannot run. This is a teaching-quality
  question for human review, not a build blocker.
- **Hard pins to document or float.** `icechunk==1.1.10` (PyPI latest 2.1.1) and `arraylake==0.25`
  (PyPI latest 1.2.0) are exact pins on fast-moving storage libraries. Pinning is defensible here —
  their APIs change often — but the [criteria](../docs/criteria.md) ask for a documented reason. Add
  a one-line comment saying why each is held, or float and re-pin only if a notebook breaks.
- **Prefer conda-forge over pip.** `xmip`, `sodapy`, and `pydap` are available on conda-forge; moving
  them out of the `pip:` block aligns with the publication criteria and shrinks the pip layer.

---
*Agent-assisted analysis, 2026-07-22. A proposal to confirm in a real build and open with the
community, not an applied change.*
