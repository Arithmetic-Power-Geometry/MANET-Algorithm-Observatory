# Section V Table — Compressed Family Status Atlas

| Family | Routing decision / information shift | Capability | Structural cost or dependency | Current evidence interpretation | Main unresolved obligation |
|---|---|---|---|---|---|
| Proactive | maintain network/neighbor state before demand | immediately available routes | continuous signaling and state | mechanism mature; performance claims condition-dependent | propagation/mobility/load robustness |
| Reactive | acquire path state on demand | avoids maintaining inactive routes | discovery/repair latency and signaling | mechanism mature; crossover remains conditional | mobility × active-demand crossover |
| Source routing | source/path representation | explicit source-controlled path | header growth and cache staleness | established mechanism | cache/path-length sensitivity |
| Hybrid | combine local/proactive and wider/reactive regimes | regime-specific cost allocation | zone/switching/controller parameters | established branch; heterogeneous evidence | boundary-selection robustness |
| Multipath | retain alternate paths | repair resilience/load distribution | extra path state and maintenance | established mechanism; benefits condition-dependent | correlated-failure evaluation |
| Geographic | substitute position/local geometry for topology state | local position-based forwarding | location service/freshness and void recovery | established mechanism | matched location-budget/void tests |
| QoS/energy | enrich objective and observed state | constraint/resource-aware routing | sensing/state and objective trade-offs | broad design branch; heterogeneous evaluation | information-budget fairness |
| Trust/security | add behavior/trust/attack state | malicious-node-aware route choice | trust acquisition/model/coordination cost | intelligent security routing established | matched threat and unseen-attack tests |
| Metaheuristic | adaptive search over routes | flexible multi-objective search | search messages/compute/convergence | study-local comparative evidence | cost-aware controlled comparison |
| RL | feedback-driven value/policy | online adaptation | reward/state/feedback/convergence | established MANET prior art | OOD generalization and cost |
| DRL/MARL | rich learned/decentralized policy | high-capacity adaptive decisions | training/inference/coordination | recent study-specific simulation | shift robustness and resource accounting |
| GNN | graph-structured representation | topology-aware learned state | structural observation and inference | established recent prior art | scale/topology transfer |
| Federated | distributed model learning | avoids centralizing raw training data | model-update coordination/non-IID data | established recent prior art | communication cost/generalization |
| Predictive/cross-layer/SDN | add future/cross-layer/controller state | anticipation or richer coordination | forecast/measurement/control-plane assumptions | established design direction | failure/cost of added information path |

The table summarizes mechanism and evidence status; it is not a performance ranking.
