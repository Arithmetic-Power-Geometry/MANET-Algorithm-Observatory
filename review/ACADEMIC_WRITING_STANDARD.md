# Academic Writing Standard

## Purpose

The eventual review should read as a rigorous scholarly synthesis, not as a protocol catalogue, promotional article, repository report, or sequence of implementation notes.

## Preferred academic vocabulary

Use precise evidence-oriented terms:
- **demonstrates / establishes** only when directly supported;
- **indicates / suggests / is consistent with** for limited evidence;
- **reports** for claims made by a cited study;
- **observed under the evaluated conditions** instead of "proved better";
- **comparative advantage** instead of "best performance";
- **condition-dependent superiority** instead of "winner";
- **evaluation regime** instead of "test setup";
- **operating regime** instead of "situation";
- **evidence maturity** instead of "quality score";
- **empirical coverage** instead of "number of experiments";
- **research obligation** instead of generic "future work";
- **capability gap** only for a failure demonstrated under controlled evidence;
- **underexplored region** for sparse literature;
- **reproducibility limitation** for insufficient artifacts/configuration;
- **external validity** for transfer beyond evaluated conditions;
- **implementation fidelity** for correspondence between evaluated code and the defined algorithm.

## Claim calibration

Never write:
- "Algorithm X is the best."
- "X always outperforms Y."
- "This proves X is superior."
- "No one has studied..."
- "The first ever..." without a documented priority search.
- "Most comprehensive..." without a defensible corpus comparison.

Prefer:
- "Under C, X achieved higher M than Y in the reported evaluation."
- "The available evidence supports a conditional advantage under..."
- "The evidence base remains insufficient to establish..."
- "The literature retrieved under the stated protocol contains limited evidence for..."
- "To our knowledge" only after the search protocol and closest-work audit justify it.

## Evidence boundary

Each synthesis paragraph should distinguish:
1. what the literature reports;
2. what can be compared;
3. what the Observatory reproduces;
4. what remains interpretation or hypothesis.

## Terminology discipline

Use **MANET routing algorithm/protocol** according to the source and mechanism. Do not use protocol, algorithm, framework, model, and architecture interchangeably.

Distinguish:
- route discovery;
- route selection;
- next-hop selection;
- route maintenance/repair;
- forwarding;
- metric estimation;
- mobility/link prediction;
- policy learning;
- coordination.

## Paragraph architecture

Preferred synthesis paragraph:
**claim → evidence → qualification → implication**.

Preferred family subsection:
**problem → mechanism → capability → cost → evidence → failure/limitation → transition to next family**.

This prevents paper-by-paper narration.

## Tone

Use restrained academic prose. Avoid:
- marketing language;
- exaggerated novelty;
- rhetorical filler;
- repeated adjectives such as novel, robust, efficient, intelligent;
- anthropomorphic AI language;
- unsupported causal claims.

## Mathematics

Equations are used only when they compress or clarify an evidence concept, frontier, metric, or formal comparison. They should not decorate a survey.
