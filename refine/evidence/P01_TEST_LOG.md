# P01 test log — 2026-11-08

Local Python 3.13 / pandas / NumPy / SciPy 1.17.0 audit executed against uploaded CSV, not GitHub-hosted CI. The committed script `P01_REPRODUCE.py` reproduces the documented calculation when passed the same CSV. The actual local execution used an equivalent expanded script with summary cross-checks. **The committed script has not itself been run in GitHub Actions.**

| Check | Result |
|---|---|
| 320 observations, 16 balanced cells, 20 seeds | PASS |
| Unique scenario/protocol/seed | PASS |
| All recorded run exit status zero, validity PASS | PASS |
| PDR numerator/denominator arithmetic | PASS |
| Original per-cell mean and sample SD | PASS |
| Seed identifier present for all protocols | PASS |
| All socket transmissions accepted | FAIL — 75 OLSR runs rejected attempts |
| Original SCALE AODV–DSR mean 0.1625 | PASS |
| Original SCALE adjusted p≈0.0437 | PASS |
| Original bootstrap CI exact numerical identity | NOT ESTABLISHED (different RNG seed) |
| Mobility and traffic realization equality | UNKNOWN |
| Independent ns-3 rerun / alternative propagation | NOT EXECUTED |
| Full independent bibliography DOI audit | NOT REPEATED (user-verified bibliography preserved) |
| V/C/E source-by-source independent coding | PENDING |

P01 is not yet complete. The research must not move to P02 while critical experimental fairness and interpretation blockers remain.
