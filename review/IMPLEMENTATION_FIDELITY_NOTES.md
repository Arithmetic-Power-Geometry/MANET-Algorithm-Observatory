# Implementation Fidelity

A protocol name alone is insufficient to identify an experiment. Controlled evidence is therefore associated with the chain

**algorithm concept → specification/version → implementation → simulator/version → parameterization → observed result**.

## OLSR example

OLSR and OLSRv2 are related but are not interchangeable experimental objects. The native ns-3 OLSR model used in the controlled benchmark corresponds to OLSRv1; literature evidence about OLSRv2 remains part of the broader evidence synthesis but is not treated as controlled OLSRv1 benchmark evidence.

## DSR scope

The benchmark label DSR refers specifically to the evaluated ns-3 implementation. Results are not generalized to untested DSR implementations or versions.

## General rule

Implementation fidelity is part of claim validity whenever protocol versions differ, specification features are omitted, parameters materially change behavior, external implementations modify the mechanism, or simulator interfaces constrain measurement.

Controlled claims therefore retain implementation identity and version information together with the evaluated condition and metric definition.
