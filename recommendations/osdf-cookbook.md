# osdf-cookbook — Recommendations

Live outcome: **build failed**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/osdf-cookbook.md) · [Repository](https://github.com/ProjectPythia/osdf-cookbook)

Static tier `healthy`. **This failure looks transient, not a cookbook defect.**

## The one thing to do: re-run

The build died with a **registry/transport error**, not a dependency error:

```
Linking python-fasthtml-0.14.9-pyhc364b38_0
ERROR: failed to receive status: rpc error: code = Unavailable desc = error reading from server: EOF
Error during build: Command '[... docker buildx build --push ...]' returned non-zero exit status 1
```

The conda solve had already succeeded and packages were most of the way through linking when the
connection to the image registry dropped mid-`--push` (`code = Unavailable … EOF`). That is a
BinderHub/registry/network hiccup on the build infrastructure, not something in this repo. The
[live-assessment method](../docs/live-assessment.md) already notes that a single failed run of an
infrastructure-dependent step is a prompt to re-run rather than a finding.

**Action: re-run the live check.** A fresh build will very likely succeed. Only if it fails again —
at the same or a different step — is there a cookbook-side problem to chase.

## Secondary env hygiene (only if a re-run confirms it builds)

The `environment.yml` is otherwise in good shape — conda-forge-first, Python pinned to a reasonable
`3.12`. Two small alignments with the [publication criteria](../docs/criteria.md):

- **Move `rioxarray` from pip to conda.** It is packaged on conda-forge; the criteria ask to prefer
  conda-forge over pip wherever possible. The genuinely pip-only packages (`OpenVisus`,
  `openvisuspy`, `import-ipynb`) should stay in the `pip:` block.
- **Document the exact pins.** `intake-esm=2025.2.3`, `pelicanfs=1.2.1`, `zarr=2.18.1` (holds zarr
  at v2), and `igwn-auth-utils=1.4.0` are all held to specific versions. If each is deliberate, add
  a one-line comment saying why; if not, float it and re-pin only when something breaks.

## What was verified

- **Root cause read from the log:** the failure is a registry transport `EOF` during
  `docker buildx --push`, after a successful solve — classic transient infrastructure failure.
- **Not verified:** a clean rebuild (no conda/mamba on this machine). The recommendation is
  deliberately "re-run first" precisely because the evidence points away from a repo defect.

---
*Agent-assisted analysis, 2026-07-22. A proposal to confirm by re-running the live check, not an
applied change.*
