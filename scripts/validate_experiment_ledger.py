#!/usr/bin/env python3
import csv
from pathlib import Path

p=Path("benchmark/experiment_ledger.csv")
rows=list(csv.DictReader(p.open(newline="", encoding="utf-8")))
assert rows, "experiment ledger is empty"
required={"run_group","workflow_run_id","protocol","protocol_selector","ns3_version","configure_status","build_status","simulation_status","schema_status","artifact_status","evidence_level","interpretation"}
assert required.issubset(rows[0]), f"missing columns: {required-set(rows[0])}"
valid={"AODV":"AODV","DSDV":"DSDV","DSR":"DSR","OLSRv1":"OLSR"}
for r in rows:
    assert r["protocol"] in valid, r
    assert r["ns3_version"]=="3.47", r
    if r["evidence_level"]!="invalidated":
        assert r["protocol_selector"]==valid[r["protocol"]], r
    if r["simulation_status"]=="PASS":
        assert r["build_status"]=="PASS", r
    if r["schema_status"]=="PASS":
        assert r["simulation_status"]=="PASS", r
    if r["artifact_status"]=="PASS":
        assert r["schema_status"]=="PASS", r
    if r["evidence_level"]=="invalidated":
        assert r["simulation_status"] in {"SUPERSEDED","FAIL","INVALID"}, r
print(f"EXPERIMENT_LEDGER=PASS rows={len(rows)}")
