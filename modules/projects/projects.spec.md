# projects/

**path:** `modules/projects/<entity_id>.md`, one file per project; its work, if the library holds it, in `modules/projects/<entity_id>/`
**status:** optional
**serves:** Purpose (P4) and Curation (P5); the primitive's continuity and connectivity

---

## 1. In Plain Words

One file for each project you're carrying: its vision, specs, status and the decisions that stand. When the use calls for it, the library holds the work itself too, or links to where the work already lives. They belong to the library.

---

## 2. The Spec

### Shape

A living manifest, `entity_type: project`, in the shape of `spec/living_manifest.md` §5.

- **The tiers:**
  - **Core:** the vision, the specs and principles, and the decisions that stand.
  - **Status:** the phase, what's blocking it, what's next, who's working on it. Each field is confirmed on its own.
  - **Relationship:** why it matters to the user, what's at stake, and deadlines tied to their life.
- **A decision is a WRITE.** The reasoning goes in its history note, so the manifest holds what was decided and the history holds why. There is no decision log inside the file (C4).
- **"Where the work is"** is a Core field when there is work:
  - **In the library:** `modules/projects/<entity_id>/`, in whatever formats the work needs (`spec/file_formats.md` §1), listed in the catalogue and read on demand (C13).
  - **Linked:** an existing system or repository beside the library, listed in the catalogue with `external` (`spec/two_indexes.md` §4.4).
  - **Nowhere yet.**
- **Oversight is one use.** A project the Ancillary oversees as its CEO records here who is doing the work, and what they report.

### Must Never Contain

- **The work itself:** the manifest is the map of the project. The work goes in its folder, or stays where it lives.
- **Copies of linked files** (C3).
- **History, a decision log or a changelog** (C4).
- **API keys, passwords, tokens or any credential.**
- **A weight** (C3).

### Loads

- **The manifest:** on demand, through the catalogue, when the project comes up (C12).
- **The work:** only when the conversation reaches for it, never at wake (C13).

### Writes

- **Created when the user starts a project, or brings one in.**
- **The manifest changes only through the six operations** (`spec/living_manifest.md` §4), each with a history entry.
- **The work is written as the work needs,** each write additive (`spec/file_formats.md` §5).
- **Linked work is written only as the platform allows**, and the Ancillary says what it changed.
- **Each new work file or linked source gets its catalogue entry.**

### Access Levels

- **Read and write (the baseline):** the Ancillary keeps the manifest current, and works in the work.
- **Read only:** the Ancillary drafts every change; the user applies it.
- **No file access:** the user pastes in the manifest, or the part of the work in question.

### Check

`tools/check_living_manifests.py` for the manifest where the platform can run code, or a read-back against `spec/living_manifest.md` §5.4, rule 6. The work is checked as its own format requires. JSON must parse.

---

## 3. To Build It

### What to Ask

Only if the user wants projects now (M8):
1. **What projects are they carrying?**
2. **For each:** what it is, where it stands, what's next, and why it matters to them.
3. **Where does the work live?** In the library, somewhere it already lives, or nowhere yet.

### Defaults

None at birth. Projects are added as the user brings them.

### What to Write, and How to Confirm It

1. Write each manifest in the shape of `spec/living_manifest.md` §5, every field `user_explicit`, confirmed today.
2. Start each history file with a LOG entry (`spec/living_manifest.md` §5.3): `- <date> · LOG · log · -`, with the note "created at the build (M8)."
3. Add each catalogue entry with its `entity_id`, and an entry for each linked source with `external`. LINK each project from `user`.
4. Read each one back in a sentence or two. On the user's yes, run the check.

### The Manual's Line

**`modules/projects/`** holds a file for each project: what it is, where it stands, and what's been decided. If the work lives somewhere else, your Ancillary links to it there instead of copying it.
