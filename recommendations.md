---
title: Recommendations
subtitle: The specific actions that would move each cookbook toward the publication criteria
---

The [live checks](reports/live.md) say *what* happens when a cookbook is built and run today.
This section says *what to do about it* — one page per cookbook, each a short, prioritised list of
concrete actions, with the actual diff for any fix that was reproduced and verified locally.

Each page is written to be the basis for a single future pull request, taken **with** the Project
Pythia community — not applied here. Consistent with the rest of this repo, nothing in these pages
has been pushed to a cookbook; the cookbook clones on this machine are used only to reproduce
failures and confirm fixes, then left untouched.

## How to read a recommendation page

Every page leads with **the one change that matters most** — the Pareto fix that gets a broken
cookbook most of the way back to working — and then lists secondary and lower-priority items below
it. Where a fix was reproduced locally, the page shows the exact diff and says so; where it could
not be fully verified (an upstream outage, a credential, a multi-gigabyte download), it is labelled
as a proposal to confirm in a real build.

:::{note} These are proposals, not verdicts
A recommendation is a hypothesis about the smallest useful change, formed from reading the repo and
reproducing its failure. It is not a review of whether the cookbook *teaches* well — that judgment
lives in the human-written [notes](https://github.com/jmunroe/pythia-cookbook-review/tree/main/notes).
Read the linked live check and the cookbook itself before opening a PR.
:::

## Priority order

Cookbooks are worked worst-first, because a broken launch button is the failure a learner hits
first:

1. **build failed** — the Binder image will not build; the launch button gives a learner nothing.
2. **execution failed** — the image builds but the run times out or the kernel dies.
3. **ran with errors** — the book builds and runs, but a cell raises.

The per-cookbook pages below are added as each cookbook is worked through. The
[live checks overview](reports/live.md) has the full outcome table.
