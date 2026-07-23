# ml-hurricane-intensity — Recommendations

Live outcome: **build failed**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/ml-hurricane-intensity.md) · [Repository](https://github.com/ProjectPythia/ml-hurricane-intensity)

Static tier `incubating`. **The environment builds cleanly locally — this failure was transient.**

## The one thing to do: re-run

The build log shows the conda solve **succeeding** — it printed the full transaction plan (`Install:
235 packages … Total download: 897MB`) — and then failed abruptly with the generic
`docker buildx … exit status 1`, no dependency error. That is the signature of a transient failure
part way through pulling ~900 MB of packages (TensorFlow dominates the download), not a broken
environment.

Reproduced locally with `mamba`:

- `mamba env create` on the current `environment.yml` **completes with exit code 0** — the full
  conda solve, download, and link all succeed.
- The `pip:` block (`visualkeras`, `global-land-mask`) installs cleanly (`aggdraw`, `pillow`,
  `numpy` pulled as wheels — no compilation failure).

So nothing in the repo is wrong. **Action: re-run the live check**; it should succeed. Only a
second failure at the same point would indicate a real problem.

## The environment is appropriate as-is

Unlike some ML cookbooks that carry an unused TensorFlow stack, here every heavy dependency is
actually used. Import scan of the 5 notebooks:

| Package | Notebooks importing it |
|---|---|
| `tensorflow` | 2 |
| `keras` | 2 |
| `visualkeras` | 1 |
| `global_land_mask` | 3 |
| `scikit-learn` | 2 |
| `seaborn` | 2 |

No trimming is warranted — TensorFlow earns its place. The ~900 MB image is inherent to a deep-
learning cookbook.

## What was verified

- **Current env builds locally:** `mamba env create` exits 0 (conda solve + download + link all
  succeed).
- **Pip block installs:** `visualkeras` and `global-land-mask` resolve and install from PyPI with
  prebuilt wheels.
- **Every heavy dependency is used** by at least one notebook.
- **Not verified:** a clean Binder rebuild (the failure was on Pythia's infrastructure). The local
  evidence points firmly to transient infrastructure, so re-running is the right first step.

## Secondary (minor)

- `environment.yml` is missing a trailing newline after `visualkeras` — cosmetic; tidy when the PR
  lands.
- Consider pinning `tensorflow` to a major line (e.g. `tensorflow>=2.16,<3`) with a one-line note,
  so a future TF 3.x release cannot silently change model behaviour — but only if the maintainers
  want the extra guardrail; an unpinned green build is also acceptable under the criteria.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm by re-running the live check, not an
applied change.*
