"""Reference checker for the weights and caps of both indexes.

It checks:
  - every weight is from 0.99 to 0.9999 (spec/two_indexes.md, section 4.4);
  - at most 15% of each index's entries are in the top tier, 0.9999, apart from
    any that the index's history records as the user's override
    (spec/curation.md C15; spec/file_formats.md, section 4.4);
  - the Eternal set ("eternal": true) is only in the memory index, within the cap
    the operational rules set, and every member has a summary (C16).
It also reports how each index's entries spread across the weight bands the
operational rules name. The spec sheets are the authority: where this script and
a sheet disagree, the sheet wins, and this script is what gets fixed.

Run it from the Ancillary's root, the folder that holds routing/:
    python -I tools/check_index_weights.py

Exit code 0 means everything passed; 1 means something failed.
Python's standard library only.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Fixed by the standard (spec/two_indexes.md, sections 4.4 and 11.1). The Eternal cap is
# the user's to set, so it is read from the operational rules instead.
LOWEST, TOP, TOP_PERCENT = 0.99, 0.9999, 15
ETERNAL_CAP = re.compile(r'Eternal set holds at most (\d+) entries')
OVERRIDE = re.compile(r"^- \d{4}-\d{2}-\d{2} — (\S+): top tier on the user's override\.", re.M)


def load(rel):
    with open(os.path.join(ROOT, rel), encoding='utf-8') as fh:
        return json.load(fh)


def overrides(history_rel):
    path = os.path.join(ROOT, history_rel)
    if not os.path.exists(path):
        return set()
    with open(path, encoding='utf-8') as fh:
        return set(OVERRIDE.findall(fh.read()))


def bands(rules):
    """The weight bands named in the rules: '0.9999', 'a to b', or 'below x'."""
    out = []
    for name in (rules.get('RETRIEVAL', {}).get('weight_bands') or {}):
        nums = [float(x) for x in re.findall(r'\d\.\d+', name)]
        if name.startswith('below') and len(nums) == 1:
            out.append((name, LOWEST, nums[0], False))
        elif ' to ' in name and len(nums) == 2:
            out.append((name, nums[0], nums[1], True))
        elif len(nums) == 1:
            out.append((name, nums[0], nums[0], True))
    return out


def in_band(weight, low, high, inclusive):
    return low <= weight <= high if inclusive else low <= weight < high


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    fails = []
    try:
        master = load('routing/manifest_index.json')
        memory_rel = master.get('memory_index', 'modules/memories/memory_index.json')
        memory = load(memory_rel)
        rules = load('routing/operational_rules.json')
        indexes = (('catalogue', master['manifests'], 'history/manifest_index.md'),
                   ('memory index', memory['memories'], 'history/memory_index.md'))
    except (OSError, ValueError, KeyError, TypeError) as ex:
        print(f'FAIL an index or the rules cannot be read: {ex}')
        return 1

    match = ETERNAL_CAP.search(str(rules.get('WRITING', {}).get('caps', '')))
    cap = int(match.group(1)) if match else None
    if cap is None:
        fails.append('the operational rules give no Eternal cap (WRITING.caps)')
    named_bands = bands(rules)

    for name, entries, history_rel in indexes:
        bad = [e.get('path') for e in entries
               if not isinstance(e.get('weight'), (int, float)) or not LOWEST <= e['weight'] <= TOP]
        if bad:
            fails.append(f'{name}: weights missing or outside {LOWEST} to {TOP}: {bad}')
        good = [e for e in entries if e.get('path') not in bad]
        top = [e['path'] for e in good if e['weight'] >= TOP]
        excused = [p for p in top if p in overrides(history_rel)]
        limit = len(entries) * TOP_PERCENT // 100
        line = f'{name}: {len(top)} of {len(entries)} in the top tier (the cap allows {limit}'
        line += f', plus {len(excused)} on the user\'s override)' if excused else ')'
        print(line)
        if len(top) > limit + len(excused):
            fails.append(f'{name}: over the top-tier cap: ' + ', '.join(p for p in top if p not in excused))
        if named_bands and good:
            spread = []
            for band, low, high, inclusive in named_bands:
                count = sum(1 for e in good if in_band(e['weight'], low, high, inclusive))
                spread.append(f'{band}: {count}')
            between = sum(1 for e in good if not any(in_band(e['weight'], lo, hi, inc) for _, lo, hi, inc in named_bands))
            if between:
                spread.append(f'between bands: {between}')
            print(f'   . {name} by band: ' + '; '.join(spread))

    if any(e.get('eternal') for e in master['manifests']):
        fails.append('catalogue: the Eternal set belongs only in the memory index')
    eternal = [e for e in memory['memories'] if e.get('eternal') is True]
    print(f'memory index: {len(eternal)} in the Eternal set' + (f' (the cap is {cap})' if cap is not None else ''))
    if cap is not None and len(eternal) > cap:
        fails.append(f'memory index: the Eternal set is over its cap ({len(eternal)} > {cap}); the user names one to leave')
    no_summary = [e.get('path') for e in eternal if not e.get('summary')]
    if no_summary:
        fails.append(f'memory index: Eternal entries without a summary: {no_summary}')

    for line in fails:
        print('FAIL ' + line)
    print('PASS' if not fails else f'{len(fails)} failed')
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
