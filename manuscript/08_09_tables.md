# Sections VIII--IX Tables

## Table VIII-1. Frozen S2 design and mean PDR

| Scenario | Nodes | Area parameter (m) | Speed (m/s) | Rate (pkt/s) | AODV | DSDV | DSR | OLSRv1 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| BASE | 25 | 250 | 5 | 2 | 0.6075 | 0.4130 | 0.6090 | 0.3905 |
| FAST | 25 | 250 | 15 | 2 | 0.3485 | 0.2080 | 0.3675 | 0.1840 |
| LOAD | 25 | 250 | 5 | 5 | 0.6238 | 0.4016 | 0.5738 | 0.3900 |
| SCALE | 50 | 354 | 5 | 2 | 0.3990 | 0.1815 | 0.2365 | 0.1240 |

Each protocol/scenario cell contains 20 predeclared seed-level replications.

## Table IX-1. Paired AODV-minus-DSR PDR

| Scenario | Mean difference | Bootstrap 95% CI | Holm-adjusted Wilcoxon p |
|---|---:|---:|---:|
| BASE | -0.0015 | [-0.1170, 0.1255] | 0.8638 |
| FAST | -0.0190 | [-0.1305, 0.0850] | 0.8960 |
| LOAD | 0.0500 | [-0.0506, 0.1608] | 1.0000 |
| SCALE | 0.1625 | [0.0280, 0.2950] | 0.0437 |

## Table IX-2. Strict rank-1 fraction

| Scenario | AODV | DSR |
|---|---:|---:|
| BASE | 0.35 | 0.55 |
| FAST | 0.50 | 0.45 |
| LOAD | 0.40 | 0.45 |
| SCALE | 0.65 | 0.15 |

DSDV/OLSRv1 may account for remaining rank-1 outcomes; ties can also occur.

## Table IX-3. Zero-delivery incidence under SCALE

| Protocol | Zero-PDR runs | Replications |
|---|---:|---:|
| AODV | 2 | 20 |
| DSDV | 7 | 20 |
| DSR | 8 | 20 |
| OLSRv1 | 8 | 20 |

These counts are stress indicators, not a continuous failure frontier.
