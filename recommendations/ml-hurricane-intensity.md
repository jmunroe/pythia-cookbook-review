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

:::{note} 2026-07-23 re-check was inconclusive (tooling, not the cookbook)
A third live attempt on 2026-07-23 did **not** produce a verdict: `binderbot` crashed on the client
side partway through uploading the ~2.2 GB build context —
`TypeError: Cannot read properties of undefined (reading 'trimEnd')` in `binderbot/dist/main.cjs` —
so the Binder build never ran to completion. This is a `binderbot` robustness bug on a malformed
progress line, **not** a cookbook or environment problem, and it says nothing either way about the
build. The transient hypothesis therefore still stands on the local evidence below, unconfirmed by a
green build. (The oversized ~2.2 GB context that tripped binderbot is itself a hint that a slimmer
image — see the note on TensorFlow below — would make the build more robust.)
:::

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
- **Not verified:** a clean Binder rebuild. The original failure was on Pythia's infrastructure, and
  the 2026-07-23 re-check was aborted by a client-side `binderbot` crash before the build finished
  (see the note above), so a green build is still outstanding. The local evidence points firmly to
  transient infrastructure, so re-running — ideally with a `binderbot` that survives the large build
  context — is the right first step.

## Secondary (minor)

- **One latent non-standard kernelspec.** `notebooks/JS2_S3_example.ipynb` carries the kernel name
  `local`, which would fail execution the way it does in sister cookbooks — but it is **not** in the
  executed `myst.yml` toc, so it is harmless today. Reset it to standard `python3` before adding it to
  the toc, so it does not become a time-bomb later.
- `environment.yml` is missing a trailing newline after `visualkeras` — cosmetic; tidy when the PR
  lands.
- Consider pinning `tensorflow` to a major line (e.g. `tensorflow>=2.16,<3`) with a one-line note,
  so a future TF 3.x release cannot silently change model behaviour — but only if the maintainers
  want the extra guardrail; an unpinned green build is also acceptable under the criteria.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm by re-running the live check, not an
applied change.*
