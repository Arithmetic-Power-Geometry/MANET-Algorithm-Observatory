# Source and Claim Policy

## Source hierarchy

For protocol definition and mechanism:
1. standards-track RFC or official specification;
2. original peer-reviewed algorithm paper;
3. authoritative project documentation;
4. later peer-reviewed analysis.

For empirical performance:
1. reproducible controlled experiment with accessible configuration/code/data;
2. peer-reviewed experiment with sufficient scenario detail;
3. non-reproducible numerical report;
4. qualitative claim.

Secondary summaries never override primary protocol specifications.

## Claim rule

Every extracted performance statement is conditional:

```
algorithm A compared with B
under scenario C
for metric M
using measurement definition D
with uncertainty U
```

If C, D, or U is unavailable, the missing field remains explicit. It is not inferred.

## No synthetic leaderboard

Numbers from heterogeneous studies are not pooled into a universal ranking. Published comparisons remain attached to their original scenario. Cross-study synthesis uses mechanism, direction, coverage, and comparability classes unless experimental alignment justifies quantitative synthesis.

## Implementation admission

An implementation enters the controlled benchmark only after:
- provenance is known;
- protocol identity/version is known;
- build is reproducible;
- smoke tests pass;
- major deviations from the defining specification are documented;
- required metrics can be collected consistently.

## Negative evidence

Failed reproduction, unavailable code, missing seed policy, contradictory results, and sensitivity to nuisance assumptions are retained as evidence rather than discarded.
