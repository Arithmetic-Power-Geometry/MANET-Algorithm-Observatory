# MANET Algorithm Observatory

A reproducible research observatory for mapping, comparing, stress-testing, and gap-mining routing algorithms for mobile ad hoc networks (MANETs).

## Research objective

The project separates two forms of evidence:

1. **Published evidence** — what the literature claims under its original assumptions and evaluation settings.
2. **Controlled evidence** — what reproducible algorithms do under a shared experimental contract.

The central questions are not only which algorithms perform well, but **under which conditions their advantages hold, where rankings change, which assumptions drive the result, and which parts of the MANET design space remain weakly tested or untested**.

## Research pipeline

```
Literature corpus
      ↓
Evidence extraction
      ↓
Protocol / algorithm ontology
      ↓
Comparability audit
      ↓
Reproducibility audit
      ↓
Common benchmark contract
      ↓
Controlled experiments
      ↓
Failure and ranking frontiers
      ↓
Evidence-backed gap map
      ↓
Candidate novel algorithm
      ↓
Same benchmark + ablation + statistics
      ↓
Versioned research artifacts
```

## Core protocol families

The observatory covers classical proactive/reactive/hybrid and multipath protocols, geographic and opportunistic routing, energy/QoS/security-aware designs, bio-inspired/metaheuristic approaches, and modern ML/RL/DRL/MARL/GNN-based routing.

## Evidence rule

Reported values from different publications are **not treated as directly comparable unless the relevant experimental conditions are sufficiently aligned**. Literature results and observatory benchmark results remain separate datasets.

## Reproducibility rule

Each controlled result must identify scenario configuration, simulator/software version, algorithm implementation/version, random seed(s), mobility source, propagation/channel configuration, traffic configuration, metrics, and analysis script.

## Repository layout

- `review/` systematic-review protocol, research questions, taxonomies, and gap framework
- `literature/` structured corpus and extracted evidence
- `agents/` algorithm-family mining specifications
- `benchmark/` shared scenario and metric contracts
- `experiments/` reproducible experiment configurations
- `analysis/` statistical, frontier, sensitivity, and gap-mining analysis
- `artifacts/` generated figures, tables, timelines, matrices, and machine-readable summaries

The repository is research infrastructure. Versioned artifacts are generated from the evidence and experimental workflow.
