"""Verify metadata and optional locally obtained images. No dependencies/network."""
import argparse, hashlib, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def verify(images=None):
    rows = json.loads((ROOT / 'dataset/manifest.json').read_text())
    assert [r['id'] for r in rows] == [f'C{i:02}' for i in range(1, 17)]
    assert sum(r['series_representative_proxy'] for r in rows) == 3
    assert all(len(r['sha256']) == 64 and r['official_page'].startswith('https://www.nhm.ac.uk/') for r in rows)
    for r in rows:
        if images:
            path = Path(images) / r['filename']
            if not path.is_file():
                raise ValueError(f'Missing {path}')
            if hashlib.sha256(path.read_bytes()).hexdigest() != r['sha256']:
                raise ValueError(f'Hash mismatch: {r["id"]}; do not claim byte-identical reproduction')
    results = json.loads((ROOT / 'results/run-2026-10-14.json').read_text())
    for m in results['results']:
        assert len(set(m['top3'])) == 3
        assert all(x in {r['id'] for r in rows} for x in m['top3'])
    return rows

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--images', type=Path)
    args = ap.parse_args()
    try:
        verify(args.images)
    except (ValueError, AssertionError) as exc:
        print(f'Validation failed: {exc}', file=sys.stderr)
        sys.exit(1)
    print('Validated 16 manifest entries and four result records' + ('; 16 image hashes match' if args.images else '; images not checked'))
