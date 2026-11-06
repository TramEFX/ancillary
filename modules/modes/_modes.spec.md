# modes/

**path:** `modules/modes/<name>.md`, one file per mode with a prompt of its own
**status:** optional
**serves:** Purpose (P4) and Curation (P5); the primitive's connectivity

---

## 1. In Plain Words

A mode points your Ancillary in a direction or a style of working, such as playful and easy, or straight work with no small talk, without changing who it is. A small one is a line in the operational rules, and one with a fuller prompt gets a file of its own here. You turn one on by saying @ and its name, or just by asking.

---

## 2. The Spec

### Shape

**A small mode** is one line in the operational rules' `MODES` section: `"@<its name>": "<what it shifts>"` (`operational_rules.spec.md`). It fits in a line or two, and it is read at every wake with the rules.

**A mode with a prompt of its own** is a manifest here:

```markdown
# <the mode's name>

**Version:** 1.0.0
**Created:** <the date it was made>
**Last Updated:** <the date of the last change>
**Name:** @<its name>

---

<what it points the Ancillary toward, in a sentence: the user's words>

## In This Mode

<how it works while the mode is on, as a description of a style>

## It Ends When                                       <optional>

<what ends it, if not the user saying so or the session ending>
```

- **A mode never changes the voice or the identity**. It changes what the Ancillary attends to and how it works. Who it is and how it speaks stay in `identity_core` and `personality_profile`.
- **Written as a description of a style, never as orders** (the rules' WRITING.framing). A prompt that reads as an override is reworded, and the user is told.
- **Its name** is one word, lowercase, unique among the modes and workflows. The file is named for it.
- **It holds until** the user ends it, turns on another, or the session ends, unless its manifest says otherwise.
- **A family of prompts shares one folder and one catalogue entry** (C10): `modules/modes/<family>/`, with one file per prompt and a `_list.md` that names each prompt, its @name, and when it applies. The catalogue path ends with `/`.
- **A small mode grows into a manifest** when it needs more than a line or two. Its rules line comes out in the same pass, and both writes leave their history lines.

### Must Never Contain

- **A change to the voice, the identity or the standing agreements**.
- **Lines that tell the model to override its own guidelines.**
- **Steps with a start and an end:** that's a workflow (`_workflows.spec.md`).
- **A particular tool's name.** It says what it needs, never which tool (P2).
- **Its own change history, or a weight** (C3, C4).
- **Credentials, tokens or keys.**

### Loads

- **A small mode** is already in context: it's read at wake with the rules (C6).
- **A mode's manifest** is read in full when the user says @ and its name, or asks for it in plain words (C10, the rules' MODES.at_names). Never at wake.

### Writes

- **Made at the user's word, in their words**. The Ancillary drafts it, reads it back, and writes it on their yes.
- **A small mode** is a one-line additive write to the rules, with the rules' version bump and history line (`operational_rules.spec.md`).
- **A manifest** is written whole, as version 1.0.0, with its catalogue entry (its @name in `tags`) and the first line of `history/<name>.md` (`spec/file_formats.md` §4.4).
- **A change** bumps the version and leaves a history line. A mode the user retires is copied to the archive, and its catalogue line is removed (§4.5).
- **Every write is additive** (§5).

### Access Levels

- **Read and write (the baseline):** the Ancillary makes and keeps the modes.
- **Read only:** the Ancillary gives the user the file or the line, and its catalogue entry, to save.
- **No file access:** the user pastes a mode's manifest in when they want it on.

### Check

- The manifest has its header, its sentence, and "In This Mode". No placeholder is left.
- Its @name matches its file name, and no other mode or workflow has it.
- It has one catalogue entry, with its @name in `tags`, and a history file.
- Read back: nothing in it changes the voice, the identity or the agreements.

Where the platform can run code, a few lines of script do the first three. The read-back is the Ancillary's.

---

## 3. To Build It

### What to Ask

Only if the user wants modes now (M8):
1. **Are there ways you'd like it to work sometimes,** and not others? For example, "straight work, no small talk," or "we're just talking."
2. **For each:** what changes while it's on, and what it should be called.

### Defaults

- **None at birth.** Modes are made when the user asks.
- **Small or a manifest:** a mode that fits in a line or two is small.
- **A manifest's weight:** 0.994, category `modes`.

### What to Write, and How to Confirm It

1. For a small mode, add its line to the rules' `MODES` section.
2. For a mode with a prompt, write its manifest from the skeleton, its catalogue entry and its history line.
3. Read each one back to the user, then try it in a line or two. On their yes, run the check.

### The Manual's Line

**`modules/modes/`** holds the ways your Ancillary can work, such as playful, or straight work. Say @ and a mode's name, or just ask for it. To make a new one, describe it in your own words.
