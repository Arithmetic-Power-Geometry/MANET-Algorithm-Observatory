# VIII. Reproducible Controlled MANET Observatory

## A. Role of the Controlled Benchmark

The controlled benchmark is not intended to replace the literature synthesis or to identify a universal routing winner. Its purpose is narrower: to provide a common experimental stratum in which selected classical implementations are observed under the same scenario definitions, seed policy, application accounting, and analysis rules. This C4 evidence makes it possible to distinguish variation caused by the controlled operating condition from differences that arise when unrelated published experiments are compared.

Four Tier-1 implementations were admitted: AODV, DSDV, DSR, and OLSRv1 in ns-3.47. The labels refer to the evaluated ns-3 implementations; in particular, the benchmark does not imply that every implementation conforming to the corresponding protocol family will exhibit identical behavior. Development and instrumentation runs were excluded from confirmatory inference.

## B. Frozen Confirmatory Design

The S2 confirmatory design was frozen before execution. Four scenarios isolate a small set of interpretable stresses. S2_BASE uses 25 nodes in a 250 m area, speed 5 m/s, an offered rate of 2 packets/s, a 60 s simulation, traffic beginning at 10 s, and a 512-byte application payload. S2_FAST retains the baseline configuration but raises speed to 15 m/s. S2_LOAD retains the baseline mobility and scale but raises the offered rate to 5 packets/s. S2_SCALE increases the population to 50 nodes and the area parameter to 354 m while retaining speed 5 m/s and rate 2 packets/s, providing an approximately constant-density scale stress.

Twenty seeds were predeclared for S2 and were disjoint from the earlier pilot set. Each protocol was executed for every seed in every scenario. The resulting design contains

4 protocols x 4 scenarios x 20 seeds = 320

confirmatory runs. All 320 raw runs passed the frozen validation gate.

## C. Measurement and Replication Unit

Application delivery is measured independently of protocol-specific routing instrumentation. Offered application datagrams form the delivery denominator, and received unique application identifiers form the numerator. This avoids changing the primary delivery definition because a protocol exposes different internal tracing facilities.

The independent replication unit for confirmatory inference is one protocol--scenario--seed run. Measurements collected within one simulation are not promoted to independent replications. Comparisons within a scenario are paired by seed, preserving the common stochastic design where applicable. This distinction is important because treating packet-level or time-sampled observations as independent would overstate the effective sample size.

## D. Statistical Analysis

For each frozen scenario, packet delivery ratio (PDR) is summarized over the 20 seed-level replications. Pairwise protocol differences are calculated seed by seed. Uncertainty for the mean paired PDR difference is represented by a bootstrap 95% interval. A paired Wilcoxon procedure is used as the rank-based inferential check, and multiplicity is controlled by Holm adjustment within each scenario family. Statistical separation is not interpreted as universal superiority: the estimand remains the paired PDR difference for the specified implementation and frozen scenario.

Ranking stability is examined separately from mean performance. For each seed and scenario, protocols are ordered by PDR and strict rank-1 membership is recorded. This reveals whether a protocol that has a favorable mean also occupies the leading position consistently across stochastic realizations.

## E. Reproducibility Boundary

The confirmatory batch, scenario manifest, predeclared seed list, analysis artifacts, and evidence checksums are versioned as part of the frozen evidence release candidate. The release audit verified 14 frozen evidence files by SHA-256 and returned CHECKSUM_AUDIT=PASS. The benchmark therefore supplies reproducible controlled evidence for the admitted scenario/metric combination.

Its external-validity boundary is equally explicit. S2 varies baseline conditions, mobility intensity, offered load, and scale through four discrete scenarios. It does not vary propagation model, does not constitute a dense factorial map of the MANET operating space, and does not provide a field-deployment comparison. Results below are therefore interpreted as condition-indexed evidence rather than estimates of protocol behavior over all MANET environments.
