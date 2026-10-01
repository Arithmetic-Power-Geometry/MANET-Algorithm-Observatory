# Implementation Fidelity as an Evidence Dimension

A protocol name is insufficient to identify an experiment.

For every controlled result the review records:

**algorithm concept → specification/version → implementation → simulator/version → parameterization → observed result**

## Example: OLSR

OLSR and OLSRv2 are related but not interchangeable experimental objects. The official ns-3 OLSR model is based on RFC 3626 and its documentation explicitly states that it is not compliant with RFC 7181 (OLSRv2).

Therefore:
- literature evidence about OLSRv2 is retained in the status atlas;
- native ns-3 OLSR benchmark evidence is labeled OLSRv1;
- no benchmark conclusion is generalized to OLSRv2 without separate evidence.

## General rule

Implementation fidelity becomes part of claim validity whenever:
- the implementation omits specification features;
- a protocol has multiple versions;
- parameters materially differ from canonical definitions;
- an external research implementation modifies the mechanism;
- simulator APIs impose measurement limitations.

This dimension will be included in the benchmark-admission table and threats-to-validity analysis.
