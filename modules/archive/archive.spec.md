# archive/

**path:** `modules/archive/<name>.v<version>.<ext>`, one copy per retired version
**status:** core (created on first use)
**serves:** Ownership (P1) and Curation (P5); the primitive's continuity

---

## 1. In Plain Words

Where a file goes when it's retired or replaced whole: its last version, kept exactly as it was. Nothing is lost when something stops being current, and nothing old crowds what's current. It's never read unless you ask for an old version.

---

## 2. The Spec

### Shape

A byte-for-byte copy of the original, in its own format, named as `spec/file_formats.md` §4.5 says: `<name>.v<version>.<ext>`.

- **What goes here:** a file retired or replaced whole. That covers a position the user lets go, a mode or a workflow they retire, a system manifest rewritten by an upgrade, and a living manifest that is no longer current but that the user wants kept.
- **A file without a version** (a living manifest) takes the date in its place: `<name>.<yyyy>_<mm>_<dd>.<ext>`.
- **If that name is taken,** the copy takes its folder's name in front, as in `history/`.
- **A file that changes in place isn't archived.** Its history file holds how it changed.
- **The folder appears with the first copy**.

### Must Never Contain

- **A copy that was edited, reformatted or summarized.** Byte for byte, or it isn't an archive copy.
- **Anything the user has asked to forget.** Forgetting reaches the archive too (`spec/living_manifest.md` §5.5).
- **Index entries.** The archive is never indexed (`spec/file_formats.md` §4.5).
- **Credentials, tokens or keys.**

### Loads

Never, unless the user asks for an old version. It is never indexed, and never flagged by an audit (`spec/file_formats.md` §4.5).

### Writes

- **One copy, when a file is retired or replaced whole,** made before the change. The original's history file records it, naming the archive path.
- **Then the catalogue line is removed,** or kept for the new version, in the same pass.
- **Never edited after.** It is removed only if the user asks to forget it.

### Access Levels

- **Read and write (the baseline):** the Ancillary makes the copy.
- **Read only:** the Ancillary tells the user which file to copy where.
- **No file access:** the user keeps the old version, and the Ancillary says which.

### Check

The copy matches the original byte for byte: by hash where code runs, otherwise by reading the two side by side. Its name follows the pattern, and nothing indexes it.

---

## 3. To Build It

### What to Ask

Nothing.

### Defaults

None at birth. The folder appears with the first copy.

### What to Write, and How to Confirm It

Nothing at the build. The first retirement creates the folder and the copy, and its check is the one above.

### The Manual's Line

**`modules/archive/`** keeps the last version of anything your Ancillary retires, exactly as it was. Ask for an old version at any time.
