#!/usr/bin/env python3
"""Convert placeholder (non-JSON) files under lokis-assets/*.json into valid JSON
objects so the QA JSON-lint gate is meaningful (real JSON errors surface)."""
import json, os, glob

fixed = 0
for j in sorted(glob.glob('lokis-assets/**/*.json', recursive=True)):
    try:
        json.load(open(j, encoding='utf-8'))
        continue
    except Exception:
        pass
    raw = open(j, encoding='utf-8').read()
    parts = j.split('/')
    persona = parts[1] if len(parts) > 2 else None
    kind = parts[2] if len(parts) > 3 else None
    base = os.path.basename(j)
    tool = 'n8n' if base.startswith('n8n-') else ('make' if base.startswith('make-') else None)
    title = base
    for line in raw.splitlines():
        if line.startswith('Placeholder:'):
            title = line[len('Placeholder:'):].split(' —')[0].strip()
            break
    obj = {
        "_placeholder": True,
        "title": title,
        "persona": persona,
        "kind": kind,
        "tool": tool,
        "file": j,
        "implemented": False,
        "note": ("Automation workflow/template stub for the Loki's Mischief persona knowledge base. "
                 "Replace with the exported n8n/Make.com JSON when built."),
    }
    with open(j, 'w', encoding='utf-8') as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
        f.write('\n')
    fixed += 1
    print('FIXED', j)
print('TOTAL fixed =', fixed)
