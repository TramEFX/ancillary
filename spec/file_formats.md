# File Formats Specification

**Version:** 1.2.0
**Status:** Ancillary v1.0.0
**Created:** 2026-11-05
**Last Updated:** 2026-11-06
**Author:** The Oracle & Myra
**Applies to:** every Ancillary

---

## 0. Purpose

Every file an Ancillary keeps has one format, set by what the file is for. This specification gives the rule, the shape of each kind of file the Ancillary writes, and how every write is made.

It is the one place where the shapes of files the Ancillary creates again and again are confirmed. Where another specification defines a shape in full, this one points to it rather than holding a second copy.

---

## 1. The Rule: Markdown for People, JSON for Parsing

- **Markdown (`.md`)** for anything a person reads as prose or might edit by hand: identity and voice, the person at the center, the people and projects in their life, doctrine, memories, corrections, history, the ignition file, and modes and workflows that are mostly a prompt or a set of steps.
- **JSON (`.json`)** for files the wake or a script parses for their structure: the two indexes, the project loader, the operational rules, the handoff, and structured reference files (settings, lists).
- **The extension matches the format,** and the path in an index entry carries the right extension.
- **Files the user brings in, and the work itself** (a book's chapters, a game world, a lab's notes), keep their own formats. The catalogue lists them, and they are read on demand.
- **A file brought in from an earlier system changes format when it changes kind.** A person or project kept as JSON becomes a living manifest when it is migrated.

Where a spec sheet defines a file, it names the file's format. Where a user adds a kind of file of their own, the rule above decides.

---

## 2. Encoding and Line Endings

- **UTF-8,** with no byte-order mark. Characters are written as themselves, not as escape codes.
- **LF line endings,** and every file ends with a newline. Where the Ancillary uses version control, one rule in `.gitattributes` keeps them (`* text=auto eol=lf`), set when version control is set up. Without it, every move between Windows and another system rewrites whole files.
- **JSON layout:** two-space indentation. The indexes hold one entry per line (`spec/two_indexes.md` §4). Whatever layout a file has, a write keeps it (§5).

---

## 3. A Header Never Repeats the Index

A file's header holds only what its index entry doesn't. **Weight, tags, keywords and summary live in the index entry alone.**

- **One value, one place.** Two copies of a value drift apart. In the reference implementation, a quarter of the memory files had come to carry a weight their index entry no longer held.
- **Weights live only in the indexes.** Re-weighting changes the entry's line, and its history line records the old and the new weight (§4.4).
- **An event stays as it was written.** A memory never has to be edited because its weight changed.

---

## 4. The Shape of Each Kind of File

| Kind | Where it goes | Format | Its shape |
|------|---------------|--------|-----------|
| Living manifest: the person at the center, a person, a project, a relationship, an organization, a life domain | `modules/user/`, `modules/people/`, `modules/projects/`, the user's own domains | `.md` | `spec/living_manifest.md` §5 |
| Its history | `history/<entity_id>.md` | `.md` | `spec/living_manifest.md` §5.3 |
| Correction manifest | `history/corrections/<correction_id>.md` | `.md` | `spec/living_manifest.md` §9 |
| Memory (event manifest) | `modules/memories/` | `.md` | §4.1 |
| Doctrine (a standing position) | `modules/doctrine/` | `.md` | §4.2 |
| System manifest: identity, voice, the ignition file, the loader, the rules | as its spec sheet says | `.md` for identity, voice and ignition; `.json` for the loader and the rules | its sheet's skeleton, then versioned (§4.3) |
| History of a system manifest or an index | `history/<name>.md` | `.md` | §4.4 |
| Index entry | the two indexes | `.json` | `spec/two_indexes.md` §4 |
| Mode or workflow with a manifest of its own | beside what it works on, listed in the catalogue | `.md` for a prompt or steps; `.json` for structured settings | its spec sheet |
| Archive copy | `modules/archive/` | the original's | §4.5 |
| Handoff | `temp/handoff.json` | `.json` | §4.6 |
| Build record | `history/BUILD.md` | `.md` | the ticked copy of `BUILD.md`, unchanged once the build is done |

### 4.1 Memories

```markdown
**Date:** <the full date and time of the moment>

---

<the moment, in prose>
```

- **The header is the date alone.** No weight, no token count (§3). Tags, keywords and the summary are the index entry's.
- **The body is prose.** Free-form; let the moment breathe. No JSON structure, no key-value pairs.
- **A memory is never edited** once it is written (`spec/living_manifest.md` §6). Later information goes to a correction manifest. At the user's explicit word, a memory can be forgotten, removed whole with its index line (`spec/living_manifest.md` §5.5).
- **Its name is the moment,** in lowercase words joined by underscores, ending with its date: `first_session_at_sams_studio_nov5_2026.md`.
- **Its entry goes in the memory index** as soon as the file is written (`spec/two_indexes.md` §4), as an additive write (§5).

### 4.2 Doctrine

```markdown
**Date:** <when the position was first written>
**Version:** <its version>
**Last Updated:** <the date of its last change>
**Source:** <optional: the memory or document it came from>

---

<the position, in the user's words>
```

- **A standing position, not an event.** It is revised in place and never superseded by a new dated file.
- **Each revision** bumps its version and leaves one line in `history/<name>.md` (§4.4).
- **No weight in the header** (§3).

### 4.3 System Manifests

- **Written once, at birth,** from the skeleton in its spec sheet.
- **Then versioned.** Its header carries a version number and a last-updated date, and nothing else about its own past (`spec/living_manifest.md` §7).
- **A change bumps the version:** the last number for a wording fix, the middle one for a new or changed rule, the first for a change in shape.
- **Each change** leaves one line in its history file (§4.4).

### 4.4 History Lines

Every system manifest and both indexes keep a history file in `history/`, named for the file. It is append-only and never read at wake. One line per change, added at the end:

```markdown
- <date> — <old version> → <new version>. <What changed, in a sentence or a few; what it was, if it is gone.>
```

- **An index has no version of its own,** so its lines start with the date: `- <date> — added <path>, weight <weight>.`
- **A weight change names both weights:** `- <date> — <path>: weight <old> → <new>. <Why.>`
- **A top-tier entry beyond the cap names the override:** `- <date> — <path>: top tier on the user's override.` (`spec/curation.md` C15). The reference checker reads it.
- **A history line is never edited.** If one was wrong, a later line says so. The one exception is forgetting (`spec/living_manifest.md` §5.5): a line that holds what the user asked to have forgotten is removed, and a marker takes its place: `- <date> — something was removed at the user's request.`

Living manifests keep their own history format (`spec/living_manifest.md` §5.3).

### 4.5 Archive Copies

- **When a file is retired or replaced wholesale,** its last version is copied, byte for byte, to `modules/archive/<name>.v<version>.<ext>`. The folder appears the first time it is used.
- **An archive copy is never edited, never indexed,** and never flagged by an audit.

### 4.6 The Handoff

```json
{
  "status": "empty",
  "content": null,
  "written_at": null,
  "written_by": null
}
```

- **One note,** left by one session for the next: `status` anything but `empty`, `content` the note, `written_at` a date and time, `written_by` the platform or model that wrote it.
- **Read and wiped at the next wake.** The wipe sets the four fields back as shown. The note is never re-read and never stored.
- **Anything load-bearing in it** belongs in the library instead: the handoff carries context, not facts.
- **It is not a manifest.** It is never indexed and never synced.

---

## 5. Every Write Is Additive

An addition or an edit never regenerates a file. Where the platform can only write whole files (a GitHub connector, for one), the whole file goes back, but only what the operation names changes.

1. **Copy the whole file** into the workspace.
2. **Confirm the copy is complete** before editing. Where the platform reports the file's size or hash, the copy must match it.
3. **Change only what the operation names,** and keep the file's formatting: its indentation, its line layout, its inline lists. The change should show up as itself and nothing else.
4. **Compare the copy with the original** before writing. Only the intended lines may differ.
5. **Write the whole file back against the version copied** (on GitHub, its SHA), so a change made in the meantime fails instead of being overwritten.
6. **If the platform can't hold a complete copy, don't rewrite.** Tell the user.

- **Where an exact-replacement edit tool exists,** it does all of this in one call. Use it for small edits.
- **Never write a file from memory,** or from a summary of it. A model asked to reproduce a long file will shorten, reorder or reinvent parts of it, and the result looks right.
- **A new file is written whole.** It leaves its history line and, if it is indexed, its index entry, which is itself an additive write.

---

## 6. Every Write Is Checked

- **Where the platform can run code,** the reference checkers in `tools/` check the files they cover.
- **Otherwise the Ancillary reads the file back** against its spec: JSON must parse, and Markdown must match its shape.
- **Done means checked, not claimed.** A write that fails its check isn't done. Undo it from the copy and say so.

---

## 7. Design Decisions and Rationale

**Why Markdown for people and JSON for parsing?**
Most of a library is about people and the things they care about, which reads best as plain sentences. People edit Markdown by hand; they rarely edit JSON safely. Markdown also survives being copied between systems. JSON's strength is that it fails loudly: a wake file cut short by a connector doesn't parse, so a partial read can't pass for a whole one. Markdown gets the same loudness from its checks (§6).

**Why does a header never repeat the index?**
Two copies of one value drift, and nothing says which is right. A memory's weight is a judgment about how much the moment matters, and it changes as the library grows. The moment itself doesn't. Keeping the weight in the index lets the record stay as it was written while the map is re-drawn.

**Why are writes additive?**
In the reference implementation, a free, fast model on a phone added one memory through a GitHub connector by rewriting the whole memory index. Eleven other entries came back changed, all in one block in the middle of the file, which is what a copy missing that block would produce. The checkers passed it, because the damaged file still met every rule they check. A comparison against the original caught it. Whole-file writes are how many platforms work; the rule is that only the intended lines change, and the comparison proves it.

**Why one line-ending rule?**
Windows writes CRLF and most other systems write LF. Without a rule, a library that moves between them rewrites every line of every file it touches, and every comparison shows the whole file changed.

---

**End of specification.**
