# Tier-1 Smoke-Test Contract

## Purpose

Before any factorial or confirmatory benchmark is run, the Observatory must demonstrate that the four Tier-1 implementations execute under one canonical experiment contract and that protocol-specific instrumentation differences are understood.

## Tier-1 implementations

- AODV — official ns-3 model
- DSDV — official ns-3 model
- DSR — official ns-3 model
- OLSR — official ns-3 OLSRv1/RFC 3626-family model

## Smoke-test questions

For every protocol:
1. Does the selected ns-3 release configure and build cleanly?
2. Does the canonical MANET scenario complete without runtime failure?
3. Are application sent/received counters non-zero and internally consistent?
4. Can PDR, goodput, delay and jitter be computed from a protocol-independent application accounting layer?
5. Can routing-control packets and bytes be collected without conflating application traffic?
6. Are protocol-specific trace sources documented?
7. Are random seeds/run numbers recorded?
8. Is the complete command/configuration emitted with each result?
9. Does rerunning the same seed reproduce the same canonical result within deterministic expectations?
10. Are known model limitations recorded before admission to the large benchmark?

## Canonical smoke scenario

The exact numerical values remain provisional until implemented, but one identical scenario must be used for all four protocols:
- IPv4 ad hoc Wi-Fi;
- fixed node count;
- fixed rectangular area;
- Random Waypoint mobility;
- fixed speed/pause;
- UDP application traffic;
- fixed number of source-destination flows;
- fixed packet size/rate;
- fixed simulation duration and warm-up;
- one explicitly named propagation model;
- fixed seed and run number.

The smoke test is not scientific performance evidence. It is an implementation and measurement validation stage.

## DSR measurement gate

DSR must not be excluded merely because a generic measurement helper is inconvenient. Application-level accounting should be the primary common measurement layer. Any FlowMonitor incompatibility or semantic mismatch in the selected ns-3 release must be documented and either:
- bypassed with common application/trace instrumentation, or
- resolved with a validated protocol-independent measurement path.

## Pass condition

Tier-1 large-scale experiments remain blocked until all four protocols have:
- BUILD=PASS
- RUN=PASS
- COMMON_METRICS=PASS
- PROVENANCE=PASS
- LIMITATIONS=RECORDED
