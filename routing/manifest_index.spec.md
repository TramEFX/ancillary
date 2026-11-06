# manifest_index.json

**path:** `routing/manifest_index.json`
**status:** core
**serves:** Curation (P5) and Legibility (P3); the primitive's continuity and connectivity

---

## 1. In Plain Words

The catalogue: one line for every file in the library except the memories, saying what each one is and where it lives. It is read at every wake and scanned before every reply, so the Ancillary can find anything without reading everything. Its header carries the Narrative Compass, a few lines on where the person's life is right now.

---

## 2. The Spec

### Shape

```json
{
  "manifest_type": "manifest_index",
  "schema_version": "2.0.0",
  "description": "What is true now, and where to find it: every manifest except the memories",
  "memory_index": "modules/memories/memory_index.json",
  "narrative_compass": {
    "updated": "<the date of the last change>",
    "chapter": "<the arc the person's life is in now>",
    "tension": "<the live pressure inside it>",
    "unresolved_thread": "<the question that remains open>"
  },
  "manifests": [
    <one entry per line, newest first>
  ]
}
```

- **The format and the entry fields are in `spec/two_indexes.md`:** one entry per line, newest first, and no count or date in the header (§4.1). The fields are in §4.4, and the Compass rules in §4.5.
- **What it lists:** every manifest in the library except these:
  - the memories, which go in the memory index;
  - the memory index itself, which the header points to;
  - this file;
  - the ignition file and the loader, which the wake reads by path;
  - history, the archive and the handoff, which are never indexed.

  That includes every living manifest, the identity files, the operational rules, doctrine, the specs in `spec/`, the manual, every mode or workflow with a manifest of its own, the user's own domains, and the work itself when the library holds it (C13).
- **An existing system, or work kept where it lives, is linked, not copied.** Its entry carries `external`, naming the sibling folder or repository, and its path starts from the folder that holds the library (`spec/two_indexes.md` §4.4). What the Ancillary needs to know about it lives in the library, usually in a project's living manifest.
- **A mode or workflow's entry carries its @name in `tags`,** so the pre-response scan finds it.
- **A folder can have one entry** when its files are a family read through one manifest, as a set of prompts is (C10). Its path ends with `/`.
- **The Compass holds no fact of its own.** Every line in it is already in a living manifest, most often the person's own (`spec/two_indexes.md` §11.5).

### Must Never Contain

- **Memories:** they belong in the memory index (`spec/two_indexes.md` §3).
- **A count, a last-updated date, token estimates, a hierarchy or other derived numbers** (C3).
- **History or notes about changes:** those go in `history/manifest_index.md`.
- **Rules:** weight bands and load hints are in the operational rules.
- **A second summary of the person's life beside the Compass** (C9).
- **The contents of a file:** an entry is the map, not a copy (C3).
- **Absolute paths, platform IDs, or anything secret (P2).**

### Loads

At every wake, in full, at step 2 (C6). It is then scanned before every reply (C12).

### Writes

- **Created at birth (M6),** with an entry for every listed file written so far. Each later milestone adds the entries for its own files.
- **Every create, move, rename or removal changes exactly one line** and leaves one history line (`spec/two_indexes.md` §4.1, `spec/file_formats.md` §4.4).
- **A weight change** names both weights in its history line.
- **The caps are enforced on every write** (C15).
- **The Compass changes only when the arc materially changes:** a chapter closing, a tension resolving, a thread answered. Each change gets one history line, naming its sources.
- **Every write is additive** (`spec/file_formats.md` §5).

### Access Levels

- **Read and write (the baseline):** the Ancillary keeps it current on every write.
- **Read only:** the Ancillary gives the user the exact line to add, change or remove, and says where.
- **No file access:** the user pastes it at every wake, at step 2, and applies the lines the Ancillary hands back.

### Check

- The file parses as JSON, and every entry is one line.
- Every path exists. A folder's path ends with `/`. An external entry whose source isn't present on this platform is reported, not failed.
- Every entry follows `spec/two_indexes.md` §4.4: keyword counts, the summary rule, and `entity_id` on every living manifest.
- At most 15% of the entries are in the top tier.
- The Compass is 200 words at most, and every claim in it traces to a source.

The reference checker `tools/check_index_weights.py` checks the weights and the caps where the platform can run code. The rest is a short script, or a read-back.

---

## 3. To Build It

### What to Ask

Nothing new. The Compass is drafted from what the user said about where things stand in their life (M4), and read back to them.

### Defaults

The entries written at M6:

| File | Weight | Category |
|------|--------|----------|
| `modules/identity/identity_core.md` | 0.9999 | identity |
| `modules/identity/personality_profile.md` | 0.9998 | identity |
| `routing/operational_rules.json` | 0.9998 | core |
| `modules/user/user.md` (entity_id `user`) | 0.9998 | core |
| each of the four files in `spec/` | 0.992 | core |

With these eight, identity is the one top-tier entry: one in eight, inside the cap. The 0.9998 entries carry a summary (`spec/two_indexes.md` §4.4).

### What to Write, and How to Confirm It

1. Write the header from the skeleton, with an empty entries array.
2. Add the entries above, one line each, as additive writes. Then add the optional library's entries as M8 writes them, at M9 the audit's, and sync's if there is a remote, and at M11 the manual's (`MANUAL.spec.md`).
3. Draft the Compass from the person's living manifest, and read it back to the user. On their yes, write it.
4. Start `history/manifest_index.md`, with one line per entry added.
5. Run the check above and tick M6.

### The Manual's Line

**`routing/manifest_index.json`** is the catalogue: how your Ancillary finds anything in its library without reading all of it. Its first lines, the Compass, are where it thinks your life is right now. If that's wrong, tell it.
