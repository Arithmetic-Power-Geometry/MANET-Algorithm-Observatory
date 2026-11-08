# P01 final audit disposition — 2026-11-08

**Disposition: DOCUMENTARY AND STATISTICAL AUDIT COMPLETED; EXPERIMENTAL VALIDATION BLOCKED.** This closes the P01 desk-audit work package, **not** the experimental reproducibility gate. No P02 rewrite is authorized by this report.

## 1. Actual verified tests
- Original user-provided `data/s2_master_results.csv` analyzed locally with Python 3.13, pandas 2.2.3, NumPy 2.3.5, SciPy 1.17.0. SHA256: `e848c565e41de92ddf41d2db52b4c3e154e848de1758c7ac07a6b7a3f6d54a56`.
- 320/320 rows, balanced 4 scenarios × 4 protocols × 20 seeds, unique keys; PDR arithmetic and original group summaries checked; all recorded `exit_status=0`, `validity_status=PASS`. Note that the original C++ runner writes PASS unconditionally, so these labels alone do **not** certify an independent execution.
- Recomputed paired two-sided Pratt Wilcoxon, six Holm comparisons **within each scenario**, 10,000 nominal paired percentile bootstrap resamples. SCALE AODV−DSR: mean 0.1625, raw p 0.010919, Holm p 0.043676, audit bootstrap CI [0.0320,0.2935]. Other scenario comparisons in `P01_AODV_DSR_RECOMPUTED.csv`.
- GitHub Actions run **42458668262**, job **128663014197**, commit `3047ae0696bef33db071f5bf7f42d18af17d25d3`: completed **success**, log states **"Ran 5 tests in 0.120s" / "OK"**. These are synthetic Python checker regression tests, not ns-3 simulator tests. URL: https://github.com/Arithmetic-Power-Geometry/MANET-Algorithm-Observatory/actions/runs/42458668262

## 2. Transmission rejection audit
All OLSR runs: **4,886 rejected / 11,000 offered datagrams** (44.42%); 75/80 runs have at least one rejection. Other protocols have zero recorded rejected sends.

| Scenario | OLSR rejected | OLSR offered | Rejected fraction | Affected runs |
|---|---:|---:|---:|---:|
| BASE | 741 | 2000 | 37.05% | 18/20 |
| FAST | 1014 | 2000 | 50.70% | 19/20 |
| LOAD | 1832 | 5000 | 36.64% | 18/20 |
| SCALE | 1299 | 2000 | 64.95% | 20/20 |

The source increments attempted packets before `SendTo` and computes `PDR = received / attempted`; this is consistent with the **offered-load** metric contract. The socket errno was not recorded in original data. **Do not infer root cause or replace denominator.** Conditional `received/accepted` is a diagnostic only, not a replacement performance metric.

## 3. Zero-delivery and missingness audit
Zero-PDR runs by scenario (AODV, DSDV, DSR, OLSR):
- BASE: 1, 1, 4, 2.
- FAST: 0, 1, 1, 5.
- LOAD: 1, 1, 4, 1.
- SCALE: 2, 7, 8, 8.

Missing `mean_delay_ms`: **47/320**; missing `mean_jitter_ms`: **51/320**. These are not to be imputed as zero. Interpretation must condition on successful matched packets.

## 4. Evidence registry review
All 15 CE001–CE015 entries were cross-checked with `literature/master_studies.csv` verification state and `literature/comparability_maturity_atlas.csv` C/E labels. See `P01_ALL_CE_CODING_AUDIT.csv`. This is a **registry-level** check, not a fresh examination of 15 complete primary publications. In particular, CE006's external C4 needs a matched-contract rationale; OBS-S2 C4 remains provisional until common realized traces are verified. V2 does not mean V3 structured quantitative extraction. Five detailed boundary examples are in `P01_CODING_EDGE_CASES.md`.

The repository distinguishes **31 workstreams, 30 registered studies, and 15 deeply extracted CE records**. These are different denominators. The bibliography's 80 inline references were previously user-verified and left unchanged.

## 5. Critical experimental gates not passed
1. **ns-3.47 compile/run:** NOT EXECUTED. No ns-3 executable in the available local environment; no simulator runtime output or new robustness measurements.
2. **OLSR socket errno cause:** UNKNOWN; diagnostic runner committed but unexecuted.
3. **Matched mobility:** UNKNOWN; sampled position diagnostics committed, but no original trace hashes or controlled replay. Matching numeric seed/run labels is insufficient. Sampled agreement, even if observed, is weaker than complete trajectory equality.
4. **Propagation sensitivity and node count vs geometry:** NOT EXECUTED. Original SCALE changes 25→50 nodes and 250×250→354×354 m, jointly; attribution to node count alone is unsupported.
5. **Primary-source CE extraction:** Registry cross-check done, but full V3 evidence sheets, coder reliability and source-page anchors not verified.
6. **C++ compilation and runtime correctness of new diagnostic source:** NOT VERIFIED. Synthetic checker CI cannot validate ns-3 APIs.

## 6. Defensible publication language before additional experiments
- The benchmark is a **bounded exploratory comparison** under recorded conditions; the observed SCALE AODV–DSR contrast is significant under the specified within-scenario Holm family, **conditional on treating numerical seeds as paired observations**. The realized mobility/traffic pairing has not been established.
- Avoid universal superiority, causal node-count scaling, GNN performance, field generalization, or propagation robustness claims.
- State OLSR socket-rejection incidence, denominator semantics and unverified cause transparently.
- Explicitly describe the source review as structured/narrative and the experimental evidence as separate. No invented PRISMA totals or source-extraction certainty.

## 7. Reproduction and continuation
- Original dataset and manuscript: user-supplied `Manuscript(20261108-065807).zip`; archive SHA of inner CSV given above.
- Reproducible analysis: `refine/evidence/P01_REPRODUCE.py` (requires original CSV supplied via `--csv`); outputs in `refine/evidence/`.
- Isolated C++ diagnostic runner: `refine/experiments/observatory_tier1_runner_diagnostic.cc`.
- Synthetic test suite: `refine/experiments/test_diagnostic_checkers.py`; successful CI link above.
- Runtime instructions: `refine/experiments/DIAGNOSTIC_EXECUTION.md`, `MOBILITY_TRACE_GATE.md`, `ROBUSTNESS_PROTOCOL.md`.
- Further work requires access to an ns-3.47 checkout/build environment, actual raw diagnostic traces and primary-source full texts.

**Exit decision:** P01 desk audit **complete with explicit unresolved experimental blockers**; P01 experimental gate **FAIL / NOT VERIFIED**. No scientific basis to certify a 95+/100 submission readiness score or any acceptance probability. P02 **not started**.
