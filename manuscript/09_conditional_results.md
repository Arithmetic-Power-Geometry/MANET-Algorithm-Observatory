# IX. Conditional Performance and Ranking Stability

## A. Scenario-Level Delivery

Mean PDR differs substantially across the four frozen operating conditions. In S2_BASE, mean PDR is 0.6075 for AODV, 0.4130 for DSDV, 0.6090 for DSR, and 0.3905 for OLSRv1. Under the higher-mobility S2_FAST condition, the corresponding means fall to 0.3485, 0.2080, 0.3675, and 0.1840. S2_LOAD yields means of 0.6238, 0.4016, 0.5738, and 0.3900, whereas S2_SCALE yields 0.3990, 0.1815, 0.2365, and 0.1240.

The means are descriptive summaries of these frozen conditions, not a global ordering. In particular, the similar AODV and DSR means in BASE, FAST, and LOAD conceal substantial seed-level variation.

## B. Paired Differences

AODV and DSR are not cleanly separated by paired PDR in three scenarios. The mean AODV-minus-DSR difference is -0.0015 in BASE, with bootstrap 95% CI [-0.1170, 0.1255] and Holm-adjusted Wilcoxon p=0.8638. In FAST the difference is -0.0190, CI [-0.1305, 0.0850], adjusted p=0.8960; in LOAD it is 0.0500, CI [-0.0506, 0.1608], adjusted p=1.0000. In SCALE the difference becomes 0.1625, CI [0.0280, 0.2950], adjusted p=0.0437. Within this benchmark, the AODV--DSR relation is therefore condition-dependent rather than represented well by one pooled ordering.

AODV has positive paired PDR differences relative to DSDV and OLSRv1 in all four frozen scenarios, with the bootstrap intervals excluding zero and Holm-adjusted Wilcoxon p<0.01 for these comparisons. DSR has positive paired differences relative to DSDV and OLSRv1 in BASE, FAST, and LOAD, with adjusted p<0.05. Under SCALE, however, DSR-minus-DSDV is -0.0550 with CI [-0.1690, 0.0420] and adjusted p=0.4396, while DSR-minus-OLSRv1 is 0.1125 with CI [0.0225, 0.2120] but adjusted p=0.2293. The latter illustrates why interval direction alone and a multiplicity-adjusted rank test need not yield the same inferential label in a small paired sample; both are reported rather than selecting the more favorable result.

## C. Seed-Level Ranking Stability

Strict rank-1 membership changes across seeds even within a fixed scenario. AODV is rank 1 in 35% of BASE seeds, 50% of FAST seeds, 40% of LOAD seeds, and 65% of SCALE seeds. DSR is rank 1 in 55%, 45%, 45%, and 15%, respectively. DSDV and OLSRv1 account for occasional rank-1 outcomes or ties not represented by the AODV/DSR fractions.

This result separates average performance from ranking stability. In BASE, for example, DSR has the highest mean PDR by only 0.0015 over AODV, while seed-level rank-1 membership is 0.55 versus 0.35. In FAST, their means and rank-1 fractions are again close. In SCALE, both the paired difference and rank-1 frequency shift toward AODV under the frozen configuration. No single protocol therefore occupies the leading position consistently across the stochastic realizations and operating conditions examined here.

## D. Zero-Delivery Stress Signal

The scale-stress condition also increases the frequency of complete delivery failure. Zero-PDR runs occur in 2 of 20 AODV replications, 7 of 20 DSDV replications, 8 of 20 DSR replications, and 8 of 20 OLSRv1 replications. These events are retained as outcomes rather than silently excluded or replaced.

The zero-delivery counts provide a useful stress signal but do not define a failure frontier. A formal frontier would require a predeclared operational requirement and a denser sweep over the condition responsible for transition between acceptable and unacceptable behavior. The four S2 scenarios are insufficient for such interpolation.

## E. What the Controlled Evidence Establishes

The S2 results support three bounded conclusions. First, protocol ordering is conditional on the operating scenario: the AODV--DSR comparison changes from unresolved separation in BASE, FAST, and LOAD to a positive AODV paired difference in SCALE. Second, seed-level rank membership is unstable enough that a single mean or one stochastic realization can give an incomplete picture of comparative behavior. Third, the SCALE scenario exposes substantial zero-delivery incidence for all four implementations, with particularly high counts for DSDV, DSR, and OLSRv1 in this frozen design.

The results do not establish that one protocol is universally best, that one family dominates another over the MANET design space, or that the observed SCALE stress defines a general scalability law. Their broader significance is methodological: routing claims become more defensible when the operating condition, stochastic replication, uncertainty, multiplicity, implementation provenance, and failure outcomes remain visible.
