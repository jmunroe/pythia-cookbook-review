# esgf-cookbook — Recommendations

Live outcome: **build failed**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/esgf-cookbook.md) · [Repository](https://github.com/ProjectPythia/esgf-cookbook)

Static tier `stale` — the published book has also stopped deploying, and for the same reason: the environment no longer solves.

## The one change that matters

**Delete the legacy `sphinx-pythia-theme` pin block from `environment.yml`.** It is the sole cause
of the build failure, and it is dead weight — the cookbook builds its site with `mystmd`, not
Sphinx.

The build fails at the pip step, not the conda solve:

```
Updating pip packages: sphinx-pythia-theme, sphinx==4.5.0, sphinxcontrib-applehelp<1.0.7,
  ... docutils==0.16, git+https://github.com/esgf2-us/intake-esgf
critical libmamba pip failed to update packages
ERROR: process "... ${MAMBA_EXE} env update ... --file environment.yml ..." exit code: 1
```

That pip block dates from when Pythia cookbooks were rendered with Sphinx. This one no longer is:
the repo has a `myst.yml` and **no `conf.py` and no `_config.yml`**, and `grep -ri sphinx` across
its config finds nothing outside `environment.yml`. The site is built by `mystmd` (already a conda
dependency). The pins `sphinx==4.5.0`, `docutils==0.16`, and `pydata-sphinx-theme<=0.8` exist only
to satisfy `sphinx-pythia-theme 2022.3.22`, and forcing those downgrades on top of the modern
`jupyter-book`/`mystmd`/`docutils` that conda has already installed is what makes pip fail.

None of these packages is imported by any notebook — they are doc-build tooling for a build system
this cookbook abandoned.

### Recommended diff

`intake-esgf` — the one genuinely needed pip line — is now published on **conda-forge** (2026.6.4),
so it moves up into the conda dependencies and the entire `pip:` block disappears:

```diff
   - ipywidgets
-  - pip
-  - pip:
-      - sphinx-pythia-theme
-      # The balance of this environment file pins several libraries in order for
-      # to satisfy dependencies for the sphinx-pythia-theme 2022.3.22 package.
-      - sphinx==4.5.0
-      - sphinxcontrib-applehelp<1.0.7
-      - sphinxcontrib-devhelp<1.0.5
-      - sphinxcontrib-htmlhelp<2.0.4
-      - sphinxcontrib-qthelp<1.0.6
-      - sphinxcontrib-serializinghtml<1.1.9
-      - pydata-sphinx-theme<=0.8
-      - docutils==0.16
-      - git+https://github.com/esgf2-us/intake-esgf
+  - intake-esgf
   - mystmd
```

This also removes the `git+https://…` install, which is slower and more fragile than a released
package (it rebuilds from `main` on every image build and breaks whenever `main` does).

If keeping `intake-esgf` on the development tip is deliberate, the minimal alternative is to keep
only that one line under `pip:` and delete everything above it:

```yaml
  - pip
  - pip:
      - git+https://github.com/esgf2-us/intake-esgf
```

## What was verified

- **Root cause reproduced.** The failing step is the pip update, per the build log. Resolving the
  legacy block against Python 3.11 pulls `sphinx==4.5.0` + `docutils==0.16` + `pydata-sphinx-theme
  0.8.0` + `sphinx-book-theme 0.3.3` — a 2022-era stack that conflicts with the conda-installed
  `mystmd`/`jupyter-book` in the same prefix.
- **The replacement exists.** `intake-esgf` resolves on both PyPI and conda-forge at 2026.6.4;
  `git+https://github.com/esgf2-us/intake-esgf` is still reachable (`git ls-remote` succeeds), so
  neither the current nor the proposed pin is a dead link.
- **Not verified:** a full conda build of the edited `environment.yml` (no conda/mamba on this
  machine). The change is confined to removing an unused, self-conflicting doc-build stack, so the
  risk is low, but confirm with one real Binder build before merging.

## Secondary (lower priority, not required to build)

- **`xesmf==0.8.2`** is a hard pin with no documented reason — a pinning "smell" under the
  [criteria](../docs/criteria.md). Try floating it to `xesmf` (or `xesmf>=0.8`) and pin again only
  if a solve or a notebook actually breaks; if it must stay pinned, add a one-line comment saying
  why.
- **`jupyter-book`** in the conda deps is very likely also unused now that the site is built with
  `mystmd`. Confirm nothing references it, then drop it to shrink the image.
- **`copyright: '2023'`** in `myst.yml` is stale; refresh when the PR lands.

---
*Agent-assisted analysis, 2026-07-22. A proposal to confirm in a real build and open with the
community, not an applied change.*
