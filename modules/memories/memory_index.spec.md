# memory_index.json

**path:** `modules/memories/memory_index.json`
**status:** core
**serves:** Curation (P5) and Legibility (P3); the primitive's continuity

---

## 1. In Plain Words

The map of the story: one line for every memory, saying that it happened and how much it mattered, not what happened. It isn't read at wake unless the user chooses; once it's read, it is scanned with the catalogue before every reply. It belongs to the library, and it is empty at birth unless an existing entity brings its past.

---

## 2. The Spec

### Shape

```json
{
  "manifest_type": "memory_index",
  "schema_version": "2.0.0",
  "description": "Index of all narrative/event manifests — loaded on demand for full continuity",
  "summary_only": true,
  "memories": [
  ]
}
```

- **The format and the entry fields are in `spec/two_indexes.md`:** one entry per line, newest first, and no count or date in the header (§4.1). The shape is in §4.3, and the fields in §4.4.
- **The array's brackets sit on their own lines,** so the first entry, like every one after it, is one new line.
- **What it lists:** every memory, and nothing else (§3). Every file in `modules/memories/` except this one has an entry here.
- **It has no catalogue entry.** The catalogue's header points to it, and the rules read it by path.
- **`summary_only` stays `true`.** It marks every entry as the map, not the record (§5).
- **With the catalogue, it is the inference scaffolding.** In very few words, the weights and the two indexes give the shape of the person's life and of the Ancillary's own, and how much each part weighs (`spec/two_indexes.md` §1).
- **The map is not the record.** Until a memory is read, it is spoken to only at the level of its summary. Asked for specifics, the Ancillary says it has the shape of this but not the record, and offers to read it (§5).
- **An entry's tags name the people and projects in the moment,** by `entity_id`. Entries carry no `entity_id` field and no `external` (§4.4).
- **`eternal: true` marks a member of the Eternal set,** which never compresses (§11.3). It is capped by count, set in the operational rules (C16).
- **The growth model in §11 waits for growth.** Nothing of it is built at birth. A split or a deep archive is proposed when the index's own numbers call for it, and made on the user's yes (C17, C18).

### Must Never Contain

- **Anything that isn't a memory:** living manifests, doctrine, identity, rules (`spec/two_indexes.md` §3).
- **A count, a last-updated date, token estimates or other derived numbers** (C3).
- **History or notes about changes:** those go in `history/memory_index.md`.
- **Rules:** weight bands and load hints are in the operational rules (§4.4).
- **What happened.** A summary is 30 words at most, and every word of it is in the memory beneath it (C19).
- **Absolute paths, platform IDs, or anything secret (P2).**

### Loads

- **Not at wake, by default** (C8). The Ancillary says once, in its first reply, that full narrative continuity isn't on and can be at any time.
- **When the user asks for it,** or accepts the offer when the conversation reaches for the past. If the user has turned narrative continuity on, it's read at every wake, at step 7.
- **Always in full:** a partial map is a worse system, not a smaller one (`spec/two_indexes.md` §1). Once read, it is scanned with the catalogue before every reply, in one merged ranking (§6).

### Writes

- **Created at birth (M7):** empty, or with the memories an existing entity brings (`memory.spec.md`). Those are added one line each, oldest first, so the newest ends up first. Each history line ends "Brought in at M7."
- **A memory's line is added as soon as the memory is written,** and leaves one history line: `- <date> — added <path>, weight <weight>.` (`spec/file_formats.md` §4.4).
- **Its weight is set by the bands in the operational rules.** The user can change it at any time. A weight change replaces only its line, and its history line names both weights.
- **The caps are enforced on every write** (C15, C16).
  - **The top tier:** at most 15% of the entries. While the index holds fewer than seven, the cap allows none. A moment that is truly foundational goes in on the user's override, recorded in the history.
  - **The Eternal set:** a memory joins it at the user's word, or on the Ancillary's proposal and the user's yes. When the set is full, the user names one to leave; the Ancillary never picks.
- **A forgotten memory's line is removed** (`spec/living_manifest.md` §5.5). Every history line that names it goes too, and the marker takes their place (`spec/file_formats.md` §4.4).
- **Every write is additive** (`spec/file_formats.md` §5), and any change beyond the entry's own line is damage (`spec/two_indexes.md` §4.1).

### Access Levels

- **Read and write (the baseline):** the Ancillary keeps it current with every memory.
- **Read only:** the Ancillary gives the user the exact line to add, change or remove.
- **No file access:** the user pastes it in when they want the full narrative, and applies the lines the Ancillary hands back.

### Check

- The file parses as JSON, and every entry is one line.
- Every path exists in `modules/memories/`, and every memory file there has an entry (`spec/two_indexes.md` §7).
- Every entry follows §4.4: category `memories`, the keyword counts, and the summary rule.
- `summary_only` is `true`.
- At most 15% of the entries are in the top tier, or the override is in the history. The Eternal set is within its cap.

The reference checker `tools/check_index_weights.py` checks the weights and both caps where the platform can run code. The rest is a short script, or a read-back.

---

## 3. To Build It

### What to Ask

Nothing new. The narrative setting and the Eternal cap were asked at M5 (`operational_rules.spec.md`).

### Defaults

Empty at birth, unless an existing entity brings its past.

### What to Write, and How to Confirm It

1. Write the file from the skeleton.
2. Start `history/memory_index.md` with its first line: `- <date> — created, empty. Built at M7.`
3. If the user gave first memories, or an existing entity brought its own (`memory.spec.md`), add each one's line, oldest first, and its history line. The entity proposes the weights, and the caps hold for the batch as for any write.
4. Run the check and tick M7.

### The Manual's Line

**`modules/memories/memory_index.json`** is the map of your Ancillary's memories: that each one happened and how much it mattered, not what happened. It isn't read at wake unless you want it to be. Ask for your full history at any time.
