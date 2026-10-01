import csv
from pathlib import Path

root=Path("artifacts/downloaded")
out=Path("artifacts/generated/tier1_smoke_summary.csv")
out.parent.mkdir(parents=True,exist_ok=True)

expected={"AODV","DSDV","DSR","OLSR"}
summary=[]
for protocol in sorted(expected):
    matches=list(root.rglob(protocol+".csv"))
    if len(matches)!=1:
        raise SystemExit(f"{protocol}: expected exactly one CSV, found {len(matches)}")
    rows=list(csv.DictReader(matches[0].open(newline="",encoding="utf-8")))
    if not rows:
        raise SystemExit(f"{protocol}: no data rows")
    rx_packets=sum(int(float(r["PacketsReceived"])) for r in rows)
    rx_rate_sum=sum(float(r["ReceiveRate"]) for r in rows)
    summary.append([protocol,len(rows),rx_packets,rx_rate_sum])

with out.open("w",newline="",encoding="utf-8") as f:
    w=csv.writer(f)
    w.writerow(["protocol","time_rows","sum_packets_received","sum_receive_rate_kbps"])
    w.writerows(summary)

print("CANONICAL_SMOKE_SET=COMPLETE")
for r in summary: print(*r,sep=" | ")
print("NOTE=Smoke values validate execution only; they are not confirmatory performance rankings.")
