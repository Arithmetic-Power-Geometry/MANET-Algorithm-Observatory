#!/usr/bin/env python3
import csv, math, sys
p=sys.argv[1]
r=list(csv.DictReader(open(p,newline="",encoding="utf-8")))
assert len(r)==1
x=r[0]
tx=int(x["app_packets_sent"]); rx=int(x["app_packets_received"]); matched=int(x["matched_packets"])
pdr=float(x["pdr"]); goodput=float(x["goodput_bps"])
assert tx>0 and 0<=rx<=tx
assert matched==rx
assert 0<=pdr<=1 and abs(pdr-rx/tx)<1e-9
assert goodput>=0
for k in ("mean_delay_ms","median_delay_ms","p95_delay_ms","mean_jitter_ms"):
    v=float(x[k]); assert math.isnan(v) or v>=0
assert x["validity_status"]=="PASS"
print("COMMON_RUNNER_VALIDATION=PASS",x["protocol"],"tx",tx,"rx",rx,"pdr",pdr)
