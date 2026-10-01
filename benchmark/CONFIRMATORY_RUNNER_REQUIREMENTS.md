# Confirmatory Runner Requirements

## Purpose

The Observatory-controlled runner replaces the upstream example as the measurement source for confirmatory Tier-1 comparisons. The upstream example remains an execution/provenance smoke test.

## Required protocol set

- AODV
- DSDV
- DSR
- OLSRv1

All labels refer to the evaluated ns-3.47 implementations.

## Common application accounting

The runner must instrument the application boundary identically for every admitted protocol.

Per run record:
- application packets sent;
- application packets received;
- application payload bytes sent;
- application payload bytes received;
- matched packet send/receive timestamps or an equivalent validated packet identity;
- simulation measurement interval.

Derived only from those measurements:
- packet-delivery ratio;
- goodput;
- end-to-end delay distribution;
- jitter under one frozen definition.

## Routing/resource accounting

Where a metric can be measured equivalently across protocols, record:
- routing/control packets;
- routing/control bytes;
- route discovery/repair events with validated semantics;
- wall-clock runtime;
- peak memory where feasible.

Protocol-specific metrics may be retained but must not masquerade as common metrics.

## Scenario manifest

Every run serializes:
- protocol and implementation;
- ns-3 version;
- Observatory commit;
- scenario ID;
- node count;
- area/geometry;
- mobility model and all mobility parameters;
- traffic model;
- flow count;
- packet size;
- offered load;
- radio/MAC;
- propagation model;
- simulation duration;
- warm-up/measurement window;
- seed;
- run number;
- assigned random streams where applicable.

## Output contract

Each run emits:
1. immutable scenario manifest;
2. run-level metrics CSV;
3. optional packet/event-level diagnostic output;
4. stdout/stderr log;
5. exit status;
6. checksum/provenance manifest.

## Validation invariants

- 0 <= PDR <= 1;
- received packets <= sent packets at the same accounting boundary;
- goodput >= 0;
- delay/jitter cannot be reported without received matched packets;
- protocol/scenario labels in output must match invocation;
- all confirmatory rows carry seed/run/provenance;
- failed runs remain visible.

## Experimental separation

Engineering runner development may use S0 seeds.

Pilot variability uses S1.

Confirmatory inference uses frozen S2.

Held-out robustness uses disjoint S3.

No final claim may be based on S0 engineering smoke values.
