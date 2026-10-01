# III. Evolution of MANET Routing as a Sequence of Design Responses

MANET routing is often presented as a chronology of protocol names. A more useful interpretation is that each major family reallocates the cost of obtaining, maintaining, or predicting route information. The resulting history is therefore not a sequence in which one generation simply replaces another. It is a sequence of responses to different operating assumptions.

## A. Maintaining Reachability Before Demand

Early proactive designs address the problem of maintaining usable routes despite topology change. DSDV augments distributed distance-vector state with destination sequence numbers, providing an explicit freshness ordering for route information. The capability gained is continuously available next-hop state with loop-avoidance properties tied to sequence-number freshness. The corresponding structural cost is persistent per-destination state and periodic or triggered dissemination.

OLSR addresses a related but different pressure. Rather than abandoning proactive topology maintenance, it reduces redundant link-state dissemination through multipoint relays. Its design response is therefore an optimization of how network knowledge is propagated. The cost remains continuous neighborhood and topology maintenance, and the value of the optimization depends on neighborhood structure and the conditions under which control information is exchanged.

These proactive mechanisms establish a recurring MANET trade-off: information acquired before demand can reduce route-acquisition delay, but maintaining that information consumes communication and state even when routes are unused.

## B. Moving the Cost to Discovery and Repair

Reactive routing changes when the network pays for route knowledge. AODV avoids maintaining inactive routes and instead uses route-request and route-reply signaling when communication is required, with sequence numbers preserving freshness. The gained capability is demand-triggered acquisition; the new cost is discovery latency, flooding, and repair signaling.

DSR moves the representation of routing knowledge further. Route discovery and maintenance are combined with source routes and route caches, allowing packets to carry an ordered path rather than relying only on distributed next-hop state. This removes the need for periodic routing advertisements but introduces source-route header growth and sensitivity to cached information becoming stale.

The proactive--reactive distinction is consequently not a contest between intrinsically superior and inferior protocols. It is a decision about when information is acquired and where its cost is paid. Mobility, active-route demand, path length, and traffic intensity can change the balance.

## C. Trading Additional State for Repair Resilience

A single active route can force a new discovery when that route breaks. Multipath mechanisms respond by maintaining alternatives. AOMDV extends on-demand distance-vector routing with multiple loop-free paths, exchanging additional route state and maintenance for the possibility of avoiding immediate rediscovery after a failure. Later ant-based multipath approaches add adaptive path preference using quantities such as next-hop availability, delay, and bandwidth.

This transition illustrates a broader principle: resilience is not free redundancy. Its value depends on whether alternate paths fail independently, remain fresh, and can be maintained at acceptable control and state cost. A multipath claim is therefore incomplete if the evaluation reports only delivery improvement without exposing the conditions and cost of maintaining alternatives.

## D. Replacing Topology Knowledge with Position and Local Geometry

Geographic routing changes the information regime rather than merely the route-search procedure. GPSR uses geographic position and local forwarding decisions, with perimeter recovery when greedy forwarding encounters a void. This can reduce dependence on global topology state, but it introduces location-service and neighbor-position assumptions.

More recent software-defined geographic designs illustrate how families can recombine. SD-GPSR couples geographic forwarding with software-defined assistance and path recovery, trading some decentralized simplicity for controller-visible information and additional recovery logic. The historical direction is therefore not from classical to intelligent in a single line; mechanisms repeatedly exchange global state, local sensing, control-plane support, and computation.

## E. Expanding the Routing Objective

As MANET studies moved beyond reachability and hop-based path choice, routing decisions increasingly incorporated delay, bandwidth, energy, mobility, trust, and security. This changes both the objective and the information required to evaluate candidate routes. A route selected for low delay need not be the route preferred for lifetime, trust, resilience, or communication cost.

The consequence is multi-objective rather than merely algorithmic. Comparisons become invalid when one method is allowed richer information or a different objective but the resulting performance is interpreted as if all methods solved the same decision problem. QoS-, energy-, and trust-aware routing should therefore be understood as changes to the routing decision contract as much as changes to the optimization mechanism.

## F. From Hand-Crafted Search to Adaptive Decision Rules

Metaheuristic routing introduces search procedures such as ant-colony mechanisms to adapt path preferences from observed network conditions. Reinforcement-learning approaches move the adaptation into a learned value or policy. Verified MANET evidence includes Q-learning designs that incorporate mobility, position, energy, stability, delay, reputation, or related state. These studies establish that adaptive learning for MANET routing is not a recent capability created by deep learning.

The cost allocation changes again. A learned decision may reduce dependence on a fixed hand-crafted rule, but it introduces reward design, feedback, exploration, state representation, convergence, and computational cost. The relevant question becomes not simply whether learning improves a reported metric, but whether the learned policy remains valid when topology, mobility, load, scale, or observation quality changes.

## G. Distributed Intelligence and Graph Representation

Recent routing work extends this trajectory through federated learning, deep reinforcement learning, multi-agent reinforcement learning, and graph neural representations. Federated trust-aware approaches distribute model construction without centralizing all raw observations. MARL--GNN designs use graph representations together with decentralized agents to adapt routing decisions to changing topology. Adjacent MANET--IoT work also combines graph representation with transformer-style decision mechanisms.

These mechanisms expand what the routing system can represent and coordinate, but they also expand the evidence obligation. Training cost, inference latency, model size, inter-agent communication, update frequency, observation availability, generalization, and retraining become part of routing cost. Sophistication of the decision rule does not by itself establish robustness or deployment maturity.

## H. Evolution as Cost Reallocation

Across these transitions, MANET routing can be interpreted as repeated reallocation of five resources: information, communication, state, computation, and time. Proactive methods acquire information before demand; reactive methods defer acquisition; source routing moves path state into packet and cache representations; multipath routing stores alternatives; geographic routing substitutes location information for parts of topology knowledge; optimization and learning add search, feedback, representation, or training.

This interpretation explains why older families remain scientifically relevant. They occupy different points in the routing design space rather than forming an obsolete-to-modern ladder. It also motivates the taxonomy in the next section: routing mechanisms should be compared by the decision they change, the information they consume, when that information becomes available, and the cost paid to obtain the resulting capability.
