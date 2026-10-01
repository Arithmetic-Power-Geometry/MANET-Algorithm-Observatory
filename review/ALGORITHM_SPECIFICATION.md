# Algorithm and Pseudocode Specification

A review paper should not contain pseudocode merely for decoration.

## Permitted algorithm blocks

### ALG-1 — Evidence Admission Procedure
Input: candidate publication.
Output: verification state, scope class, evidence role, eligibility.

Purpose: make corpus/evidence admission reproducible.

### ALG-2 — Claim Comparability Procedure
Input: two quantitative claims and their condition signatures.
Output: C0–C4 comparability class plus mismatch reasons.

Purpose: operationalize the paper's comparability framework.

### ALG-3 — Benchmark Baseline Admission
Input: candidate algorithm implementation.
Output: admitted/blocked plus implementation-fidelity and fairness requirements.

Purpose: prevent convenience-based comparator selection.

### ALG-4 — Failure Frontier Estimation
Input: algorithm, scenario grid, requirement vector.
Output: estimated boundary between adequate and inadequate operating regions.

Purpose: formalize applicability rather than universal ranking.

### ALG-5 — Research Obligation Prioritization
Input: gap evidence, contradiction evidence, reproducibility, impact, resolvability.
Output: evidence-backed priority class.

Purpose: convert generic future work into testable research obligations.

## Candidate novel algorithm

Its pseudocode is added only after the G-CAP gate passes and the mechanism is frozen before confirmatory evaluation.

## Academic presentation

Each algorithm must define:
- inputs;
- outputs;
- assumptions;
- deterministic/stochastic elements;
- computational role;
- connection to an RQ or artifact.

Avoid pseudo-formal algorithms that merely restate prose.
