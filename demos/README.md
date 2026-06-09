# proofloop demos

Two runnable demos showing the open baseline and where the optional GMS backend
lifts it. Both run with **no license**; the GMS columns light up when `knowlytix`
is installed.

## Setup

```bash
# from the repo root, editable installs of the base + this package
pip install -e ../beyond-prompt-and-pray   # glassloop (base library)
pip install -e .                            # proofloop
```

## Demo 2 — runtime monitoring

```bash
python demos/runtime_monitoring.py
```

Feeds a governed agent benign + malicious actions and prints a live
`ALLOW / DENY / ESCALATE` stream (decided before each action runs), then the
tamper-evident, hash-chained audit trail. The final "evasive injection" slips the
regex baseline — the case the GMS semantic intent guard catches.

## Demo 1 — validation report

```bash
python demos/validation_report.py     # writes demos/out/validation_report.html
```

Designs a balanced DoE test matrix, runs the governed agent on each case, scores
pass/fail by gate outcome, and renders a report (console + HTML) with
baseline-vs-GMS columns (DoE coverage, per-case results, groundedness).

## The before/after

Without a license you see the open baseline run end-to-end and exactly where it
falls short. Install the licensed [`knowlytix`](https://knowlytix.ai/) backend to
populate the GMS columns (geometric plausibility gate, GeometricJudge, factor
attribution) — the *Beyond Ship and Pray, Pro Edition*.
