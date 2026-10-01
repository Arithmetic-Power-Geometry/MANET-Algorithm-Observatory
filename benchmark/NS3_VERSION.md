# Frozen ns-3 Benchmark Version

## Canonical simulator
**ns-3.47**, released 2026-02-16.

Every result records the exact upstream release and Observatory commit. Changing simulator version after confirmatory evaluation begins requires a new benchmark version and compatibility audit.

## Tier-1 rationale
The upstream MANET comparison example supports AODV, DSDV, DSR, and OLSR. It also documents that FlowMonitor is not usable with DSR in that comparison path. Common primary metrics therefore require protocol-independent application accounting or another validated common trace layer.

## Freeze order
Simulator version -> runner source -> scenario contract -> metric definitions -> seed list -> confirmatory execution.
