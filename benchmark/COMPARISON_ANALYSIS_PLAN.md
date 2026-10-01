# Tier-1 Comparison Analysis Plan

## Primary principle

The comparison is condition-indexed. There is no universal winner variable.

For protocol A under condition x, define a metric vector:

P_A(x) = [PDR, goodput, delay, jitter, control cost, discovery/repair behavior, runtime, memory]

## Analysis layers

### 1. Run validity
Reject/flag runs with:
- missing raw output;
- non-zero simulator exit;
- invalid application accounting;
- missing provenance;
- scenario mismatch.

### 2. Within-condition summaries
For each protocol × condition:
- number of valid replications;
- mean where appropriate;
- median where appropriate;
- standard deviation;
- confidence interval;
- distributional diagnostics.

### 3. Pairwise effects
For each metric and condition:
- effect direction;
- absolute difference;
- relative difference where meaningful;
- uncertainty;
- inferential test only after assumptions/test choice are frozen.

### 4. Multi-objective analysis
Identify Pareto-efficient protocols under each operating condition rather than collapsing all metrics into an arbitrary single score.

### 5. Ranking stability
Measure how pairwise ordering changes across:
- mobility;
- density/scale;
- load;
- propagation;
- seed uncertainty.

### 6. Failure frontiers
Define requirements before analysis, e.g.:
- minimum delivery reliability;
- maximum delay;
- maximum control/resource budget.

Estimate where a protocol crosses from satisfying to violating a requirement.

## Reporting rule

A result must always retain:
protocol + implementation + condition + metric definition + replication count + uncertainty.

A sentence such as "AODV outperforms OLSR" is inadmissible without the qualifying condition and metric.
