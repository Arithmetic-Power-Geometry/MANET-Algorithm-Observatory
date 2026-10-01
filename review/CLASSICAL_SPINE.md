# Classical MANET Routing Spine

This document records the mechanism-level backbone that later literature families will be mapped onto.

## Evolutionary chain

### DSDV — freshness before demand
**Problem:** classical distributed Bellman-Ford behavior is problematic under broken and changing links.

**Mechanism:** destination sequence numbers order routing information by freshness while nodes periodically advertise routing state.

**Capability gained:** loop-safe distance-vector routing for dynamic ad hoc networks.

**Cost exposed:** maintaining fresh routes consumes control capacity even when many routes are unused.

**Next question:** can route state be acquired only when communication needs it?

### AODV — demand before maintenance
**Problem:** proactive maintenance spends resources on inactive destinations.

**Mechanism:** route requests/replies discover routes on demand while destination sequence numbers preserve freshness and loop freedom.

**Capability gained:** no requirement to maintain routes to inactive destinations.

**Cost exposed:** route discovery and rediscovery become visible latency/control costs when topology churn is high.

**Next question:** can useful route knowledge be retained or diversified without paying continuous global maintenance?

### DSR — source-controlled cached paths
**Problem:** obtain routes entirely on demand with minimal periodic routing traffic.

**Mechanism:** route discovery, route maintenance, route caches, and complete source routes carried in packets.

**Capability gained:** sender control and multiple cached routes without periodic table exchange.

**Cost exposed:** source-route headers grow with path length and cached knowledge can age under mobility.

### OLSR — proactive availability with selective flooding
**Problem:** classic link-state flooding is costly in dense wireless networks.

**Mechanism:** multipoint relays reduce redundant control forwarding and topology advertisement.

**Capability gained:** routes are immediately available while flooding is reduced relative to naive link state.

**Cost exposed:** topology/control state is still continuously maintained; behavior depends on neighborhood structure and MPR selection.

### ZRP — make locality a control knob
**Problem:** purely proactive and purely reactive designs occupy opposite sides of a maintenance/search tradeoff.

**Mechanism:** proactive routing inside a radius-defined zone; reactive discovery outside it.

**Capability gained:** explicit tunability between local preparedness and global search.

**Cost exposed:** the appropriate zone radius is condition-dependent.

**Frontier hypothesis:** a fixed radius may be dominated when mobility, route demand, or density changes faster than the chosen radius adapts.

### TORA — localize the reaction
**Problem:** topology changes can trigger far-reaching recomputation/control.

**Mechanism:** link reversal builds a destination-oriented directed structure and attempts to localize reactions to failures.

**Capability gained:** loop-free multipath routing with localized maintenance.

**Cost exposed:** richer temporal/reference-level state and synchronization/order assumptions complicate implementation and evaluation.

### AOMDV — keep alternatives ready
**Problem:** single-path on-demand routing can repeatedly rediscover routes after path failures.

**Mechanism:** maintain multiple loop-free, disjoint alternate paths during discovery.

**Capability gained:** faster recovery from mobility-induced route failure.

**Cost exposed:** additional path state and the possibility that alternate paths become correlated or stale.

### OLSRv2 — metric-aware proactive modernization
**Problem:** OLSRv1 is hop-count-centered and uses an older signaling framework.

**Mechanism:** retains MPR principles while allowing non-hop metrics and more flexible signaling.

**Capability gained:** standards-track metric-aware proactive routing.

**Cost exposed:** proactive state/signaling costs remain; simulator support is less uniform than for OLSRv1.

### Babel — loop avoidance with dynamic reconvergence
**Problem:** distance-vector reconvergence can create loops/black holes.

**Mechanism:** feasibility-based loop avoidance with update/request mechanisms.

**Capability gained:** standards-track routing intended to remain robust in dynamic wireless mesh environments.

**Cost exposed:** direct MANET comparison requires a carefully verified implementation and metric configuration.

## First benchmark spine

Tier T1 is the minimum reproducible classical comparison target:

```
DSDV ↔ AODV ↔ DSR ↔ OLSR ↔ AOMDV
```

AODV, DSDV, DSR, and OLSR have documented ns-3 model support. AOMDV requires implementation verification before admission.

Tier T2 is the extension layer:

```
ZRP ↔ TORA ↔ OLSRv2 ↔ Babel
```

These methods are scientifically important but must not be silently substituted with non-equivalent implementations.

## Initial falsifiable hypotheses

**H1 — maintenance/search crossover.** As active route demand increases while topology churn remains moderate, proactive maintenance should become more competitive with reactive discovery.

**H2 — churn frontier.** Increasing link churn should increase reactive rediscovery/repair burden, but the location of the crossover depends on traffic demand and propagation assumptions.

**H3 — density frontier.** OLSR's MPR mechanism should alter the scaling of flooding cost with density relative to unoptimized dissemination, but dense connectivity alone does not imply end-to-end superiority.

**H4 — multipath frontier.** AOMDV should benefit when alternate paths remain sufficiently independent and valid; its advantage should contract when failures are spatially correlated or alternatives stale together.

**H5 — model-induced ranking instability.** Algorithm ranking is not invariant to propagation/connectivity modeling and must be measured rather than assumed.

These are hypotheses for controlled testing, not conclusions.
