# Evidence Maturity Ladder

A protocol can be algorithmically sophisticated yet empirically immature. The review therefore reports evidence maturity separately from novelty.

## E0 — Definition
Mechanism/specification exists.

## E1 — Demonstration
Limited illustrative simulation or analytical example.

## E2 — Comparative simulation
Compared against meaningful baselines, but scenario/statistical breadth may be limited.

## E3 — Reproducible comparative evidence
Implementation, configuration, seeds/data, and analysis are sufficient for independent reproduction.

## E4 — Robustness evidence
Sensitivity across mobility, scale, density, traffic, propagation, seeds, and nuisance choices.

## E5 — Generalization / stress evidence
Held-out or out-of-distribution conditions; adversarial/failure stress where relevant.

## E6 — Emulation/testbed evidence
Physical or high-fidelity network testbed evidence.

## E7 — Field evidence
Operational mobile deployment evidence.

## E8 — Independent replication
Important claims reproduced by an independent group or implementation.

## Important rule

These levels are evidence descriptors, not quality scores or rankings. A method may have strong theoretical value while having low deployment maturity.

## Review visualization

Each family receives an evidence profile rather than one scalar score:

```
Simulation      █████
Reproducible    ███
Robustness      ██
Generalization  █
Testbed         █
Field
Replication
```

This immediately shows where a research family is mature and where evidence is missing.
