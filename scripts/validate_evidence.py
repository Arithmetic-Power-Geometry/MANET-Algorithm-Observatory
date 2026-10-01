import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "literature" / "evidence_schema.csv"
SPINE = ROOT / "literature" / "classical_spine.csv"

def headers(path):
    with path.open(newline="", encoding="utf-8") as f:
        return next(csv.reader(f))

def main():
    required_schema = {
        "study_id","title","year","algorithm","family","baseline","scenario",
        "mobility_model","propagation_model","simulator_testbed","metric",
        "comparability_class","reproducibility_status","hidden_assumption","gap_tags"
    }
    missing = required_schema - set(headers(SCHEMA))
    if missing:
        raise SystemExit(f"evidence schema missing fields: {sorted(missing)}")

    with SPINE.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if len(rows) < 9:
        raise SystemExit("classical spine unexpectedly incomplete")
    ids = [r["id"] for r in rows]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate classical-spine IDs")
    mandatory = ["protocol","family","problem_targeted","core_mechanism",
                 "capability_gained","structural_cost","primary_source",
                 "status","benchmark_tier"]
    for r in rows:
        empty = [k for k in mandatory if not r.get(k,"").strip()]
        if empty:
            raise SystemExit(f'{r.get("id","?")} missing {empty}')
    print(f"OK: evidence schema validated; {len(rows)} classical protocols registered")

if __name__ == "__main__":
    main()
