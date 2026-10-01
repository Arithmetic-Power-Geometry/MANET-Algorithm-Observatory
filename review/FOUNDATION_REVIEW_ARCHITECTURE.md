# Foundation Review Architecture

## Purpose

The review is designed as a reusable research map rather than a catalogue of routing protocols.

Its central object is the complete chain:

```
research problem
→ routing decision
→ mechanism
→ required information
→ assumptions
→ evaluation design
→ evidence strength
→ demonstrated capability
→ failure condition
→ unresolved obligation
```

## Six layers

### Layer I — Historical mechanism atlas
Tracks why each major routing family appeared, what prior limitation it addressed, and which new cost it introduced.

### Layer II — Complete status atlas
For each algorithm/family:
- maturity: proposed / specified / standardized / maintained / historical;
- evidence: analytical / simulation / emulation / testbed / field;
- implementation availability;
- simulator availability;
- reproducibility;
- scale tested;
- mobility regimes;
- propagation realism;
- security evidence;
- energy evidence;
- learning/generalization evidence where applicable;
- known failure modes;
- unresolved questions.

### Layer III — Claim-validity atlas
Every performance claim is attached to:
- comparator;
- scenario;
- metric definition;
- simulator/testbed;
- repetitions/seeds;
- uncertainty;
- implementation provenance;
- comparability class C0–C4.

### Layer IV — Research-space coverage atlas
Maps tested and untested cells across:
algorithm × mobility × scale × density × traffic × propagation × energy × attack × deployment evidence.

### Layer V — Contradiction and frontier atlas
Separates:
- genuine contradictory results;
- results that only appear contradictory because scenarios differ;
- ranking reversals caused by environment/model choices;
- known and hypothesized failure frontiers.

### Layer VI — Executable evidence atlas
Controlled Observatory experiments reproduce admissible algorithms under the common benchmark contract. These results remain separate from published evidence.

## Reader views

The same evidence base must answer five different researcher questions:

1. **New researcher:** What exists and how did the field evolve?
2. **Algorithm designer:** What mechanism space is already occupied?
3. **Experimental researcher:** What should a fair benchmark contain?
4. **Reviewer/editor:** Is a claimed comparison scientifically commensurate?
5. **Future researcher:** Which unresolved gap has enough evidence to justify new work?

## Non-goal

The review does not manufacture a universal leaderboard from heterogeneous literature.

## Standard of contribution

Breadth alone is insufficient. The review should contribute reusable structures:
- an ontology;
- evidence schema;
- comparability rules;
- status cards;
- gap vocabulary;
- benchmark contract;
- machine-readable corpus;
- reproducible visual artifacts.
