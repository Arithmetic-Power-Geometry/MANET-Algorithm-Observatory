# P01 preregistered proposed robustness experiment — NOT EXECUTED

Question: does the SCALE AODV–DSR offered-application PDR difference persist when propagation changes, and can node count be separated from geometry?

1. Freeze original ns-3.47 revision, protocol implementations, measurement windows, packet source/receiver, and metric definitions. Reproduce original SCALE first.
2. Build replayable per-seed initial topology, mobility and application-event traces independent of protocol RNG. Check per-protocol trace SHA-256 equality for each seed; if unequal, mark comparison unmatched.
3. Factor propagation (original default Yans vs an explicitly specified and justified alternative), node count (25/50), and area (250×250 / 354×354 m), keeping speed and offered traffic constant. Report the eight or more factorial cells; where compute budget limits, prioritize SCALE original vs alternative propagation, then geometry controls.
4. Use original 20 registered seeds if valid and paired, with a preregistered pilot that is not used to change confirmatory hypotheses. Predefine exclusion rules and outcome measures.
5. Primary endpoint: difference in `app_packets_received/app_packets_sent` across AODV and DSR, with attempted-send denominator disclosed. Secondary: socket accepted rate, rejection counts, goodput, conditional delay where defined and route-control overhead if instrumented.
6. Report paired differences, raw two-sided Pratt Wilcoxon, Holm family, paired percentile or BCa bootstrap intervals with seed and method. Compare effect signs and intervals across propagation models; report whether difference persists, vanishes or reverses without making unsupported claims of equivalence.
7. Save executable commands, full config, simulator binary revision, raw traces, hashes, results and failure logs.

**Execution status: NOT EXECUTED.** The local runtime has no ns-3 executable. A protocol is not experimental evidence. Do not introduce hypothetical values into the manuscript.
