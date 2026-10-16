"""Prepare a local model-input folder without answer keys or results."""
import argparse, shutil
from pathlib import Path
from verify import ROOT, verify
ap = argparse.ArgumentParser()
ap.add_argument('--images', required=True, type=Path)
ap.add_argument('--out', default=Path('model-input'), type=Path)
args = ap.parse_args()
rows = verify(args.images)
# Refuse an existing destination to avoid mixing old answers or overwriting inputs.
args.out.mkdir(parents=True, exist_ok=False)
for row in rows:
    shutil.copy2(args.images / row['filename'], args.out / row['filename'])
shutil.copy2(ROOT / 'prompts/judge.zh.txt', args.out / 'prompt.txt')
shutil.copy2(ROOT / 'dataset/captions-input.en.txt', args.out / 'captions.txt')
print(f'Prepared {args.out}: 16 images + prompt + captions. No answers included.')
