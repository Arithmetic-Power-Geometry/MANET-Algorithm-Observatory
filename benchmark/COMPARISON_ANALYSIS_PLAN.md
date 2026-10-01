# Confirmatory Comparison Analysis Plan

## Principle

All comparisons are condition-indexed. There is no universal winner variable.

## Run validity

A run is excluded from confirmatory analysis when required raw output is missing, simulator execution fails, application accounting is invalid, provenance is incomplete, or the scenario identity does not match the contract.

## Within-condition summaries

For each protocol and scenario, analysis retains the number of valid seed-level replications and reports the metric summaries required by the comparison.

## Pairwise effects

Pairwise PDR analysis uses seed-matched absolute differences, bootstrap 95% confidence intervals, paired Wilcoxon tests with Pratt treatment of zeros, and Holm adjustment within each scenario family.

The replication unit is the protocol-scenario-seed run; packet-level observations within a run are not treated as independent replications.

## Ranking stability

Seed-level rank membership is retained because protocol ordering can vary across random realizations and operating conditions.

## Zero-delivery incidence

Complete-delivery failure is summarized separately from mean PDR so that a lower mean is not interpreted as a formal failure frontier.

## Reporting rule

Every controlled claim retains implementation identity, scenario, metric definition, replication unit, uncertainty, and the relevant comparison boundary.
