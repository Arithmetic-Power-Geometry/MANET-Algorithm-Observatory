import csv, hashlib
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
FILES=[
"literature/master_studies.csv",
"literature/classical_evidence_v3.csv",
"literature/closest_reviews.csv",
"literature/comparability_maturity_atlas.csv",
"literature/contradiction_registry.csv",
"literature/research_obligations.csv",
"literature/gap_registry.csv",
"benchmark/S2_CONFIRMATORY_SEEDS.csv",
"benchmark/S2_SCENARIOS.csv",
"artifacts/s2/pairwise_pdr_gate6.csv",
"artifacts/s2/FINAL_BENCHMARK_TABLES.md",
"artifacts/FINAL_ARTIFACT_INDEX.csv",
"review/GATE7_CAPABILITY_DECISION.md",
"review/CORPUS_STOPPING_RULE.md",
]
def main():
    missing=[p for p in FILES if not (ROOT/p).is_file()]
    if missing: raise SystemExit("missing frozen evidence: "+", ".join(missing))
    rows=[]
    for p in FILES:
        b=(ROOT/p).read_bytes()
        rows.append((p,len(b),hashlib.sha256(b).hexdigest()))
    out=ROOT/"artifacts"/"EVIDENCE_CHECKSUMS.csv"
    with out.open("w",newline="",encoding="utf-8") as f:
        w=csv.writer(f); w.writerow(["path","bytes","sha256"]); w.writerows(rows)
    print(f"FROZEN_EVIDENCE_FILES={len(rows)}")
    print("CHECKSUM_AUDIT=PASS")
if __name__=="__main__": main()
