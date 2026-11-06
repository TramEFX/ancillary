# people/

**path:** `modules/people/<entity_id>.md`, one file per person
**status:** optional
**serves:** Ownership (P1) and Curation (P5); the primitive's continuity

---

## 1. In Plain Words

One file for each person who matters in your life: who they are, what's going on with them, and what they mean to you. Each one is kept current, and how it changed lives in its history. They belong to the library.

---

## 2. The Spec

### Shape

A living manifest, `entity_type: person`, in the shape of `spec/living_manifest.md` §5. Its worked example (§11) is a person's file.

- **`entity_id`** is the person's name, in lowercase words joined by underscores, and never changes.
- **The tiers:**
  - **Core:** who they are.
  - **Status:** what's going on with them, each field confirmed on its own.
  - **Relationship:** what they mean to the user, and how the Ancillary should treat them in conversation: what to be careful with, what not to bring up. This is where a boundary about a person lives.
- **`links`** names `user`, and any related people or projects, by entity_id.
- **One file per person who recurs** (C2). A one-off mention stays in the memory where it appeared.

### Must Never Contain

- **Anything the user wouldn't want kept about someone.** What's held is what matters to the user's life, never what was gathered for its own sake.
- **Secrets about them, and contact details** unless the user wants the Ancillary to use them.
- **A guess presented as a fact,** about them or their feelings. A read is marked `[interpretation]`.
- **History inside the file** (C4), or **events**, which are memories.
- **A weight** (C3).

### Loads

On demand, through the catalogue, when the conversation turns to them (C12).

### Writes

- **Proposed when someone keeps coming up,** and created on the user's yes: "Sam's come up a few times. Want me to keep a file on them?"
- **Then only through the six operations** (`spec/living_manifest.md` §4). Each one leaves a history entry in `history/<entity_id>.md`.
- **A new file gets its catalogue entry, with `entity_id`** (§8), and a LINK from `user`.
- **A correction is advertised, never cascaded** (§9).
- **Every write is additive** (`spec/file_formats.md` §5).

### Access Levels

- **Read and write (the baseline):** the Ancillary keeps them current.
- **Read only:** the Ancillary gives the user each change and its history entry.
- **No file access:** the user pastes a person's file in when they come up.

### Check

`tools/check_living_manifests.py` where the platform can run code. Otherwise a read-back against `spec/living_manifest.md` §5.4, rule 6.

---

## 3. To Build It

### What to Ask

Only if the user wants people files now (M8):
1. **Who matters most in their life right now?**
2. **For each:** who they are to the user, and what's going on with them.
3. **Is there anything the Ancillary should be careful about** when this person comes up?

### Defaults

None at birth. People files grow as people come up.

### What to Write, and How to Confirm It

1. Write each file in the shape of `spec/living_manifest.md` §5, every field `user_explicit`, confirmed today.
2. Start each history file with a LOG entry (`spec/living_manifest.md` §5.3): `- <date> · LOG · log · -`, with the note "created at the build (M8)."
3. Add each catalogue entry with its `entity_id`, and LINK each person from `user`.
4. Read each one back in a sentence or two. On the user's yes, run the check.

### The Manual's Line

**`modules/people/`** holds a file for each person who matters to you. Your Ancillary will ask before starting one, and you can ask it to change, remove or forget anything in them.
