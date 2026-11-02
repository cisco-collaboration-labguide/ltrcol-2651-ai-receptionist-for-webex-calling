"""Catch unexpected lab credentials and validate referenced image assets.

Exact occurrences from the owner's original training guide are approved in a
path-specific, hashed manifest. New credential occurrences still fail validation.
"""
from pathlib import Path
import html
import re
import json
import hashlib
from collections import Counter


docs = Path('docs')
patterns = [r'dcloud\s*(?:\d+|z{4})\s*!', r'cb\d+\.dc-\d+\.com',
            r'last\s+(?:four|4)[ -]+digits', r'dcloudconnect[^\s]*[?]']
manifest = Path(__file__).with_name('approved_lab_credentials.json')
approved = json.loads(manifest.read_text(encoding='utf-8')) if manifest.exists() else {}
errors = []
referenced = set()
for path in docs.rglob('*.md'):
    relative = path.relative_to(docs)
    if not path.is_file() or relative.parts[0] == 'introduction.md':
        continue
    source = path.read_text(encoding='utf-8')
    plain = html.unescape(re.sub(r'<[^>]+>', '', source))
    found = Counter(hashlib.sha256(m.group().lower().encode()).hexdigest()
                    for pattern in patterns for m in re.finditer(pattern, plain, re.I))
    permitted = approved.get(path.as_posix(), {})
    if any(count > permitted.get(digest, 0) for digest, count in found.items()):
        errors.append(f'Unapproved lab credential occurrence in {path}')
    referenced.update(re.findall(r'assets/images/([^\s)]+)', source))
assets = {p.name for p in (docs / 'assets/images').iterdir() if p.is_file()}
if assets != referenced:
    errors.append('Image directory contains missing or unreferenced files; review before publishing.')
if list(docs.rglob('*.docx')) or list(docs.rglob('*.zip')):
    errors.append('Original documents/archives must not be included in public docs.')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: credential scan with exact source exceptions; {len(assets)} referenced image assets.')
