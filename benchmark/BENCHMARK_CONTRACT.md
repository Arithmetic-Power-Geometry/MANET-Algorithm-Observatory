# S2 Controlled Benchmark Contract

## Purpose

The S2 benchmark provides a bounded, protocol-independent comparison of four validated ns-3.47 routing implementations: AODV, DSDV, the evaluated ns-3 DSR implementation, and OLSRv1.

It is not a benchmark of the complete MANET literature and does not validate the complete taxonomy.

## Experimental configuration

The controlled configuration uses:

- ns-3.47;
- IEEE 802.11b in ad hoc mode;
- the ns-3 default Yans channel configuration;
- periodic UDP traffic from node 0 to the last node;
- a common IPv4 addressing plan;
- Random Waypoint mobility;
- uniformly sampled initial and waypoint positions;
- node speed uniformly sampled from 0 to the scenario-specific maximum;
- pause time of 1 s.

Packet delivery ratio is measured at the application boundary as uniquely matched received datagrams divided by offered application datagrams during the measurement interval. Socket acceptance does not alter the denominator.

## Confirmatory scenarios

| Scenario | Nodes | Area (m × m) | Max speed (m/s) | Offered rate (packets/s) | Payload |
|---|---:|---:|---:|---:|---:|
| BASE | 25 | 250 × 250 | 5 | 2 | 512 bytes |
| FAST | 25 | 250 × 250 | 15 | 2 | 512 bytes |
| LOAD | 25 | 250 × 250 | 5 | 5 | 512 bytes |
| SCALE | 50 | 354 × 354 | 5 | 2 | 512 bytes |

Each simulation lasts 60 s, with measurement traffic beginning at 10 s.

The same scenario parameters and predeclared seed set are used across all four protocol implementations. The ns-3 seed and run number are set before node creation. Application sender and receiver, metric definitions, and measurement interval remain protocol independent.

## Replication

Twenty predeclared seeds are used per protocol and scenario:

4 protocols × 4 scenarios × 20 seeds = 320 validated confirmatory runs.

## Statistical contract

The experimental unit is one protocol-scenario-seed run. Pairwise comparisons are matched by seed. Analysis reports absolute paired differences, 10,000-resample bootstrap 95% intervals, paired Wilcoxon tests with Pratt treatment of zeros, and Holm adjustment within each scenario family.

Statistical significance is not treated as practical importance, and no global winner is constructed by averaging incompatible operating regimes.

## Interpretation boundary

The benchmark supports condition-indexed comparison, seed-level ranking analysis, and discrete stress contrasts. It does not establish a universal protocol ranking, a continuous failure frontier, or learning-method generalization.
