"""Reference checker for living manifests (spec/living_manifest.md, section 5.4, rule 6).

It checks each living manifest's form. It can't tell whether a field is true.
The spec sheets are the authority: where this script and a sheet disagree,
the sheet wins, and this script is what gets fixed (tools/tools.spec.md).

Run it from the Ancillary's root, the folder that holds routing/:
    python -I tools/check_living_manifests.py            every living manifest under modules/
    python -I tools/check_living_manifests.py FILE ...    just these files

Exit code 0 means every file passed; 1 means at least one failed.
Python's standard library only.
"""
import datetime
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Fixed by the standard: spec/living_manifest.md sections 3, 4, 5.1, 5.2 and 10.
ENTITY_TYPES = {'person', 'project', 'relationship', 'organization', 'life_domain'}
SOURCES = {'user_explicit', 'user_implicit', 'external_document'}
CLAIMS = {'fact', 'interpretation', 'aspiration', 'promise'}
TIER_SECTIONS = ['Core', 'Status', 'Relationship']
STALE_DAYS = 90
DATE = re.compile(r'^\d{4}-\d{2}-\d{2}$')
CONFIRMATION = re.compile(r'\(confirmed (\S+), (\w+)\)\s*$')


def scalar(text):
    """One value in the header's small grammar: a word, [a, b] or { k: v, k: v }."""
    text = text.split(' #', 1)[0].strip()
    if text.startswith('[') and text.endswith(']'):
        return [x.strip() for x in text[1:-1].split(',') if x.strip()]
    if text.startswith('{') and text.endswith('}'):
        pairs = [p.split(':', 1) for p in text[1:-1].split(',') if p.strip()]
        if any(len(p) != 2 for p in pairs):
            raise ValueError(f'cannot read {text!r}')
        return {k.strip(): scalar(v) for k, v in pairs}
    return None if text in ('', 'null', '~') else text


def parse_header(text):
    """The header between the first two --- lines: scalars, inline lists and maps, one level of nesting."""
    if text.startswith('﻿'):
        raise ValueError('the file starts with a byte-order mark (spec/file_formats.md section 2)')
    if not text.startswith('---\n'):
        raise ValueError('the file does not start with a --- header')
    end = text.find('\n---\n', 4)
    if end < 0:
        raise ValueError('the header is not closed with ---')
    header, parent = {}, None
    for line in text[4:end].split('\n'):
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        key, colon, value = line.strip().partition(':')
        if not colon:
            raise ValueError(f'cannot read header line {line!r}')
        key = key.strip()
        if line.startswith(' ') and parent is not None:
            header[parent][key] = scalar(value)
        elif value.split(' #', 1)[0].strip() == '':
            header[key], parent = {}, key
        else:
            header[key], parent = scalar(value), None
    return header, text[end + 5:]


def as_date(value):
    if isinstance(value, str) and DATE.match(value):
        try:
            return datetime.date.fromisoformat(value)
        except ValueError:
            return None
    return None


def load_catalogue():
    path = os.path.join(ROOT, 'routing', 'manifest_index.json')
    with open(path, encoding='utf-8') as fh:
        entries = json.load(fh)['manifests']
    by_id = {e['entity_id']: e['path'] for e in entries if 'entity_id' in e}
    by_path = {e['path']: e for e in entries if 'path' in e}
    return by_id, by_path


def section(body, name):
    match = re.search(rf'^## {name}\s*$(.*?)(?=^## |\Z)', body, re.M | re.S)
    return match.group(1) if match else ''


def check(path, by_id, by_path, today):
    fails, notes = [], []
    rel = os.path.relpath(path, ROOT).replace('\\', '/')
    with open(path, encoding='utf-8') as fh:
        text = fh.read()
    try:
        h, body = parse_header(text)
    except ValueError as ex:
        return [f'header: {ex}'], notes

    # The header (spec/living_manifest.md section 5.1).
    if h.get('manifest_type') != 'living':
        fails.append('manifest_type must be "living"')
    if h.get('entity_type') not in ENTITY_TYPES:
        fails.append(f'entity_type {h.get("entity_type")!r} is not one of {sorted(ENTITY_TYPES)}')
    eid = h.get('entity_id')
    if not isinstance(eid, str) or not re.match(r'^[a-z0-9_]+$', eid):
        fails.append('entity_id is missing, or not lowercase words joined by underscores')
    for key in ('schema_version', 'created', 'updated', 'history', 'tiers', 'links', 'pending_corrections'):
        if key not in h:
            fails.append(f'the header has no {key}')
    created, updated = as_date(h.get('created')), as_date(h.get('updated'))
    if 'created' in h and not created:
        fails.append('created is not a YYYY-MM-DD date')
    if 'updated' in h and not updated:
        fails.append('updated is not a YYYY-MM-DD date')
    if created and updated and updated < created:
        fails.append('updated is earlier than created')
    migrated = h.get('migrated')
    if migrated is not None and not as_date(migrated):
        fails.append('migrated is not a YYYY-MM-DD date')
    history = h.get('history')
    if isinstance(history, str) and not os.path.exists(os.path.join(ROOT, history)):
        fails.append(f'its history file {history} does not exist')

    # Both dated tiers have dates and a source.
    tiers = h.get('tiers') if isinstance(h.get('tiers'), dict) else {}
    for tier in ('core', 'relationship'):
        t = tiers.get(tier)
        if not isinstance(t, dict):
            fails.append(f'tiers.{tier} is missing')
            continue
        upd, conf, source = as_date(t.get('updated')), as_date(t.get('confirmed')), t.get('source')
        if not upd:
            fails.append(f'tiers.{tier}.updated is missing or not a date')
        if not conf:
            fails.append(f'tiers.{tier}.confirmed is missing or not a date')
        if source not in SOURCES:
            why = ' (an inference is never a source)' if source == 'inferred' else ''
            fails.append(f'tiers.{tier}.source {source!r} is not a valid source{why}')
        if conf and conf > today:
            fails.append(f'tiers.{tier}.confirmed is in the future')
        if conf and (today - conf).days >= STALE_DAYS and not migrated:
            notes.append(f'{tier} was last confirmed {conf}: ask whether it still holds')
    if 'status' in tiers:
        fails.append('tiers.status must not exist: each Status field carries its own confirmation')

    # Every link and pending correction resolves.
    links = h.get('links')
    if 'links' in h and not isinstance(links, list):
        fails.append('links is not a list')
    for link in links if isinstance(links, list) else []:
        if link not in by_id:
            fails.append(f'the link {link!r} matches no entity_id in the catalogue')
    pending = h.get('pending_corrections')
    if 'pending_corrections' in h and not isinstance(pending, list):
        fails.append('pending_corrections is not a list')
    for cid in pending if isinstance(pending, list) else []:
        if not os.path.exists(os.path.join(ROOT, 'history', 'corrections', f'{cid}.md')):
            fails.append(f'the pending correction {cid!r} has no file in history/corrections/')

    # The body (spec/living_manifest.md section 5.2).
    heads = [x for x in re.findall(r'^## (.+?)\s*$', body, re.M) if x in TIER_SECTIONS]
    if heads != TIER_SECTIONS:
        fails.append(f'the body needs ## Core, ## Status and ## Relationship, once each, in that order (found {heads})')
    for line in section(body, 'Status').split('\n'):
        if not line.startswith('- **'):
            continue
        label = line[4:].split(':**', 1)[0]
        match = CONFIRMATION.search(line)
        if not match:
            fails.append(f'the Status field "{label}" has no (confirmed YYYY-MM-DD, source)')
            continue
        conf, source = as_date(match.group(1)), match.group(2)
        if not conf:
            fails.append(f'the Status field "{label}": {match.group(1)!r} is not a YYYY-MM-DD date')
        elif conf > today:
            fails.append(f'the Status field "{label}": its confirmed date is in the future')
        elif (today - conf).days >= STALE_DAYS and not migrated:
            notes.append(f'the Status field "{label}" was last confirmed {conf}: ask whether it still holds')
        if source not in SOURCES:
            why = ' (an inference is never a source)' if source == 'inferred' else ''
            fails.append(f'the Status field "{label}": {source!r} is not a valid source{why}')
    for mark in re.findall(r'`\[(\w+)\]`', body):
        if mark not in CLAIMS:
            fails.append(f'the claim mark [{mark}] is not one of {sorted(CLAIMS)}')

    # Its catalogue entry carries its entity_id (spec/living_manifest.md section 8).
    entry = by_path.get(rel)
    if not entry:
        fails.append('it has no entry in the catalogue')
    elif entry.get('entity_id') != eid:
        fails.append(f'its catalogue entry has entity_id {entry.get("entity_id")!r}, not {eid!r}')
    return fails, notes


def living_manifests(by_path):
    """Every file under modules/ that opens with a --- header (only living manifests do,
    spec/file_formats.md section 4), and every file the catalogue gives an entity_id."""
    found = set()
    for folder, subfolders, files in os.walk(os.path.join(ROOT, 'modules')):
        subfolders[:] = [d for d in subfolders if d != 'archive']
        for name in files:
            if name.endswith('.md'):
                path = os.path.join(folder, name)
                with open(path, encoding='utf-8') as fh:
                    if fh.read(8).lstrip('﻿').startswith('---'):
                        found.add(os.path.normpath(path))
    for rel, entry in by_path.items():
        path = os.path.normpath(os.path.join(ROOT, rel))
        if 'entity_id' in entry and 'external' not in entry and os.path.isfile(path):
            found.add(path)
    return sorted(found)


def main(args):
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    today = datetime.date.today()
    try:
        by_id, by_path = load_catalogue()
    except (OSError, ValueError, KeyError, TypeError) as ex:
        print(f'FAIL routing/manifest_index.json cannot be read: {ex}')
        return 1
    files = [os.path.abspath(a) for a in args] if args else living_manifests(by_path)
    failed = 0
    for path in files:
        fails, notes = check(path, by_id, by_path, today)
        print(('FAIL ' if fails else 'PASS ') + os.path.relpath(path, ROOT).replace('\\', '/'))
        for line in fails:
            print('   - ' + line)
        for line in notes:
            print('   . ' + line)
        failed += bool(fails)
    print(f'{len(files)} checked, {failed} failed')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
