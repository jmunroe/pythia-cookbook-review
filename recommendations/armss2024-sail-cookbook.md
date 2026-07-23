# armss2024-sail-cookbook — Recommendations

Live outcome: **execution failed**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/armss2024-sail-cookbook.md) · [Repository](https://github.com/ProjectPythia/armss2024-sail-cookbook)

Static tier `incubating`. **The build works; execution dies in 7 seconds because the notebooks ask for a kernel that does not exist on Binder.** A mechanical one-line-per-notebook fix.

## The one change that matters

**Reset every notebook's `kernelspec` to the standard `python3`.** The image builds fine, but
`myst build --execute` fails almost instantly (6.79s) with **zero cells run** — because the
notebooks were saved with a kernel named `conda-base-py` that is not installed in the Binder image.
The live check's stderr says it outright:

```
The 'conda-base-py' kernel is not available. Please pick another suitable kernel instead,
or install that kernel.
```

`conda-base-py` (display name "Python [conda env:base] *") is the kernel name from the author's own
JupyterHub. It is baked into each notebook's `metadata.kernelspec`. On any other environment — the
Binder image learners actually launch — that name resolves to nothing, so MyST cannot start a
kernel and the whole book fails before a single cell executes. That is why the run shows
**0 errors** and near-zero memory: nothing ran.

**12 of the 16 notebooks** carry `conda-base-py`; the other 4 already use the correct `python3`, so
the fix is simply to make the 12 match the 4.

### The fix

Set `metadata.kernelspec` in every notebook to the standard block already present in the working
four:

```json
"kernelspec": {
  "display_name": "Python 3 (ipykernel)",
  "language": "python",
  "name": "python3"
}
```

Any of these applies it repo-wide (run from the repo root):

```bash
# with jupytext
jupytext --set-kernel python3 **/*.ipynb

# or a dependency-free rewrite
python - <<'PY'
import json, glob
for nb in glob.glob("**/*.ipynb", recursive=True):
    if ".ipynb_checkpoints" in nb: continue
    d = json.load(open(nb))
    d.setdefault("metadata", {})["kernelspec"] = {
        "display_name": "Python 3 (ipykernel)", "language": "python", "name": "python3"}
    json.dump(d, open(nb, "w"), indent=1); open(nb, "a").write("\n")
PY
```

## What was verified

- **Root cause confirmed from the live check's own stderr:** `'conda-base-py' kernel is not
  available`, execution exited in 6.79s with 0 cells executed.
- **Scope confirmed:** 12 of 16 notebooks carry `kernelspec.name == "conda-base-py"`; 4 already use
  `python3`.
- **Not verified end-to-end:** whether the notebooks then run *clean* once the kernel resolves.
  Fixing the kernelspec is guaranteed to get past the kernel-selection failure, but — as the osdf
  re-check showed — real cell errors can surface only once execution actually starts. A live re-run
  with the kernelspec corrected is the way to confirm, and to reveal any remaining cell-level issues.

## Secondary

- Several notebooks live at the **repo root** (`OPC.ipynb`, `SMPS.ipynb`, `Radiometer.ipynb`) rather
  than under `notebooks/`. Consider consolidating under `notebooks/` for consistency with the
  cookbook template.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with a live re-run and open with the
community, not an applied change.*
