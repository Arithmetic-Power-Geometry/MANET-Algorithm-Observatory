#!/usr/bin/env python3
"""Independent packet-delivery-ratio analysis. Run from repository root with CSV supplied at --csv.
Requires pandas numpy scipy. This script does NOT run ns-3."""
import argparse,hashlib,json
from pathlib import Path
import numpy as np,pandas as pd
from scipy.stats import wilcoxon
p=argparse.ArgumentParser();p.add_argument('--csv',required=True);p.add_argument('--out',default='refine/evidence/paired_contrasts.csv');a=p.parse_args()
d=pd.read_csv(a.csv)
assert len(d)==320 and not d.duplicated(['scenario_id','protocol','seed']).any()
assert d.groupby(['scenario_id','protocol']).size().eq(20).all()
assert np.allclose(d.pdr,d.app_packets_received/d.app_packets_sent)
assert d.validity_status.eq('PASS').all() and d.exit_status.eq(0).all()
rows=[]
for sc,g in d.groupby('scenario_id'):
 v=g.pivot(index='seed',columns='protocol',values='pdr').sort_index()
 protocols=sorted(v.columns)
 family=[]
 for i,x in enumerate(protocols):
  for y in protocols[i+1:]:
   delta=(v[x]-v[y]).to_numpy()
   pv=wilcoxon(delta,zero_method='pratt',alternative='two-sided',method='auto').pvalue
   rng=np.random.default_rng(20261108)
   sample=rng.integers(0,len(delta),size=(10000,len(delta)))
   lo,hi=np.quantile(delta[sample].mean(axis=1),[.025,.975])
   family.append(dict(scenario=sc,a=x,b=y,n=len(delta),mean=float(delta.mean()),raw_p=float(pv),ci_low=float(lo),ci_high=float(hi)))
 running=0
 for i,r in enumerate(sorted(family,key=lambda r:r['raw_p'])):
  running=max(running,min(1.,(len(family)-i)*r['raw_p']))
  r['holm_p']=running
 rows+=family
out=Path(a.out);out.parent.mkdir(parents=True,exist_ok=True);pd.DataFrame(rows).to_csv(out,index=False)
print(json.dumps({'n':len(d),'protocols':sorted(d.protocol.unique()),'scenarios':sorted(d.scenario_id.unique()),'rejected_runs_by_protocol':d.assign(rej=d.tx_rejected.gt(0)).groupby('protocol').rej.sum().to_dict(),'rejected_attempts_by_protocol':d.groupby('protocol').tx_rejected.sum().to_dict(),'sha256':hashlib.sha256(Path(a.csv).read_bytes()).hexdigest(),'output':str(out)},indent=2))
