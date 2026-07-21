# Cross-cutting gaps

Generated from `snapshot-2026-07-21.json` (collected 2026-07-21). Do not edit — regenerate with `python scripts/report.py`.

Denominators exclude the `not-a-cookbook` tier (7 of 75 repos).

| Finding | Count | Of |
|---|---|---|
| Gallery cookbooks without a Zenodo DOI | 1 | 30 |
| Gallery cookbooks with no tagged release | 0 | 30 |
| Gallery cookbooks not deploying (>30d) | 4 | 30 |
| Cookbooks with a failing or absent nightly build | 17 | 68 |
| Cookbooks with undocumented version pins | 31 | 68 |
| Cookbooks pulling deps from pip | 23 | 68 |
| Cookbooks with no environment.yml | 0 | 68 |
| Repos still carrying Sphinx config | 5 | 68 |
| Cookbooks with Sphinx packages in environment.yml | 32 | 68 |
| Repos still linking to cookbook-template | 18 | 68 |
| Cookbooks with no author ORCID | 7 | 68 |

## Gallery cookbooks without a Zenodo DOI — 1/30

The DOI is the last step of the publication checklist, and the community lists it as a basic criterion. Missing means the flow was never finished.

## Gallery cookbooks not deploying (>30d) — 4/30

Published and quietly broken — the worst learner experience in the collection.

## Cookbooks with a failing or absent nightly build — 17/68

Some are legitimately unable to run in CI (credentials, data volume). Those need a documented exemption, not a red mark.

## Cookbooks with undocumented version pins — 31/68

The community asks authors to avoid pins except where needed, and to document why. Pins without explanation are the finding.

## Cookbooks pulling deps from pip — 23/68

conda-forge is preferred wherever possible; pip is a flag for human review, not an automatic failure.

## Repos still carrying Sphinx config — 5/68

`_config.yml`/`_toc.yml` means the MyST migration never reached this cookbook.

## Cookbooks with Sphinx packages in environment.yml — 32/68

Cookbooks build with MyST now, so a Sphinx toolchain in the environment is dead weight from before the migration. It is rarely harmless: these entries are usually tightly pinned, and a live check found they can stop the Binder image building at all — see the live report.

## Repos still linking to cookbook-template — 18/68

`trigger-replace-links` was never run — links point at the template, not the book.

## Cookbooks with no author ORCID — 7/68

Author metadata is a basic publication criterion; ORCIDs make credit resolvable.

