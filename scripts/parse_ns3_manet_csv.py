import csv,sys
from pathlib import Path
if len(sys.argv)!=3: raise SystemExit("usage: parse_ns3_manet_csv.py INPUT OUTPUT")
src,dst=Path(sys.argv[1]),Path(sys.argv[2])
if not src.exists(): raise SystemExit(f"missing ns-3 output: {src}")
with src.open(newline="",encoding="utf-8",errors="replace") as f:
    rows=[r for r in csv.reader(f) if r and any(c.strip() for c in r)]
if not rows: raise SystemExit("ns-3 output is empty")
dst.parent.mkdir(parents=True,exist_ok=True)
with dst.open("w",newline="",encoding="utf-8") as f: csv.writer(f).writerows(rows)
print(f"PARSE_PASS rows={len(rows)} output={dst}")
