# S2 Confirmatory Benchmark Tables

The S2 benchmark uses 20 predeclared seeds per protocol and scenario. Results are condition-specific and are not a universal protocol leaderboard.

## Mean packet delivery ratio

| Scenario | AODV | DSDV | DSR | OLSRv1 |
|---|---:|---:|---:|---:|
| BASE | 0.6075 | 0.4130 | 0.6090 | 0.3905 |
| FAST | 0.3485 | 0.2080 | 0.3675 | 0.1840 |
| LOAD | 0.6238 | 0.4016 | 0.5738 | 0.3900 |
| SCALE | 0.3990 | 0.1815 | 0.2365 | 0.1240 |

## Paired AODV-minus-DSR PDR

| Scenario | Mean difference | Bootstrap 95% CI | Holm-adjusted Wilcoxon p |
|---|---:|---:|---:|
| BASE | -0.0015 | [-0.1170, 0.1255] | 0.8638 |
| FAST | -0.0190 | [-0.1305, 0.0850] | 0.8960 |
| LOAD | 0.0500 | [-0.0506, 0.1608] | 1.0000 |
| SCALE | 0.1625 | [0.0280, 0.2950] | 0.0437 |

BASE, FAST, and LOAD do not provide evidence of a reproducible directional separation between AODV and DSR. Under SCALE, the paired difference is positive in this sample and remains distinguishable after Holm adjustment.

## Strict seed-level rank-1 fraction

| Scenario | AODV | DSR |
|---|---:|---:|
| BASE | 0.35 | 0.55 |
| FAST | 0.50 | 0.45 |
| LOAD | 0.40 | 0.45 |
| SCALE | 0.65 | 0.15 |

Rank-1 membership varies across seeds and operating conditions.

## Zero-delivery incidence under SCALE

| Protocol | Zero-PDR runs | Total |
|---|---:|---:|
| AODV | 2 | 20 |
| DSDV | 7 | 20 |
| DSR | 8 | 20 |
| OLSRv1 | 8 | 20 |

This is a discrete stress indicator and does not establish a continuous failure frontier.
