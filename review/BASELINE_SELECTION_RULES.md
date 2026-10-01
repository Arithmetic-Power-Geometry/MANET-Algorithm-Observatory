# Scientific Baseline Selection

## Why baseline selection matters

A proposed MANET algorithm can appear strong simply because weak, old, or mismatched comparators were selected. The Observatory therefore treats baseline selection as part of the scientific hypothesis.

## Mandatory baseline roles

For a new method, select baselines by role rather than by a fixed count.

### B1 — Historical anchor
A well-understood classical protocol relevant to the operating regime.

### B2 — Mechanism-nearest baseline
The existing method whose routing decision and information requirements most closely match the proposal.

### B3 — Strong conventional baseline
A mature non-learning/non-proposed-family method appropriate to the same problem.

### B4 — Recent reproducible baseline
A recent method addressing the same capability, admitted only if its implementation can be verified.

### B5 — Component ablations
Remove or replace each claimed novel mechanism.

### B6 — Cost-matched control
Where feasible, compare against a method/control with similar state, compute, communication, or feature budget.

## Baseline admission questions

A comparator is scientifically useful only if we can answer:
- What hypothesis does it test?
- Is its implementation faithful?
- Is it tuned fairly?
- Does it solve the same task?
- Does it receive comparable information?
- Is the evaluation budget comparable?
- Are metric definitions identical?

## Information fairness

If a new method observes information unavailable to a baseline, the comparison must disclose the information advantage.

Define an information set I(A). A claimed algorithmic gain is interpreted together with:

```
I(new) versus I(baseline)
```

This prevents extra sensing/global state from being mislabeled as purely algorithmic superiority.

## Cost fairness

For each method record:
- control messages/bytes;
- stored state;
- computational work;
- training cost where applicable;
- inference cost;
- extra sensing/location requirements.

## No cherry-picked benchmark

The final confirmatory benchmark is frozen before confirmatory results are inspected.
