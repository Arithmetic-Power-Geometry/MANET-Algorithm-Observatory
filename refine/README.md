# Wireless Networks refinement workspace

Target: **Wireless Networks** (Springer Nature), official journal 11276. This directory is a staged, evidence-first development workspace for *Evolution and Evidence in MANET Routing: From Classical Protocols to Graph Learning*.

## Source of truth and non-negotiable safeguards
- Preserve the original repository, manuscript, simulation observations, verified bibliography, publication identities and primary citation metadata; never silently regenerate or replace verified references. The supplied November 2026 manuscript ZIP contains an **inline 80-entry bibliography** in `main.tex`, not a separate `references.bib`. Carry its content forward exactly except documented corrections.
- Maintain traceability from original manuscript claims and tables to original CSVs and code. Label all changes as **source-derived**, **newly verified**, **newly reproduced**, **hypothetical**, or **pending**. Never fabricate experimental data, extra runs, inter-rater agreement, bibliography searches, graph-learning baselines, acceptance probabilities or testbed results.
- Do not claim the original 31 workstreams are 31 studies: 30 registered studies, 15 deeply structured evidence records, four benchmark protocols, four scenarios and 20 seeds per protocol/scenario are different populations.
- Protect baseline numerical results. The reported 320 runs, SCALE AODV-minus-DSR PDR difference 0.1625, CI [0.0280, 0.2950], and adjusted p=0.0437 are **claims to reproduce from artifacts**, not newly validated results in this workspace.
- The supplied journal template package is the December 2024 **sn-jnl** class. Journal-specific rules prevail: max **20 pages of manuscript text excluding figures and bibliography**, 10-point Times New Roman, double line spacing, standard margins, 150–250-word abstract, 4–6 keywords, numbered references, complete editable source, declarations and data availability. Verify the policy again at final submission. Use the user-supplied template files under their license; do not republish arbitrary third-party class files without checking redistribution terms.
- The journal's subject scope is wireless/mobile networks, protocol design and performance. Frame as **MANET evidence synthesis plus controlled routing-performance evaluation**; graph learning is literature-level unless new legitimate implementation evidence is produced. Determine whether Review Article is available during submission; otherwise justify an appropriate regular article classification without misrepresentation.
- Quality goal **95+/100 on an auditable internal readiness rubric**, never a promise of journal acceptance.

## Three sequential prompts
1. [P01 — evidence and reproducibility audit](P01_evidence_and_experiment_audit.md): identify and repair scientific blockers, run cheapest discriminating experiment if technically possible, commit auditable records.
2. [P02 — evidence synthesis and manuscript rewrite](P02_evidence_synthesis_and_rewrite.md): revise every section, preserve verified sources, strengthen graph-learning and comparative claims, commit complete evidence-backed manuscript content.
3. [P03 — Springer template, build and final gate](P03_springer_template_and_submission.md): port to supplied template, enforce journal limits, compile and visually inspect, release only verified submission artifacts and final checklist.

## Required directory outputs (created only when actually available)
`refine/evidence/`: source manifest, audit logs, tracked statistical outputs, V/C/E decision ledger and evidence limitations.
`refine/experiments/`: design, reproducible commands, actual outputs and hashes, including negative/failure records.
`refine/manuscript/`: revised sections, figures, declarations and bibliography retained from verified source.
`refine/submission/`: Springer LaTeX source ZIP, compiled review PDF, measured length/format report, cover letter and preflight.
`refine/prompts/`: optional execution logs (avoid storing private chat or prompt history in publication-ready artifacts).

Advance to the next prompt only after recording the earlier prompt's commit hash and blockers. Prior work is never overwritten without an explicit provenance note.

## Official guidance
- https://link.springer.com/journal/11276/submission-guidelines
- https://link.springer.com/journal/11276/aims-and-scope
