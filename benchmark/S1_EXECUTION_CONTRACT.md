# S1 Pilot Execution Contract

S1 begins only after the common engineering runner passes the same validation contract for AODV, DSDV, DSR, and OLSRv1.

## Execution unit
A single ns-3.47 checkout and release build is reused for the complete S1 batch. The exact Observatory commit is embedded in every output row.

## Frozen inputs
- Protocols: AODV, DSDV, DSR, OLSRv1 (ns-3 implementations)
- Seeds: benchmark/S1_PILOT_SEEDS.csv
- Factor definitions: benchmark/PILOT_FACTOR_DESIGN.csv
- Metric definitions: benchmark/METRIC_FORMULAE.md
- Output contract: benchmark/COMMON_RUN_OUTPUT_SCHEMA.csv

## Required pipeline
1. Checkout the exact Observatory commit and ns-3.47.
2. Build the Observatory runner once.
3. Execute every admitted protocol × seed × S1 scenario combination with identical executable and scenario parameters.
4. Validate every raw CSV independently before aggregation.
5. Preserve failed runs and their diagnostics; never silently replace a failed seed.
6. Aggregate only rows that pass the frozen validity contract.
7. Produce a manifest containing commit, ns-3 version, scenario, protocol, seed, run number, raw artifact path, and validity.
8. Upload raw results, validation manifest, and aggregate pilot artifact.
9. Use S1 only for feasibility, runtime, instrumentation, and variance estimation. Do not make protocol-superiority claims from S1.
10. Freeze S2 replication count and confirmatory scenario values before inspecting S2 effects.

## Admission gate
S1 results are not paper evidence until the pilot gate is closed and S2 is frozen. S1 may determine feasibility and replication requirements, but must not be used to select favorable protocols, seeds, scenarios, or effect directions.
