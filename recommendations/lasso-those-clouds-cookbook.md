# lasso-those-clouds-cookbook — Recommendations

Live outcome: **execution failed**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/lasso-those-clouds-cookbook.md) · [Repository](https://github.com/ProjectPythia/lasso-those-clouds-cookbook)

Static tier `incubating`. **The build works; execution dies in ~6 seconds because the notebooks ask for a kernel Binder does not have.** A mechanical fix.

## The one change that matters

**Reset every notebook's `kernelspec` to the standard `python3`.** The image builds, but
`myst build --execute` fails after 6.18s with **zero cells run**, because the notebooks were saved
with a kernel named `conda-base-py` that the Binder image does not contain. From the live check's
stderr:

```
The 'conda-base-py' kernel is not available. Please pick another suitable kernel instead,
or install that kernel.
```

`conda-base-py` ("Python [conda env:base] *") is the author's local JupyterHub kernel name, baked
into `metadata.kernelspec`. On the Binder image learners launch, that name resolves to nothing, so
MyST cannot start a kernel and the book fails before any cell runs — hence **0 errors** and
near-zero memory.

**5 of the 9 notebooks** carry `conda-base-py`; the other 4 already use `python3`, so the fix is to
make the 5 match the 4.

### The fix

Set `metadata.kernelspec` in every notebook to the standard block:

```json
"kernelspec": {
  "display_name": "Python 3 (ipykernel)",
  "language": "python",
  "name": "python3"
}
```

From the repo root:

```bash
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

- **Root cause confirmed from the live check's stderr:** `'conda-base-py' kernel is not available`,
  execution exited in 6.18s with 0 cells executed.
- **Scope confirmed:** 5 of 9 notebooks carry `kernelspec.name == "conda-base-py"`; 4 already use
  `python3`.
- **Not verified end-to-end:** whether the notebooks run clean once the kernel resolves — a live
  re-run with the kernelspec corrected is the way to confirm and to surface any remaining cell-level
  errors (as the osdf re-check did).

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with a live re-run and open with the
community, not an applied change.*
