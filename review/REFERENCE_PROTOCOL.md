# Reference Verification Protocol

## Goal
Every reference in the eventual paper must be both valid and necessary.

## Required metadata
- title;
- authors;
- year;
- venue;
- DOI/RFC/standard identifier where available;
- source type;
- algorithm/family;
- evidence role;
- primary/secondary classification;
- verification status;
- date verified.

## Selection rules
1. Cite primary specifications for protocol definitions.
2. Cite original algorithm papers for foundational mechanisms.
3. Cite recent high-quality surveys to establish the state of review literature and non-redundancy.
4. Cite empirical papers only for claims their experiments actually test.
5. Do not cite a secondary review for a numerical result when the primary paper is available.
6. Retain negative/contradictory studies.
7. Do not pad the bibliography with papers that do not contribute evidence.

## Verification states
- V0 discovered
- V1 bibliographic metadata checked
- V2 primary text checked for cited claim
- V3 evidence row extracted
- V4 included in synthesis/artifact

Only V2+ references may support substantive paper claims.

## Citation integrity
A reference appearing in a table/figure must exist in the master registry. A master-registry entry must not be cited for a claim outside its verified evidence role.
