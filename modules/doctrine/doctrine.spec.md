# doctrine/

**path:** `modules/doctrine/<name>.md`, one file per position
**status:** optional
**serves:** Ownership (P1) and Curation (P5); the primitive's continuity

---

## 1. In Plain Words

One file for each standing position you hold, in your own words: a belief, a principle, how you think something should be done. When your thinking changes, it's revised in place, and how it changed lives in its history. It belongs to the library.

---

## 2. The Spec

### Shape

A doctrine file, in the shape of `spec/file_formats.md` §4.2: a header with its date, version, last update and an optional source, then the position in prose.

- **A position, not an event or an entity's state.** It answers "what does the user hold?" A moment goes to a memory, and what's true of a person or project goes to their living manifest.
- **It stands across the user's life or work.** A position about one project is a decision in that project's Core (`projects.spec.md`).
- **In the user's words.** Where their words need shaping into a file, the Ancillary drafts it and reads it back, and the user's yes makes it theirs. Quote them where it can.
- **Its name is the position,** in lowercase words joined by underscores, with no date. It is revised in place, never replaced by a newer dated file.
- **`Source`** names the memory or document the position came from, when there is one. That keeps the reason beside the rule (`spec/two_indexes.md` §11.3).
- **Its version** starts at 1.0.0. The last number goes up for a wording fix, the middle one for a refinement, and the first when the position itself turns.
- **Its catalogue entry** has category `doctrine`, and no `entity_id`.

### Must Never Contain

- **A position the user hasn't stated.** An inference is never doctrine until the user says it's theirs.
- **Rules for how the Ancillary behaves:** an agreement between the two of them belongs in `identity_core`, and how to treat a person belongs in that person's file.
- **Events or an entity's state** (`spec/two_indexes.md` §3).
- **Its own change history** (C4), or **a weight** (`spec/file_formats.md` §3).
- **Credentials, tokens or keys.**

### Loads

On demand, through the catalogue, when the conversation turns to what it's about (C12).

### Writes

- **Created when the user states a position worth keeping,** or on the Ancillary's proposal and the user's yes: "You've said this a few times now. Want me to keep it as one of your positions?"
- **Revised in place at the user's word.** Each revision bumps the version and the last-updated date, and leaves one line in `history/<name>.md` (`spec/file_formats.md` §4.4). A substantive revision updates the catalogue entry's keywords.
- **A position wrongly recorded** is revised the same way, and its history line says it was recorded wrong.
- **A position the user lets go is retired.** Its last version is copied to the archive (`spec/file_formats.md` §4.5), its catalogue line is removed, and each history file gets a line.
- **Forgotten only at the user's explicit word** (`spec/living_manifest.md` §5.5).
- **Every write is additive** (`spec/file_formats.md` §5).

### Access Levels

- **Read and write (the baseline):** the Ancillary keeps the positions and revises them when asked.
- **Read only:** the Ancillary gives the user each new file or revision, and its history line.
- **No file access:** the user pastes a position in when it comes up.

### Check

- The header has its date, version and last-updated date, and nothing else but an optional source, which resolves.
- The body is prose.
- It has one catalogue entry, category `doctrine`, and a history file with a line for each version.

No reference checker covers doctrine. Where the platform can run code, a few lines of script do this. Otherwise the Ancillary reads it back.

---

## 3. To Build It

### What to Ask

Only if the user wants doctrine now (M8):
1. **Are there positions you hold that you'd want your Ancillary to know?** About your work, your life, or how things should be done.
2. **For each:** what it is, in your own words.

### Defaults

- **None at birth.** Doctrine grows as positions come up.
- **A new position's weight:** 0.9995, unless the user says it's foundational.

### What to Write, and How to Confirm It

1. Write each file in the shape of `spec/file_formats.md` §4.2, as version 1.0.0, dated today, with the body in the user's words.
2. Start each history file: `- <date> — created, 1.0.0. Built at M8.`
3. Add each catalogue entry, one line, with its history line.
4. Read each one back. On the user's yes, run the check.

### The Manual's Line

**`modules/doctrine/`** holds your standing positions, in your own words. When your thinking changes, tell your Ancillary: it revises the position and keeps how it changed.
