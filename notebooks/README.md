# Notebooks — Beyond Ship and Pray

The testing/validation chapters, running on the open `proofloop` library
(which builds on `forgeloop`): trajectory evaluation, failure-mode DoE,
testing agents, and the GMS calibration appendix.

```bash
pip install proofloop   # pulls forgeloop (the base) from PyPI automatically
jupyter lab
```

## Tiers

- **Open (no license):** `10_trajectory_evaluation` and `11_failure_modes_doe`
  run on `forgeloop` + `proofloop`. Their GMS cells (geometric judge) print a
  "requires GMS" hint when `knowlytix` is absent; the rest runs.
- **Pro tier (licensed):** `16_testing_agents` uses `CapstoneTestHarness`, which
  ships in the licensed *Beyond Ship and Pray, Pro Edition* (`knowlytix`). The
  import is wrapped so the notebook degrades gracefully without it.
  `appendix_C_gms_calibration` covers the geometric calibration that backs the
  Pro tier.

See also the runnable [`demos/`](../demos) — the live runtime-monitoring and
validation-report demos, with the real GMS gate when `knowlytix` is installed.
