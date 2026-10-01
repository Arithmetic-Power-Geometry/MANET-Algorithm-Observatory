# Common Runner Engineering Validation — COMMON-ENG-001

Workflow run: 36835523188  
Observatory commit: 7a2c916806d1fb0c7852e388e9ea88e08ef441d2  
ns-3: 3.47  
Scenario: engineering-common-001  
Seed/run: 12345 / 1

All four Tier-1 implementations completed and passed the synchronized output/metric validator.

The scenario offered 100 application datagrams per protocol. No application datagrams were delivered in this specific engineering scenario, so delay and jitter are undefined and goodput is zero. OLSRv1 synchronously rejected all 100 offered datagrams at SendTo, while AODV, DSDV, and DSR accepted all 100. This difference is retained as an engineering diagnostic only.

## Interpretation boundary

This is **not a performance ranking** and must not be cited as evidence that one routing protocol is superior or inferior. It is a single-seed engineering validation whose purpose is to verify build, execution, application-offered-load accounting, packet identity, duplicate suppression, CSV serialization, validation, artifact retention, and provenance.

Because no protocol delivered a packet, the next pilot stage must include at least one connectivity-feasible scenario that exercises received-packet identity, PDR, goodput, delay, and jitter before confirmatory benchmarking.
