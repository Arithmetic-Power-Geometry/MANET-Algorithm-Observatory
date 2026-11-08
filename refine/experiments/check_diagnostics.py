#!/usr/bin/env python3
"""Check per-run socket accounting and attempted-traffic equality; no false mobility claims."""
import argparse,csv,collections,pathlib,sys
p=argparse.ArgumentParser()
p.add_argument("runs",nargs="+",help="CSV output from diagnostic runner for one scenario/seed, one file per protocol")
p.add_argument("--prefixes",nargs="+",required=True,help="Matching diagnosticPrefix values")
a=p.parse_args()
if len(a.runs)!=len(a.prefixes): p.error("one prefix per run")
observations=[]
for run,prefix in zip(a.runs,a.prefixes):
 with open(run,newline="") as f:
  rows=list(csv.DictReader(f))
 if len(rows)!=1: raise SystemExit("FAIL: expected exactly one row: "+run)
 r=rows[0]
 attempts=int(r["tx_attempts"]); accepted=int(r["socket_accepted_packets"]); rejected=int(r["tx_rejected"])
 if attempts!=accepted+rejected: raise SystemExit("FAIL socket accounting: "+run)
 if int(r["app_packets_received"])>attempts: raise SystemExit("FAIL delivery count: "+run)
 with open(prefix+"-attempts.csv",newline="") as f: trace=list(csv.DictReader(f))
 if len(trace)!=attempts: raise SystemExit("FAIL attempt count: "+run)
 if len({(v["source_id"],v["sequence"]) for v in trace})!=len(trace): raise SystemExit("FAIL duplicate packet IDs: "+run)
 with open(prefix+"-socket-errors.csv",newline="") as f: errors=list(csv.DictReader(f))
 if sum(int(v["count"]) for v in errors)!=rejected: raise SystemExit("FAIL errno count: "+run)
 observations.append((r["protocol"],[(v["source_id"],v["sequence"],v["simulation_time_ns"]) for v in trace]))
 print("PASS accounting",r["protocol"],"attempted",attempts,"rejected",rejected,"errno",errors)
 baseline=observations[0][1]
for protocol,trace in observations[1:]:
 if trace!=baseline: raise SystemExit("FAIL traffic-attempt trace mismatch: "+protocol)
print("PASS application attempt schedules identical across listed runs")
print("UNKNOWN mobility realization equivalence: this diagnostic does not record node trajectories")
