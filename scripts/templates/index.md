---
title: Project Pythia Cookbook Review
subtitle: A repeatable status assessment of every Project Pythia cookbook
---

{{GENERATED_NOTE}}

:::{note} Snapshot {{DATE}}
{{TOTAL}} cookbook repositories in the ProjectPythia organization, {{GALLERY}} of them published in
the [cookbook gallery](https://cookbooks.projectpythia.org/). Regenerated from
`{{SNAPSHOT}}`.

This is an independent assessment by [James Munroe](https://github.com/jmunroe), not an official
Project Pythia product.
:::

## Why this exists

The ProjectPythia GitHub organization holds **{{TOTAL}} cookbook repositories**. Only
**{{GALLERY}}** are listed in the gallery. The rest are a mix of genuine in-flight cookbooks,
Cookoff leftovers, and test repositories.

The gallery's own [status page](https://cookbooks.projectpythia.org/status) tracks nightly build
health for the published set — a useful signal, but a narrow one. It cannot see the cookbooks that
never reached the gallery, and a green build says nothing about whether a cookbook still *teaches*
anything.

This project produces a dated, repeatable snapshot of every cookbook, and pairs it with human
review notes for the things no script can judge.

## The bar

Not invented here. From the Project Pythia community meeting of **21 July 2026**, the basic
criteria for publication on the gallery:

- Topic is relevant to the broad Pythia community (should have some geoscience connection)
- Notebooks have reasonable narrative flow so the code and results are understandable
- Notebooks run without error and the cookbook publishes itself on GitHub
- `environment.yml` is set up appropriately — favor conda-forge over pip wherever possible; avoid
  version pins except where needed, and document reasons
- Author metadata, gallery tags and description are all appropriate
- Repo is archived on Zenodo with a DOI

:::{important} Rule of thumb
Your cookbook doesn't need to be finished, just useful.
:::

Three of those criteria — topic relevance, narrative flow, and whether metadata is *appropriate*
rather than merely present — cannot be checked by a script. They require reading the cookbook, and
that human judgment is the point of the exercise. See [](docs/criteria.md) for the full text and
what it changes about the assessment.

## Current state

::::{grid} 2 2 4 4

:::{card} {{TOTAL}}
cookbook repos
:::

:::{card} {{GALLERY}}
in the gallery
:::

:::{card} {{NEEDS_ATTENTION}}
published & slipping
:::

:::{card} {{REVIEWED}}
human reviews written
:::

::::

{{TIER_TABLE}}

Tiers are assigned automatically from objective checks and are best read as *hypotheses* — a human
review can confirm or override any of them. Critically, **no tier penalises a cookbook for being
small or unfinished**; only for being broken or invisible. Full definitions in [](docs/rubric.md).

## Where the collection stands

{{GAP_TABLE}}

The detail behind each of these, cookbook by cookbook, is in [](reports/gaps.md).

## Live checks

The numbers above come from reading configuration and CI state. A separate,
[live assessment](docs/live-assessment.md) actually builds a cookbook on
[Project Pythia's BinderHub](https://binder.projectpythia.org) — the environment its launch button
sends learners to — and records how long it takes, what errors it raises, and how much memory it
needs.

This matters because Pythia's own builds no longer touch Binder: the binderbot steps in
`cookbook-actions` are gated behind a Sphinx-era `_config.yml` that MyST cookbooks no longer have,
so notebooks execute on a GitHub runner instead. Nothing else measures what a cookbook costs to
run until a learner's kernel dies.

{{LIVE_SUMMARY}}

:::{danger} A passing badge does not mean the notebooks ran
Chasing a discrepancy the live checks turned up, we read Project Pythia's own nightly logs:
**{{CI_AFFECTED}} of {{CI_SCANNED}} gallery cookbooks** had notebooks raise an exception during
their most recent nightly — and the build reported success anyway, because
`myst build --execute` exits 0 when a cell fails. Everything after the failing cell is skipped,
so the published page is silently truncated.

[The full list and what to do about it](reports/ci-errors.md)
:::

Results and method: [](reports/live.md) · [](docs/live-assessment.md)

## Read the findings

::::{grid} 1 1 3 3

:::{card} Cookbooks by tier
:link: reports/by-tier.md
Grouped by health, with the specific failing checks for each cookbook.
:::

:::{card} Full dashboard
:link: reports/dashboard.md
Every cookbook, one row each.
:::

:::{card} Cross-cutting gaps
:link: reports/gaps.md
Patterns spanning the whole collection.
:::

::::

## How it works

`scripts/audit.py` collects facts about every cookbook repository — build status, deploy freshness,
citation metadata, environment configuration — into a dated JSON snapshot. Snapshots are
append-only and committed, so the collection's health can be compared over time. Everything else,
including this page, is derived from them.

The [methodology](docs/methodology.md) documents where each metric comes from and, more usefully,
where it lies: a disabled workflow serves a passing badge forever, `pushedAt` counts bot commits as
activity, and a green nightly means only that the notebooks executed without raising.

The [workflow](docs/workflow.md) describes the review loop, and why per-cookbook notes are written
by a human and never generated.

:::{caution} This project assesses; it does not act
No pull requests or issues are filed on ProjectPythia repositories from this workflow. Findings are
intended to inform work done *with* the Project Pythia community.
:::

## Project Pythia

- [Project Pythia](https://projectpythia.org) — the community education hub for geoscientific Python
- [Cookbook Gallery](https://cookbooks.projectpythia.org/) — the published cookbooks
- [Pythia Foundations](https://foundations.projectpythia.org/) — the core learning materials
- [Cookbook Guide](https://projectpythia.org/cookbook-guide) — how to write and publish a cookbook
- [Cookbook Template](https://github.com/ProjectPythia/cookbook-template) — the canonical repo shape
- [ProjectPythia on GitHub](https://github.com/ProjectPythia) — every repository assessed here
