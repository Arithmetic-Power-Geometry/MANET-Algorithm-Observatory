# Paper Readiness Ledger

## Rule

The paper is written **last**. No full manuscript drafting begins until all mandatory gates marked P0 or P1 are complete or explicitly waived with a scientific reason.

The repository is the research system; the paper is a compressed, journal-ready view of the frozen evidence.

## P0 — Mandatory before drafting

### A. Scope and novelty
- [x] Primary MANET scope defined.
- [x] Adjacent-domain transfer policy defined.
- [x] Closest-review comparison framework defined.
- [ ] Closest-review matrix saturated through final search date.
- [ ] Every claimed review-level novelty has a documented closest-prior-review delta.
- [ ] Final research questions frozen.

### B. Literature corpus
- [x] Master study registry created.
- [x] V0–V4 verification system created.
- [ ] Classical routing corpus saturated.
- [ ] Hybrid/multipath/geographic corpus saturated.
- [ ] QoS/energy corpus saturated.
- [ ] Security/trust corpus saturated.
- [ ] Metaheuristic corpus saturated.
- [ ] ML/RL/DRL corpus saturated.
- [ ] MARL/GNN/predictive/federated/cross-layer corpus saturated.
- [ ] Testbed/field corpus saturated.
- [ ] Negative/contradictory evidence search completed.
- [ ] Duplicate/preprint-final reconciliation completed.
- [ ] Final search update completed immediately before drafting.

### C. Reference integrity
- [x] Reference verification protocol defined.
- [ ] All substantive references V2+.
- [ ] All synthesized references V3+.
- [ ] All figure/table references resolve to master registry.
- [ ] DOI/RFC/metadata audit passes.
- [ ] No unsupported secondary-source substitution for primary claims.

### D. Structured evidence
- [x] Evidence schema defined.
- [x] Complete-status schema defined.
- [ ] Evidence rows populated for all synthesis studies.
- [ ] C0–C4 comparability assigned where quantitative comparisons are discussed.
- [ ] E0–E8 evidence maturity profiles completed.
- [ ] Information requirements completed.
- [ ] Communication/compute/storage costs completed where available.
- [ ] Missing evidence explicitly coded rather than inferred.

### E. Contradictions and gaps
- [x] Gap vocabulary defined.
- [x] Research-obligation registry started.
- [ ] Contradiction candidates extracted.
- [ ] Apparent contradictions separated from true contradictions.
- [ ] Gap atlas completed.
- [ ] Literature gaps separated from demonstrated capability gaps.
- [ ] Candidate G-CAP independently checked against closest prior work.

### F. Benchmark
- [x] Benchmark contract architecture defined.
- [x] Baseline-selection rules defined.
- [ ] Simulator/version frozen.
- [ ] Canonical environment reproducible.
- [ ] T1 algorithms build and pass smoke tests.
- [ ] Implementation fidelity documented.
- [ ] Scenario matrix frozen.
- [ ] Seed/repetition policy frozen.
- [ ] Metric definitions frozen.
- [ ] Development vs confirmatory scenarios separated.
- [ ] Information-fairness audit complete.
- [ ] Cost-fairness audit complete.
- [ ] Full controlled benchmark complete.
- [ ] Statistical analysis complete.
- [ ] Sensitivity/robustness analysis complete.
- [ ] Ranking-stability analysis complete.
- [ ] Failure-frontier analysis complete.

### G. Novel algorithm gate
- [ ] Decide from evidence whether a novel algorithm is scientifically justified.
- [ ] If NO: document why the review/benchmark stands independently.
- [ ] If YES: verify G-CAP, closest mechanisms, and novelty before design.
- [ ] Freeze algorithm before confirmatory testing.
- [ ] Compare against B1–B6 baseline roles as applicable.
- [ ] Ablation complete.
- [ ] Sensitivity complete.
- [ ] Complexity/resource accounting complete.
- [ ] Held-out/OOD evaluation complete where applicable.
- [ ] Negative results retained.

### H. Artifacts
- [x] Stable artifact IDs defined.
- [x] Visual language defined.
- [ ] RV-F01–RV-F12 generated from data.
- [ ] Core RV tables generated from data.
- [ ] BM-F01–BM-F08 generated.
- [ ] Benchmark tables generated.
- [ ] Candidate-algorithm artifacts generated only if G-CAP gate passes.
- [ ] Every plotted number traceable to versioned result data.
- [ ] Figure readability checked at two-column publication size.
- [ ] Captions state evidence boundary and takeaway.

### I. Reproducibility
- [x] Repository validation workflows started.
- [ ] Environment manifest frozen.
- [ ] All analysis scripts deterministic under fixed inputs.
- [ ] Clean-run workflow regenerates canonical artifacts.
- [ ] Artifact checksums recorded.
- [ ] Release tag frozen.
- [ ] Archival DOI created if appropriate.
- [ ] Reproduction instructions tested from clean environment.

## P1 — Mandatory before submission

### J. Journal fit
- [x] Aspirational COMST architecture defined.
- [x] Ad Hoc Networks scope fit verified.
- [ ] Current target-journal article type/guidelines rechecked at submission.
- [ ] Current quartile/metrics checked from authoritative source available to authors.
- [ ] Final journal chosen based on completed contribution, not prestige alone.
- [ ] Page/word/figure/reference constraints satisfied.
- [ ] Non-redundancy statement updated against newest surveys.

### K. Manuscript integrity
- [ ] Abstract claims map exactly to results.
- [ ] Introduction contributions map exactly to demonstrated outputs.
- [ ] Methods reproduce actual corpus/benchmark workflow.
- [ ] Results contain no unsupported extrapolation.
- [ ] Discussion distinguishes evidence from interpretation.
- [ ] Conclusion introduces no new claim.
- [ ] All figures/tables/algorithms cited in text.
- [ ] All references verified.
- [ ] Terminology/acronyms consistent.
- [ ] No repository wording implies manuscript generation.
- [ ] No author/developer instructions remain.
- [ ] Final line-by-line claim–evidence audit passes.

## Drafting trigger

Full paper drafting begins when:
1. all P0 gates are complete or scientifically waived;
2. the final artifact set is frozen;
3. the target journal is selected;
4. the repository release used by the paper is immutable/tagged.

Until then, only outlines, captions, schemas, and evidence notes may be prepared.
