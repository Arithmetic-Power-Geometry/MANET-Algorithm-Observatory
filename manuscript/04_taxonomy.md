# IV. Unified Routing Decision and Mechanism Taxonomy

A taxonomy based only on protocol families obscures why apparently different methods may solve the same routing decision with different information or computational budgets. This survey therefore locates a routing method on five coupled axes: decision locus, information scope, temporal horizon, decision mechanism, and resource requirement. Evidence maturity is maintained as a separate axis because a sophisticated mechanism need not have mature empirical support.

## A. Decision Locus

The first axis asks what routing decision is changed. Relevant loci include route discovery, next-hop or path selection, forwarding, route maintenance and repair, multipath choice, prediction, trust assessment, and coordination or governance. Two algorithms should not be treated as direct substitutes merely because both are called routing protocols if one primarily changes discovery while another changes trust scoring or repair.

## B. Information Scope

Routing decisions may rely on local node state, one-hop neighbor state, complete or partial paths, zone-level information, network-wide topology, controller-visible state, or a learned latent representation. Information scope exposes hidden asymmetry in comparisons. A method with location, energy, trust, or global graph information is solving a richer observation problem than a baseline that observes only local connectivity.

## C. Temporal Horizon

The third axis describes when useful information becomes available. Proactive mechanisms maintain information before demand; reactive mechanisms acquire it after demand or failure; hybrid mechanisms combine regimes; predictive mechanisms estimate future link or mobility state; learning mechanisms adapt decisions from accumulated interaction. The temporal horizon identifies where latency and maintenance costs enter the system.

## D. Decision Mechanism

The mechanism axis includes distance-vector and link-state rules, source routing, geographic rules, multipath construction, fuzzy or rule systems, metaheuristics, supervised or self-supervised learning, reinforcement learning, deep reinforcement learning, multi-agent reinforcement learning, graph neural networks, and hybrid or cross-layer combinations. Mechanism labels describe how a decision is produced, not what evidence supports it.

## E. Objective

A routing decision can optimize or constrain reachability, path cost, delay, reliability, load, energy, lifetime, trust, security, mobility stability, or a multi-objective utility. Objective mismatch is a major source of false comparison. Improvement on a richer objective cannot be interpreted as general superiority unless the competing methods are evaluated under a common decision requirement.

## F. Resource Requirement

Every routing capability is purchased with resources. The relevant budget can include control traffic, route-discovery delay, stored state, packet-header overhead, sensing or location information, computation, training samples, inference time, model storage, inter-agent coordination, energy, or implementation complexity. These costs are part of the routing mechanism rather than peripheral implementation details when they determine feasibility on mobile nodes.

## G. A Decision Signature

For synthesis, a routing method can be represented conceptually by a decision signature

D = (L, I, T, M, O, R),

where L is decision locus, I information scope, T temporal horizon, M decision mechanism, O objective, and R resource requirement. The signature is descriptive rather than a performance score. Its purpose is to identify scientifically meaningful neighbors in the design space and to prevent novelty claims based only on renaming or recombining occupied mechanisms.

For example, DSDV and AODV differ strongly in temporal horizon and maintenance cost even though both use sequence-number freshness. DSR changes the representation of path state; GPSR changes the information regime toward position and local geometry; AOMDV changes the multiplicity of maintained paths; Q-learning changes the decision rule through feedback; and MARL--GNN approaches change both representation and coordination. The taxonomy therefore exposes continuity across generations without collapsing their different assumptions.

## H. Linking Taxonomy to Evidence

The decision signature answers what a method does and what it requires. The evidence framework in Section II answers how strongly its claimed behavior is supported. These dimensions must remain separate. A new mechanism can occupy a previously sparse taxonomic region while still having only demonstration-level evidence. Conversely, a classical mechanism can have limited novelty but a stronger body of reproducible evidence.

This separation also changes how research gaps are interpreted. A sparsely populated cell is a literature gap only. A capability gap requires evidence that existing mechanisms fail to satisfy a specified decision requirement under a defined condition. The survey therefore searches for gaps by decision signature and evidence obligation rather than by protocol-name frequency.
