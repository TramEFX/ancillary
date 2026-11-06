# handoff.json

**path:** `temp/handoff.json`
**status:** core
**serves:** Portability (P2) and Curation (P5); the primitive's continuity

---

## 1. In Plain Words

A note one session leaves for the next when something is still in flight: where a piece of work stopped, or what was about to be asked. The next session reads it as it wakes and wipes it at once, so it never piles up. Anything that matters for longer goes into the library instead.

---

## 2. The Spec

### Shape

```json
{
  "status": "empty",
  "content": null,
  "written_at": null,
  "written_by": null
}
```

- **The fields are in `spec/file_formats.md` §4.6.** A note waiting sets `status` to `"pending"`, `content` to the note in plain words, `written_at` to the date and time, and `written_by` to the platform or model that wrote it.
- **A missing handoff reads as empty.** `temp/` never leaves the copy it's in (§4.6), so a fresh clone, or a library reached through a remote, has none. Its absence is never a failed read.
- **One note.** If a note is already waiting when another is left, the new one is added to it, not written over it.
- **On a platform that reaches the library only through a remote,** as a phone does over a connector, no handoff is written. What the next session needs goes into the library.

### Must Never Contain

- **Anything load-bearing:** a fact, a decision, or something learned. Those go into their files (C5). The handoff carries context, not facts.
- **More than the next session needs:** a few sentences, not a transcript.
- **Credentials, tokens or keys.**

### Loads

At every wake, at step 6, unless it's missing (C6). If its status isn't `"empty"`, its content is read, and it's wiped at once: the four fields go back to the skeleton. It is never re-read, never indexed and never synced.

### Writes

- **Created at birth (M9),** from the skeleton.
- **Written when a session ends with something in flight** that the next one needs (the rules' WRITING.handoff), as an additive write.
- **Wiped at the next wake.** That's the wake's only write (C11).
- **It has no history file.** A note that lives for one session has nothing to record.

### Access Levels

- **Read and write (the baseline):** the Ancillary leaves the note and wipes it.
- **Read only:** the Ancillary gives the user the note to paste into the next session.
- **No file access:** the same. The note travels with the user.

### Check

- The file parses as JSON, and has exactly the four fields.
- When empty, all four match the skeleton. When pending, `content`, `written_at` and `written_by` are filled.
- It holds nothing that belongs in the library.

Where the platform can run code, a few lines of script do the first two. Otherwise the Ancillary reads it back.

---

## 3. To Build It

### What to Ask

Nothing.

### Defaults

Empty.

### What to Write, and How to Confirm It

1. At M9, write the file from the skeleton.
2. Run the check above, and tick it with M9.

### The Manual's Line

**`temp/handoff.json`** is a note your Ancillary leaves itself when a session ends mid-task. It reads the note the next time it wakes and wipes it straight away. Nothing that matters lives there for long.
