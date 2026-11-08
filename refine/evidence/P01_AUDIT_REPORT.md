# P01 evidence and statistical audit — 2026-11-08

## Scope and source provenance
Independently inspected user-supplied `Manuscript(20261108-065807).zip` containing `main.tex`, `data/s2_master_results.csv` (320 rows × 36 columns), `data/s2_pdr_summary.csv` (16 groups), `REFERENCE_AUDIT.md` (80 references), figures and prior PDF. These uploaded files were examined locally; this report records findings, not a claim that their binary bytes were uploaded to GitHub. Source CSV SHA-256: `e848c565e41de92ddf41d2db52b4c3e154e848de1758c7ac07a6b7a3f6d54a56`. Original dataset records observatory commit `ebc5fdacff7ad44cecbe79b7aff3b1923f03777b`, ns-3 3.47.

Original inline `thebibliography` and 80-entry verification audit were preserved without alteration. No new references were generated or claimed verified.

## Tests and outcomes
- PASS: 320 rows, 4 scenarios × 4 protocols × 20 seeds; no duplicate (scenario, protocol, seed) keys.
- PASS: `validity_status=PASS` and `exit_status=0` on all 320 records.
- PASS: PDR arithmetic equals `app_packets_received/app_packets_sent` and original group mean/SD agree with source summary.
- PASS: complete common numeric seed keys for four protocols in each scenario.
- FAIL for assumption of zero socket rejections: **75/80 OLSR runs have positive `tx_rejected`; total 4,886 rejected application socket attempts**. AODV, DSDV, DSR each have zero. This means PDR computed with attempted application sends includes socket-level admission failures and should be described as *offered application-packet delivery*, not solely network forwarding success. Need inspect implementation and root cause; changing denominator without a predeclared metric is not acceptable.
- UNKNOWN: same seed means identical topology, mobility, source–destination/traffic trace across protocols. The CSV has numeric seeds, but no trace hashes or mobility/traffic replay verification.
- UNKNOWN: independent re-execution of ns-3 simulations; no ns-3 executable detected in local environment. No new propagation/geometry experiment performed.
- MISSING by design: delay columns have 47 nulls and jitter 51 nulls. Need distinguish zero matched packets and metric undefinedness rather than silently impute.

## Recomputed paired analysis
Method: SciPy 1.17.0 `wilcoxon(delta, zero_method='pratt', alternative='two-sided', method='auto')`; six unordered protocol pairs per scenario, Holm step-down family **within scenario**. Bootstrap audit uses 10,000 paired-seed percentile resamples with NumPy RNG 20261108; these nominal intervals need not reproduce the original bootstrap random seed and are not family-wise adjusted.

| Scenario | AODV−DSR mean | Raw Pratt p | Holm p | Audit percentile 95% CI |
|---|---:|---:|---:|---|
| BASE | -0.0015 | 0.822578 | 0.863846 | [-0.1150, 0.1230] |
| FAST | -0.0190 | 0.895987 | 0.895987 | [-0.1275, 0.0855] |
| LOAD | 0.0500 | 0.653849 | 1.000000 | [-0.0520, 0.1584] |
| SCALE | **0.1625** | **0.010919** | **0.043676** | **[0.0320, 0.2935]** |

Original manuscript SCALE interval [0.0280,0.2950] is not identical to this independently seeded bootstrap interval but direction is concordant. The original adjusted p=0.0437 is independently reproduced to rounding. The original BASE adjusted p=0.8638 is also reproduced. This is a **statistical replication of provided CSV**, not an independent ns-3 reproduction.

For SCALE DSR−OLSR: mean 0.1125, raw Pratt p=0.076419, Holm p=0.229258, nominal bootstrap interval [0.0215,0.2110]. No mathematical contradiction: nominal bootstrap CI for the mean and multiplicity-adjusted signed-rank test have different targets/adjustments. Do not claim Holm significance from a nominal CI excluding zero. SCALE DSDV−OLSR has the same adjusted p=0.229258.

SCALE mean PDR by protocol: AODV 0.3990, DSDV 0.1815, DSR 0.2365, OLSR 0.1240. These are **scenario-specific**, not general superiority claims.

## Important limitations
The experiment compares BASE (25 nodes, 250×250 m) with SCALE (50 nodes, 354×354 m); area, geometric distance distributions and node count change together. Single UDP flow node 0→last, RandomWaypoint, 802.11b and default Yans channel restrict external validity. A seed-label match is not proof of common random numbers. No field experiment, GNN implementation, independent coder or new channel sweep is claimed.

## Evidence classification audit status
The supplied manuscript records 31 workstreams, 30 registered studies and 15 deep evidence records, with original CE001–CE015 and OBS-S2 classifications. The group assignments in Table VIII were inspected. Source-specific recoding and five worked edge cases remain **PENDING**, not verified. Do not infer E4 robust generalization from one channel configuration.

## Decision
**P01 PARTIAL / BLOCKED** until original simulator trace equality, socket-rejection root cause, full V/C/E claim ledger and discriminating experiment are audited. P02 must not begin yet.
