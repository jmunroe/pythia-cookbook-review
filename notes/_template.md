---
cookbook: <repo-name>
reviewed: YYYY-MM-DD
reviewer: <github-handle>
tier_override: # healthy | degraded | stale | incubating | abandoned | not-a-cookbook
recommendation: # adopt | hand-off | fix | retire
---

# <repo-name>

Read the **rendered book** at <https://projectpythia.org/repo-name>, not just the repo. The
automated tier in `reports/` is a hypothesis; this file is where it gets confirmed, refined, or
overridden.

The first three sections cover the community publication criteria that no script can check
(see [docs/criteria.md](../docs/criteria.md)).

## Topic & audience

*Is the topic relevant to the broad Pythia community — is there a real geoscience connection? Who
is this for, and what should they already know? Are the stated prerequisites honest?*

## Narrative & teaching quality

*Do the notebooks have reasonable narrative flow — can a reader follow the code and understand the
results? Is there enough prose around the code, or is it a script with headings? Do the figures
show what the text claims?*

## Metadata appropriateness

*Not "are the fields non-empty" — the script checks that. Are the title, description, gallery tags,
and author list actually right and useful? Would the gallery card make someone click?*

## Currency

*Is the science still sound? Is the tooling advice still current practice, or does it teach a
pattern the ecosystem has moved past? Do the data sources still exist and still return what the
notebooks expect?*

## What's broken

*Beyond the automated findings — what actually fails when you run it or read it? Copy the relevant
lines from `reports/by-tier.md` and add what they miss.*

## Effort to fix

*Rough size, and what specifically would need to happen. Note whether the fix is mechanical
(metadata, workflows, environment) or substantive (content rewrite, data source migration).*

## Recommendation

*One of:*

- **adopt** — worth taking maintainership of.
- **hand off** — worth keeping, but needs an owner who isn't us. Who?
- **fix** — a specific, bounded repair. Say exactly what. If it lands, cut a release and refresh
  the Zenodo DOI, per the community's suggestion.
- **retire** — archive it and be honest with learners rather than leaving it in the gallery.

*Remember the rule of thumb: a cookbook doesn't need to be finished, just useful. Small and
incomplete is not a reason to retire; broken, misleading, or irrelevant is.*
