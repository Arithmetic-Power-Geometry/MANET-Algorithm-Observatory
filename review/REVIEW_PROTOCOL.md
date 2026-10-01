# Systematic Evidence Review Protocol

## Scope

Mobile ad hoc network routing research, from foundational MANET routing mechanisms through modern optimization, learning, security-aware, energy-aware, and adaptive approaches.

## Review design

The review combines:

- systematic literature search and screening;
- mechanism-centered taxonomy;
- decision-centered taxonomy;
- experimental-design audit;
- reproducibility audit;
- claim-comparability audit;
- condition-specific gap mining;
- later controlled reproduction in the Observatory benchmark.

## Research questions

**RQ1 — Evolution.** How has the MANET routing problem evolved from classical topology-based routing to adaptive, optimization-based, and learning-based routing?

**RQ2 — Decision mechanism.** What decision does each protocol or algorithm make, what information does it require, and at what temporal/spatial horizon?

**RQ3 — Evaluation coverage.** Which mobility, density, scale, traffic, propagation, energy, failure, and adversarial regimes have actually been tested?

**RQ4 — Comparability.** Which published performance claims are directly comparable, partially comparable, or non-comparable?

**RQ5 — Reproducibility.** Which studies provide enough implementation and experimental detail to reproduce their claims?

**RQ6 — Robustness.** How sensitive are conclusions to mobility, propagation, topology, traffic, random seed, and implementation choices?

**RQ7 — Failure frontiers.** Where does each routing family begin to degrade or cease to satisfy an application constraint?

**RQ8 — Ranking stability.** When and why do pairwise or multi-algorithm rankings change across scenario conditions?

**RQ9 — Generalization.** For learned algorithms, how well do policies transfer across topology, scale, mobility, traffic, channel, and adversarial shifts?

**RQ10 — Cost.** What control, computation, communication, training, inference, memory, energy, and deployment costs accompany reported gains?

**RQ11 — Evidence gaps.** Which gaps are literature gaps, reproducibility gaps, evaluation gaps, contradiction gaps, or experimentally demonstrated capability gaps?

**RQ12 — Research opportunity.** Which verified capability gaps justify a new routing mechanism rather than another parameter-tuned variant?

## Study strata

The corpus is tagged by evidence stratum:

1. standards / protocol specifications;
2. foundational algorithm papers;
3. comparative experimental studies;
4. optimization/metaheuristic routing;
5. security/trust routing;
6. energy/QoS-aware routing;
7. ML/RL/DRL/MARL/GNN routing;
8. real-device/testbed studies;
9. systematic reviews/surveys;
10. reproducibility/benchmarking methodology.

## Inclusion criteria

A study is eligible when it materially addresses MANET routing or an algorithmic mechanism directly transferable to MANET routing and provides at least one of: mechanism definition, protocol specification, comparative evaluation, analytical result, reproducibility artifact, or empirical routing result.

## Exclusion criteria

Exclude items that only mention MANETs without routing relevance, lack enough technical detail to identify the routing mechanism, duplicate an already included version without additional evidence, or are inaccessible secondary descriptions where the primary source is available.

## Extraction principle

Do not extract a single "performance score" from heterogeneous papers. Extract the claim together with its experimental context.

Every empirical claim is represented as:

```
claim
algorithm
baseline
scenario
node_count
area_density
mobility_model
speed
pause_time
traffic
load
radio
mac
propagation_model
terrain_or_obstruction
energy_model
attack_model
simulator_or_testbed
duration
randomization
replications
metric
effect
uncertainty
implementation_source
artifact_availability
limitations
```

## Comparability classes

- **C0 — non-comparable:** materially different or insufficiently reported settings.
- **C1 — qualitative only:** mechanism-level comparison possible; numeric comparison invalid.
- **C2 — partially comparable:** several core conditions aligned but important nuisance variables differ.
- **C3 — strongly comparable:** core scenario, measurement definition, and experimental assumptions aligned.
- **C4 — controlled:** produced under the shared Observatory benchmark.

## Gap classes

- **G-LIT:** sparse or absent literature.
- **G-REP:** insufficient reproducibility.
- **G-EVAL:** important condition not evaluated.
- **G-CONTRA:** apparently conflicting claims requiring controlled resolution.
- **G-ROB:** result sensitive to nuisance assumptions.
- **G-GEN:** weak out-of-distribution/generalization evidence.
- **G-COST:** computational/communication/energy cost omitted.
- **G-REAL:** simulation-to-real evidence missing.
- **G-CAP:** controlled experiments demonstrate a capability failure that remains unresolved.

A candidate novel algorithm should primarily target **G-CAP**, ideally supported by G-CONTRA/G-ROB/G-GEN rather than only G-LIT.

## Review outputs

The review stage should generate:

- PRISMA-style screening flow;
- historical mechanism timeline;
- routing-family taxonomy;
- decision-authority taxonomy;
- evidence coverage matrix;
- baseline network;
- evaluation-practice audit;
- reproducibility matrix;
- propagation/mobility realism matrix;
- learning-generalization matrix;
- claim contradiction map;
- research-gap atlas;
- benchmark candidate list.

The later benchmark stage adds ranking-stability maps, Pareto fronts, sensitivity plots, failure frontiers, and novel-algorithm comparisons.
