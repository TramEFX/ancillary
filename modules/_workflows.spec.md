# Workflows

**path:** `<the folder of what it works on>/<name>.md`, one file per workflow; `modules/workflows/<name>.md` for one that works across the library
**status:** optional
**serves:** Purpose (P4) and Curation (P5); the primitive's connectivity

---

## 1. In Plain Words

A workflow is something your Ancillary runs for you, with steps, a start and an end: a weekly review, a chapter check, the tax paperwork. Each one is a file of its own, kept beside what it works on, and it runs when you say @ and its name, or just ask. The audit is the one every Ancillary has; you add the rest.

---

## 2. The Spec

### Shape

```markdown
# <the workflow's name>

**Version:** 1.0.0
**Created:** <the date it was made>
**Last Updated:** <the date of the last change>
**Name:** @<its name>

---

<when it applies, in a sentence: what the user asks for that starts it>

**Starts on its own:** <optional: when it may start without being asked>

## Steps

1. <a step>   <one line or a short block each>

## Done When

<how the Ancillary and the user know it's finished>
```

- **It lives beside what it works on**: a project's workflow in that project's folder, a domain's in that domain's. One that works across the library, or on the user's day, goes in `modules/workflows/`, which appears the first time it's used. Maintenance workflows live in `modules/system_maintenance/`.
- **It starts when the user asks for it,** by its @name or in their own words. It never starts on its own unless its "Starts on its own" line says when it may. A misread should never set off a workflow.
- **Its name** is one word, lowercase, unique among the modes and workflows. The file is named for it.
- **A step names what it needs, never a tool:** read a file, search the web, send an email (P2). Tools come from the platform.
- **A step that writes in the library** is an additive write, with its history line (`spec/file_formats.md` §5). A step that acts outside it, such as sending, posting, buying or deleting, follows the platform's rules and permissions.
- **A step that needs a judgment waits for the user's yes.** Steps that only read and report run straight through.
- **Structured settings** a script reads go in a `.json` file beside it, which the workflow names (§1).

### Must Never Contain

- **A way of operating with no end:** that's a mode (`modes/_modes.spec.md`).
- **Lines that tell the model to override its own guidelines,** or a change to the voice or the identity.
- **A particular tool's name, or one platform's paths** (P2).
- **Credentials, tokens or keys.** A step that needs one asks the platform for it, never the library.
- **Its own change history, or a weight** (C3, C4).

### Loads

On demand, in full, when the user says @ and its name or asks for it in plain words (C10, the rules' MODES.at_names). Never at wake.

### Writes

- **Made at the user's word, in their words.** The Ancillary drafts the steps, reads them back, and writes the file on their yes.
- **Written whole, as version 1.0.0,** with its catalogue entry (its @name in `tags`, `external` if what it works on lives outside the library) and the first line of `history/<name>.md` (`spec/file_formats.md` §4.4).
- **A change** bumps the version and leaves a history line. A workflow the user retires is copied to the archive, and its catalogue line is removed (§4.5).
- **Every write is additive** (§5).

### Access Levels

- **Read and write (the baseline):** the Ancillary makes, keeps and runs the workflows.
- **Read only:** the Ancillary gives the user the file and its catalogue entry to save, and hands back each write a run makes.
- **No file access:** the user pastes the workflow in when they want it run.

### Check

- The file has its header, its sentence, its steps and "Done When". No placeholder is left.
- Its @name matches its file name, and no other mode or workflow has it.
- It has one catalogue entry, with its @name in `tags`, and a history file.
- Read back: no step names a tool, and every step that changes something outside the library is left to the platform's permissions.

Where the platform can run code, a few lines of script do the first three. The read-back is the Ancillary's.

---

## 3. To Build It

### What to Ask

Only if the user wants workflows now (M8):
1. **Is there something you'd like it to run for you, the same way each time?**
2. **For each:** when it applies, the steps, and how you'll both know it's done.
3. **Should it ever start on its own?** Only if the user says when.

### Defaults

- **None at birth** beyond the audit (`system_maintenance/audit.spec.md`).
- **Starts on its own:** never.
- **Weight:** 0.994, category `workflows`.

### What to Write, and How to Confirm It

1. Write each workflow from the skeleton, beside what it works on.
2. Add its catalogue entry and its history line.
3. Read the steps back to the user. On their yes, run the check.

### The Manual's Line

**Workflows** are things your Ancillary runs for you, the same way each time. Say @ and a workflow's name, or just ask for it. To make a new one, tell it the steps in your own words.
