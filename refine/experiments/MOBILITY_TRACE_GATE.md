# P01 mobility trace diagnostic gate (2026-11-08)

## Changes committed
- `observatory_tier1_runner_diagnostic.cc`: optional `--diagnosticPrefix` now emits `-mobility.csv` with (simulation_time_ns,node_id,x_m,y_m,z_m) at simulation time 0 and every `--mobilitySampleSeconds` seconds through the simulation end. Sampling is enabled only with a diagnostic prefix. The default sampling period is 0.5 seconds; it is not proof of continuous-path equality.
- `check_mobility.py`: checks schema, uniqueness, complete rectangular time×node sampling grid, identical time/node keys and coordinate agreement across 2+ traces. Prints SHA-256 hashes and fails on mismatches. Default tolerance is zero; a nonzero tolerance must be disclosed.
- Corrected a previous diagnostic runner defect: generated CSV strings had double-escaped newline sequences, which would have yielded literal backslash-n instead of line breaks. This was fixed in commit `a2aee37c4dda87b7489b2d6ffb9e570d57da2351`.

## Required execution
1. Compile the diagnostic scratch runner under the exact ns-3.47 environment and capture compiler output. Compilation **has not occurred here**.
2. For one frozen scenario and seed, run all four protocols with identical CLI arguments except protocol/output/prefix. Archive the original stdout/stderr and exit codes.
3. Run `python refine/experiments/check_diagnostics.py RUN_AODV.csv RUN_DSDV.csv RUN_DSR.csv RUN_OLSR.csv --prefixes PREFIX_AODV PREFIX_DSDV PREFIX_DSR PREFIX_OLSR`.
4. Run `python refine/experiments/check_mobility.py PREFIX_AODV-mobility.csv PREFIX_DSDV-mobility.csv PREFIX_DSR-mobility.csv PREFIX_OLSR-mobility.csv`.
5. Investigate OLSR socket errno counts. If sampled traces disagree, introduce fixed mobility trace replay or independent RNG streams before treating seed-wise contrasts as physically paired.
6. Even if sampled traces agree, record the limitation that sub-sampling cannot prove equal trajectories between sample times. A stronger replay design is still required for rigorous paired comparison.

## Scientific interpretation
These files are **diagnostic instrumentation and verification code only**. No ns-3 execution, error-code observations, mobility equality results, or new performance claims were produced. The original S2 confirmatory benchmark remains unchanged and retains its original limitations. P01 remains open; P02 is not started.
