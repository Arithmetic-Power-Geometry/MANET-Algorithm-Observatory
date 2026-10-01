# Gate 6 — S2 confirmatory analysis

Source: GitHub Actions run 36845825031, artifact s2-confirmatory (11153444629). Design: 4 protocols × 20 predeclared disjoint seeds × 4 frozen scenarios = 320 validated raw runs.

## Interpretation rules
S2 is confirmatory for the frozen benchmark only. It does not establish a universal MANET protocol ordering. Comparisons are paired by seed within scenario. PDR uncertainty is assessed from the 20 independent seed-level replication units; time samples are not treated as independent replications.

## Mean PDR by scenario
| Scenario | AODV | DSDV | DSR | OLSRv1 |
|---|---:|---:|---:|---:|
| BASE | 0.6075 | 0.4130 | 0.6090 | 0.3905 |
| FAST | 0.3485 | 0.2080 | 0.3675 | 0.1840 |
| LOAD | 0.6238 | 0.4016 | 0.5738 | 0.3900 |
| SCALE | 0.3990 | 0.1815 | 0.2365 | 0.1240 |

## Paired PDR findings
AODV versus DSR is not cleanly separated in BASE (mean paired difference -0.0015; bootstrap 95% CI -0.1170 to 0.1255), FAST (-0.0190; -0.1305 to 0.0850), or LOAD (0.0500; -0.0506 to 0.1608). In SCALE, the paired difference is 0.1625 with bootstrap 95% CI 0.0280 to 0.2950; Holm-adjusted Wilcoxon p=0.0437.

AODV exceeds DSDV and OLSRv1 in paired PDR in all four frozen scenarios under this benchmark, with bootstrap intervals excluding zero and Holm-adjusted Wilcoxon p<0.01 in each comparison. DSR exceeds DSDV and OLSRv1 in BASE, FAST, and LOAD under the same analysis; SCALE comparisons involving DSR are less stable after multiplicity correction.

## Ranking stability
Seed-level rank-1 membership changes substantially. Strict rank-1 fractions for AODV/DSR are BASE 0.35/0.55, FAST 0.50/0.45, LOAD 0.40/0.45, SCALE 0.65/0.15. Therefore the evidence does not support a single universal winner claim.

## Failure/zero-delivery signal
Zero-PDR frequency rises under SCALE: AODV 2/20, DSDV 7/20, DSR 8/20, OLSRv1 8/20. This is a stress/failure signal for the frozen scale scenario, not yet a formal failure frontier; a frontier claim requires a predeclared threshold and denser condition sweep.

## Gate decision
Gate 6 confirmatory comparison is substantially complete for the frozen S2 design. Formal continuous failure-frontier claims remain unsupported by only four discrete scenarios and must not be overstated. The next gate is literature/comparability synthesis and G-CAP determination. A new routing algorithm is not justified solely by these classical-protocol comparisons.
