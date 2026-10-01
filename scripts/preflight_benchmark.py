import csv
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
STATUS=ROOT/"benchmark"/"smoke_test_status.csv"
REQ=["build","run","common_metrics","provenance","limitations_recorded"]

with STATUS.open(newline="",encoding="utf-8") as f:
    rows=list(csv.DictReader(f))

expected={"AODV","DSDV","DSR","OLSRv1"}
found={r["protocol"] for r in rows}
if found != expected:
    raise SystemExit(f"Tier-1 identity mismatch: expected {sorted(expected)}, found {sorted(found)}")

blocked=[]
for r in rows:
    missing=[k for k in REQ if r[k]!="pass"]
    if missing:
        blocked.append((r["protocol"],missing))

print("Tier-1 benchmark preflight")
for p,missing in blocked:
    print(f"BLOCKED {p}: {', '.join(missing)}")

if blocked:
    print("LARGE_BENCHMARK_GATE=CLOSED")
else:
    print("LARGE_BENCHMARK_GATE=OPEN")
