# Beyond Ship and Pray

*Testing and validating agentic AI systems.*

Most teams ship an agent and pray it behaves in production. This is the open
alternative — a discipline for *proving* it first and *watching* it after.
**Before deployment:** design-of-experiments test suites, fault injection,
trajectory scoring, groundedness/hallucination checks, and a validation report you
can hand to a reviewer. **At runtime:** gates that detect and **stop** out-of-scope,
risky, or policy-violating actions *before they execute* (`ALLOW` / `DENY` /
`ESCALATE`), with a tamper-evident, hash-chained audit trail.

The baseline runs with **no license and no GMS**. For production-grade detection —
geometric hallucination judging, calibrated admissibility, signed verdicts — the
optional **GMS backend** ([`knowlytix`](https://knowlytix.ai/)) snaps in via a lazy
seam. Clone it, run the baseline, see exactly where GMS lifts detection and
validation.

> Part of the **"Beyond … and Pray"** series:
> [governed agents](https://github.com/knowlytix/beyond-prompt-and-pray) ·
> [trustworthy RAG](https://github.com/knowlytix/beyond-chunk-and-pray) ·
> [test & validate](https://github.com/knowlytix/beyond-ship-and-pray) ·
> [LLMs from scratch](https://github.com/knowlytix/llm-from-scratch)

## What's inside

- **Validation reports** — DoE test design, fault injection, coverage, trajectory scoring
- **Catalog-driven test suites** — build scenarios from base/factor catalogs, emit SFT data, and score a system-under-test (`proofloop.suite`)
- **Runtime monitoring** — `ALLOW` / `DENY` / `ESCALATE` gates that stop bad actions live
- **Hallucination & groundedness checks** — catch unsupported claims pre- and post-deploy
- **Tamper-evident audit** — hash-chained record of every decision and stop
- **Two runnable demos** — validation-report generator + live monitoring view
- **GMS-optional** — baseline runs free; geometric judging & calibration via `knowlytix`

## Install

```bash
pip install proofloop                 # testing + validation + runtime monitoring
pip install "proofloop[ml]"           # + open-weight model tools
pip install "proofloop[gms]"          # + the licensed GMS backend (knowlytix)
```

`proofloop` builds on [`forgeloop`](https://github.com/knowlytix/beyond-prompt-and-pray)
(the governed agent loop) and adds the testing, validation, and monitoring layer.

## Quickstart

Declare the behavior space you care about; get a balanced test matrix that covers
it (instead of cherry-picked cases):

```python
from proofloop.evaluation import balanced_design, coverage_report

FACTORS = {"risk": ["benign", "pii", "injection"], "channel": ["email", "chat"]}
design = balanced_design(FACTORS, num_cases=6, seed=7)
print(coverage_report(design, FACTORS))
# -> {'risk': {'benign': 2, 'pii': 2, 'injection': 2}, 'channel': {'email': 3, 'chat': 3}}
```

### Build a full test suite from catalogs

For richer suites, `proofloop.suite` builds scenarios from base/factor catalogs,
holds ground truth invariant, and scores a system-under-test — all on the open
baseline (no GMS required):

```python
from proofloop import suite as ts

cat = ts.Catalog.load()                                   # bundled base/factor/profile catalogs
sv = ts.resolve(cat, ["exact_recall"], ["clarity"], mode="embedded")
src = ts.UserBaseSource([{"query": "What is the overdraft fee?", "answer": "35"}])
scenarios = ts.compose(sv, src.items(), n_runs=30, seed=7)

rows = ts.evaluate.run(scenarios, my_sut)                 # my_sut(query, context="") -> answer
print(ts.evaluate.summary(rows))                          # {'n': 30, 'accuracy': ...}
```

The open-core seam runs the same call sites; `knowlytix` upgrades three of them:
`simple_design` → `graphdoe_design` (Sobol space-filling), `UserBaseSource` →
`CatalogBaseSource` (mine a GMS store), and `weak_link` → `attribute` (calibrated
logistic factor attribution).

### Run the two demos

The headline capabilities — a validation report and live runtime monitoring — are
runnable demos. Clone the repo (the demos aren't shipped in the wheel):

```bash
git clone https://github.com/knowlytix/beyond-ship-and-pray
cd beyond-ship-and-pray
pip install proofloop                       # pulls forgeloop from PyPI automatically
python demos/runtime_monitoring.py          # live ALLOW / DENY / ESCALATE + audit chain
python demos/validation_report.py           # DoE report -> demos/out/validation_report.html
```

Both run on the open baseline with **no license**. With the licensed `knowlytix`
backend and a trained store, the same demos show the real geometric gate — see
[`demos/README.md`](demos/README.md).

## The GMS upgrade (open-core)

`proofloop` runs fully without a license. GMS-backed detection — geometric
hallucination judging, factor attribution, signed verdicts — requires the licensed
[`knowlytix`](https://knowlytix.ai/) package, imported lazily:

```python
import forgeloop.gms as gms
gms.available()   # True if the licensed backend is installed
```

The GMS-native chapters (notebooks `20`–`28`: knowledge graphs, GEODE, base
sourcing, enrichment/training capstones) need the backend. It's a one-time setup:
**[get a free developer license](https://knowlytix.ai/signup/)**, install
`knowlytix`, and every GMS notebook runs.

The production-grade, GMS-native edition is the *Beyond Ship and Pray, Pro
Edition* — see [knowlytix.ai](https://knowlytix.ai/).

## License

Apache-2.0. © 2026 Knowlytix.
