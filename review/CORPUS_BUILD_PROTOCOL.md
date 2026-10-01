# Corpus Build Protocol

## Stage A — Anchor sources
Primary specifications and foundational papers define mechanisms.

## Stage B — Closest reviews
Recent surveys/systematic reviews establish:
- what has already been synthesized;
- terminology;
- candidate primary studies;
- unresolved evaluation issues;
- non-redundancy obligations.

## Stage C — Primary-study expansion
For each family agent:
1. mine primary studies cited by closest reviews;
2. search forward for newer work;
3. search backward for defining work;
4. verify bibliographic identity;
5. classify scope;
6. extract evidence only after primary text verification.

## Stage D — Implementation evidence
Search official/research repositories and simulator documentation separately from publication claims.

## Stage E — Saturation
A family is not marked corpus-complete until:
- defining works are present;
- major mechanism variants are present;
- recent representative work is present;
- strongest reproducible implementations are assessed;
- contradictory/negative evidence has been actively searched;
- adjacent-domain transfer evidence has been considered and tagged.

## Deduplication key

Prefer DOI/RFC. Otherwise normalize title + year + first author. Preprint and final publication are linked, not counted as independent evidence unless they contain materially different experiments.

## Verification

V0 discovered
V1 metadata checked
V2 source checked for the cited role
V3 structured evidence extracted
V4 used in synthesis/artifact

A V0/V1 source can populate discovery maps but cannot support substantive conclusions.
