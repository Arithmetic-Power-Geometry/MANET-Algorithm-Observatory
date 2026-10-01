# Evidence Review Protocol

## Scope

The review covers mobile ad hoc network routing from foundational proactive and reactive mechanisms through hybrid, multipath, geographic, QoS-aware, energy-aware, security-aware, metaheuristic, machine-learning, reinforcement-learning, federated, multi-agent, and graph-based approaches.

## Review design

The review combines mechanism-centered synthesis, decision-centered taxonomy, experimental-design audit, reproducibility audit, claim-comparability audit, condition-specific gap analysis, and controlled reproduction for a bounded classical benchmark.

The primary population is MANET routing. VANET, FANET, WSN, DTN, mesh, IoT, and related studies are retained only as transfer or boundary evidence unless they directly include the MANET population.

## Corpus construction

Source discovery proceeds in four stages:

1. protocol specifications and foundational papers anchor mechanism identity;
2. recent reviews establish terminology, candidate primary studies, and non-redundancy;
3. backward and forward citation tracing expands primary-study coverage;
4. implementation repositories and simulator documentation are inspected separately from publication claims.

Bibliographic identity is resolved preferentially by DOI or RFC; otherwise, normalized title, year, and first author are used for deduplication. Preprints and final publications are linked rather than counted as independent evidence unless they contain materially different experiments.

The review uses conceptual saturation rather than exhaustive enumeration. Search continues when a source reveals a previously unrepresented mechanism, information scope, temporal mode, deployment regime, or materially conflicting result, and stops when additional sources repeat already represented mechanism classes without changing the synthesis.

Because the review did not use a single database-enumeration stage with a recorded retrieval total, database-specific hit counts and a PRISMA-style identification flow are not reported.

## Evidence extraction

Empirical claims retain their experimental context, including algorithm or protocol, baseline, scenario, node count, geometry or density, mobility, speed, traffic and load, radio/MAC/propagation, simulator or testbed, duration, randomization, replication, metric definition, effect, uncertainty, implementation source, artifact availability, and limitations.

## Verification states

- **V0** — discovery
- **V1** — bibliographic verification
- **V2** — cited-role verification
- **V3** — structured extraction
- **V4** — synthesis/artifact admission

Sources with unresolved bibliographic identity, scope, or experimental context remain at the lower verification or comparability state rather than being promoted by inference.

## Comparability states

- **C0** — definition or mechanism evidence only
- **C1** — qualitative comparison only
- **C2** — partial comparability with material nuisance differences
- **C3** — core scenario, metric definition, implementation identity, and major assumptions align, but evidence was not produced under one shared or explicitly matched controlled contract
- **C4** — common-contract or explicitly matched controlled evidence with aligned scenario realization, metric definition, implementation provenance, and replication unit

## Evidence maturity

Evidence maturity is tracked independently from verification and comparability:

- **E0** definition
- **E1** demonstration
- **E2** comparative simulation
- **E3** reproducible comparison
- **E4** robustness evidence
- **E5** generalization or stress evidence
- **E6** emulation or testbed evidence
- **E7** field evidence
- **E8** independent replication

These dimensions are evidence descriptors and are not aggregated into a protocol-performance score.

## Research obligations

The evidence synthesis tracks unresolved obligations including robustness, evaluation coverage, out-of-distribution generalization, resource cost, simulation-to-real correspondence, seed-level uncertainty, and demonstrated capability gaps. A capability-gap claim requires controlled evidence that an existing mechanism fails to supply a defined capability under explicit information and resource constraints.
