# Multi-Agent Literature Mining Architecture

All agents use the same extraction schema and confidence rules. An agent is responsible for a routing family, not for independently defining what counts as evidence.

## Agents

| ID | Focus |
|---|---|
| A00 | Standards, definitions, and foundational MANET assumptions |
| A01 | DSDV and proactive distance-vector routing |
| A02 | AODV family |
| A03 | DSR family |
| A04 | OLSR / OLSRv2 |
| A05 | ZRP and hybrid routing |
| A06 | AOMDV and multipath routing |
| A07 | TORA and temporally adaptive routing |
| A08 | Geographic / position-based routing |
| A09 | Babel and modern loop-avoiding distance-vector routing |
| A10 | Opportunistic / DTN-style MANET routing |
| A11 | QoS-aware routing |
| A12 | Energy-aware routing |
| A13 | Trust- and security-aware routing |
| A14 | ACO / AntHocNet / swarm routing |
| A15 | GA / PSO and evolutionary routing |
| A16 | GWO / WOA / newer metaheuristics and hybrids |
| A17 | Fuzzy / game-theoretic / rule-based adaptive routing |
| A18 | Classical ML routing |
| A19 | Q-learning / tabular RL |
| A20 | DQN / DDQN / value-based DRL |
| A21 | Policy-gradient / actor-critic / PPO routing |
| A22 | Multi-agent reinforcement learning |
| A23 | Graph neural network routing |
| A24 | GNN + RL / MARL hybrids |
| A25 | Federated / distributed learning |
| A26 | Mobility/link prediction routing |
| A27 | Cross-layer and SDN-assisted MANET routing |
| A28 | Blockchain-assisted routing/security |
| A29 | Real-device/testbed and sim-to-real evidence |
| A30 | Reproducibility, benchmark methodology, and negative results |

## Mandatory questions for every algorithm agent

1. What routing decision is changed?
2. What network information must be observed?
3. Is information local, neighborhood, path, or global?
4. Is the method reactive, proactive, predictive, or mixed?
5. What state must be stored?
6. What messages/control packets are introduced?
7. What computation is required per decision/update?
8. What assumptions are made about synchronization, location, trust, energy, or topology?
9. Which baselines were used?
10. Were baselines tuned fairly?
11. Which mobility model and speed regime were used?
12. Which propagation/channel assumptions were used?
13. What scale/density/load was tested?
14. Which metrics were measured and how defined?
15. How many seeds/repetitions were used?
16. Is uncertainty reported?
17. Is implementation code available?
18. Is the exact experiment reproducible?
19. Which conditions were not tested?
20. What failure mode follows from the mechanism?
21. Is the claimed gain conditional on a narrow regime?
22. Does another paper report a conflicting conclusion?
23. Is the comparison actually commensurate?
24. What is the strongest hidden assumption?
25. Which controlled experiment would most efficiently falsify the claimed advantage?

## Agent output

Each agent emits structured rows into the shared evidence schema. Free-text narrative is secondary; every major conclusion must trace to one or more evidence rows.
