import csv,glob
from pathlib import Path
files=sorted(glob.glob("artifacts/smoke/normalized/*.csv"))
expected={"AODV","DSDV","DSR","OLSRv1"}; seen=set(); summary=[]
for p in files:
    proto=Path(p).stem.split("_")[0]; seen.add(proto)
    with open(p,newline="",encoding="utf-8") as f: rows=list(csv.reader(f))
    summary.append((proto,len(rows),p))
missing=expected-seen
if missing: raise SystemExit("missing protocol outputs: "+", ".join(sorted(missing)))
out=Path("artifacts/smoke/smoke_comparison.csv"); out.parent.mkdir(parents=True,exist_ok=True)
with out.open("w",newline="",encoding="utf-8") as f:
    w=csv.writer(f); w.writerow(["protocol","nonempty_csv_rows","normalized_output"]); w.writerows(summary)
print("SMOKE_OUTPUT_SET=COMPLETE")
for x in summary: print(*x,sep=" | ")
