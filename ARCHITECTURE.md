# Architecture

`proofloop` is the **test / validate / monitor** layer for agentic AI. It sits on
top of `glassloop` (the governed agent loop) and is **open-core**: everything runs
free, and a licensed **GMS backend** (`knowlytix`) snaps in to upgrade detection
from heuristic to calibrated-geometric — through the *same* interfaces, so your
code doesn't change.

```
┌──────────────────────────────────────────────────────────────────┐
│  YOUR AGENT  (any framework, any LLM)                              │
│     exposes proposed actions + produces answers                    │
└───────────────┬───────────────────────────────────────────────────┘
                │
┌───────────────▼───────────────────────────────────────────────────┐
│  glassloop   — the governed agent loop (open, Apache-2.0)          │
│    typed actions · gates (ALLOW/DENY/ESCALATE) · budgets ·         │
│    human escalation · hash-chained audit · BaseLM adapters         │
└───────────────┬───────────────────────────────────────────────────┘
                │
┌───────────────▼───────────────────────────────────────────────────┐
│  proofloop   — test · validate · monitor (open, Apache-2.0)        │
│    DoE suites · fault injection · trajectory metrics ·             │
│    groundedness · the 3-judge verifier interface                   │
└───────────────┬───────────────────────────────────────────────────┘
                │  gms.available()? lazy seam — same gate/judge API
┌───────────────▼───────────────────────────────────────────────────┐
│  GMS backend (knowlytix)  — licensed, optional                    │
│    geometric admissibility gate · GMS verifier (ENM, score_triple, │
│    holonomy, tension) · signed verdicts · calibration             │
└────────────────────────────────────────────────────────────────────┘
```

## The three capabilities

Each is one composable piece. The open tier is real and runs free; the GMS tier
is the licensed upgrade that plugs into the *same* call site.

| Capability | What it does | Open (`pip install`) | GMS upgrade (licensed) |
|---|---|---|---|
| **Runtime governance** | gate every action *before* it executes | policy + scope gates (`ALLOW`/`DENY`/`ESCALATE`), audit | calibrated **geometric admissibility** gate (out-of-scope / off-manifold actions) |
| **Verification** | judge a claim against ground truth | string-match + **your own LLM-as-judge** | **GMS verifier** catches fabrications both string-match *and* the LLM judge miss |
| **Validation** | prove it before you ship | **DoE** test design, fault injection, coverage, trajectory scoring | factor attribution, signed verdicts, calibration metrics |

## The open-core seam

GMS is never required. The seam is one call:

```python
import glassloop.gms as gms
gms.available()        # True iff the licensed knowlytix backend is installed
```

Gates and judges share one interface, so the GMS version is a drop-in:

```python
gates = [SyntaxGate(), PolicyGate(...), PlausibilityGate()]      # open baseline
gates.append(GMSPlausibilityGate(store, theta=θ, ...))          # licensed upgrade — same list
```

When `knowlytix` is absent, GMS-gated paths degrade gracefully and the rest keeps
running — so the open baseline is always reproducible (and is exactly what CI runs).

## LLM-agnostic

Anything LLM-shaped is a `BaseLM` — a protocol with a single `complete(prompt)`
method. **Switch providers freely:** Claude, a local Qwen, OpenAI, or your own
client — the framework never hard-codes a vendor.

```python
from glassloop.protocols import BaseLM          # any object with .complete(prompt) -> str
from glassloop.models import AnthropicAdapter, QwenAdapter, MockLM

judge_lm: BaseLM = AnthropicAdapter()           # or QwenAdapter() (local), or your OpenAI wrapper
```

The LLM-as-judge tier takes any `BaseLM`. So *your* model judges, and GMS is the
geometric check that backstops it.

## How you use it

```bash
pip install proofloop          # pulls glassloop (the base) from PyPI
# optional model tools:  pip install "proofloop[ml]"
# licensed GMS backend:  pip install "proofloop[gms]"   (knowlytix — see https://knowlytix.ai/)
```

1. **Wrap your agent** in a `GovernanceHarness` with the gates/policies you want.
2. **Point the validators** at your behavior factors (DoE) and your ground truth.
3. **Plug your LLM** (any `BaseLM`) into the judge.
4. **Add the GMS store** trained on *your* workflow to upgrade the gate/verifier.

Open is the front door; GMS is the calibrated engine behind it.

## What's open vs Pro

| | Open (Apache-2.0) | Pro / GMS (licensed `knowlytix`) |
|---|---|---|
| Agent loop, gates, audit | ✅ | ✅ |
| DoE, fault injection, metrics | ✅ | ✅ + factor attribution |
| Runtime scope gate | heuristic (size/rules) | **calibrated geometric** |
| Verifier | string-match + your LLM | **GMS verifier** (ENM, geodesic, holonomy) |
| Signed verdicts, calibration | — | ✅ |
| Trained domain store | — | ✅ (trained on your workflow) |

See [`demos/`](demos/) for runnable demos and [`demos/demo.ipynb`](demos/demo.ipynb)
for the end-to-end walkthrough.
