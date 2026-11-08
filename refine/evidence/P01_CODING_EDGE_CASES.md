# P01 preliminary V/C/E coding trace — five grounded cases

This is a **source-ledger cross-check**, not independent double coding. Source: `literature/comparability_maturity_atlas.csv`, `review/EVIDENCE_MATURITY_LADDER.md`, `literature/contradiction_registry.csv`. Full primary-text recoding remains pending.

| Record | Existing class | Supported use | Caution / edge decision |
|---|---|---|---|
| CE002 / M0002 AODV RFC | C0/E0 | Mechanism definition/history | An RFC identifies protocol behavior, not an empirical performance comparator; do not infer AODV beats DSR |
| CE005 / M0005 AOMDV | C1/E1 | Multipath demonstration | Original evaluation not normalized to Observatory contract; no cross-paper numerical ranking |
| CE006 / M0012 propagation study | C4/E4 | Within-study sensitivity to propagation | External robustness result does not validate Observatory SCALE result under an untested propagation regime; independent source verification pending |
| CE013 / M0028 MARL–GNN | C1/E2 | Study-specific learning evaluation | Learning-based improvement remains local to its baselines, observation budget, training and deployment assumptions; no Observatory GNN experiment |
| CE014 / M0029 transformer–GNN | C1/E2 | Adjacent MANET–IoT boundary prior art | Adjacent population cannot be generalized to ordinary MANET without transfer validation |
| OBS-S2 / Observatory | C4/E4 (existing) | Four scenario-controlled protocol comparisons | E4 describes sensitivity across the tested scenarios only, **not** propagation robustness or independent replication. Common seed labels do not prove common realized mobility traces |

**Coding limitations:** source identity versus source claim validation are different. The repository ladder E4 is sensitivity over relevant operating conditions, whereas E8 requires independent replication. E6/E7 are evidence settings, not inherently superior for all estimands. V0–V4 assignment for each primary record, primary-page anchors, 25-question extraction audit, independent coder agreement and sensitivity of borderline codes remain **UNKNOWN/PENDING**. Preserve existing classifications until source-grounded recoding.

**Contradiction register:** C001–C004 are labeled 'resolved' in the original registry. In P01 they are reinterpreted as *apparent contradictions contextualized by condition signatures*; no matched cross-paper causal contradiction is experimentally resolved by this label alone.
