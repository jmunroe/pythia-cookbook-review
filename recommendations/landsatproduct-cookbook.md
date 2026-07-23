# landsatproduct-cookbook — Recommendations

Live outcome: **execution failed** (30-minute timeout). [← All recommendations](../recommendations.md) · [Live check](../reports/live/landsatproduct-cookbook.md) · [Repository](https://github.com/ProjectPythia/landsatproduct-cookbook)

Static tier `incubating`. **The build works; execution hangs for the full 30 minutes waiting for credentials that never come.**

## The one change that matters

**Stop logging in with `strategy="interactive"`.** The notebooks authenticate to NASA Earthdata
with:

```python
auth.login(strategy="interactive", persist=True)      # several notebooks
earthaccess.login(strategy="interactive")             # calibration / preprocessing
```

In an automated build there is no terminal: `strategy="interactive"` prompts for a username and
password on stdin, the kernel blocks waiting for a reply that never arrives, and the run sits there
until it is killed at the **1800-second timeout**. That is the failure the live check recorded —
`TIMEOUT after 1800s`, execution never finishing.

Switch every login to a non-interactive strategy that reads credentials from the environment:

```diff
- earthaccess.login(strategy="interactive")
+ earthaccess.login(strategy="environment")   # reads EARTHDATA_USERNAME / EARTHDATA_PASSWORD
```

`earthaccess` supports `strategy="environment"` (env vars) and `strategy="netrc"` (a `~/.netrc`
entry). Either lets the build proceed unattended, and both still work for a learner who has set
their credentials. This is the single change that turns a 30-minute hang into a real run.

## Also real: a missing data file

Independently, the live check surfaced a hard error:

```
FileNotFoundError: [Errno 2] No such file or directory:
  '/home/jovyan/landsatproduct-cookbook/Data/Landsat_validation_202009_202103_1.0.csv'
```

A validation notebook reads a `Data/…csv` that is not in the repository and is not produced earlier
in the run. Either commit the file (if small), fetch it with `pooch`/`earthaccess` at the top of the
notebook, or generate it from an earlier step. Until then that notebook cannot run even with
credentials fixed.

## What was verified

- **Root cause of the hang identified:** multiple notebooks call `login(strategy="interactive")`,
  which blocks on a stdin prompt under headless execution; the live check timed out at exactly
  1800s with nothing completing past the early notebooks.
- **Missing-file error captured** from the live check stderr (the `Data/…csv` above).
- **Not verified end-to-end:** a clean run after both fixes — the notebooks also need valid Earthdata
  credentials injected as env vars, and may reveal further data-access issues once they proceed. A
  live re-run with `strategy="environment"` and credentials set is the way to confirm.

## Secondary

- One notebook (`validation_step1.ipynb`) carries a non-standard `kernelspec` name (`local`).
  Normalise it to `python3` along with the rest, so it does not become a second execution blocker.
- The repo has duplicated notebooks at both the root (`calibration.ipynb`) and under `notebooks/`;
  consolidate to avoid confusion about which is canonical.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with a live re-run (credentials injected)
and open with the community, not an applied change.*
