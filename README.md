# Project Pythia cookbook review

A workspace for assessing the overall status of every [Project Pythia][pythia] cookbook.

[pythia]: https://projectpythia.org

## Why

The ProjectPythia GitHub org holds roughly **70 cookbook repositories**. Only **30** are listed in
the [gallery][gallery]. The rest are a mix of genuine in-flight cookbooks, Cookoff leftovers, and
test repos — and nobody has a consolidated picture of which cookbooks are healthy, which are
quietly rotting, and which never finished.

The gallery's own [status page][status] tracks nightly build state for the published 30. That is a
useful signal but a narrow one: it can't see the cookbooks that never made it into the gallery, and
a green build says nothing about whether a cookbook still *teaches* anything.

This repo produces a dated, repeatable snapshot of every cookbook against Pythia's own publication
criteria, and pairs it with human review notes for the things no script can judge.

[gallery]: https://cookbooks.projectpythia.org/
[status]: https://cookbooks.projectpythia.org/status.html

## The bar we assess against

Not invented here. From the Pythia community meeting of **2026-07-21**:

> - Topic is relevant to the broad Pythia community (should have some geoscience connection)
> - Notebooks have reasonable narrative flow so the code and results are understandable
> - Notebooks run without error and cookbook publishes itself on GitHub
> - `environment.yml` is set up appropriately (favor conda-forge over pip; avoid version pins
>   except where needed, and document reasons)
> - Author metadata, gallery tags and description are all appropriate
> - Repo is archived on Zenodo with DOI
>
> **Rule of thumb: your cookbook doesn't need to be finished, just useful.**

Full text and its consequences for the assessment: [`docs/criteria.md`](docs/criteria.md).
Made checkable: [`docs/rubric.md`](docs/rubric.md).

Note that **three of those six criteria cannot be checked by a script.** Topic relevance, narrative
flow, and whether metadata is *appropriate* rather than merely *present* all require reading the
cookbook. That is what `notes/` is for.

## Quickstart

Needs `gh` (authenticated), Python 3.9+, and `PyYAML`.

```bash
python scripts/audit.py          # collect  -> data/snapshot-YYYY-MM-DD.json
python scripts/report.py         # present  -> reports/*.md
./scripts/sync-clones.sh <name>  # clone a cookbook locally for deep reading
cp notes/_template.md notes/<name>.md   # then write the review
```

Start with [`reports/by-tier.md`](reports/by-tier.md) — it groups cookbooks by health and spells
out the specific failing checks for each.

## Health tiers

Assigned automatically, overridable by hand in a note file. Ordered by how much a learner is hurt:

| Tier | Meaning |
|---|---|
| `stale` | In the gallery, but the book has stopped deploying. Published and quietly broken. |
| `degraded` | In the gallery but slipping: failing CI, lagging deploy, or missing DOI/citation metadata. |
| `abandoned` | Real content, never published, no activity in over a year. |
| `incubating` | Real content, not yet in the gallery, still active. |
| `healthy` | Working and citable. |
| `not-a-cookbook` | Scaffold, sandbox, or archived. Listed so the counts reconcile. |

Tiers never penalise a cookbook for being small or unfinished — only for being broken or invisible.

## Layout

```
docs/       criteria (the bar), rubric (made checkable), methodology (where metrics lie), workflow
scripts/    audit.py (collect), report.py (present), sync-clones.sh (fetch repos locally)
data/       dated JSON snapshots — append-only, the historical record
reports/    generated markdown — regenerated freely, never hand-edited
notes/      per-cookbook human review — hand-written, never generated
```

Cookbook clones land as **siblings** of this repo (`../radar-cookbook`), never inside it.

## Scope

This repo assesses. It does not act on upstream: no PRs, no issues filed on ProjectPythia repos, no
edits to cloned cookbooks from here. Those are separate, deliberate steps taken with the community,
informed by what this workspace finds.
