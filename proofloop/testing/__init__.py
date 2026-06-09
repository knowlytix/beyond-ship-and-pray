"""Testing adapters: DoE-based testing for agents. See the testing chapter.

Thin adapters over the knowlytix harness (`knowlytix.harness.testing`,
`knowlytix.harness.graphdoe`). Two harnesses:

  * `GraphDOEHarness` --- the knowledge-QA-shaped harness (ingest a document,
    generate GMS-primitive questions, run a `(question, context) -> str`
    evaluator, attribute failures).

The capstone-specific `CapstoneTestHarness` (deeply GMS-native) lives in the
paid Pro edition, not this open package.
"""

from proofloop.testing.harness import (
    FactorAttribution,
    GraphDOEHarness,
    TestResult,
)
from proofloop.testing.judge import GeometricJudge, JudgeVerdict

__all__ = [
    "FactorAttribution",
    "GeometricJudge",
    "GraphDOEHarness",
    "JudgeVerdict",
    "TestResult",
]
