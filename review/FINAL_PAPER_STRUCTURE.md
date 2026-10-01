# Final Paper Structure — Evidence-Centered MANET Routing Atlas

This is a **pre-drafting structural specification**, not manuscript prose.

## Front matter

### Title
Final title selected only after contribution freeze. It should signal:
- MANET routing;
- evidence-centered synthesis;
- evolution/current status;
- reproducibility/comparability;
- applicability or failure frontiers.

### Abstract
Six-function structure:
1. field importance and persistent problem;
2. limitation of existing review organization/evaluation;
3. scope and review method;
4. new evidence-centered framework;
5. principal evidence/benchmark findings;
6. reusable contribution and research implications.

No result enters the abstract until it exists in frozen artifacts.

---

## I. Introduction — From Protocol Proliferation to Cumulative Evidence

Purpose:
- establish why another MANET routing review is needed;
- identify fragmentation in mechanism, evaluation, and evidence;
- distinguish this review from recent surveys;
- state RQs and contributions.

Main visual: **RV-F01 MANET Routing Evidence Compass**.

Main table: closest-review differentiation matrix.

---

## II. Review Methodology and Evidence Model

### A. Scope and population boundary
MANET primary population; adjacent-domain transfer policy.

### B. Search and corpus construction
Databases, search strings, dates, backward/forward chaining, version merging.

### C. Eligibility and extraction
Inclusion/exclusion, evidence schema, missing-data policy.

### D. Verification and reproducibility
V0–V4 reference/evidence states.

### E. Comparability
C0–C4 framework.

### F. Evidence maturity
E0–E8 profiles.

### G. Threats to review validity
Coverage, selection, extraction, classification, temporal cutoff.

Main tables: review protocol; evidence coding dictionary.

---

## III. Evolution of MANET Routing as a Sequence of Design Responses

Not a year-by-year history.

Organize as:
**limitation → design response → gained capability → introduced cost → subsequent response**.

Cover:
- proactive;
- reactive;
- source routing;
- link-state optimization;
- hybrid;
- multipath;
- geographic/opportunistic transitions.

Main visual: **RV-F02 Causal Evolution River**.

---

## IV. Unified Routing Decision and Mechanism Taxonomy

### A. Decision locus
discovery / selection / forwarding / repair / prediction / governance.

### B. Information horizon
local / neighbor / path / zone / network / latent learned state.

### C. Temporal horizon
current / reactive / anticipatory / learned adaptive.

### D. Mechanism
classical rules / optimization / fuzzy / metaheuristic / ML / RL / DRL / MARL / GNN / hybrid.

### E. Resource and information requirements
control, storage, compute, sensing, training, coordination.

Main visual: **RV-F03 Decision × Information × Time Cube**.

Main table: unified mechanism taxonomy.

---

## V. Complete Status of MANET Routing Families

This is the paper's principal reference section.

Each family is synthesized using the same seven-part microstructure:
1. decision problem;
2. mechanism;
3. required information;
4. capability;
5. structural cost;
6. evidence maturity;
7. unresolved obligation.

Subsections:
A. Proactive routing
B. Reactive routing
C. Hybrid routing
D. Multipath routing
E. Geographic and position-assisted routing
F. QoS-aware routing
G. Energy-aware routing
H. Trust/security-aware routing
I. Metaheuristic routing
J. ML-assisted routing
K. RL/DRL routing
L. MARL/GNN and distributed learning
M. Predictive, federated, cross-layer and emerging designs

Main visual: **RV-F04 Complete Family Status Map**.
Main table: compressed complete-status atlas.

---

## VI. What the Evidence Actually Supports

### A. Simulation evidence
### B. Statistical practice
### C. Reproducibility
### D. Robustness
### E. Generalization
### F. Testbed and field evidence
### G. Independent replication

Main visuals:
- **RV-F05 Evidence Maturity Landscape**
- **RV-F06 Evaluation-Space Coverage Heatmap**
- **RV-F08 Reproducibility Landscape**

Central question:
**How strong is the evidence, independently of how sophisticated the algorithm appears?**

---

## VII. Why MANET Routing Results Disagree

### A. Mobility-model dependence
### B. Propagation/channel dependence
### C. Scale and density confounding
### D. Traffic/load dependence
### E. Metric-definition differences
### F. Baseline selection and tuning
### G. Information-budget asymmetry
### H. Computational/resource-budget asymmetry
### I. Implementation differences

Main visuals:
- **RV-F07 Claim Comparability Network**
- **RV-F09 Contradiction Resolution Map**

No heterogeneous literature leaderboard is permitted.

---

## VIII. Reproducible Controlled Benchmark

### A. Benchmark admission
### B. Implementation fidelity
### C. Scenario design
### D. Metrics
### E. Seed/statistical protocol
### F. Information and cost fairness
### G. Confirmatory separation

Main table: admitted algorithms and rationale.
Main visual: **BM-F01 Scenario Design Map**.

---

## IX. Applicability, Ranking Stability, and Failure Frontiers

This section converts benchmarking from "who wins?" to "where does each mechanism remain adequate?"

### A. Conditional pairwise differences
### B. Pareto efficiency
### C. Ranking reversals
### D. Requirement-defined failure
### E. Applicability regions

Main visuals:
- **BM-F02 Ranking Stability Surface**
- **BM-F03 Pareto Performance Map**
- **BM-F08 Failure Frontier Atlas**

---

## X. Evidence-Backed Gap Atlas

Separate:
G-LIT, G-REP, G-EVAL, G-CONTRA, G-ROB, G-GEN, G-COST, G-REAL, G-CAP.

Every high-priority gap must state:
- evidence supporting the gap;
- evidence against it;
- what remains unknown;
- experiment required to resolve it.

Main visual: **RV-F10 Research Obligation Atlas**.

---

## XI. Designing the Next MANET Routing Study

A reusable research protocol:
1. locate operating regime;
2. identify routing decision;
3. identify closest mechanism;
4. select B1–B6 baselines;
5. equalize information/cost where possible;
6. freeze development and confirmatory scenarios;
7. report uncertainty;
8. stress nuisance assumptions;
9. test failure conditions;
10. release reproducible artifacts.

Main visual: **RV-F12 Researcher Navigation Map**.

This section is intended to give the paper long-term tutorial value.

---

## XII. Research Agenda: From Open Topics to Falsifiable Obligations

Do not list generic topics such as "use AI" or "improve security."

Each agenda item is:
**unresolved claim → missing evidence → falsifiable experiment → expected decision consequence**.

If a verified G-CAP exists, it may motivate a separate algorithm contribution. The review remains scientifically complete without forcing one.

---

## XIII. Threats to Validity

Separate:
- corpus validity;
- classification validity;
- comparability validity;
- implementation validity;
- benchmark external validity;
- temporal validity.

---

## XIV. Conclusion

Answer the RQs directly:
- what is established;
- what is conditionally established;
- what remains weakly supported;
- what is contradictory;
- what remains unresolved.

No new claims or future-work list appears here.

## Arrangement principle

The paper moves through:
**understand → classify → assess evidence → explain disagreement → reproduce → map frontiers → identify obligations → guide future research**.

This arrangement is preferred over protocol-by-protocol chronology because it serves both new and experienced researchers.
