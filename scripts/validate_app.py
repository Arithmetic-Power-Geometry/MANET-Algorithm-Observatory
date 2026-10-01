from pathlib import Path
import csv
import ast

ROOT=Path(__file__).resolve().parents[1]
required=[
"streamlit_app.py",
"app_core/data.py",
"app_pages/home.py",
"app_pages/algorithms.py",
"app_pages/evidence.py",
"app_pages/benchmark.py",
"app_pages/gaps.py",
"app_pages/methodology.py",
"app_pages/reproducibility.py",
"literature/master_studies.csv",
"literature/complete_status.csv",
"literature/pending_work.csv",
"benchmark/IMPLEMENTATION_PROVENANCE.csv",
"benchmark/smoke_test_status.csv",
]

missing=[p for p in required if not (ROOT/p).exists()]
if missing:
    raise SystemExit("missing app dependencies: "+", ".join(missing))

for p in required:
    if p.endswith(".py"):
        ast.parse((ROOT/p).read_text(encoding="utf-8"), filename=p)

def headers(path):
    with (ROOT/path).open(newline="",encoding="utf-8") as f:
        return set(next(csv.reader(f)))

contracts={
"literature/master_studies.csv":{"study_id","title","verification_state","scope","study_type"},
"literature/complete_status.csv":{"algorithm_name","family","benchmark_admission"},
"literature/pending_work.csv":{"work_id","priority","task","status"},
"benchmark/IMPLEMENTATION_PROVENANCE.csv":{"algorithm","implementation","admission_status"},
"benchmark/smoke_test_status.csv":{"protocol","overall"},
}
for path,needed in contracts.items():
    absent=needed-headers(path)
    if absent:
        raise SystemExit(f"{path} missing columns: {sorted(absent)}")

print("APP_INTEGRITY=PASS")
