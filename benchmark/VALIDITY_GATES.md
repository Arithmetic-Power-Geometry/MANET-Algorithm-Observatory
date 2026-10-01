# Controlled Benchmark Validity Gates

## V-G1 Simulator identity
Exact ns-3 release and source revision are recorded.

## V-G2 Implementation identity
Every result identifies the evaluated implementation, not only the abstract protocol name.

## V-G3 Scenario identity
All condition-defining parameters are serialized with the result.

## V-G4 Randomness identity
Seed, run number, and assigned random streams are recorded sufficiently to reproduce a run.

## V-G5 Metric admissibility
A metric is reported only when its required numerator, denominator, event timing, or trace source is directly measured under a common definition.

## V-G6 Cross-protocol measurement equivalence
The measurement path must not favor or exclude a protocol. DSR-specific FlowMonitor constraints therefore prevent FlowMonitor from serving as the sole common Tier-1 measurement layer.

## V-G7 Replication
Confirmatory comparisons use a frozen multi-seed policy. Single-run values are never inferential evidence.

## V-G8 Condition-indexed interpretation
Comparative conclusions remain attached to the evaluated operating condition.

## V-G9 Negative-result retention
Null differences, ranking reversals, failed scenarios, and unstable estimates remain in the evidence record.

## V-G10 Smoke/confirmatory separation
Upstream example output validates execution only. It is not promoted into the final performance benchmark without the confirmatory instrumentation and scenario contract.
