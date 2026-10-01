# Final benchmark tables — S2

These values come from the frozen S2 confirmatory design: 20 predeclared seeds per protocol per scenario. They are condition-specific evidence, not a universal protocol leaderboard.

## BM-T01 — Mean PDR

| Scenario | AODV | DSDV | DSR | OLSRv1 |
|---|---:|---:|---:|---:|
| BASE | 0.6075 | 0.4130 | 0.6090 | 0.3905 |
| FAST | 0.3485 | 0.2080 | 0.3675 | 0.1840 |
| LOAD | 0.6238 | 0.4016 | 0.5738 | 0.3900 |
| SCALE | 0.3990 | 0.1815 | 0.2365 | 0.1240 |

## BM-T03 — Strict seed-level rank-1 fraction

| Scenario | AODV | DSR | Interpretation |
|---|---:|---:|---|
| BASE | 0.35 | 0.55 | rank-1 membership varies by seed |
| FAST | 0.50 | 0.45 | near-balanced rank-1 membership |
| LOAD | 0.40 | 0.45 | neither protocol dominates seed-wise |
| SCALE | 0.65 | 0.15 | AODV more often rank-1 in this frozen scale condition |

Fractions do not necessarily sum to one because DSDV/OLSR can be rank-1 and ties can occur.

## BM-T04 — Zero-delivery incidence in SCALE

| Protocol | Zero-PDR runs | Total |
|---|---:|---:|
| AODV | 2 | 20 |
| DSDV | 7 | 20 |
| DSR | 8 | 20 |
| OLSRv1 | 8 | 20 |

This is a discrete stress indicator, not a continuous failure frontier.
