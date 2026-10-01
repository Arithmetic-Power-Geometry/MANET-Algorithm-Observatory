# MANET Researcher Field Guide

## The five-minute use case

A researcher entering a MANET routing problem should be able to use the Observatory in this order:

1. **Locate the problem regime** — mobility, scale, density, traffic, propagation, energy, adversary, deployment.
2. **Locate the routing decision** — next hop, route discovery, route repair, multipath choice, metric selection, prediction, trust, resource allocation.
3. **Identify occupied mechanism families** — classical, hybrid, multipath, geographic, optimization, learning, cross-layer.
4. **Identify mandatory baselines** — historical anchor, mechanism-nearest competitor, strongest reproducible relevant method.
5. **Inspect evidence maturity** — simulation, reproducibility, testbed, field, generalization.
6. **Inspect known failure/frontier evidence.**
7. **Inspect open obligations** — what experiment would resolve the gap?
8. Only then design a new method.

## Researcher questions answered by the atlas

### "I have a new MANET algorithm. What should I compare with?"
Use the baseline-selection matrix. A baseline is selected because it tests a scientific claim, not because it is easy to beat.

### "Has my idea already been tried?"
Search by decision role + information scope + temporal mode + mechanism, not only algorithm name.

### "Which algorithm is best?"
There is no context-free answer. Inspect conditional evidence and, after Observatory experiments exist, the applicability/frontier maps.

### "Where are the real gaps?"
Prefer G-CAP (demonstrated capability gap) over G-LIT (few papers).

### "Can I trust a reported improvement?"
Inspect comparability class, uncertainty, implementation provenance, propagation/mobility assumptions, and reproduction status.

## The status-card principle

Every important algorithm receives a one-page equivalent status card:

```
Identity
↓
Decision changed
↓
Information required
↓
Mechanism
↓
Capability
↓
Cost
↓
Evidence maturity
↓
Where tested
↓
Where not tested
↓
Known failure
↓
Closest alternatives
↓
Reproducibility
↓
Open obligations
```

The paper should make these cards visually scannable; the repository stores the full records.
