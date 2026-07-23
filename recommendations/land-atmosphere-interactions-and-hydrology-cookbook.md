# land-atmosphere-interactions-and-hydrology-cookbook — Recommendations

Live outcome: **execution failed**. [← All recommendations](../recommendations.md) · [Live check](../reports/live/land-atmosphere-interactions-and-hydrology-cookbook.md) · [Repository](https://github.com/ProjectPythia/land-atmosphere-interactions-and-hydrology-cookbook)

Static tier `incubating`. **The build works; execution dies in ~10 seconds because the notebooks ask for hackathon kernels Binder does not have.** A mechanical fix.

## The one change that matters

**Reset every notebook's `kernelspec` to the standard `python3`.** The image builds, but
`myst build --execute` fails after 9.55s with **zero cells run**. The notebooks were saved on a
hackathon JupyterHub and carry that hub's kernel names, which do not exist in the Binder image. From
the live check's stderr:

```
The 'conda-env-miniconda3-hackathon_env-py' kernel is not available. Please pick another
suitable kernel instead, or install that kernel.
```

The notebooks reference **two** non-existent kernels — `conda-env-miniconda3-hackathon_env-py`
(display "Python [conda env:miniconda3-hackathon_env]") on 5 notebooks and
`2025-digital-earths-global-hackathon` on 4 — while only 2 notebooks use the correct `python3`. On
the Binder image learners launch, neither hackathon kernel resolves, so MyST cannot start a kernel
and the book fails before any cell runs. That is why the run shows **0 errors** and near-zero
memory: nothing executed.

### The fix

Normalise `metadata.kernelspec` in every notebook to the standard block:

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

- **Root cause confirmed from the live check's stderr:** the hackathon kernel is not available;
  execution exited in 9.55s with 0 cells executed.
- **Scope confirmed:** 9 of 11 notebooks carry a non-standard kernel (5 ×
  `conda-env-miniconda3-hackathon_env-py`, 4 × `2025-digital-earths-global-hackathon`); 2 already
  use `python3`.
- **Not verified end-to-end:** whether the notebooks run clean once the kernel resolves. This
  cookbook grew out of a hackathon, so some notebooks may also depend on hackathon-specific data
  paths or credentials — a live re-run with the kernelspec corrected will confirm and reveal any
  remaining cell-level issues.

## Secondary

- Being hackathon-derived, check that data access in the notebooks does not rely on a
  hub-specific mount or cached dataset that a public Binder session cannot reach; surface any such
  dependency in the same PR.

---
*Agent-assisted analysis, 2026-07-23. A proposal to confirm with a live re-run and open with the
community, not an applied change.*
