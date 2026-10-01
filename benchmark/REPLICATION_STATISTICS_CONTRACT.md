# Replication and Statistical Analysis Contract

## Purpose

This contract is frozen before confirmatory performance results are inspected. Its purpose is to separate exploratory engineering from confirmatory inference and to reduce analysis choices made after observing favorable outcomes.

## Experimental units

A run is uniquely identified by:
- Observatory commit;
- ns-3 version;
- protocol implementation;
- scenario identifier;
- seed;
- run number;
- complete parameter manifest;
- metric-definition version.

Repeated measurements within one simulation are not treated as independent experimental replications.

## Development vs confirmatory runs

Development runs:
- diagnose instrumentation;
- determine feasible factor ranges;
- detect simulator/implementation failure;
- estimate runtime;
- do not support final comparative claims.

Confirmatory runs:
- use frozen scenarios, metrics and seed policy;
- are retained regardless of result direction;
- support the final comparative analysis.

## Replication policy

The final number of independent replications is selected before confirmatory execution using pilot variability and precision requirements, subject to computational feasibility.

The repository must record:
- rationale for replication count;
- seed list;
- any failed/censored run;
- reason for exclusion, if exclusion is scientifically necessary.

A failed run is never silently replaced.

## Descriptive reporting

For each protocol × condition × metric report, as appropriate:
- valid replication count;
- mean;
- median;
- standard deviation;
- interquartile range;
- confidence interval;
- minimum/maximum for diagnostic use.

Choice of central tendency must match the metric distribution and be documented.

## Pairwise comparison

For each predeclared comparison:
- absolute effect;
- relative effect where meaningful;
- uncertainty interval;
- inferential procedure appropriate to design/distribution;
- multiplicity handling where families of hypotheses are tested.

Statistical significance alone is not interpreted as practical importance.

## Effect size

Report a metric-appropriate effect size and its uncertainty wherever inferential comparison is used.

## Multiple conditions

Protocol ranking is treated as a function of condition. A global winner is not inferred by averaging incompatible operating regimes.

## Multi-objective comparison

Where metrics conflict, report Pareto efficiency or explicit application constraints. Do not construct an arbitrary weighted score merely to force a total ranking.

## Ranking stability

For each condition family, estimate how protocol ordering changes across:
- mobility intensity/model;
- node scale/density;
- offered load;
- propagation assumption.

A ranking reversal is reported only when the metric definition and comparison boundary remain consistent.

## Failure frontier

A failure frontier requires a predeclared operational requirement, such as a delivery, delay, or resource constraint. Thresholds must be motivated by an application requirement or clearly labeled as analytical thresholds.

## Missingness and failures

Record:
- simulator failure;
- instrumentation failure;
- zero-delivery regime;
- timeout;
- invalid configuration;
- missing artifact.

Missing runs are not imputed into performance results without a separately justified method.

## Reproducibility

Every final table/figure must be regenerable from immutable raw results through versioned analysis code.
