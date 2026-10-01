# Controlled Result Reporting Standard

## Required sentence structure

**Under [condition], [implementation] produced [effect] on [metric] relative to [comparator], with [uncertainty/statistical evidence].**

## Examples of admissible interpretation

- "Under high mobility in the specified Random Waypoint regime, the evaluated AODV implementation exhibited a higher packet-delivery ratio than the evaluated OLSRv1 implementation."
- "The ordering was not stable after changing the propagation assumption."
- "The available replications do not establish a practically meaningful difference under this condition."

## Inadmissible interpretation

- "AODV is the best MANET routing protocol."
- "OLSR is unsuitable for high mobility."
- "DSR is inferior."
- "Protocol X is robust" when robustness was not stress-tested.

## Implementation qualifier

Where simulator fidelity is incomplete or implementation-specific, results are attributed to the evaluated implementation.

## Negative and null evidence

Null effects, reversals, failed runs, unstable estimates, and implementation limitations are retained. They are not removed because they weaken a preferred narrative.
