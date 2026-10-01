# Foundation Review Paper Blueprint

## Working concept

**A systematic evidence atlas of MANET routing: mechanisms, evaluation validity, reproducibility, failure frontiers, and open capability space.**

The paper should not be written as an encyclopedia of protocol names. Its organizing unit is the **routing decision and the evidence supporting performance claims**.

## Recommended structure

1. Introduction — why another MANET review is necessary
2. Review protocol and evidence model
3. Evolution of MANET routing decisions
4. Unified routing ontology
5. Classical routing families
6. Optimization, energy, QoS, trust, and security extensions
7. Learning-based routing: ML → RL → DRL → MARL → GNN
8. Experimental practices across the literature
9. Comparability audit: when published numbers can and cannot be compared
10. Reproducibility and artifact audit
11. Mobility, propagation, topology, and traffic realism
12. Cost audit: control, compute, communication, energy, training, inference
13. Generalization and sim-to-real evidence
14. Contradiction map and ranking instability
15. Evidence-gap atlas
16. Benchmark specification motivated by the review
17. Research agenda organized by capability gaps
18. Threats to validity
19. Conclusion

## Distinguishing contribution

The review separates:

```
reported superiority
        ≠
comparable superiority
        ≠
reproduced superiority
        ≠
robust superiority
        ≠
universal superiority
```

The review therefore avoids producing a universal algorithm ranking from heterogeneous published values.

## Novel-algorithm gate

A new routing algorithm is proposed only after the benchmark identifies a stable unresolved capability gap. The new method is then evaluated against the protocols that define the relevant frontier, under the same scenario and statistical contract.

## Paper-writing gate

Full paper prose is deferred until:
- literature corpus is frozen for the review version;
- extraction validation is complete;
- taxonomy is stable;
- evidence matrices are generated;
- benchmark algorithms are selected;
- controlled comparisons are complete for reproducible methods;
- gap claims have evidence links;
- all figures/tables are generated from versioned scripts.
