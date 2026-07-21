#!/usr/bin/env python3
"""Present the green-nightly-with-errors scan as reports/ci-errors.md.

Generated output -- never hand-edit. Regenerate with:
    python scripts/ci_errors.py && python scripts/report_ci.py
"""

import argparse
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
REPORTS = ROOT / "reports"

ORG = "ProjectPythia"


def newest():
    scans = sorted(DATA.glob("ci-errors-*.json"))
    if not scans:
        raise SystemExit("No scans in data/. Run scripts/ci_errors.py first.")
    return scans[-1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scan", type=pathlib.Path)
    args = parser.parse_args()

    path = args.scan or newest()
    data = json.loads(path.read_text())
    results = data["results"]
    affected = sorted(
        (r for r in results if r["notebooks"] and (r["run"] or {}).get("conclusion") == "success"),
        key=lambda r: -len(r["notebooks"]),
    )
    clean = [r for r in results if not r["notebooks"] and not r.get("reason")]
    unreadable = [r for r in results if r.get("reason")]

    date = path.stem.replace("ci-errors-", "")
    lines = [
        "# Green nightlies with failing notebooks",
        "",
        f"Generated from `{path.name}` (collected {date}). Do not edit — regenerate with "
        "`python scripts/ci_errors.py && python scripts/report_ci.py`.",
        "",
        ":::{danger} A passing badge does not mean the notebooks ran",
        f"**{len(affected)} of {data['scanned']} gallery cookbooks** had at least one notebook "
        "raise an exception during their most recent nightly build — and the build reported "
        "**success** anyway.",
        ":::",
        "",
        "## Why this happens",
        "",
        "`myst build --execute` exits 0 when a cell raises. The exception is captured into the "
        "page and the build carries on, so the workflow — whose health is the command's exit "
        "status — goes green, the book deploys, and the gallery card says passing.",
        "",
        "MyST logs each failure like this:",
        "",
        "```",
        "⛔️ notebooks/01-easygems.ipynb An exception occurred during code execution, "
        "halting further execution",
        "```",
        "",
        "Note **halting further execution**: every cell after the failure is skipped, so the "
        "published page is silently truncated. A learner sees a lesson that stops partway, or a "
        "traceback where a figure should be.",
        "",
        "This is measured from Project Pythia's own CI logs, not from a reproduction — there is "
        "no environment confound. See [the method](../docs/live-assessment.md).",
        "",
        "## Affected cookbooks",
        "",
        "| Cookbook | Notebooks raising | Gallery says | Nightly run |",
        "|---|---|---|---|",
    ]

    for r in affected:
        run = r["run"] or {}
        lines.append(
            f"| [{r['cookbook']}](https://github.com/{ORG}/{r['cookbook']}) "
            f"| **{len(r['notebooks'])}** "
            f"| {'✅ passing' if r.get('published_as_passing') else '—'} "
            f"| [{run.get('conclusion')}]({run.get('url')}) |"
        )

    lines += ["", "## Detail", ""]
    for r in affected:
        lines += [f"### {r['cookbook']}", ""]
        for n in r["notebooks"]:
            ename = f" — `{n['ename']}`" if n.get("ename") else ""
            url = f"https://github.com/{ORG}/{r['cookbook']}/blob/main/{n['notebook']}"
            lines.append(f"- [`{n['notebook']}`]({url}){ename}")
        lines.append("")

    lines += [
        "## Cookbooks whose latest nightly showed no execution errors",
        "",
        ", ".join(f"`{r['cookbook']}`" for r in clean) or "none",
        "",
    ]
    if unreadable:
        lines += [
            "## Not assessed",
            "",
            "\n".join(
                f"- `{r['cookbook']}` — {r['reason']}" for r in unreadable
            ),
            "",
        ]

    lines += [
        "## What to do with this",
        "",
        "This is a finding about the **shared build configuration**, not about any one cookbook. "
        "MyST supports `error_rules`, so failing the build on execution errors looks like a "
        "one-place change in "
        "[`cookbook-actions`](https://github.com/ProjectPythia/cookbook-actions) or the shared "
        "[`pythia-config`](https://github.com/ProjectPythia/pythia-config).",
        "",
        "Worth raising with the Pythia maintainers before acting: turning this on would flip a "
        "large fraction of the gallery red overnight, which is a decision for the community "
        "rather than a fix to land unannounced. The counts above are the argument for making it, "
        "and the list is the work it implies.",
        "",
    ]

    REPORTS.mkdir(parents=True, exist_ok=True)
    out = REPORTS / "ci-errors.md"
    out.write_text("\n".join(lines) + "\n")
    print(f"Wrote {out} ({len(affected)} affected of {data['scanned']})")


if __name__ == "__main__":
    main()
