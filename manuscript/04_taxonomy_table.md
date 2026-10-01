# Section IV Table — Representative Decision Signatures

| Representative mechanism | Decision locus | Information scope | Temporal horizon | Mechanism | Principal capability | Structural cost / requirement |
|---|---|---|---|---|---|---|
| DSDV | next-hop selection/maintenance | network | proactive | distance vector + sequence freshness | continuously maintained fresh routes | periodic/triggered dissemination and per-destination state |
| AODV | route discovery/repair | path/local | reactive | RREQ/RREP + sequence freshness | on-demand route acquisition | discovery latency, flooding and repair signaling |
| DSR | discovery/maintenance | path/source | reactive | source route + route cache | on-demand routing without periodic advertisements | header growth and cache staleness |
| OLSRv1 | topology routing | neighbor/network | proactive | link state + MPR dissemination | reduced redundant proactive flooding | continuous neighbor/topology state |
| AOMDV | route discovery/repair | path | reactive | loop-free multipath | alternate routes after failure | additional route state and maintenance |
| GPSR | next-hop forwarding | neighbor/geographic | local/reactive | greedy + perimeter forwarding | routing from position/local geometry | location service and position freshness |
| Ant multipath | multipath selection | path | adaptive | ant-colony search | load-aware adaptive path preference | search/control and multipath maintenance |
| Q-learning routing | adaptive next-hop/path | local/path | learning | value/reward feedback | online adaptation | reward design, feedback, convergence and compute |
| Federated trust routing | trust-aware route choice | distributed | learning | federated + multi-objective optimization | distributed security-aware adaptation | coordination, training and trust-state cost |
| MARL--GNN routing | decentralized dynamic route choice | graph/distributed | learning | graph representation + multi-agent DRL | topology-aware distributed adaptation | training, inference and inter-agent information cost |

This table describes decision structure and evidence-backed mechanism roles; it is not a protocol ranking.
