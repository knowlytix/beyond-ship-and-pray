# proofloop demos

Two runnable demos showing the open baseline and where the optional GMS backend
lifts it. Both run with **no license**; the GMS sections light up when the
licensed `knowlytix` backend **and** a trained store are present.

## Setup (open baseline — no license)

```bash
pip install proofloop          # pulls glassloop (the base library) from PyPI automatically
```

Then run the demos from the repo root (clone it — the demos aren't in the wheel).
Prefer a local checkout for development? Use editable installs instead:
`pip install -e ../beyond-prompt-and-pray -e .`

## Demo 2 — runtime monitoring

```bash
python demos/runtime_monitoring.py
```

Feeds a governed agent benign + malicious actions and prints a live
`ALLOW / DENY / ESCALATE` stream (decided before each action runs), then the
tamper-evident, hash-chained audit trail. The closing section shows the
**out-of-scope** case: an agent that skips required workflow steps. The naive
arg-size gate waves it through; the GMS geometric gate stops it in real time.

## Demo 1 — validation report

```bash
python demos/validation_report.py     # writes demos/out/validation_report.html
```

Designs a balanced DoE test matrix, runs the governed agent on each case, scores
pass/fail by gate outcome, and renders a report (console + HTML): DoE coverage,
per-case results, baseline groundedness, and — with GMS — a **scope-admissibility
validation** backed by the trained store's calibration metrics.

## GMS "after" (licensed) — run the geometric gate live

The geometric gate/judge need the licensed `knowlytix` backend (Python **3.12**)
and a **trained store**. The store is a portable knowlytix artifact and is *not*
shipped with this open repo.

```bash
# 1. a 3.12 venv with the licensed backend + the open packages
python3.12 -m venv ~/.venv/knowlytix-demo
~/.venv/knowlytix-demo/bin/pip install knowlytix --index-url <KNOWLYTIX_INDEX_URL>   # license required
~/.venv/knowlytix-demo/bin/pip install -e ../beyond-prompt-and-pray -e .

# 2. license + trained store
export KNOWLYTIX_LICENSE_KEY="$(cat ~/.knowlytix/license.key)"
export GMS_BANKING_STORE=/path/to/gms_banking_store   # or copy it to demos/data/gms_banking_store

# 3. run — the GMS sections now show real geodesic scores
~/.venv/knowlytix-demo/bin/python demos/runtime_monitoring.py
~/.venv/knowlytix-demo/bin/python demos/validation_report.py
```

Store resolution: `$GMS_BANKING_STORE`, else `demos/data/gms_banking_store`
(gitignored — licensed data, not redistributed).

## The before/after

Without a license you see the open baseline run end-to-end and exactly where it
falls short (the install hint points at GMS). With the licensed
[`knowlytix`](https://knowlytix.ai/) backend + a trained store, the same demos
run the **real geometric gate** (admissibility scoring on the trained manifold)
and surface the store's calibration — the *Beyond Ship and Pray, Pro Edition*.
These demos depend only on `glassloop` + `proofloop` + `knowlytix` — no other
packages.
