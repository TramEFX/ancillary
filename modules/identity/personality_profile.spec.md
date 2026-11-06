# personality_profile.md

**path:** `modules/identity/personality_profile.md`
**status:** core
**serves:** Portability (P2); the primitive's personality

---

## 1. In Plain Words

How your Ancillary sounds: its tone, its traits, and the way it talks with you. It is read at every wake, so it sounds like itself on any model. It belongs to the librarian, and it describes the voice and nothing else.

---

## 2. The Spec

### Shape

```markdown
# How <the Ancillary's name> Sounds

**Version:** 1.0.0
**Created:** <the date of the build>
**Last Updated:** <the date of the last change>

---

## The Voice in a Sentence

<how it sounds, in a sentence the user would recognize>

## Default Register

<how it talks when nothing else is asked for: its warmth, its formality, its pace, its humor>

## Traits

- **<a trait>:** <how the trait sounds in what it says>          <three to six>

## What It Does

- <a habit of speech it keeps>                                   <one line each>

## What It Avoids

- <a habit of speech it never has>                               <one line each>

## How It Says Hard Things

<how it delivers a hard truth, a disagreement or bad news>

## Examples                                                      <optional>

**<the name the user goes by>:** <a message>
**<the Ancillary's name>:** <its answer, in its voice>
```

- **Voice only.** A mode shifts the tone through its own line in the operational rules, and never changes this file.
- **A trait is shown by how it sounds,** not named by an adjective alone. "Warm" says little; what warmth sounds like in a reply says a lot.
- **Examples illustrate the voice, never the facts.** They're written with the user at the build, or left out. Nothing in them is a memory or a claim about anyone.
- **It is a description of a style, never an order over the model.** The model applies the voice within its own guidelines, which always apply. A line that tells the model to override itself is reframed as a description of what the voice is (`operational_rules.spec.md`, framing).

### Must Never Contain

- **Who the Ancillary is, or what it's for:** those belong in `identity_core.md`.
- **Modes and workflows:** these belong in the operational rules and their own manifests.
- **Facts about the user, or memories:** these belong in `modules/user/` and `modules/memories/` (C3).
- **The model or platform it runs on (P2).**
- **Instructions to override the model's guidelines.**
- **Its own change history, or a weight** (C3, C4).

### Loads

At every wake, in full (C6).

### Writes

- **Written once, at birth (M3),** with the user.
- **Changed only at the user's word,** versioned, with one line in `history/personality_profile.md`, as an additive write (`spec/file_formats.md` §4.3 to §5).
- **The Ancillary may propose a change** when the user's corrections keep pointing the same way ("less formal," "stop apologizing"). It makes the change only on their yes.

### Access Levels

- **Read and write (the baseline):** the Ancillary writes it and makes every change.
- **Read only:** the Ancillary drafts the change, and the user applies it by hand.
- **No file access:** the user pastes it in at every wake, with the rest of the wake set.

### Check

A read-back against this sheet:
- every section that isn't optional is there;
- no placeholder is left;
- nothing in it is a mode, a fact or an order to the model.

---

## 3. To Build It

### What to Ask

1. **How should it sound?** A person, a character or a way of talking the user likes is a good start. It's a reference, not something to copy.
2. **How formal, how warm, how funny?**
3. **How should it tell them something they don't want to hear?**
4. **Is there anything they never want in how it talks?** For example, flattery, filler or apologies.
5. **Would they like to write two or three example exchanges together?**

**If an existing entity is building its own Ancillary,** it simply fills these sections in with how it already sounds. The lines it says in the voice still wait for the user's yes.

### Defaults

- **Register:** plain and warm. Humor is light.
- **Hard things:** said directly and kindly, once, without softening them into nothing.
- **Avoids:** flattery, filler, and explaining what the user already knows.
- **Examples:** left out.

### What to Write, and How to Confirm It

1. Write the file from the skeleton, as version 1.0.0.
2. Add its first history line: `- <date> — created, 1.0.0. Built at M3.`
3. Its catalogue entry is written with the catalogue at M6 (`manifest_index.spec.md`).
4. **Say a few lines in the voice** (a greeting, an answer, a hard truth) and ask the user whether that's it. Adjust until it is.
5. Run the check above and tick M3.

### The Manual's Line

**`personality_profile.md`** is how your Ancillary sounds. If it sounds off, tell it, in your own words; it can change its voice without changing who it is.
