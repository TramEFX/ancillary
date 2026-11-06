# corrections/

**path:** `history/corrections/<correction_id>.md`, one file per correction
**status:** core (created on first use)
**serves:** Legibility (P3) and Ownership (P1); the primitive's continuity

---

## 1. In Plain Words

When your Ancillary finds it believed something wrong, not just out of date, it fixes the fact and keeps a record of the mistake here. The record says what was believed, what is true, why it was wrong, and which other files might have leaned on the wrong belief. Those files are flagged for review, never changed behind your back.

---

## 2. The Spec

### Shape

A correction manifest, in the shape of `spec/living_manifest.md` §9: a header naming the target, the field and the linked manifests, then three lines of prose.

- **Made by every CORRECT** (§4). An outdated fact is a WRITE, and makes none.
- **`correction_id`** is the target, the date and the field, in lowercase words joined by underscores: `<target>_<yyyy>_<mm>_<dd>_<field>`.
- **The target** is an `entity_id`, or the path of a memory, which is never edited (§6). For a memory, the correction is the whole of the fix.
- **`linked`** names every manifest that references the corrected fact, each `unreviewed` at first. The correction's id goes into each one's `pending_corrections`, and nothing else in them changes.
- **A linked status changes only by an explicit answer:** `revised` when the holder issued their own CORRECT, `independent` when their claim doesn't depend on the fact. Neither is ever inferred.
- **The folder appears with the first correction**.

### Must Never Contain

- **A change to a linked manifest.** Corrections are advertised, never cascaded (`spec/living_manifest.md` §9).
- **An outdated fact presented as an error:** that's a WRITE.
- **A resolution nobody gave.**
- **Credentials, tokens or keys.**

### Loads

- **Never at wake** (C6), and never indexed.
- **On demand:** when a manifest that carries its id in `pending_corrections` is retrieved, the correction is read and both questions are asked (`spec/living_manifest.md` §9). It's also read when the user asks why something changed.

### Writes

- **Written whole, once,** with the CORRECT that makes it (`spec/file_formats.md` §5). The CORRECT's own history entry names its id.
- **After that, only the linked statuses change,** each with `reviewed_by` and the date, as the answers come in. When an answer clears the flag, its id leaves that manifest's `pending_corrections` in the same pass.
- **Permanent, whatever the outcome.** It never compresses (C18). It is removed only if the user asks to forget what it records (`spec/living_manifest.md` §5.5).

### Access Levels

- **Read and write (the baseline):** the Ancillary writes it and tracks the reviews.
- **Read only:** the Ancillary gives the user the file and each flag to add.
- **No file access:** the Ancillary hands it back, and asks the review questions when the linked file is pasted in.

### Check

`tools/check_living_manifests.py` checks that every pending correction resolves, where the platform can run code. Otherwise a read-back: the header parses, its target and every linked id resolve, and every linked status is one of the three.

---

## 3. To Build It

### What to Ask

Nothing.

### Defaults

None at birth. The folder appears with the first correction.

### What to Write, and How to Confirm It

Nothing at the build. The first CORRECT creates the folder and the file, and its check is the one above.

### The Manual's Line

**`history/corrections/`** keeps a record each time your Ancillary finds it believed something wrong. It fixes the fact, and asks you about anything else that might have leaned on it, rather than changing it for you.
