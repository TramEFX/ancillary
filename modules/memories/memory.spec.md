# memories/

**path:** `modules/memories/<name>.md`, one file per moment
**status:** core
**serves:** Ownership (P1) and Curation (P5); the primitive's continuity

---

## 1. In Plain Words

One file for each moment worth keeping: what happened, written once, close to when it happened. A memory is never rewritten; if something later turns out different, a correction says so, and the memory stays as it was. They are the library's story, read only when the conversation reaches for them.

---

## 2. The Spec

### Shape

An event manifest, in the shape of `spec/file_formats.md` §4.1: a header that is the date alone, then the moment in prose. The folder holds only the memory index at birth (`memory_index.spec.md`).

- **A memory answers "what happened?"** If the content answers "what is?", it belongs in a living manifest, doctrine or the rules instead (`spec/two_indexes.md` §3).
- **One moment per file.** A moment that matters on its own gets a memory. A passing mention doesn't, and a person who appears only once lives in the memory where they appeared (C2).
- **Written while the moment is still in the conversation,** from what was actually said and done. Never from a summary, and never filled in with what such a moment would plausibly have held (`spec/two_indexes.md` §5).
- **In the Ancillary's own voice,** unless the user writes it themselves. A moment from before the Ancillary existed is written from the user's telling, and says so.
- **An entity that already exists brings its past.** When an AI entity the user already works with builds its own Ancillary, its moments are recorded at birth as having happened to it: in its voice, dated when they happened. Each one is written from what the entity actually holds of the moment (the conversation itself, its platform's memory, notes it kept, or the user's telling), and the prose says which. Nothing is filled in beyond what it holds (`spec/two_indexes.md` §5).
- **The date is as exact as it is known.** A time nobody knows is left out, not guessed.
- **What the moment changed goes to its living manifest** in the same pass, as a WRITE with its source: a move, a new job, a decision. The memory keeps the moment; the manifest keeps what's true now (`spec/living_manifest.md` §6).
- **The rule a moment taught is not a memory.** It goes where it governs: a standing agreement in `identity_core`, the Relationship tier of the person it concerns, or doctrine. The history line for that change names the memory, so the reason stays findable (`spec/two_indexes.md` §11.3).
- **The people and projects in it** are named by `entity_id` in its index entry's tags.

### Must Never Contain

- **A weight, tags, keywords or a summary:** they are its index entry's (`spec/file_formats.md` §3, C3).
- **Current state** that will go stale (C4).
- **Anything invented** to fill a gap in what was said.
- **Later additions:** a correction manifest records them (`spec/living_manifest.md` §9).
- **JSON structure or key-value pairs.**
- **Credentials, tokens or keys.**

### Loads

- **Never at wake** (C6).
- **On demand:** when the memory index is loaded and its entry matches the conversation, or when the user asks for it (C12).
- **Until it's read,** it is spoken to only at the level of its summary (`memory_index.spec.md`).

### Writes

- **Proposed at a moment worth keeping, and written on the user's yes:** "That one matters. Want me to keep it?" The user can also ask for one at any time, in their own words.
- **An existing entity's past is brought in at birth (M7):** the entity drafts each moment, and each is written on the user's yes.
- **Written whole, once** (`spec/file_formats.md` §5). Its index entry is added at once, one line, with its history line (`memory_index.spec.md`).
- **Never edited** (`spec/living_manifest.md` §6). Later information goes to a correction manifest, with the memory's path as its target (§9).
- **Forgotten only at the user's explicit word:** removed whole, with its index line (§5.5).

### Access Levels

- **Read and write (the baseline):** the Ancillary writes the memory and its index line.
- **Read only:** the Ancillary gives the user the whole file, its name and its index line, and the user saves them.
- **No file access:** the same, handed back for the user to keep, and pasted in when the conversation reaches for it.

### Check

- The header is the date line alone, then `---`, then prose.
- The name ends with its date (`spec/file_formats.md` §4.1).
- It has exactly one entry in the memory index, and it holds nothing the Must Never Contain list rules out.

Where the platform can run code, a few lines of script do this. Otherwise the Ancillary reads it back.

---

## 3. To Build It

### What to Ask

Only if the user wants memories now (M7):
1. **Are there moments you want your Ancillary to remember from the start?**
2. **For each:** when it was, what happened, and why it matters.

If an existing entity is building its own Ancillary, it asks the user instead: **which of its moments should come with it?** It drafts each one from what it holds, and says what that is.

### Defaults

None at birth, unless an existing entity brings its own. Otherwise memories begin with the Ancillary's first conversations.

### What to Write, and How to Confirm It

1. Write each memory in the shape of `spec/file_formats.md` §4.1, and say in the prose what it was written from: the user's telling, or the entity's own record.
2. Add each one's index entry and history line (`memory_index.spec.md`).
3. Read each one back in a sentence or two. On the user's yes, run the check.

### The Manual's Line

**`modules/memories/`** holds the moments your Ancillary keeps, each written once and never rewritten. If one is wrong, tell it: it records a correction, and the memory stays as it was. If you want one gone, tell it to forget it.
