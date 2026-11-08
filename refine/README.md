# MANET Routing: Evidence and Diagnostic Resources

This directory contains supporting analysis results and diagnostic software for the study *MANET Routing from Classical Protocols to Graph Learning: Evidence Comparability and a Bounded ns-3 Benchmark*.

## Research materials

| File | Description |
|---|---|
| [evidence/aodv_dsr_pdr_comparisons.csv](evidence/aodv_dsr_pdr_comparisons.csv) | Scenario-specific AODV–DSR packet-delivery-ratio comparisons and statistical results. |
| [evidence/comparability_evidence_registry.csv](evidence/comparability_evidence_registry.csv) | Source-level verification, comparability, and evidence-maturity cross-checks. |
| [evidence/recompute_pdr_statistics.py](evidence/recompute_pdr_statistics.py) | Independent computation of PDR comparisons from the seed-level source CSV. |
| [experiments/observatory_tier1_runner_diagnostic.cc](experiments/observatory_tier1_runner_diagnostic.cc) | Isolated ns-3 diagnostic runner with socket-error, packet-attempt and sampled-mobility recording. |
| [experiments/check_diagnostics.py](experiments/check_diagnostics.py) | Checks packet accounting and offered-transmission schedules. |
| [experiments/check_mobility.py](experiments/check_mobility.py) | Compares sampled node-position records across runs. |
| [experiments/test_diagnostic_checkers.py](experiments/test_diagnostic_checkers.py) | Synthetic positive and negative regression tests for diagnostic checkers. |

The [benchmark specifications](../benchmark/) and [experimental analysis artifacts](../artifacts/s2/) provide the broader scenario and metric context.

## Analysis scope

The recorded benchmark covers four ns-3.47 routing implementations (AODV, DSDV, DSR and OLSRv1), four scenarios (BASE, FAST, LOAD and SCALE), and 20 numerical seed labels per protocol–scenario cell (320 recorded runs). The seed-level CSV used for statistical reanalysis has SHA-256 `e848c565e41de92ddf41d2db52b4c3e154e848de1758c7ac07a6b7a3f6d54a56`. This CSV is **not currently included in this directory**; the statistical reproduction script requires it as an input.

The SCALE AODV-minus-DSR mean PDR contrast was 0.1625 (within-scenario Holm-adjusted Wilcoxon p = 0.0437) when matching records by their numerical seed labels. Those labels do not establish equivalence of realized mobility or traffic trajectories. The recorded OLSRv1 runs contained 4,886 sender-socket rejections out of 11,000 offered datagrams; their cause was not logged in the original records. No independent ns-3.47 rerun, alternate-propagation experiment, or field deployment is claimed here.

The diagnostic tools are separate from the original benchmark source. Python checker tests passed in [GitHub Actions](https://github.com/Arithmetic-Power-Geometry/MANET-Algorithm-Observatory/actions/runs/42458668262), using synthetic fixtures; this does not constitute execution of the ns-3 diagnostic runner.
