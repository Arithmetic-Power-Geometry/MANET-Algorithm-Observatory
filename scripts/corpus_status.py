import csv
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / 'literature' / 'master_studies.csv'
OUT = ROOT / 'artifacts' / 'generated' / 'corpus_status.md'

def main():
    with MASTER.open(newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    ids = [r['study_id'] for r in rows]
    if len(ids) != len(set(ids)):
        raise SystemExit('duplicate study_id')
    allowed = {'V0','V1','V2','V3','V4'}
    bad = [r['study_id'] for r in rows if r['verification_state'] not in allowed]
    if bad:
        raise SystemExit(f'invalid verification state: {bad}')
    states = Counter(r['verification_state'] for r in rows)
    scopes = Counter(r['scope'] for r in rows)
    primary = sum(r['in_primary_population'] == 'yes' for r in rows)
    partial = sum(r['in_primary_population'] == 'partial' for r in rows)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    lines = ['# Corpus Status','',f'Total registered studies: **{len(rows)}**',f'Primary MANET population: **{primary}**',f'Partial/mixed population: **{partial}**','','## Verification','']
    lines += [f'- {k}: {states.get(k,0)}' for k in ['V0','V1','V2','V3','V4']]
    lines += ['','## Scope counts','']
    lines += [f'- {k}: {v}' for k,v in sorted(scopes.items())]
    lines += ['','Generated from the master study registry; counts are corpus-management metadata, not scientific conclusions.','']
    OUT.write_text('\n'.join(lines), encoding='utf-8')
    print(f'OK: {len(rows)} studies; generated corpus status')

if __name__ == '__main__':
    main()
