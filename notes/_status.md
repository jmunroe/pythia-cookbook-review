# Project status & handoff

Working state of the cookbook review, for picking up in a fresh session. Not published (the site
toc only includes `reports/` and `docs/`). Update this when state changes.

_Last updated: 2026-07-21._

## What this is

Assessment of every Project Pythia cookbook against the community's publication criteria
([docs/criteria.md](../docs/criteria.md)). Public repo `jmunroe/pythia-cookbook-review`, site at
<https://jmunroe.github.io/pythia-cookbook-review/>. See [README](../README.md) and
[CLAUDE.md](../CLAUDE.md) for conventions — the load-bearing ones:

- `data/` is append-only; `reports/`, `index.md`, `site` are generated (never hand-edit);
  **`notes/*.md` are hand-written by a human and must never be machine-generated.**
- Cookbook clones live as siblings (`../<name>`), never inside this repo.

## What's built and working

| Capability | Scripts | Output |
|---|---|---|
| Static audit of all org cookbooks | `audit.py` → `report.py` | `data/snapshot-*.json`, `reports/{dashboard,by-tier,gaps}.md` |
| MyST site (auto-deploys on push) | `build_site.py` + `myst.yml` | `index.md` → GitHub Pages |
| Live BinderHub build/run + memory | `live_check.py` → `report_live.py` | `data/live/*.json`, `reports/live.md` |
| Green-nightly-with-errors scan | `ci_errors.py` → `report_ci.py` | `data/ci-errors-*.json`, `reports/ci-errors.md` |
| Local ARM credential test | `arm_probe.py` | stdout only |
| Clone/refresh sibling repos | `sync-clones.sh` | `../<name>` |

Tooling needs: `gh` (authed), Python + PyYAML, and for live checks `npm i -g binderbot mystmd`
(node at `~/.nvm/versions/node/v22.22.0/bin`).

## Data collected so far (all 2026-07-21)

- **Static snapshot:** 75 cookbook repos. Tiers: 24 healthy, 4 stale, 2 degraded, 38 incubating,
  7 not-a-cookbook. (Caveat: nearly every repo shows a same-day push from an org-wide sweep, so
  `days_since_push` is currently useless and the incubating/abandoned split is unreliable — needs
  last-*human*-commit instead.)
- **Live checks (5 of 30 gallery):** HRRR-AWS + eofs ran clean; esgf **build fails** (Sphinx pins
  unsolvable); landsat-ml runs but notebooks have drifted from upstream APIs; radar runs with ARM
  credentials working (2 remaining errors are the public NEXRAD S3 bucket + a real fastbarnes bug).
- **CI-errors scan:** **12 of 30 gallery cookbooks publish a green nightly while notebooks raised**
  during that build. `myst build --execute` exits 0 on cell errors, so the workflow goes green and
  the page deploys truncated. vapor(15), kerchunk(10), ocean-bgc(7) worst. This is the biggest
  finding; it's a shared-config issue, not per-cookbook.

## Key cross-cutting findings

1. **Green nightly ≠ notebooks ran** (12/30). Candidate fix is `error_rules` in `cookbook-actions`
   / `pythia-config`; would flip much of the gallery red, so it's a community decision. See
   `reports/ci-errors.md`.
2. **33 cookbooks carry Sphinx-era packages in `environment.yml`** (13 in gallery), all depending
   on `sphinx-pythia-theme` which Pythia archived March 2026. Dead weight from the MyST migration;
   fatal for esgf (pins won't solve).
3. Pythia's own builds no longer use Binder — the binderbot steps in `cookbook-actions` are dead
   code gated behind a Sphinx-era `_config.yml`.

## What's NOT done — the actual review

**Zero human review notes written** (`notes/*.md`). This is the point of the project: the three
community criteria a script can't check — geoscience relevance, narrative flow, appropriate
metadata — plus content currency. The automated tiers are only hypotheses. Workflow in
[docs/workflow.md](../docs/workflow.md); template in [notes/_template.md](_template.md).

Also pending: only 5 of 30 gallery cookbooks live-checked; the other ~45 org repos unexamined;
history-over-time tracking is deferred (idea captured in `docs/live-assessment.md`).

## Suggested next steps

1. **Start writing per-cookbook notes**, worst-tier first: the 4 `stale` and 2 `degraded` are
   published-but-broken, so a learner is hurt now. `cp notes/_template.md notes/<name>.md`, read the
   *rendered* book, fill in judgment. `report.py` links each dashboard row to its note.
2. Optionally live-check more gallery cookbooks (`python scripts/live_check.py <name>`; add
   `--env-file ~/.config/pythia-cookbook-review/arm.env` for ARM ones).
3. Decide where cross-cutting findings (esp. the green-nightly one) get raised with the Pythia
   community — this repo assesses, it does not act upstream.

## Environment / credentials

- **ARM:** `~/.config/pythia-cookbook-review/arm.env` (mode 600) holds `ARM_USERNAME` and a valid
  ARM Live **access token** as `ARM_PASSWORD` (16-char hex; the notebooks misname it "password").
  Verify anytime with `python scripts/arm_probe.py --env-file ~/.config/pythia-cookbook-review/arm.env`.
- Not committed; `.gitignore` blocks `*.env` as a backstop.

## Side-quest: binderbot #15 (parked, awaiting maintainers)

Live checks need env vars (e.g. ARM creds) inside Binder kernels; binderbot had no way to do that.
Built `--env` on fork `jmunroe/binderbot@env-injection` (reviewed, house-style, **no PR opened**).
**Blocker:** it writes an IPython startup file under `~/.ipython/` (hidden), and mybinder.org
refuses hidden-path writes (`allow_hidden=false` default) — works on Pythia's hub, not the
reference hub. Posted findings + a terminal-API alternative to
<https://github.com/2i2c-org/binderbot/issues/15>, awaiting maintainer direction. Do not open the
PR until they respond. Our own `live_check.py` does its own injection in Python, so this side-quest
does not block the cookbook review.
