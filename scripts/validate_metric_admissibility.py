import csv
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"benchmark"/"METRIC_ADMISSIBILITY.csv"
rows=list(csv.DictReader(p.open(newline="",encoding="utf-8")))
required={"packet_delivery_ratio","goodput","end_to_end_delay","jitter","routing_control_packets","routing_control_bytes"}
names={r["metric"] for r in rows}
missing=required-names
if missing: raise SystemExit("missing required metric admissibility rows: "+", ".join(sorted(missing)))
for r in rows:
    if r["metric"]=="packet_delivery_ratio" and r["confirmatory_admissible_from_upstream_csv"].lower()=="yes":
        raise SystemExit("PDR must not be admitted from upstream receive-only CSV")
print("METRIC_ADMISSIBILITY=PASS")
