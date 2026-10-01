# MANET Algorithm Observatory

Reproducible research software and evidence artifacts supporting the study **Evolution and Evidence in MANET Routing: From Classical Protocols to Graph Learning**.

The repository separates published evidence from controlled evidence and preserves the data structures, benchmark contracts, simulator configuration, validation workflows, and analysis artifacts used to support condition-indexed comparison of MANET routing methods.

## Scope

The evidence architecture covers classical proactive and reactive routing, hybrid and multipath routing, geographic and QoS-aware routing, security and energy-aware methods, metaheuristics, machine learning, reinforcement learning, graph learning, distributed intelligence, deployment evidence, and reproducibility.

The literature layer is organized into 31 workstreams under a common extraction framework. Registered studies and deeper structured evidence records are maintained separately from bibliography size so that coverage responsibility, evidence registration, and structured extraction are not conflated.

## Evidence model

Three independent dimensions delimit inference:

- **Verification (V0--V4):** discovery through synthesis/artifact admission.
- **Comparability (C0--C4):** definition-level evidence through controlled common-contract comparison.
- **Maturity (E0--E8):** definition through demonstration, comparative simulation, reproducibility, robustness, generalization/stress, testbed, field evidence, and independent replication.

These dimensions are evidence descriptors, not protocol-performance scores.

## Controlled benchmark

The confirmatory S2 benchmark evaluates AODV, DSDV, the evaluated ns-3 DSR implementation, and OLSRv1 under a common protocol-independent measurement contract in ns-3.47.

- 4 protocols
- 4 pre-specified scenarios
- 20 predeclared seeds per protocol and scenario
- 320 validated confirmatory runs

The benchmark is a bounded classical-protocol bridge. It does not validate the complete taxonomy and does not establish a universal protocol ordering.

The primary AODV-versus-DSR result is condition-dependent: BASE, FAST, and LOAD do not provide evidence of a reproducible directional separation, while SCALE yields a paired AODV-minus-DSR packet-delivery-ratio difference of 0.1625 with bootstrap 95% CI [0.0280, 0.2950] and Holm-adjusted Wilcoxon p = 0.0437.

## Repository structure

- `review/` — review protocol, corpus construction, evidence definitions, and scope controls
- `literature/` — registered studies, structured evidence, comparability/maturity atlas, contradiction registry, and research obligations
- `benchmark/` — scenario, metric, provenance, seed, and statistical contracts
- `sim/ns3/` — ns-3.47 benchmark runner
- `scripts/` — validation, parsing, summarization, and release-audit utilities
- `artifacts/` — versioned controlled-analysis outputs
- `.github/workflows/` — reproducible validation and confirmatory-run workflows

## Reproducibility

Controlled results retain implementation identity, simulator version, scenario parameters, random seed, mobility and channel assumptions, traffic configuration, metric definitions, and analysis provenance. Literature evidence and controlled benchmark evidence remain distinct datasets.

## Citation

Akhtar, M. A. K. (2026). *Evolution and Evidence in MANET Routing: From Classical Protocols to Graph Learning* (Version V1). Zenodo. https://doi.org/10.5281/zenodo.23085033

## Copyright

Copyright © 2026 Mohammad Amir Khusru Akhtar.
