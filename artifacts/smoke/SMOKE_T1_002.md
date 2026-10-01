# Tier-1 Canonical Smoke Result — SMOKE-T1-002

## Provenance

- GitHub Actions run: 36818359200
- frozen simulator: ns-3.47
- workflow source commit: 7bbab7901529c6d4ab145c3fefe87cffd174b367
- protocols: AODV, DSDV, DSR, OLSRv1 (upstream label OLSR)
- source-interface contract check: PASS for all four jobs
- configure/build/execution/schema/artifact jobs: PASS
- compare job: PASS

## Upstream smoke diagnostics

| protocol | time rows | summed PacketsReceived | summed ReceiveRate (kbps) |
|---|---:|---:|---:|
| AODV | 200 | 1349 | 690.688 |
| DSDV | 200 | 724 | 370.688 |
| DSR | 200 | 1102 | 564.224 |
| OLSRv1 | 200 | 665 | 340.480 |

The generated summary was checked against the downloaded raw protocol CSV artifacts.

## Interpretation boundary

These values are engineering smoke diagnostics from the upstream ns-3 example. They demonstrate successful protocol execution and a functioning comparison pipeline.

They are **not** admitted as confirmatory protocol-performance evidence because:
- one engineering run is not an inferential replication design;
- the upstream CSV does not provide the common application sent-packet denominator required for Observatory PDR;
- it does not provide the frozen common delay/jitter accounting;
- the scenario is not the confirmatory factorial design;
- no uncertainty estimate is available.

Therefore no manuscript statement such as “AODV is better than DSR/DSDV/OLSR” may be derived from this table.

## Next gate

Implement and validate the Observatory-controlled common application measurement runner, then execute S1 pilot seeds before selecting S2 confirmatory replication counts.
