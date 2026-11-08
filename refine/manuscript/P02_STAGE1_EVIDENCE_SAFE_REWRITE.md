# P02 Stage 1 — Evidence-safe opening and benchmark corrections

This is the first editorial step of P02, **not a complete rewritten manuscript**. Source basis: original `main.tex` from user-provided `Manuscript(20261108-065807).zip`; P01 audit `refine/evidence/P01_FINAL_DISPOSITION.md`. Preserve the 80 verified bibliography items and their citation keys. No new sources or experiments are asserted.

## Proposed revised title
**MANET Routing from Classical Protocols to Graph Learning: Evidence Comparability and a Bounded ns-3 Benchmark**

## Revised abstract (draft)
Mobile ad hoc network (MANET) routing research spans proactive, reactive, multipath, geographic, learning-based, and graph-based mechanisms, yet performance claims are often evaluated under incompatible conditions. This structured narrative review examines routing evolution through decision location, information availability, temporal horizon, and communication or computational cost. It separates bibliographic verification, claim comparability, and evidence maturity instead of combining them into a protocol score. The repository organizes 31 thematic workstreams, registers 30 studies, and maintains 15 detailed comparative-evidence records; these are distinct units of analysis. A bounded ns-3.47 dataset contains 320 recorded runs of AODV, DSDV, DSR, and OLSRv1 across four scenarios and 20 numerical seeds per protocol–scenario cell. Reanalysis finds an AODV-minus-DSR mean packet-delivery-ratio difference of 0.1625 under the joint node-count/area SCALE condition (within-scenario Holm-adjusted Wilcoxon p = 0.0437). However, identical seed labels do not establish identical realized mobility traces, and the OLSRv1 records contain 4,886 rejected socket transmissions whose causes were not logged. Consequently, this benchmark supports a conditional descriptive contrast, not universal superiority or causal scaling attribution. Learning and graph-based routing are discussed from published evidence, not benchmarked experimentally here. The resulting synthesis identifies specific requirements for trace matching, propagation robustness, resource accounting, and simulation-to-real validation.

## Keywords
Mobile ad hoc networks; routing protocols; evidence comparability; reproducibility; graph neural networks; ns-3

## Research questions
**RQ1 — Comparability.** Which documented scenario, implementation, measurement, and replication attributes must align before two MANET routing performance claims can be compared quantitatively?

**RQ2 — Mechanism evolution.** How do routing families redistribute observation, control signaling, stored state, computation, training, and inference costs rather than eliminate them?

**RQ3 — Conditional ranking.** How do the four recorded classical protocol comparisons change across BASE, FAST, LOAD and the joint size/geometry SCALE condition, and which differences survive the declared multiplicity correction?

## Required corrections to original manuscript before any journal submission
1. Replace '320 validated confirmatory runs' with '320 recorded benchmark runs whose CSV arithmetic and group summaries were independently checked; simulator-level validity and trace fairness were not independently verified.' The runner hardcodes the PASS label.
2. Replace '20 independent seed-level runs' with '20 runs indexed by predeclared numerical seeds'; stochastic independence and paired physical realizations are not established.
3. Retain the SCALE AODV−DSR point difference 0.1625 and Holm p 0.0437, explicitly conditional on numerical-seed pairing. Report the P01 bootstrap interval [0.0320, 0.2935] as an **independent reanalysis** with its specified RNG and algorithm; do not silently substitute it for the manuscript's original [0.0280, 0.2950] interval.
4. Explain SCALE changes **both** nodes (25→50) and square side (250→354 m), so node-count effects cannot be isolated.
5. Explain the offered-load denominator, and report OLSRv1 4,886/11,000 socket send rejections (44.42%), 75/80 runs affected; cause unknown.
6. Delay and jitter missingness: 47/320 and 51/320 respectively; do not set missing values to zero.
7. Separate graph-learning mechanisms described in literature from protocols experimentally benchmarked. No RouteNet-Fermi MANET experiment was performed.
8. Treat V2 source coding as cited-role verification, not primary full-text quantitative extraction; OBS-S2 C4 remains provisional, and CE006 external C4 requires justification.
9. Do not claim PRISMA database retrieval counts without actual search logs. Keep 31 workstreams, 30 registered studies and 15 CE records distinct.
10. Ensure all figures/tables/algorithms have in-text references and source anchors; preserve original figure assets and bibliography.

## P02 stage gate
Next: revise every section of original source into `refine/manuscript/main.tex`, preserve exact bibliography, build `claim_to_evidence.csv`, and compile/test where tools permit. The original manuscript and the P01 experiment limitations remain intact. **P03 not started.**
