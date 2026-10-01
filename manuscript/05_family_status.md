# V. Status of Major MANET Routing Families

The taxonomy becomes useful only when each routing family is described with the same questions. This section therefore uses a common status structure: the routing decision being changed, the mechanism and information required, the capability gained, the structural cost introduced, the maturity of the supporting evidence, and the unresolved evidence obligation. The purpose is not to rank families but to expose what is known at different levels of confidence.

## A. Proactive Routing

Proactive routing maintains reachability information before a packet requires it. DSDV represents the distance-vector branch: destination sequence numbers impose freshness ordering on distributed routing state, while periodic and triggered advertisements maintain routes. OLSRv1 represents proactive link-state optimization: HELLO and topology-control messages maintain neighborhood and topology state, while multipoint relays reduce redundant dissemination.

The shared capability is immediate availability of route state when forwarding demand appears. The shared cost is maintenance that continues independently of whether a destination is actively used. DSDV pays through routing-table dissemination and per-destination state; OLSRv1 additionally depends on neighborhood structure, MPR selection, and topology-control behavior. Foundational specifications establish these mechanisms, but heterogeneous evaluations do not justify a context-free ordering among proactive designs or against other families. Controlled external evidence further shows that propagation assumptions can materially change conclusions involving selected classical protocols. The corresponding obligation is therefore robustness across channel, mobility, scale, density, and demand rather than another unconditional average-performance comparison.

## B. Reactive Routing

Reactive routing moves route acquisition toward the moment of demand. AODV uses route-request and route-reply signaling with sequence-number freshness and route-error maintenance. DSR combines on-demand discovery with source routes and route caches. Both reduce the need for continuous route advertisements, but they allocate cost differently: AODV incurs discovery and repair signaling, whereas DSR additionally places path information in packet headers and relies on cache validity.

Their evidence status illustrates why mechanism and evaluation must be separated. The protocol specifications provide strong evidence for how the mechanisms operate, but they do not establish modern performance superiority. The important unresolved question is conditional: under what combination of mobility, active-route demand, path length, load, and channel conditions does deferred acquisition outweigh continuous maintenance? The Observatory addresses a small controlled part of this question for AODV and the evaluated ns-3 DSR implementation, but it does not map the full reactive--proactive crossover surface.

## C. Hybrid Routing

Hybrid routing combines different information horizons or temporal regimes, typically attempting to keep inexpensive local information available while avoiding full network-wide maintenance. The attraction is structural: a MANET need not choose one global point on the proactive--reactive spectrum if route demand and mobility are heterogeneous.

The difficulty is that hybridization introduces its own boundary decisions. Zone size, hierarchy, controller reach, update frequency, or switching criteria determine when the system behaves proactively and when it pays discovery cost. Consequently, a hybrid method should be evaluated not only against pure families but also against the overhead and sensitivity of the mechanism that chooses between regimes. In the present verified corpus, hybrid routing is part of the mechanism map, but its evidence is not normalized sufficiently to support a quantitative cross-family ranking.

## D. Multipath Routing

Multipath routing changes route maintenance by retaining alternatives. AOMDV extends reactive distance-vector routing with multiple loop-free paths; ant-based designs can further adapt path preference using observations such as availability, delay, or bandwidth. The capability is resilience to a single active-path failure and, in some designs, load distribution.

The additional paths are also the principal cost. They consume state, discovery or maintenance effort, and can provide less resilience than expected when failures are correlated or alternatives become stale together. The key open obligation is therefore correlation-aware evaluation: single-path and multipath methods should be compared under controlled failures in which alternate-path independence is varied rather than assumed. Existing mechanism evidence supports the rationale for alternate routes but does not establish a universal resilience advantage.

## E. Geographic and Position-Assisted Routing

Geographic routing substitutes location and local geometry for part of the topology knowledge used by conventional route construction. GPSR is the foundational example in the verified corpus, using greedy forwarding with perimeter recovery. The information requirement shifts toward node position, neighbor position, and a location service; the benefit is that forwarding need not depend on maintaining complete end-to-end topology state.

This family introduces a different failure surface. Position error, stale neighbor information, geographic voids, and the cost or availability of location information become routing variables. Software-defined geographic designs such as SD-GPSR show that geographic forwarding can be combined with controller assistance and explicit recovery mechanisms. Such combinations expand capability but also change the information and infrastructure assumptions. Geographic methods should therefore be compared under matched location-information budgets and void/recovery conditions rather than treated as ordinary topology-routing substitutes.

## F. QoS-, Energy-, and Resource-Aware Routing

QoS-aware routing changes the objective from reachability alone to requirements such as delay, bandwidth, reliability, or combinations of these quantities. Energy-aware routing similarly introduces residual energy, lifetime, transmission cost, or related resource state into path selection. These approaches are best understood as modifications of the routing decision contract: the algorithm receives additional state and is asked to satisfy a richer objective.

The central evidence problem is fairness. A method using bandwidth, energy, queue, or mobility information should not be compared with a simpler baseline as though both operate with the same observation budget. Moreover, improvement in one objective can move cost elsewhere. A defensible evaluation must therefore report both the added information required and the resulting resource trade-off. The present evidence atlas treats these families as established design branches but does not collapse heterogeneous study-local results into a common quantitative ordering.

## G. Trust- and Security-Aware Routing

Security-aware routing incorporates evidence about node behavior, reputation, trust, attacks, or route integrity into forwarding decisions. Verified recent work includes reputation-guided Q-learning and federated trust-aware routing. These mechanisms demonstrate that trust and learning can be integrated directly into route choice rather than added only as an external security layer.

Their evidence obligation is correspondingly broader. Attack model, adversary knowledge, trust observations, false-positive behavior, coordination cost, and adaptation under previously unseen attacks all affect interpretation. A security-aware route can appear superior because it observes information unavailable to a conventional baseline. Comparisons therefore need matched threat models and explicit accounting of trust acquisition and learning cost.

## H. Metaheuristic Routing

Metaheuristic methods use search or population-inspired procedures to construct or adapt routes under objectives that may be difficult to optimize with a fixed local rule. The verified corpus includes ant-colony multipath routing, where path preference reflects observations including next-hop availability, delay, and bandwidth.

Such methods can represent multi-objective or dynamic decisions, but the search process itself consumes messages, state, computation, or convergence time. Evidence should distinguish the value of the selected route from the cost of discovering and maintaining it. Study-local comparative simulation establishes the existence of adaptive metaheuristic MANET routing, but it does not establish that metaheuristics dominate classical or learning approaches across conditions.

## I. Reinforcement-Learning Routing

Reinforcement learning replaces part of a hand-crafted route-selection rule with value or policy adaptation driven by feedback. Verified MANET work includes Q-learning approaches using mobility, position, energy, stability, delay, reputation, or related state. This is important historically because it establishes adaptive learning as prior MANET routing capability rather than a feature introduced only by contemporary deep models.

The capability comes with new dependencies: state representation, reward definition, feedback availability, exploration, convergence, and adaptation rate. A policy tuned to one topology or mobility distribution may not remain useful under another. The principal unresolved obligations are therefore out-of-distribution generalization and full resource accounting. Performance improvement inside a training-like scenario is not evidence of general routing adaptability.

## J. Deep and Multi-Agent Reinforcement Learning

Deep reinforcement learning extends the representational capacity of learned routing decisions, while multi-agent reinforcement learning distributes decision making across nodes or agents. Verified recent MANET evidence includes dynamic decentralized routing that combines multi-agent deep reinforcement learning with graph neural representations.

These approaches can encode richer topology-dependent state and coordination than tabular learning, but their routing cost includes model training, inference, observation exchange, inter-agent information, update frequency, and possibly retraining. Current verified evidence is predominantly study-specific comparative simulation. The central question is therefore not whether deep models can produce routes, which is already established, but whether their additional representational capacity survives topology, scale, mobility, traffic, and observation shifts at an acceptable resource cost.

## K. Graph-Based and Federated Learning

Graph neural networks align naturally with network topology because nodes, links, and neighborhoods can be represented directly in graph form. Federated learning addresses a different constraint: distributed model construction without centralizing all raw observations. Verified MANET evidence includes both MARL--GNN dynamic routing and federated multi-objective trust-aware routing; adjacent MANET--IoT work further combines graph representation with transformer-style decision mechanisms.

These branches occupy different points in the information and coordination space. A graph model may require timely structural observations; a federated method requires model-update coordination and must confront non-identically distributed local experience. Their existence closes any simple literature-gap argument that MANET routing lacks graph, federated, or distributed intelligent mechanisms. What remains unresolved is capability under defined distribution shift, communication budgets, and deployment constraints.

## L. Predictive, Cross-Layer, and Software-Defined Routing

Predictive routing attempts to act on anticipated mobility, link quality, or future topology rather than only the current network state. Cross-layer methods incorporate information from lower or higher layers into routing decisions. Software-defined approaches introduce controller-visible state or centralized/partially centralized coordination. SD-GPSR provides one verified example of geographic routing combined with software-defined assistance and explicit recovery.

These methods can improve observability or coordination, but they alter the system boundary. Prediction requires a forecast and a horizon; cross-layer routing requires additional measurements; software-defined routing requires controller reachability, synchronization, or control-plane assumptions. Their evaluation must therefore include the failure and cost of the added information path, not only the quality of the resulting route.

## M. What the Status Atlas Establishes

Three conclusions follow from the family-level synthesis. First, MANET routing already contains a wide range of decision mechanisms, including proactive and reactive rules, source routing, multipath, geographic forwarding, metaheuristics, reinforcement learning, federated learning, multi-agent deep reinforcement learning, and graph representation. A new contribution cannot establish novelty merely by adding adaptivity, AI, trust, multipath behavior, or graph learning.

Second, evidence depth is uneven. Foundational protocols are well defined, but many contemporary comparisons remain study-local and cannot be combined safely because scenarios, information budgets, baselines, and statistical practices differ. Algorithmic sophistication and evidence maturity therefore remain separate dimensions.

Third, the strongest surviving research questions concern evidence validity: robustness to assumptions, reproducibility across seeds and implementations, out-of-distribution generalization, resource cost, and simulation-to-real correspondence. In the frozen corpus, no specific missing intelligent-routing capability has yet been demonstrated strongly enough to justify a capability-gap claim. This is why the present work proceeds to evidence comparability and controlled reproduction rather than introducing another routing algorithm.
