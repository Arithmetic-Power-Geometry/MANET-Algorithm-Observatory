# Shared MANET Benchmark Contract

This contract is frozen before comparing a candidate novel algorithm.

## Design principle

The benchmark is factorial where computationally feasible and stratified where a full Cartesian product is prohibitive. Development/tuning scenarios must be separated from confirmatory evaluation scenarios.

## Core factors

### Scale
Candidate levels: 10, 25, 50, 100, 250, 500 nodes. Larger cases are added only for implementations that remain computationally feasible.

### Mobility
At least:
- static control;
- Random Waypoint;
- Gauss-Markov;
- group/reference-point mobility;
- one structured/trace-based mobility regime.

### Speed
Use multiple low/medium/high mobility bands appropriate to the selected mobility model. Exact values are recorded in scenario manifests.

### Density / geometry
Vary area and node count independently enough to distinguish scale effects from density effects.

### Traffic
At least:
- UDP/CBR;
- bursty UDP;
- TCP where protocol behavior warrants it;
- multiple source-destination concurrency levels.

### Load
Include light, moderate, high, and near-saturation offered load.

### Propagation
At least one idealized/open-field model and one more realistic obstruction/fading-sensitive configuration. Rankings are never reported without identifying the propagation configuration.

### Failures / security
Later benchmark layers include node/link failure and representative routing attacks for methods claiming resilience.

## Metrics

### Network performance
- packet delivery ratio;
- throughput/goodput;
- end-to-end delay;
- jitter;
- packet loss/drop reason;
- hop count/path stretch.

### Routing dynamics
- route discovery latency;
- route lifetime;
- route breaks;
- repairs;
- convergence/reconvergence time;
- normalized routing/control overhead;
- control bytes and packets.

### Resource cost
- energy per delivered packet/bit;
- network lifetime where meaningful;
- CPU/runtime;
- memory;
- model size;
- communication cost.

### Learning-specific
- training samples/episodes;
- wall-clock training cost;
- inference latency;
- seed variance;
- training stability;
- zero-shot/OOD transfer;
- retraining requirement.

## Statistics

Use independent random seeds. Report distributional summaries and uncertainty, not only single means. Pairwise tests and effect sizes are selected based on design and distributional assumptions. Multiple comparisons are corrected where appropriate.

## Fairness

- Same scenario realizations whenever implementations permit.
- Same traffic and mobility traces for paired comparison.
- Protocol-specific tuning is allowed only through a documented, predeclared tuning budget.
- Candidate method hyperparameters are fixed before confirmatory tests.
- Baselines may not be deliberately left at known-poor defaults when a documented standard configuration exists.

## Development versus confirmation

```
development scenarios ∩ confirmatory scenarios = ∅
```

where possible at the trace/seed level. Out-of-distribution tests deliberately alter topology, scale, mobility, traffic, channel, or attack regime.

## Interpretation

The benchmark does not declare a universal winner. It estimates conditional superiority, Pareto efficiency, ranking stability, and failure boundaries.
