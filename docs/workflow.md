# The review workflow

One pass through every cookbook, repeatably.

## The loop

```
audit  →  report  →  triage  →  sync clones  →  write notes  →  roll up
```

### 1. Audit — collect the facts

```bash
python scripts/audit.py
```

Writes `data/snapshot-YYYY-MM-DD.json`. Takes a few minutes for the full org. Add `--limit N` to
sample while developing, `--no-cache` to force fresh fetches.

### 2. Report — turn facts into a picture

```bash
python scripts/report.py
```

Regenerates `reports/dashboard.md` (every cookbook, one row each), `reports/by-tier.md` (grouped,
with the specific failing checks spelled out), and `reports/gaps.md` (cross-cutting findings).

**Never hand-edit anything in `reports/`.** It is generated output and the next run destroys it.
If a report says something wrong, fix `report.py` or the rubric.

### 3. Triage — decide where to spend attention

Read `reports/by-tier.md` top-down. The tiers are ordered by how much a learner is hurt by the
problem:

- `stale` and `degraded` first — these are *published* cookbooks that are broken. Someone arriving
  from the gallery today has a bad experience.
- `abandoned` next — stranded work that could be revived or cleanly retired.
- `incubating` — the pipeline. Whose cookbook needs an advocate?
- `healthy` — sample a few to keep the harness honest, otherwise leave alone.

### 4. Sync clones — get the content locally

```bash
./scripts/sync-clones.sh radar-cookbook esgf-cookbook
```

Shallow-clones to `../<name>/`, alongside this repo. Re-running fast-forwards. Only needed for
cookbooks you are going to read; the audit itself never touches a clone.

### 5. Write notes — the part that matters

```bash
cp notes/_template.md notes/radar-cookbook.md
```

Then actually read the cookbook — the rendered book, not just the repo. The automated tier is a
hypothesis; the note confirms it, refines it, or overrides it via `tier_override`.

The questions worth answering are the ones CI cannot:

- Does it teach the thing it claims to teach?
- Is the science and the tooling advice still current?
- Are the stated prerequisites honest?
- If it is broken, is it worth fixing — or has the ecosystem moved past it?
- Who, realistically, would maintain it?

Land on one of four recommendations: **adopt** (take maintainership), **hand off** (find it an
owner), **fix** (a specific, bounded repair), **retire** (archive it and be honest with learners).

### 6. Roll up

Once enough notes exist, `reports/gaps.md` plus the recommendations become the actual deliverable:
a proposal to the Pythia community about the state of the cookbook collection.

## Conventions

| Directory | Who writes it | Lifecycle |
|---|---|---|
| `data/` | `audit.py` | append-only, committed — the historical record |
| `reports/` | `report.py` | regenerated, overwritten freely |
| `index.md` | `build_site.py` | regenerated; edit `scripts/templates/index.md` instead |
| `notes/` | **a human** | hand-written, never generated |
| `docs/` | a human | changes when upstream Pythia guidance changes |

Everything in `reports/` and `docs/` is also a page on the [published site][site] — `myst.yml`
pulls them straight into the table of contents, so writing markdown here is publishing.

[site]: https://jmunroe.github.io/pythia-cookbook-review/

The reason `notes/` is never generated: the whole value of this exercise is human judgment about
teaching quality. A machine-written note would look identical to a real one and quietly poison the
conclusions.

## Scope discipline

This repo assesses. It does not act on upstream. No PRs, no issues filed on ProjectPythia repos,
no edits to cloned cookbooks from here — those are separate, deliberate steps taken with the
community, informed by what this workspace found.
