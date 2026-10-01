#!/usr/bin/env python3
import csv, math, sys
p=sys.argv[1]
with open(p,newline="",encoding="utf-8") as fh:
    reader=csv.DictReader(fh)
    r=list(reader)
assert len(r)==1
x=r[0]
assert None not in x, "data row has more columns than header"
required={"node_count","area_width_m","area_height_m","mobility_model","max_speed_mps","traffic_model","packet_rate_pps","payload_bytes","app_packets_sent","app_packets_received"}
assert required.issubset(x), f"schema missing: {required-set(x)}"
assert x["mobility_model"]=="RandomWaypoint"
assert x["traffic_model"]=="UDP-periodic"
tx=int(x["app_packets_sent"]); rx=int(x["app_packets_received"]); matched=int(x["matched_packets"])
pdr=float(x["pdr"]); goodput=float(x["goodput_bps"])
print("COMMON_RUNNER_DIAGNOSTIC",x["protocol"],"tx",tx,"rx",rx,"matched",matched,"pdr",pdr,"goodput_bps",goodput,flush=True)
assert tx>0 and 0<=rx<=tx
assert matched==rx
assert 0<=pdr<=1 and abs(pdr-rx/tx)<1e-9
assert goodput>=0
for k in ("mean_delay_ms","median_delay_ms","p95_delay_ms","mean_jitter_ms"):
    v=float(x[k]); assert math.isnan(v) or v>=0
assert x["validity_status"]=="PASS"
print("COMMON_RUNNER_VALIDATION=PASS",x["protocol"],"tx",tx,"rx",rx,"pdr",pdr)
