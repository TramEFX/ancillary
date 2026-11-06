# history/

**path:** `history/<name>.md`, one file beside every file that changes
**status:** core
**serves:** Legibility (P3) and Curation (P5); the primitive's continuity

---

## 1. In Plain Words

The record: how each file in the library came to say what it says now, kept beside it rather than inside it. Every change leaves a line, and lines are only ever added, so the record of the Ancillary's own mistakes can't quietly disappear. It is never read at wake, and it is there whenever you ask how something changed.

---

## 2. The Spec

### Shape

Each history file has the shape of the file it records:

| It records | Its file | Its shape |
|---|---|---|
| A living manifest | the path in the manifest's `history` field, normally `history/<entity_id>.md` | `spec/living_manifest.md` §5.3 |
| A system manifest, doctrine, a mode, a workflow | `history/<name>.md` | `spec/file_formats.md` §4.4 |
| The copies of `spec/` and `tools/`, each as one set | `history/spec.md`, `history/tools.md`: one line per copy or upgrade, naming the standard's version | `spec/file_formats.md` §4.4 |
| An index | `history/manifest_index.md`, `history/memory_index.md` | `spec/file_formats.md` §4.4 |
| The audit's runs | `history/audit.md`, beside the audit's own changes | `system_maintenance/audit.spec.md` |
| A correction | `history/corrections/<correction_id>.md` | `corrections/corrections.spec.md` |
| The build | `history/BUILD.md`, the ticked copy of the roadmap | unchanged once the build is done |

- **It is named for the file it records,** without its folder or extension. If that name is already taken in `history/`, the new one takes its folder's name in front: `history/<folder>_<name>.md`.
- **It starts with the file's first write.** Every file written at the build leaves its first line, so `history/` exists from M1.
- **One line per change, added at the end.** Memories have none of their own: a memory is written once, and its index's history records it.
- **`history/` is the record; version control isn't**. Where the platform can run git, git is a backup and an undo. The record lives in the files, so it moves with the library and any model can read it.
- **A forgotten thing leaves a marker,** never what it was (`spec/living_manifest.md` §5.5).

### Must Never Contain

- **What a file says now:** that's the file's (C4).
- **An edited line.** A line that was wrong is followed by one that says so.
- **What the user asked to have forgotten** (`spec/living_manifest.md` §5.5).
- **Credentials, tokens or keys,** even as an old value.

### Loads

- **Never at wake** (C6).
- **On demand:** when the user asks how something changed or why, when a correction is reviewed, or when COMPRESS runs (`spec/living_manifest.md` §4).
- **History is never indexed.** A history file is found by its name or by the `history` field of the file it records.

### Writes

- **Append-only, with two exceptions** (`spec/living_manifest.md` §5.4, rule 4):
  - COMPRESS, for a living manifest's history only, and only where the full version survives in version control or a snapshot (C18). A correction's line never compresses.
  - Forgetting, at the user's explicit word, which leaves its marker.
- **Every line is written with the change it records,** in the same pass. A change with no history line isn't finished.
- **Every write is additive** (`spec/file_formats.md` §5): the line goes at the end, and nothing above it moves.
- **`history/BUILD.md`** is moved in at M12 and never written again.

### Access Levels

- **Read and write (the baseline):** the Ancillary writes every line with its change.
- **Read only:** the Ancillary gives the user each change together with its history line, and the user adds both.
- **No file access:** the Ancillary hands back the line with the change. Keeping the record is the user's, and the Ancillary says so once.

### Check

- Every line matches its shape (`spec/living_manifest.md` §5.3, `spec/file_formats.md` §4.4).
- Against the copy taken before the write, only lines at the end were added, apart from a COMPRESS or a forget's marker.
- Every file that changes has its history file.

`tools/check_living_manifests.py` checks that every living manifest's history file exists, where the platform can run code. The rest is a short script, or a read-back.

---

## 3. To Build It

### What to Ask

Nothing.

### Defaults

`history/` is laid out at M1, and each file starts with its file's first write.

### What to Write, and How to Confirm It

1. At M1, lay out `history/`, and start `history/spec.md` with the copy of `spec/`: `- <date> — copied, version <the standard's version>. Built at M1.`
2. Every milestone writes each file's history line with the file itself, as its sheet says.
3. At M12, move the ticked copy of BUILD.md to `history/BUILD.md`, and tick nothing in it again.
4. At M10, run the check above over the whole folder.

### The Manual's Line

**`history/`** is the record of how everything in your Ancillary changed: one line per change, never rewritten. Ask your Ancillary how something changed, and it reads it here. If you want something gone from the record too, ask it to forget it.
