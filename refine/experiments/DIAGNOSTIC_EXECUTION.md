# P01 next diagnostic run — instrumentation prepared, NOT EXECUTED

The isolated instrumented runner is `refine/experiments/observatory_tier1_runner_diagnostic.cc`, copied from original `sim/ns3/observatory_tier1_runner.cc` and extended **without modifying the original**. Its purpose is diagnostic, not a new confirmatory result.

## Additions
- Record socket `GetErrno()` immediately after a negative UDP `SendTo` and aggregate integer error codes by run.
- Record source ID, sequence and scheduled attempt timestamp for every offered datagram.
- Fail if attempted packets != accepted + rejected, received unique packets > offered, or main CSV cannot be opened.
- Optional `--diagnosticPrefix` writes `-socket-errors.csv` and `-attempts.csv` files. No diagnostic files are written when the prefix is omitted.
- No change to original PDR numerator/denominator, protocol selection, mobility, PHY, traffic rate, or original benchmark source.

## How to run in an ns-3.47 checkout
1. Copy `observatory_tier1_runner_diagnostic.cc` into `scratch/observatory_tier1_runner_diagnostic.cc` of an ns-3.47 source checkout. Preserve original repository source.
2. Configure/build ns-3 according to the checkout's supported build instructions. Example: `./ns3 configure --enable-examples && ./ns3 build`. This command is illustrative, not a verified execution log.
3. For each of the four protocols and a fixed registered scenario/seed, run the scratch program with the original scenario values, `--protocol=AODV` (or DSDV/DSR/OLSR), `--seed=...`, `--run=...`, `--scenario=...`, `--nodes=...`, `--area=...`, `--ratePps=...`, `--speed=...`, `--output=...`, and `--diagnosticPrefix=...`. Pass options through the ns-3 `--run` argument according to your local version.
4. Validate with `python refine/experiments/check_diagnostics.py RUN_AODV.csv RUN_DSDV.csv RUN_DSR.csv RUN_OLSR.csv --prefixes PREFIX_AODV PREFIX_DSDV PREFIX_DSR PREFIX_OLSR`.
5. Record exact source commit, compiler and simulator version, build command, exit codes, raw CSVs and SHA-256 hashes. Compare errno codes with ns-3 socket error enumerations before attributing failures to route absence.

## Important limits
**No mobility traces or explicit RNG stream assignments have been added.** Traffic-attempt schedule equality is a narrower check than topology/mobility equality. It does not establish fair common-random-number pairing. Before claiming paired trace fairness, implement a separate, verified per-node mobility trace/replay protocol.

The current source retains the original hardcoded `PASS` output label, but now aborts on two basic accounting invariants. This is **not** a comprehensive independent validator; retain `UNKNOWN` for overall validity until a separate validator is run.

**Status:** source change committed; C++ compilation and ns-3 runtime diagnostics **NOT EXECUTED**. The local environment does not have ns-3.47. No new performance claim should enter the manuscript.
