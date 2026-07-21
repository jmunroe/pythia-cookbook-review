# Publication criteria (Pythia community meeting, 2026-07-21)

The community's own statement of the bar for publishing a cookbook on the gallery. This is the
**authoritative** list — [`rubric.md`](./rubric.md) exists to make it checkable, and where the two
disagree, this file wins.

> **Basic criteria for publication on the gallery:**
>
> - Topic is relevant to the broad Pythia community (should have some geoscience connection)
> - Notebooks have reasonable narrative flow so the code and results are understandable
> - Notebooks run without error and cookbook publishes itself on GitHub
> - `environment.yml` is set up appropriately
>   - Favor conda-forge over pip wherever possible
>   - Avoid version pins except where needed, and document reasons
> - Author metadata, gallery tags and description are all appropriate
> - Repo is archived on Zenodo with DOI (we suggest making a new release after review and revision)
>
> **Rule of thumb: your cookbook doesn't need to be finished, just useful.**

## What this changes about how we assess

**The rule of thumb is the most important line.** "Useful, not finished" means incompleteness is
not a defect. An unfinished cookbook that teaches something real is a success; a polished one that
no longer runs is not. Tiering must not punish scope — only brokenness, and only invisibility.

**Version pinning is a smell, not a virtue.** The community asks authors to *avoid* pins except
where needed, and to document why. So `audit.py` records `pinned_count` and the pinned specs as
something to *look at*, not a box to tick. A heavily pinned `environment.yml` with no explanatory
comments is a finding. This is the opposite of the usual reproducibility instinct, and it is
deliberate: a pinned cookbook silently rots as the ecosystem moves, and Pythia would rather a
cookbook break loudly in CI than teach a frozen 2023 stack.

**pip usage is a flag, not a failure.** conda-forge is preferred "wherever possible" — which
concedes that sometimes it isn't. We record `pip_dep_count` and the actual pip deps so a human can
judge whether each was necessary.

**Three of the seven criteria are unmeasurable by machine.** Topic relevance, narrative flow, and
whether metadata is "appropriate" all require reading the cookbook. That is not a gap in the
harness — it is the reason `notes/` exists, and the note template asks these questions directly.

**"Publishes itself on GitHub" is two checks, not one.** Notebooks running without error is the
nightly build; the cookbook publishing itself is the `gh-pages` deploy. A cookbook can pass the
first and fail the second, and the deploy date is the check that catches a silently disabled
workflow (see [methodology.md](./methodology.md)).

**A new release is expected after review.** The meeting suggests cutting a release once a cookbook
has been reviewed and revised. So for any cookbook this project actually fixes, the closing step is
a release and a refreshed Zenodo DOI — not just a merged PR.

## Mapping criteria to checks

| Community criterion | How we assess it |
|---|---|
| Geoscience relevance | **Human** — `notes/` → *Topic & audience* |
| Narrative flow | **Human** — `notes/` → *Narrative & teaching quality* |
| Notebooks run without error | `build.nightly_conclusion` |
| Cookbook publishes itself | `build.days_since_deploy`, `discoverability.site_live` |
| conda-forge over pip | `environment.uses_conda_forge`, `environment.pip_dep_count` |
| Avoid undocumented pins | `environment.pinned_count`, `environment.has_comments` (human confirms) |
| Author metadata appropriate | `metadata.has_orcid`, `metadata.author_count`, `metadata.has_citation` |
| Gallery tags & description appropriate | `discoverability.has_real_tags`, `metadata.has_real_abstract` (human confirms) |
| Zenodo DOI | `metadata.has_doi`, `metadata.has_release` |
