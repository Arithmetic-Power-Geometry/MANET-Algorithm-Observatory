# Tier-1 Classical Benchmark Freeze

## Admitted native spine

The first controlled benchmark uses four protocols with official ns-3 MANET implementations:

- AODV
- DSDV
- DSR
- OLSR (version 1 / RFC 3626 family)

This is an implementation-provenance decision, not a claim that these are the four strongest protocols.

## Why these four

They provide a reproducible classical mechanism contrast:

| Protocol | Acquisition | Representation/control emphasis |
|---|---|---|
| DSDV | proactive | distance-vector table maintenance |
| AODV | reactive | on-demand distance-vector discovery/repair |
| DSR | reactive | source routing and route caching |
| OLSR | proactive | link-state dissemination optimized by MPRs |

## Explicit exclusion from Tier 1

### OLSRv2
The verified ns-3 OLSR model implements OLSRv1 and explicitly states that it is not compliant with OLSRv2. OLSRv2 therefore remains a literature/status object until a faithful implementation is verified.

### AOMDV
Scientifically important for multipath analysis, but an external implementation is not admitted until provenance, build reproducibility, and mechanism fidelity are verified.

## Benchmark interpretation

Tier 1 is the **native reproducibility spine**. It is not the final baseline set for every later algorithm.

Later tiers may add verified:
- multipath;
- geographic;
- QoS/energy/security;
- learning-based methods.

## Fidelity rule

The manuscript must name the exact evaluated implementation and specification relationship. It must never report an ns-3 OLSRv1 result as evidence for OLSRv2.
