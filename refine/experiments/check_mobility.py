#!/usr/bin/env python3
"""Strictly compare sampled mobility traces across protocol runs.
Exact equality is a diagnostic, NOT proof of continuous-path equivalence.
"""
import argparse,csv,hashlib
from pathlib import Path
p=argparse.ArgumentParser()
p.add_argument("traces",nargs="+",help="Per-run diagnostic -mobility.csv paths")
p.add_argument("--tolerance",type=float,default=0.0,help="Absolute coordinate tolerance in metres; default exact")
a=p.parse_args()
if len(a.traces)<2: p.error("supply at least two traces")
if a.tolerance<0: p.error("negative tolerance")
baseline=None
for name in a.traces:
 path=Path(name)
 with path.open(newline="",encoding="utf-8") as f:
  reader=csv.DictReader(f)
  required={"simulation_time_ns","node_id","x_m","y_m","z_m"}
  if not required.issubset(reader.fieldnames or []): raise SystemExit(f"FAIL schema: {name}")
  rows={}
  for row in reader:
   key=(int(row["simulation_time_ns"]),int(row["node_id"]))
   if key in rows: raise SystemExit(f"FAIL duplicate sample {key}: {name}")
   rows[key]=tuple(float(row[c]) for c in ("x_m","y_m","z_m"))
 if not rows: raise SystemExit(f"FAIL empty trace: {name}")
 times=sorted({t for t,_ in rows});nodes=sorted({i for _,i in rows})
 if len(rows)!=len(times)*len(nodes): raise SystemExit(f"FAIL incomplete sample grid: {name}")
 digest=hashlib.sha256(path.read_bytes()).hexdigest()
 print(f"TRACE {name}: samples={len(rows)} nodes={len(nodes)} times={len(times)} sha256={digest}")
 if baseline is None: baseline=rows;continue
 if rows.keys()!=baseline.keys(): raise SystemExit(f"FAIL sampling keys differ: {name}")
 mismatch=[(k,baseline[k],v) for k,v in rows.items() if any(abs(x-y)>a.tolerance for x,y in zip(baseline[k],v))]
 if mismatch: raise SystemExit(f"FAIL mobility mismatch in {len(mismatch)} samples, first={mismatch[0]}: {name}")
print("PASS sampled mobility positions agree across all supplied traces")
print("LIMITATION: periodic samples do not establish identical continuous trajectories between samples.")
