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

`proofloop` builds on [`glassloop`](https://github.com/knowlytix/beyond-prompt-and-pray)
(the governed agent loop) and adds the testing, validation, and monitoring layer.

## The GMS upgrade (open-core)

`proofloop` runs fully without a license. GMS-backed detection — geometric
hallucination judging, factor attribution, signed verdicts — requires the licensed
[`knowlytix`](https://knowlytix.ai/) package, imported lazily:

```python
import glassloop.gms as gms
gms.available()   # True if the licensed backend is installed
```

The production-grade, GMS-native edition is the *Beyond Ship and Pray, Pro
Edition* — see [knowlytix.ai](https://knowlytix.ai/).

## License

Apache-2.0. © 2026 Knowlytix.
