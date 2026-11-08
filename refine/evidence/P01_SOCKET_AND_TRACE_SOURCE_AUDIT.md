# P01 continuation — socket-rejection and trace-fairness source audit

Source inspected: [sim/ns3/observatory_tier1_runner.cc](../../sim/ns3/observatory_tier1_runner.cc), blob `6ec56f95213a1f9fb8f6830f6d4b1a425a4a0b3b`, and [benchmark/METRIC_FORMULAE.md](../../benchmark/METRIC_FORMULAE.md). This is **static source inspection**, not an ns-3 execution.

## Verified implementation facts
- Sender `StartApplication()` creates a UDP socket and calls `Bind()`; negative bind status causes early return.
- `Send()` constructs a packet with 20-byte `ObservatoryHeader`, increments `gTxAttempts` and `gOfferedBytes` **before** `mSocket->SendTo(p,0,mPeer)`.
- A nonnegative `SendTo` return increments `gTxAccepted`; a negative return increments `gTxRejected`. The code **does not record `GetErrno()`**, so the source and CSV do not reveal why a socket rejected an attempt.
- `gRxPackets` increments only after a packet with valid header and previously unseen (source ID, sequence number) is received. `pdr=gRxPackets/gTxAttempts`. This matches the benchmark's **offered application datagrams** denominator, so it is not inherently a metric-definition bug.
- `gRxBytes` counts `p->GetSize()` **after** removing the 20-byte header; `gOfferedBytes` adds `mPayload` before send. Therefore payload goodput uses application bytes excluding the custom header.
- `gBindStatus` is a global single sender status; the experiment is single-flow (node 0 to last node), starts at 10 s, stops at 60 s. Sender application schedules at `1/ratePps`; no attempt is made at or after stop.
- `RngSeedManager::SetSeed(seed)` and `SetRun(run)` precede topology and mobility installation, but **no explicit `AssignStreams` calls or replayed mobility traces** are present. Installing different routing helpers before application operation can alter RNG consumption. Identical seed/run labels alone are insufficient to establish identical realizations.
- `YansWifiChannelHelper::Default()` is used with `WIFI_STANDARD_80211b`, `AdhocWifiMac` and RandomWaypoint. Channel and MAC attribute values are not all serialized into output CSV; full effective configuration needs an ns-3 runtime attribute dump.
- `validity_status=PASS` and `exit_status=0` are **hardcoded into the output row**, not a comprehensive run-validation assertion. Consequently P01's previous PASS check confirms recorded fields, not successful independent runtime verification.
- The file explicitly describes itself as an **engineering validation runner**, with confirmatory scenario values frozen elsewhere. Before attributing source behavior to all 320 confirmatory rows, compare source hash and command provenance against the frozen S2 runner. This source inspection alone does not prove identical implementation was used.

## Important correction to earlier P01 interpretation
The 4,886 OLSR rejected attempts are **not evidence of a faulty PDR formula**. The formula intentionally measures delivered packets per offered application datagram. They do raise a fairness/attribution question: are failures due to no route, socket error, implementation behavior, or another cause? Without recorded `GetErrno()` and route trace data, the cause is **UNKNOWN**. Do not relabel as 'network-layer forwarding loss' or silently replace the denominator with socket-accepted sends.

## Minimal diagnostic modification — proposed, NOT executed
1. After `SendTo` returns negative, capture `mSocket->GetErrno()` immediately and increment a per-error counter. Persist error-code frequency per run.
2. Persist `tx_attempts`, `tx_accepted`, `tx_rejected`, and separately compute `rx/attempts` (primary) and `rx/accepted` (diagnostic, undefined when accepted=0). Do not replace primary endpoint.
3. Explicitly allocate reproducible mobility streams or generate a per-seed mobility trace independent of protocol; save per-node position time series and traffic attempt schedules, compare hashes across all four protocol runs.
4. Record effective propagation/MAC configuration, routing-helper provenance, source commit, build configuration and simulator version. Rerun original 320 conditions with frozen commands before robustness changes.
5. Investigate rejection causes with error-code counts and route availability. Report whether a rejection represents expected protocol inability to route rather than an implementation fault.
6. Validate application metrics with assertions and independent checks before writing `validity_status=PASS`; preserve failure records rather than forcing success status.

## Gate status
- **PASS (source inspection):** offered-load denominator matches declared metric contract.
- **FAIL (instrumentation completeness):** no socket errno counters or trace hashes; hardcoded PASS field is insufficient as a validator.
- **UNKNOWN (causal attribution):** root cause of OLSR rejected sends.
- **UNKNOWN (trace fairness):** common mobility/traffic realizations across protocols.
- **NOT EXECUTED:** diagnostic reruns, channel perturbation, factorial geometry study.

These are P01 blockers; P02 is not authorized.
