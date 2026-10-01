# II. Review Methodology and Evidence Model

## A. Scope and Population Boundary

This survey treats routing in mobile ad hoc networks (MANETs) as the primary evidence population. The scope includes foundational routing protocols, routing mechanisms designed around quality of service, energy, security and trust, optimization and learning-based approaches, and empirical work concerned with reproducibility, emulation, testbeds, or deployment. The organizing unit is not the protocol name alone, but the routing decision being made, the information available to that decision, the temporal horizon over which it acts, and the cost of maintaining the required state.

Evidence from vehicular ad hoc networks, flying ad hoc networks, wireless sensor networks, delay-tolerant or opportunistic networks, wireless mesh networks, Internet-of-Things settings, and related tactical networks is not pooled automatically with MANET evidence. Such studies are retained only when they provide transfer evidence for a routing mechanism or boundary evidence for an evaluation issue. This distinction is necessary because constrained road mobility, aerial mobility, store-carry-forward operation, sensing-dominated energy budgets, or infrastructure assumptions can change the routing problem itself. Population labels therefore remain visible throughout the synthesis.

## B. Corpus Construction and Stopping Rule

The corpus was constructed in stages. Primary specifications and foundational papers were first used to establish protocol mechanisms and terminology. Recent surveys and systematic reviews were then examined to identify existing synthesis boundaries, candidate primary studies, and evaluation problems. Primary-study expansion proceeded by backward tracing to defining work and forward expansion toward recent mechanism variants. Implementation evidence, simulator documentation, and software provenance were examined separately from publication claims so that the existence of an implementation was not inferred from a paper description.

Bibliographic identity was resolved preferentially by DOI or RFC identifier; otherwise, normalized title, year, and authorship were used. Preprints and final publications were linked rather than counted as independent evidence unless they contained materially different experiments.

The review was frozen on 1 October 2026. It uses conceptual saturation rather than claiming enumeration of every MANET-routing publication. A family was considered represented when a defining or representative mechanism had a verified primary or specification source where available, recent review evidence had been checked for omitted major branches, and quantitative claims used in synthesis had been extracted at the level required by those claims. Search continued when a source introduced a previously unrepresented decision mechanism, information scope, temporal mode, deployment regime, or materially conflicting result. Additional papers that repeated an already represented mechanism without changing the synthesis did not, by themselves, extend the stopping boundary. Consequently, corpus completeness in this survey means mechanism-level saturation within the declared scope, not exhaustive bibliographic coverage.

## C. Evidence Extraction and Verification

Each study is represented by a structured evidence record. The extraction schema preserves bibliographic identity together with the algorithm or family, routing decision, information scope, temporal horizon, baselines, node scale and density, mobility, traffic and offered load, radio and propagation assumptions, simulator or testbed, replication policy, metric definition, uncertainty, implementation and data availability, reported limitations, hidden assumptions, and gap tags. Details that could not be verified were retained as missing rather than reconstructed from neighboring studies.

Evidence passes through five verification states. V0 denotes discovery, V1 bibliographic verification, V2 verification of the source for the role in which it is cited, V3 structured evidence extraction, and V4 admission to a synthesis or generated artifact. Substantive conclusions in the survey are supported only by V2-or-higher evidence. Protocol definitions preferentially use primary specifications, foundational mechanisms use original papers, and quantitative results use the primary empirical source when available. Reviews are used principally for synthesis context, corpus expansion, and identification of broader evidence patterns.

## D. Comparability Classes

A central methodological distinction is between the existence of evidence and its comparability. Published values are not placed into a common performance leaderboard merely because they report a metric with the same name. Comparability depends on the implementation, simulator and version, radio and MAC configuration, propagation model, mobility process, node scale and density, traffic and offered load, experiment duration, seed policy, metric definition, and other information or resource budgets.

The survey therefore uses classes C0--C4. C0 evidence supports definitions or mechanisms but not quantitative comparison. C1 denotes study-local or weakly commensurate evidence for which important experimental dimensions differ or remain unavailable. C2 denotes partial comparability, and C3 denotes strong comparability when the relevant experimental contract is sufficiently aligned for a bounded quantitative comparison. C4 is reserved for controlled evidence generated under a common or explicitly matched contract. These classes constrain the claims that may be drawn from a study; they are not scores of scientific merit.

This rule is especially important for apparent contradictions. Two studies reporting different protocol orderings do not constitute a logical contradiction unless their comparison boundaries are sufficiently aligned. Differences in propagation, mobility, scale, load, implementation, or metric definition are first treated as candidate explanatory variables. An unconditional statement such as “protocol A outperforms protocol B” is therefore replaced, where possible, by a condition-indexed claim.

## E. Evidence Maturity

Algorithmic sophistication and empirical maturity are evaluated separately. The evidence-maturity ladder ranges from E0, where a mechanism or specification is defined, through E1 demonstration and E2 comparative simulation, to E3 reproducible comparative evidence. E4 denotes robustness evidence across relevant nuisance conditions; E5 adds held-out, out-of-distribution, or stress evidence; E6 denotes emulation or testbed evidence; E7 field evidence; and E8 independent replication.

The ladder is descriptive rather than a scalar ranking. A theoretically important routing mechanism can be at an early empirical stage, while a simpler protocol can have a much deeper body of reproducible or deployment evidence. For this reason, the survey reports evidence profiles and the highest verified evidence role relevant to a claim rather than converting maturity into an overall protocol score.

## F. Separation of Published and Controlled Evidence

The literature synthesis and the MANET Algorithm Observatory form two distinct evidence strata. Published studies retain their original experimental conditions and are interpreted within their comparability class. The Observatory does not retroactively normalize heterogeneous published results. Instead, it provides a controlled bridge for a limited set of implementations that satisfy explicit admission and provenance requirements.

The frozen controlled benchmark uses ns-3.47 implementations of AODV, DSDV, DSR, and OLSRv1. Development and instrumentation runs were separated from confirmatory evaluation. The confirmatory design used four frozen operating scenarios, 20 predeclared independent seeds per protocol and scenario, protocol-independent application accounting, and paired analysis where the common seed structure permits it. This produces 320 validated confirmatory runs. The benchmark is used to examine conditional differences and ranking stability, not to infer a universal routing winner or to substitute four classical implementations for the broader MANET literature.

## G. Review-Validity Controls

Several controls limit overinterpretation. First, adjacent-network evidence is explicitly labeled rather than silently pooled. Second, missing experimental details remain missing. Third, heterogeneous quantitative results are not combined when their comparison signatures are incompatible. Fourth, negative and conflicting evidence is retained. Fifth, evidence maturity is reported separately from algorithmic novelty. Sixth, the corpus has an explicit temporal cutoff, so developments after 1 October 2026 fall outside the frozen synthesis. Finally, the controlled benchmark is interpreted only within its admitted scenarios and metrics. In particular, its four discrete scenarios do not establish a continuous failure frontier, and propagation sensitivity observed in external evidence is not presented as an Observatory experiment.

These rules make the review intentionally conservative: a narrower condition-valid conclusion is preferred to a stronger statement obtained by erasing differences among experiments.
