# Live assessment

The [static audit](./methodology.md) reads configuration and CI state. The live check asks a
different question: **does this cookbook actually run today, in the environment its launch button
sends learners to, and what does it cost to run?**

## Why this is not redundant with Pythia's CI

Project Pythia's cookbook builds no longer touch Binder. `cookbook-actions`'
[`build-book.yaml`][buildbook] still contains binderbot steps, but every one of them is gated on the
existence of a Sphinx-era `_config.yml` with `execute.execute_notebooks == 'binder'`. Since the MyST
migration cookbooks ship `myst.yml` and no `_config.yml`, so that branch is dead for all but the
handful of repos our snapshot finds still carrying Sphinx config. Those steps also still install
`pangeo-gallery/binderbot`, an implementation last touched in 2022 that
[2i2c's binderbot][binderbot] has replaced.

The live default is `myst build --execute --html` on a GitHub runner under micromamba, with a
30-minute timeout. That is a fine correctness check, but it means:

- nothing tests the cookbook in the **Binder image learners actually launch**;
- nothing measures **resource cost** at all, so "this cookbook needs 6 GB" is invisible until a
  learner's kernel dies.

[buildbook]: https://github.com/ProjectPythia/cookbook-actions/blob/main/.github/workflows/build-book.yaml
[binderbot]: https://2i2c.org/binderbot/

## How it works

`scripts/live_check.py` drives four steps:

```
binderbot start        → a live Jupyter session on the hub, and build timing
GET /api/metrics/v1    → memory sampled while the notebooks run
myst build --execute   → the same command Pythia's own build uses
binderbot stop         → release the pod (always, even on failure)
```

[BinderBot][binderbot] is a small Node CLI over `@jupyterhub/binderhub-client`. `binderbot start`
streams the BinderHub build log and prints `{"url": …, "token": …}` when the session is ready;
`myst build --execute` picks those up from `JUPYTER_BASE_URL` / `JUPYTER_TOKEN` and runs the
notebooks on the remote pod instead of locally.

We drive the **CLI** rather than the `2i2c-org/binderbot` GitHub Action deliberately: the action
starts the session for you, which would hide the build-phase timing that is one of the things we
are trying to measure.

Memory works without any cooperation from the cookbook, because repo2docker ships
[`jupyter-resource-usage`][jru] in its base conda environment. Every Binder image therefore serves
an authenticated `/api/metrics/v1` reporting `rss` summed across the server and all its children —
including the kernel doing the work — plus `limits.memory.rss`, the pod's `MEM_LIMIT`. So we get
**peak against limit**, not just an absolute number.

[jru]: https://github.com/jupyter-server/jupyter-resource-usage

## What is recorded

| Field | Meaning |
|---|---|
| `build.seconds` | Wall time from invocation to a ready session |
| `build.image_cached` | **Read this before any duration.** See below |
| `build.failed`, `build.log` | Build outcome and the timestamped BinderHub log |
| `execution.seconds`, `execution.exit_code` | The `myst build --execute` run |
| `errors[]` | Per-cell `ename` / `evalue` / traceback, read from MyST's built JSON |
| `resources.peak_rss_bytes` | Peak sampled memory |
| `resources.memory_limit_bytes` | The pod's limit |
| `resources.peak_fraction_of_limit` | How close it came to being killed |
| `resources.peak_cpu_percent`, `cpu_count` | Only when the hub enables CPU tracking |
| `toc_notebooks` | The notebooks MyST actually executed |

Results land in `data/live/<cookbook>-<date>.json`, alongside the static snapshots and under the
same append-only rule.

## What the first sample found

The pilot deliberately mixed cookbooks the static checks called healthy with ones they called
stale, to see whether a live run adds anything. It did — and it fed a finding back into the static
audit.

`esgf-cookbook` was the first cookbook to get a **fresh** image build rather than a cached one, so
its `environment.yml` was genuinely exercised for the first time. It failed after ~7 minutes:
`pip failed to update packages`, resolving `sphinx==4.5.0`, `pydata-sphinx-theme<=0.8`,
`docutils==0.16` and five pinned `sphinxcontrib-*` entries. Those are **Sphinx-era dependencies
that the MyST migration should have removed** — the cookbook builds with MyST now and needs none of
them. Their pins are what make the environment unsolvable, so the Binder image cannot build at all.

That is the community's "avoid version pins except where needed" rule failing in the most concrete
way available: a learner clicking the launch button gets nothing.

Generalising it turned up something larger. The static audit now checks for Sphinx-era packages in
`environment.yml`, and **33 cookbooks carry them — 13 of those in the gallery**. All 33 depend on
[`sphinx-pythia-theme`][theme], **a repository Project Pythia archived in March 2026**. Most carry
only that one entry and still build; `esgf-cookbook` and `xbatcher-ML-1-cookbook` carry the whole
nine-package Sphinx stack, and both are in the `stale` tier.

This is the pattern worth reporting upstream: the MyST migration moved the build, but left the old
toolchain behind in the environment, where it is at best dead weight and at worst fatal.

[theme]: https://github.com/ProjectPythia/sphinx-pythia-theme

## `myst build --execute` exits 0 when cells raise

`radar-cookbook` executed with **five cell errors and an exit code of 0**. The build command does
not fail because a notebook raised; the error is recorded in the page output and the build carries
on to render it.

That matters beyond this project, because `myst build --execute --html` is exactly the default
build command in Pythia's `cookbook-actions`. A cookbook whose notebooks throw can therefore show a
**green nightly**, since the workflow checks the command's exit status. MyST does have configurable
`error_rules`, so a project can choose to fail on execution errors — but nothing in the shared
cookbook configuration appears to set that.

**Confirmed, and it is widespread.** `scripts/ci_errors.py` reads each gallery cookbook's own
nightly log from the Actions API — Pythia's real CI, so there is no Binder-versus-runner confound —
and looks for MyST's `⛔️ … An exception occurred during code execution` marker. On 2026-07-21,
**12 of the 30 gallery cookbooks had notebooks raise in a run that reported success**, every one of
them published as passing. `vapor-python-cookbook` had all 15. Full list in
[the report](../reports/ci-errors.md).

So "the nightly is green" is a much weaker guarantee than the [static rubric](./rubric.md) assumed,
and this is a finding about the shared build configuration rather than about any one cookbook.

Concretely: never report a live run's health from the exit code alone. The report shows the exit
code and a separate *notebooks ran clean* row for this reason.

## Credentialed cookbooks

Some cookbooks read credentials that Pythia's CI supplies as repository secrets and a Binder
session does not have. `radar-cookbook` is the example: three of its notebooks call
`os.getenv("ARM_USERNAME")` / `ARM_PASSWORD` and die on `len(None)` without them.

Exporting the variables before running the check does nothing, because the notebooks execute **on
the Binder pod**, not here. BinderBot's own test suite documents this — it asserts
`"CI" not in os.environ` for exactly this reason.

So `live_check.py` seeds them into the session:

```bash
python scripts/live_check.py radar-cookbook --env ARM_USERNAME --env ARM_PASSWORD
python scripts/live_check.py radar-cookbook --env-file ~/.config/pythia-cookbook-review/arm.env
```

It works by uploading an IPython startup script
(`~/.ipython/profile_default/startup/00-live-check-env.py`) through the Jupyter contents API in the
window between the session becoming ready and MyST starting its first kernel. IPython runs
everything in that directory at kernel startup, so every kernel inherits the variables.

**Secrets discipline.** `--env` takes variable *names* and reads values from this process — never
from the command line, which is visible in `ps` and echoed into CI logs. Only the **names** are
written to `data/live/*.json` and only names are logged; values never touch the repository. Keep
any `--env-file` outside the repo (`.gitignore` blocks `*.env` as a backstop, not as permission).
The uploaded file lives on a single-user pod that is destroyed when the session stops.

Two limits: it only reaches **Python** kernels, and it depends on the hub allowing writes to hidden
paths (`ContentsManager.allow_hidden` defaults to `False`; Pythia's hub permits it). A refused
upload is reported loudly rather than swallowed, because silently skipping it reproduces the
baffling `len(None)` failure this exists to fix.

This capability existed in the old `pangeo-gallery/binderbot` as `--pass-env-var` and was lost in
2i2c's rewrite, which delegates execution to MyST. Filed upstream as
[2i2c-org/binderbot#15](https://github.com/2i2c-org/binderbot/issues/15), with an offer to
contribute the implementation — the ordering it depends on is something only BinderBot can own.

## What is kept, and what is not

The measurements are the result. The things the build produced are not.

- **Nothing is retained on the hub.** `binderbot stop` destroys the pod, in a `finally`, so a
  crash or a Ctrl-C cannot strand one.
- **Committed to this repo:** only `data/live/<cookbook>-<date>.json` — timings, resource samples,
  error details, and the timestamped BinderHub log text. No notebooks, no rendered HTML, no
  images. **Never a session token**; those records are public.
- **Left on your disk:** `myst build` writes a few hundred MB into `../<cookbook>/_build`
  (executed outputs, rendered HTML, site JSON, MyST themes). It is gitignored by the cookbook, so
  it is never committed anywhere — but it is real disk.

On a **successful** run the script deletes that output, keeping only `_build/templates` (~130 MB
of MyST theme that would otherwise be re-downloaded every run and has no bearing on execution). On
a **failed** run it is kept so you can inspect what went wrong, and the record's
`build_artifacts` field says where it is and how large. `--keep-build` keeps it either way.

## Limitations

These decide whether a number means anything. Read them before quoting one.

**A cached image makes build time meaningless.** If BinderHub already holds an image for that
repo and ref, the "build" is a pod launch of a few seconds and tests *nothing* about whether
`environment.yml` still solves. Only a fresh build exercises the environment. `image_cached` is
recorded next to every duration for exactly this reason, and a cached run must never be read as
"the environment is fine". To force a real environment test, run against a ref whose
`environment.yml` has changed.

**`myst build --execute` only runs notebooks in the toc.** A repo can carry notebooks no build ever
touches. The pilot is a live example: `HRRR-AWS-cookbook` has two notebooks in the repo but
`myst.yml` lists only `notebooks/example-workflows/plot-2mt.ipynb`. Report notebooks *executed*,
never notebooks *present*.

**Sampled memory is a floor, not a true peak.** A three-second poll can miss a short allocation
spike, and the figures cover the server plus every child process, not just the notebook's kernel.

**Compare `pss` to the limit, not `rss`.** `rss` is summed over every process, so pages shared
between the server and its kernels are counted once each. `radar-cookbook` read **12.2 GB of `rss`
against an 8.6 GB pod limit it never actually breached**; its `pss` — which apportions shared
pages — was 3.0 GB, or 35% of the limit. The report headlines `pss` where the endpoint provides it,
labels which basis it used, and shows `rss` only as an upper bound. A "memory" number above 100% of
a hard cgroup limit is a measurement artefact, not a finding.

**Errors are per-cell, and MyST writes each page twice.** Its AST is emitted under both
`_build/site/content` and `_build/html`, so a naive walk counts every error twice — radar's five
errors first read as ten. The collector reads the canonical copy and de-duplicates.

**A missing credential looks like a cookbook defect.** Some cookbooks need secrets that
`cookbook-actions` injects and this check does not: `radar-cookbook` produced `PermissionError:
Forbidden` and `Access Denied` reaching ARM data, because we have no `ARM_USERNAME` /
`ARM_PASSWORD`. That is an environment gap on our side, not a broken cookbook. Check the secrets
list in [`build-book.yaml`][buildbook] before calling a credential error a finding.

**Hitting the memory limit looks like an execution error, not a resource metric.** The kernel is
killed, so expect a dead-kernel failure rather than a clean out-of-memory signal.

**A red run may be an upstream outage.** These cookbooks read remote data — the pilot pulls HRRR
from S3. One failure is a prompt to re-run, not a finding about the cookbook. Confirm before
writing it into a note.

**CPU and disk are usually absent.** `track_cpu_percent` and `track_disk_usage` default to off in
`jupyter-resource-usage`, so those fields are recorded when the hub provides them and omitted
otherwise, rather than reported as zero.

## Resource etiquette

Runs happen on [`binder.projectpythia.org`][hub], Project Pythia's BinderHub on NSF-funded
Jetstream2 capacity. That is an appropriate use of the resource, and it is still shared capacity
that exists for learners.

The design keeps each run deliberate:

- **manual only** — a local command or a `workflow_dispatch` trigger; never a schedule;
- **one cookbook per invocation** — no gallery-wide sweeps;
- **guaranteed shutdown** — `binderbot stop` runs in a `finally`, so an exception or an interrupt
  never strands a pod.

Please do not add a cron trigger to the live-check workflow.

[hub]: https://binder.projectpythia.org

## Idea: tracking a cookbook over time

Not built yet, noted so it is not lost. `data/live/` is already dated, append-only, one file per
run per cookbook — the substrate for a history exists. What is undecided is where the *series*
should live and how it should be presented: repeated JSON records are fine for a handful of runs
and awkward for hundreds.

The questions worth answering before building it: which fields are worth trending (execution
seconds and peak memory, almost certainly; build seconds only for fresh builds, since cached ones
are noise), how to keep comparisons honest across changing hub hardware and image contents, and
whether the series belongs in this repo at all versus something built for time series. Decide that
before accumulating a lot of data in a shape that turns out to be wrong.

## Relationship to tiering

Live results **do not feed the automatic tiers** in `reports/`. A live check is a point-in-time
sample of a network-dependent workflow, and one bad sample is not evidence of a broken cookbook.
Live findings belong in the per-cookbook note, where a human can weigh them.
