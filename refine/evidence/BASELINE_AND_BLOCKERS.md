# Frozen baseline from supplied files (2026-11-08)

Original manuscript source (user-uploaded archive): `main.tex`, IEEEtran journal class, approximately 75,289 bytes of UTF-8 source with inline `thebibliography` (80 cited entries per bundled audit); 13-page compiled PDF; six original keywords; data files `data/s2_master_results.csv` and `data/s2_pdr_summary.csv`; seven original figure PDFs plus alternate figure; supplied generated summaries and audit documents. Original bibliography verification is **user-provided and supported by bundled REFERENCE_AUDIT.md**, not independently revalidated here.

Claimed experimental design: four protocols (AODV, DSDV, ns-3 DSR, OLSRv1); BASE/FAST/LOAD/SCALE; 20 seeds each; 320 runs; baseline 25 nodes/250m square, scale 50 nodes/354m square; Random Waypoint, single UDP flow, ns-3.47. Original abstract reports SCALE AODV minus DSR PDR = 0.1625, bootstrap 95% CI [0.0280,0.2950], Holm adjusted p=0.0437. This log is a **source inventory, not reproduction confirmation**.

External reviewer concerns (uploaded text): insufficiently demonstrated V/C/E novelty, 15-record deep corpus, unfairly equated paired seeds, scale-geometry confounding, narrow Yans/802.11b/RWP/single-flow experiment, bootstrap/Holm family ambiguity, negative-result interpretation, claims for graph-learning that are literature rather than benchmark evidence. Corresponding gate tests live in P01.

Official journal instructions (checked 2026-11-08): https://link.springer.com/journal/11276/submission-guidelines. Currently stated: online submission with editable source, 20 text pages (excluding figures/bibliography), double-spacing, 10pt Times New Roman, standard margins, 150–250-word abstract, 4–6 keywords, numbered references, funding/COI/author declarations and data availability. Springer Nature template supplied by user: December 2024 ZIP; no adaptation or compilation has yet been claimed.

**Status:** P01 instruction set and baseline inventory only. No new experiment run, no statistical replication, no section rewrite, no Springer compilation, no submission. Proceed by running Prompt 1.
