#!/usr/bin/env python3
"""Synthetic fixtures only: exercise diagnostic checkers without ns-3.
Run: python -m unittest refine/experiments/test_diagnostic_checkers.py -v
"""
import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

def write_csv(path, columns, rows):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)

class DiagnosticCheckerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def run_script(self, script, *args):
        return subprocess.run([sys.executable, str(HERE / script), *map(str,args)],
                              text=True, capture_output=True, check=False)

    def build(self, protocol, rejected=0, mismatch=False):
        prefix = self.root / protocol
        run = self.root / (protocol + ".csv")
        write_csv(run, ["protocol","tx_attempts","socket_accepted_packets",
                        "tx_rejected","app_packets_received"],
                  [{"protocol":protocol,"tx_attempts":2,
                    "socket_accepted_packets":2-rejected,
                    "tx_rejected":rejected,"app_packets_received":1}])
        write_csv(Path(str(prefix)+"-attempts.csv"),
                  ["source_id","sequence","simulation_time_ns"],
                  [{"source_id":0,"sequence":0,"simulation_time_ns":100},
                   {"source_id":0,"sequence":1,"simulation_time_ns":200 if not mismatch else 201}])
        write_csv(Path(str(prefix)+"-socket-errors.csv"),["socket_errno","count"],
                  ([{"socket_errno":3,"count":rejected}] if rejected else []))
        return run,prefix

    def mobility(self, name, altered=False):
        path=self.root/(name+"-mobility.csv")
        write_csv(path,["simulation_time_ns","node_id","x_m","y_m","z_m"],
                  [{"simulation_time_ns":t,"node_id":i,
                    "x_m":float(i)+(1 if altered and t==100 and i==1 else 0),
                    "y_m":0.0,"z_m":0.0}
                   for t in (0,100) for i in (0,1)])
        return path

    def test_matching_traffic_and_accounting(self):
        a,pa=self.build("AODV")
        b,pb=self.build("OLSR",rejected=1)
        result=self.run_script("check_diagnostics.py",a,b,"--prefixes",pa,pb)
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)

    def test_detects_traffic_mismatch(self):
        a,pa=self.build("AODV")
        b,pb=self.build("OLSR",mismatch=True)
        result=self.run_script("check_diagnostics.py",a,b,"--prefixes",pa,pb)
        self.assertNotEqual(result.returncode,0)
        self.assertIn("mismatch",result.stderr+result.stdout)

    def test_detects_errno_accounting_mismatch(self):
        a,pa=self.build("AODV",rejected=1)
        write_csv(Path(str(pa)+"-socket-errors.csv"),["socket_errno","count"],[])
        result=self.run_script("check_diagnostics.py",a,"--prefixes",pa)
        self.assertNotEqual(result.returncode,0)
        self.assertIn("errno count",result.stderr+result.stdout)

    def test_matching_sampled_mobility(self):
        a=self.mobility("AODV")
        b=self.mobility("OLSR")
        result=self.run_script("check_mobility.py",a,b)
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)

    def test_detects_mobility_mismatch(self):
        a=self.mobility("AODV")
        b=self.mobility("OLSR",altered=True)
        result=self.run_script("check_mobility.py",a,b)
        self.assertNotEqual(result.returncode,0)
        self.assertIn("mobility mismatch",result.stderr+result.stdout)

if __name__ == "__main__":
    unittest.main()
