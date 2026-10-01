# Tier-1 Pilot Design Rules

## Objective

The pilot is not used to establish protocol superiority. It is used to:
- validate instrumentation;
- estimate runtime and variance;
- identify infeasible/saturated factor combinations;
- freeze exact factor values;
- determine confirmatory replication requirements.

## Factor logic

### Scale vs density
Node count and area are not treated as the same factor.

Two complementary regimes are required:
1. constant area while node count changes;
2. area scaled with node count to approximately preserve density.

This avoids attributing a density effect to network scale.

### Mobility
At least two mobility processes are used before robustness claims:
- Random Waypoint;
- Gauss-Markov.

Speed/intensity bands are frozen after feasibility testing, before confirmatory effect inspection.

### Load
Traffic load includes light, moderate, and stress regimes. A protocol advantage observed only near saturation is reported as such.

### Propagation
At minimum:
- Friis reference;
- LogDistance robustness condition.

A ranking that changes with propagation is treated as condition-dependent rather than contradictory.

## Pilot sampling

Do not execute the full Cartesian product initially.

Use a balanced screening subset that:
- covers every factor level;
- includes interaction-relevant corner cases;
- is identical across all four protocols;
- uses S1 seeds only.

The exact screening matrix is frozen before pilot execution.

## Confirmatory promotion

A factor/level is promoted to the confirmatory benchmark only if:
- simulation semantics are valid;
- measurement invariants pass;
- runtime is feasible;
- the level is scientifically interpretable;
- it does not duplicate another level without purpose.

All removals and changes are logged with reasons.
