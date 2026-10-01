# Experimental Provenance Admission Gate

A run may enter an Observatory comparison artifact only when all applicable gates pass.

1. Frozen simulator version matches the benchmark contract.
2. Protocol selector matches the checked-out simulator source interface.
3. Protocol implementation identity is recorded.
4. Configuration succeeds.
5. Required target builds successfully.
6. Simulation exits successfully.
7. Output schema validates.
8. Required raw artifacts and logs exist.
9. Scenario/seed/run identity is recorded for inferential experiments.
10. The run is not marked superseded, invalidated, or excluded.

A CSV file by itself is not evidence.

Smoke evidence validates execution and provenance only. It cannot be promoted to confirmatory performance evidence.

Any superseded run remains in provenance history but is excluded from quantitative synthesis.
