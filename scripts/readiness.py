import csv
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
PENDING = ROOT / "literature" / "pending_work.csv"

def main():
    with PENDING.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    allowed = {"pending","in_progress","complete","waived"}
    bad = [r["work_id"] for r in rows if r["status"] not in allowed]
    if bad:
        raise SystemExit(f"invalid status: {bad}")
    counts = Counter(r["status"] for r in rows)
    p0_open = [r for r in rows if r["priority"]=="P0" and r["status"] not in {"complete","waived"}]
    print(f"tasks={len(rows)} complete={counts['complete']} in_progress={counts['in_progress']} pending={counts['pending']} waived={counts['waived']}")
    print(f"P0 open={len(p0_open)}")
    if p0_open:
        print("PAPER_DRAFTING_GATE=CLOSED")
        for r in p0_open:
            print(f"{r['work_id']}: {r['task']} [{r['status']}]")
    else:
        print("PAPER_DRAFTING_GATE=OPEN")

if __name__ == "__main__":
    main()
