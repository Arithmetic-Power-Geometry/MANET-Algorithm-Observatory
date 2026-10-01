import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUS = ROOT / "literature" / "complete_status.csv"
SPINE = ROOT / "literature" / "classical_spine.csv"

ALLOWED_BENCHMARK = {"not assessed","candidate","admitted","blocked"}
ALLOWED_TEMPORAL = {"proactive","reactive","hybrid","predictive","adaptive"}

def load(path):
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def main():
    status = load(STATUS)
    spine = load(SPINE)
    if not status:
        raise SystemExit("complete_status.csv has no records")
    spine_ids = {r["id"] for r in spine}
    ids = [r["algorithm_id"] for r in status]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate algorithm_id in complete_status.csv")
    unknown = sorted(set(ids) - spine_ids)
    if unknown:
        raise SystemExit(f"status IDs absent from classical spine: {unknown}")
    for r in status:
        if r["benchmark_admission"] not in ALLOWED_BENCHMARK:
            raise SystemExit(f'{r["algorithm_id"]}: invalid benchmark_admission')
        if r["temporal_mode"] not in ALLOWED_TEMPORAL:
            raise SystemExit(f'{r["algorithm_id"]}: invalid temporal_mode')
        if not r["primary_spec"].strip():
            raise SystemExit(f'{r["algorithm_id"]}: missing primary_spec')
        if not r["last_verified"].strip():
            raise SystemExit(f'{r["algorithm_id"]}: missing last_verified')
    print(f"OK: {len(status)} complete-status records validated against {len(spine)} spine records")

if __name__ == "__main__":
    main()
