# Figure and Table Architecture

The review should be visually navigable. Every major visual answers a distinct research question.

## Flagship figures

**F1 — MANET routing evolutionary causal map**  
Problem → mechanism → gained capability → new cost → next research branch.

**F2 — Routing decision cube**  
Axes: decision role × information horizon × temporal horizon. Algorithms occupy cells rather than only family labels.

**F3 — Historical-to-intelligent mechanism river**  
Shows how classical routing mechanisms connect to QoS, energy, trust, metaheuristics, ML, RL, MARL, GNN, prediction, and cross-layer control.

**F4 — Evidence pyramid**  
For each family: specification/theory → simulation → reproducible simulation → emulation → testbed → field.

**F5 — Research-space coverage heatmap**  
Algorithm family × mobility/scale/propagation/traffic/security/energy/deployment dimensions.

**F6 — Claim comparability map**  
Published algorithm comparisons represented as edges, styled by C0–C4 comparability.

**F7 — Reproducibility landscape**  
Code, configuration, seed policy, statistics, artifacts, environment, testbed availability.

**F8 — Contradiction map**  
Pairs of claims that disagree, annotated with whether scenario mismatch explains the apparent contradiction.

**F9 — Ranking-stability surface**  
Controlled benchmark artifact showing where pairwise rankings change.

**F10 — Failure-frontier atlas**  
Regions where each admitted algorithm ceases to satisfy selected application constraints.

**F11 — Gap atlas**  
G-LIT / G-REP / G-EVAL / G-CONTRA / G-ROB / G-GEN / G-COST / G-REAL / G-CAP.

**F12 — Researcher navigation map**  
Given an application condition, identifies evidence-rich families, weak-evidence regions, and benchmark obligations without claiming a universal winner.

## Core tables

**T1** Review protocol and databases/search windows  
**T2** Complete protocol/algorithm status atlas  
**T3** Mechanism and information requirements  
**T4** Standards and implementation availability  
**T5** Published evaluation conditions  
**T6** Metrics and statistical practice  
**T7** Reproducibility audit  
**T8** Learning-specific training/generalization audit  
**T9** Security/adversarial evidence  
**T10** Energy/resource-cost evidence  
**T11** Real-device/testbed evidence  
**T12** Contradictions and proposed resolution experiments  
**T13** Benchmark admission and exclusion rationale  
**T14** Evidence-backed research gaps  
**T15** Research agenda expressed as falsifiable obligations

## Presentation rule

Avoid giant unreadable protocol tables. The main paper presents compressed status views; complete machine-readable records live in the repository artifacts.
