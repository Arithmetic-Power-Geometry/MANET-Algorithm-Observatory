# Smoke Validation vs Confirmatory Benchmark

## Smoke validation

The upstream ns-3.47 `manet-routing-compare` example is used only to establish:
- simulator build reproducibility;
- successful execution of AODV, DSDV, DSR and OLSRv1;
- common scenario execution;
- raw-output capture;
- deterministic provenance;
- initial cross-protocol measurement sanity.

The upstream default scenario is not treated as sufficient evidence for a journal-level performance conclusion.

## Confirmatory benchmark

The confirmatory benchmark will use an Observatory-controlled runner with frozen:
- node count and geometry factors;
- mobility model and mobility intensity;
- traffic demand and offered load;
- propagation/channel model;
- simulation duration and warm-up;
- independent seeds;
- metric definitions;
- implementation parameters;
- statistical analysis.

## Scientific separation

Smoke outputs answer:
**Can all admitted implementations be executed and measured reproducibly?**

Confirmatory outputs answer:
**How does performance change across controlled operating regimes, with uncertainty and fairness constraints?**

No smoke-test ranking may appear as a substantive algorithm ranking in the paper.
