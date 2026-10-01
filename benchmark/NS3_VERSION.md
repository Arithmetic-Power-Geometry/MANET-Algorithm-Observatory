# ns-3 Benchmark Version

The controlled benchmark uses **ns-3.47**.

The evaluated implementation identities are AODV, DSDV, the ns-3 DSR implementation used by the runner, and OLSRv1. OLSRv1 and OLSRv2 are not treated as interchangeable experimental objects.

The benchmark uses protocol-independent application accounting so that the primary packet-delivery-ratio measurement does not depend on protocol-specific internal tracing.

Any future change in simulator version, runner logic, scenario definitions, metric definitions, or seed policy constitutes a distinct experimental configuration and must be evaluated separately.
