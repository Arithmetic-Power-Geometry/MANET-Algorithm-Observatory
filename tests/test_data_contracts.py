import csv
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def read(path):
    with (ROOT/path).open(newline="",encoding="utf-8") as f:
        return list(csv.DictReader(f))

def test_master_ids_unique():
    rows=read("literature/master_studies.csv")
    ids=[r["study_id"] for r in rows]
    assert len(ids)==len(set(ids))

def test_tier1_protocol_identity():
    rows=read("benchmark/smoke_test_status.csv")
    assert {r["protocol"] for r in rows}=={"AODV","DSDV","DSR","OLSRv1"}

def test_no_false_smoke_pass():
    rows=read("benchmark/smoke_test_status.csv")
    for r in rows:
        if r["overall"]=="pass":
            assert all(r[k]=="pass" for k in ["build","run","common_metrics","provenance","limitations_recorded"])

def test_paper_gate_not_premature():
    rows=read("literature/pending_work.csv")
    open_p0=[r for r in rows if r["priority"]=="P0" and r["status"] not in {"complete","waived"}]
    assert open_p0
