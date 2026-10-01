# S2 Confirmatory Analysis

The controlled S2 analysis comprises 4 protocols × 4 pre-specified scenarios × 20 predeclared seeds = 320 validated protocol-scenario-seed runs.

## Statistical unit

The experimental unit is one protocol-scenario-seed run. Pairwise comparisons are matched by seed. Reported uncertainty uses 10,000-resample bootstrap 95% intervals, paired Wilcoxon tests with Pratt treatment of zeros, and Holm adjustment within each scenario family.

## AODV versus DSR

The analysis does not provide evidence of a reproducible directional separation in BASE, FAST, or LOAD:

- BASE: mean paired difference -0.0015; 95% CI [-0.1170, 0.1255]; adjusted p = 0.8638
- FAST: -0.0190; [-0.1305, 0.0850]; adjusted p = 0.8960
- LOAD: 0.0500; [-0.0506, 0.1608]; adjusted p = 1.0000

Under SCALE, the paired AODV-minus-DSR difference is 0.1625 with 95% CI [0.0280, 0.2950] and Holm-adjusted p = 0.0437.

## Ranking stability

Strict rank-1 fractions for AODV/DSR are:

- BASE: 0.35 / 0.55
- FAST: 0.50 / 0.45
- LOAD: 0.40 / 0.45
- SCALE: 0.65 / 0.15

The variation is condition-specific evidence and is not interpreted as a universal protocol ordering.

## Zero-delivery incidence

Under SCALE, zero-PDR counts are:

- AODV: 2/20
- DSDV: 7/20
- DSR: 8/20
- OLSRv1: 8/20

The four discrete scenarios support stress contrasts but do not establish a continuous failure frontier.

## Scope

The S2 benchmark is a bounded classical-protocol bridge under a common ns-3.47 measurement contract. Learning- and graph-based methods are synthesized from the literature and are not included in this controlled comparison because their training, observation, tuning, and implementation budgets are not equalized by the S2 contract.
