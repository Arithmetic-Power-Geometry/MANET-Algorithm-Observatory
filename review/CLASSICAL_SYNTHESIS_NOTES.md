# Classical Routing — Academic Synthesis Notes

These notes are evidence scaffolding, not manuscript prose.

## Proactive distance-vector routing

### DSDV
**Design problem.** Distributed distance-vector routing requires a mechanism for distinguishing fresh route information from stale information under topology change.

**Mechanism.** DSDV augments routing information with destination sequence numbers and distributes routing-table updates.

**Scientific interpretation.** Its principal contribution is not simply that it is "proactive"; it introduces an explicit freshness ordering into distributed route maintenance.

**Evidence boundary.** The foundational source establishes the mechanism. Contemporary comparative claims require separate empirical evidence.

**Transition.** Continuous maintenance motivates the question of whether route information should be acquired only when demanded.

## Reactive distance-vector routing

### AODV
**Design problem.** Maintaining routes to inactive destinations can consume control resources unnecessarily.

**Mechanism.** AODV discovers routes on demand through route-request/route-reply signaling and uses destination sequence numbers to preserve route freshness.

**Scientific interpretation.** AODV shifts cost from continuous maintenance toward demand-triggered discovery and repair.

**Research consequence.** The relevant comparison with proactive routing is therefore a conditional maintenance–discovery trade-off, not a universal protocol ranking.

## Reactive source routing

### DSR
**Design problem.** Establish on-demand paths while avoiding periodic routing advertisements.

**Mechanism.** Route discovery and maintenance are combined with route caches and source routes carried in packet headers.

**Scientific interpretation.** DSR relocates part of routing state from distributed next-hop tables to source-controlled path representations and cached knowledge.

**Research consequence.** Evaluation should expose path length, mobility, cache validity, and header cost rather than report packet delivery alone.

## Proactive link-state optimization

### OLSR
**Design problem.** Conventional link-state dissemination can create redundant control forwarding in dense wireless neighborhoods.

**Mechanism.** Multipoint relays select subsets of nodes for optimized dissemination and topology advertisement.

**Scientific interpretation.** OLSR does not remove proactive maintenance; it changes the structure of dissemination.

**Research consequence.** Density, neighborhood geometry, MPR selection, channel assumptions, and control overhead belong in any meaningful comparison.

## Reactive multipath routing

### AOMDV
**Design problem.** A single active route can force rediscovery immediately after failure.

**Mechanism.** AOMDV extends on-demand distance-vector routing to maintain multiple loop-free alternate paths.

**Scientific interpretation.** Multipath routing exchanges additional route state for repair resilience.

**Research consequence.** Its benefit should be tested against path independence, correlated failures, alternate-path staleness, and additional control/state cost.

## Cross-cutting validity result

Recent controlled evidence indicates that propagation-model choice can materially alter the relative conclusions drawn for AODV, OLSR, and DSDV. The review should therefore treat propagation configuration as part of the claim condition rather than as incidental simulator metadata.

## Synthesis principle

The classical families should be presented as **different allocations of routing cost and information**, not as a sequence of obsolete protocols:

- proactive methods pay before demand;
- reactive methods pay at discovery/repair;
- source routing pays in path representation/cache behavior;
- optimized link state pays in persistent neighborhood/topology maintenance;
- multipath methods pay for alternate-state resilience.

This mechanism-centered interpretation creates the bridge to optimization and learning methods, which likewise exchange additional information, computation, prediction, or training for routing capability.
