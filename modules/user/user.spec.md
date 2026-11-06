# user.md

**path:** `modules/user/user.md`
**status:** core
**serves:** Ownership (P1) and Curation (P5); the primitive's continuity

---

## 1. In Plain Words

Who you are, as your Ancillary knows you: the person at the center of the library. It holds what's true about you now, each part dated and sourced, and how it changed lives in its history. It belongs to the library, at its center.

---

## 2. The Spec

### Shape

A living manifest (`spec/living_manifest.md` §5), written once at birth:

```markdown
---
manifest_type: living
entity_type: person
entity_id: user
schema_version: 1.4.0
created: <the date of the build>
updated: <the date of the last change>
history: history/user.md
tiers:
  core:         { updated: <the date>, confirmed: <the date>, source: user_explicit }
  relationship: { updated: <the date>, confirmed: <the date>, source: user_explicit }
links: []
pending_corrections: []
---

# <the name the user goes by>

## Core

- **Name:** <the name the user goes by>
- **<a Core field>:** <who they are: what they do, what they value, how they work>    <claim mark where it's needed>

## Status

- **<a Status field>:** <what's true now> (confirmed <the date>, user_explicit)       <claim mark where it's needed>

## Relationship

- **What they come to the Ancillary for:** <in their words>
- **<a Relationship field>:** <what helps them, and what doesn't>                     <optional>
```

- **`entity_id` is always `user`.** Every other manifest links to the person this way.
- **Every field is something the user told it,** and only what matters to this Ancillary's use (C1). A field is never filled with a guess.
- **The Relationship tier is how the two of them work together:** what the user comes to it for, what helps and what doesn't. The standing agreements between them are in `identity_core.md`, and aren't repeated here (C3).
- **An area of the person's own life** (income, housing, health) is a living manifest of its own beside this one, with `entity_type: life_domain`. It links back to `user`.
- **The Narrative Compass draws from this file.** When Status changes the arc, the Compass is reviewed (`manifest_index.spec.md`).

### Must Never Contain

- **A guess presented as a fact.** An inference is never a source (`spec/living_manifest.md` §4).
- **History, or notes about what changed:** those belong in `history/user.md` (C4).
- **Other people's details:** each person who matters has a file of their own (`people.spec.md`).
- **Events:** a moment is a memory, and the truth it left goes here.
- **Who the Ancillary is, or how it speaks.**
- **Passwords, account numbers, government IDs or anything secret.**
- **A link out of the library:** who the user is always lives in the library.
- **A weight** (C3).

### Loads

On demand, through the catalogue, before any reply it bears on (C12). It isn't part of the wake set (C6).

### Writes

- **Written once, at birth (M4),** from a conversation with the user.
- **Then only through the six operations** (`spec/living_manifest.md` §4), as life changes. Each one appends an entry to `history/user.md`.
- **Staleness:** a confirmed date 90 days old prompts a natural question (§10).
- **A substantive change** updates the catalogue entry's keywords (§8).
- **Every write is additive** (`spec/file_formats.md` §5).

### Access Levels

- **Read and write (the baseline):** the Ancillary keeps it current.
- **Read only:** the Ancillary gives the user the exact change and the history entry, and the user applies them.
- **No file access:** the user pastes it in when the conversation needs it, and applies the changes the Ancillary hands back.

### Check

`tools/check_living_manifests.py` where the platform can run code. Otherwise a read-back against `spec/living_manifest.md` §5.4, rule 6.

---

## 3. To Build It

### What to Ask

This is a short freshness interview (`spec/living_manifest.md` §10), so everything arrives confirmed:
1. **What should it call them?**
2. **Who are they?** What they do, what they care about, how they like to work.
3. **What's going on right now** that the Ancillary should know about?
4. **What do they come to it for?**
5. **What helps them, and what doesn't?**
6. **Is there anything they'd rather it not keep?**

### Defaults

- **Required:** the name and what they come to it for. Everything else is as shared.
- **Forward-looking statements are marked `[aspiration]`** until they're confirmed done.

### What to Write, and How to Confirm It

1. Write the file from the skeleton, every field `user_explicit`, confirmed today.
2. Start `history/user.md` with a LOG entry (`spec/living_manifest.md` §5.3): `- <date> · LOG · log · -`, with the note "created at the build (M4)."
3. Read it back to the user in plain words, and ask what's wrong or missing.
4. On their yes, run the check and tick M4. Its catalogue entry is written at M6 (`manifest_index.spec.md`).

### The Manual's Line

**`modules/user/user.md`** is you, as your Ancillary knows you. Tell it when something changes; it keeps what's true now here, and how it changed in `history/`.
