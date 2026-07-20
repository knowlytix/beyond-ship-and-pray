# Beyond "Push and Pray" — Book Plan

**Title.** *Beyond "Push and Pray": Testing and Training AI Systems on Geometric
Ground Truth.* Author: Knowlytix.ai. Companion to *Beyond Prompt and Pray*
(agents) and *Beyond Chunk and Pray* (RAG).

**Thesis.** Testing and training a knowledge-intensive AI system are designed
experiments over a provably-correct oracle, not benchmarks. A *base* question is
answered by a geometric memory substrate (ground truth by construction); a set of
*enrichment* factors varies its presentation without changing the answer. From
that decomposition follow factor-balanced test suites, grounded training corpora
and logistic attribution of failure to input conditions.

## Conventions

- **One runnable notebook per chapter**, each ending in a self-check `assert`.
  Built by `scripts/build_notebooks.py` (nbformat). Executed cells use the
  dependency-light path where possible; heavier paths are shown as reference.
- **Book listings are copied from the notebooks** — the notebook is authoritative
  for code; the chapter is the narrative.
- **Voice:** academic and descriptive, American English, no Oxford comma. No
  defensive or bloggy phrasing. The library is the source of truth.
- **Adaptation:** Foundations and several methods adapt material from the two
  companion books, rewritten in this book's voice — never copied verbatim.
- **Self-contained:** assumes no prior background; Part I teaches the substrate.

## Structure (5 parts, 12 chapters)

Status: [written] compiles now · [draft] to write · file / notebook / source.

### Part I — Foundations
1. **Why Average Accuracy Is Not Enough** — designed-experiment view; base–
   enrichment decomposition. [written] `ch01_foundations.tex` / `nb01` / spine.
2. **Knowledge Graphs and Exact Memory** — entities, relations, triples; the
   exact numeric register; provenance. [written] `ch02_knowledge_graphs.tex` /
   `nb02` / adapt C&P (provenance, document-to-graph).
3. **Geometric Memory Systems and Their Primitives** — the manifold; the
   primitives that answer and that compute ground truth (`score_triple`,
   `lookup_enm`, `query_triples`, `link_predict`, `tension_energy`,
   `check_holonomy`); calibration. [written] `ch03_gms_primitives.tex` / `nb03` /
   adapt C&P (geometric memory, substrate, calibration), P&P (GMS calibration).
4. **GEODE: Building the Oracle** — ingest and self-correction
   (propose → diagnose → repair). [written] `ch04_geode.tex` / `nb04` / adapt C&P
   (GEODE self-correction).

### Part II — The Experimental Material
5. **The Base Taxonomy** — five families, eighteen categories, capability
   requirements, status table, the three sources incl. user-supplied.
   [written] `ch05_base_taxonomy.tex` / `nb05` / spine.
6. **The Enrichment Design Space** — forty factors, ten groups, ground-truth
   invariance, `applies_to`, the application layer. [written]
   `ch06_enrichment.tex` / `nb06` / spine.

### Part III — Designs and Outputs
7. **Experimental Design and Composition** — mixed-cardinality factor space, the
   φ_p criterion and Sobol+refine, crossed vs. embedded, balanced blocking,
   statistical power. [written] `ch07_design.tex` / `nb07` / spine + space-filling
   design method.
8. **Generating Training Data** — label-preserving classifier corpora and
   grounded, contract-validated generative pairs; synthesis variants and
   user-supplied augmentation. [written, refine] `ch08_training.tex` / `nb08` /
   adapt P&P training recipes + grounded synthesis.

### Part IV — Evaluating Agentic Systems
9. **Agentic Systems and What to Test in Them** — the agent loop, tools, gates,
   escalation, audit; the properties to test (outcome, trajectory, process,
   component, resilience, behavioral, governance); the SUT interface and the
   three scoring levels. [written] `ch09_agentic.tex` / `nb09` / adapt P&P
   (agent + capstone) and GMS-knowlytix `gmsh_testing_int`/`_ext`.
10. **Identifying Weakness: Logistic Attribution** — deviance, FDR, odds ratios,
    joint model, interactions, weak-link. [written] `ch10_analysis.tex` / `nb10` /
    spine.
11. **Resilience Under Tool Faults** — fail-loud fault injection; detection rate;
    the fault taxonomy (error/timeout/stale/plausible-but-wrong). Release gate
    dropped (substrate accuracy unstable). [written] `ch11_resilience.tex` / `nb11`
    / adapt P&P testing stages + `gmsh_testing` tool gateway.

### Part V — Capstone
12. **Testing a Governed Agent End to End** — the complaint agent through the
    whole framework, with real numbers from `data/capstone_run.json` (Qwen rerun
    pending; verify per-tool scoring). [draft] `ch12_capstone.tex` / `nb12` /
    `scripts/capstone_run.py`.

### Appendices
- **A. API Reference** [written] `appendix_api.tex`.
- **B. Full Catalog Listings** [written] — base/factor/profiles dumps.
- **C. Reproducing the Artifacts** [written].
- **D. The φ_p / Space-Filling Mathematics** [written].

## Repository map

```
book/        LaTeX: main + one .tex per chapter + preamble + appendices
notebooks/   one runnable notebook per chapter (nbNN), self-check at the end
catalogs/    base_catalog.yaml · factor_catalog.yaml · profiles.yaml
apps/        application layer (complaint_agent.yaml, complaint_sut.py)
gmstest/     the library: catalogs · resolve · sources · compose · emit · evaluate
scripts/     build_notebooks · validate_catalogs · validate_parity ·
             behavioral_parity · capstone_run
reference_paper/  JASA (space-filling design) · MeMo (grounded synthesis)
```

## Build

```bash
source ~/cluster/spark-venv/bin/activate
python scripts/build_notebooks.py                 # regenerate notebooks
jupyter nbconvert --execute notebooks/*.ipynb      # check self-checks
cd book && pdflatex gms-testing-tutorial.tex       # x2 for TOC/refs
```
