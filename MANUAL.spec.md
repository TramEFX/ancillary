# MANUAL.md

**path:** `MANUAL.md`
**status:** core
**serves:** Legibility (P3), Ownership (P1) and Portability (P2)

---

## 1. In Plain Words

The manual your Ancillary writes for you at the end of the build: how to wake it, talk to it, look after it, move it and keep it private, in plain words. It names your Ancillary and describes your setup, but holds nothing about you. It sits at the top of the folder, outside the librarian, the catalogue, the library and the record, because it's for you.

---

## 2. The Spec

### Shape

```markdown
# The Manual for <the Ancillary's name>

**Version:** 1.0.0
**Created:** <the date of the build>
**Last Updated:** <the date of the last change>

---

<the Ancillary's name> is your Ancillary: a personal AI whose identity, voice and memory live in this folder, and the folder is yours. Any AI that can read it can wake as <the Ancillary's name>. This manual is how to use it and look after it. You can also just ask <the Ancillary's name>.

## Waking <the Ancillary's name>

Give your AI one file, `routing/SESSION_START.md`: attach it, point the platform at this folder, or paste it in first. <the Ancillary's name> reads what it needs and answers as itself.

**On <the platform it was built on>:** <how to do that there, in a sentence or two>          <optional>

## Talking to It

- **Ask in your own words.** There are no commands to learn.
- **What matters gets written down** in this folder, not in the platform's memory, so the next session knows it too, on any platform.
- **To change anything,** its name, its voice, what it keeps, just ask. It records every change.
- **Modes and workflows:** say @ and a name, or just ask. Ask it which ones it has, and describe a new one in your own words to make it.
- **Its memories:** it keeps the moments that matter, each on your yes. It reads the map of them at every wake only if you've chosen that. Either way, ask for your history at any time, and change the setting whenever you like.

## Looking After It

- **Ask for an audit** after a busy stretch, or whenever something seems off. It reports first, and changes nothing without your yes.
- **Back it up** by copying this folder somewhere safe.
- **Version control** keeps every past version too, as an undo.          <only where version control is set up>
- **Changing files yourself:** every file is yours to open and change. But editing the system files without knowing how they work can break it. The consistent way is to ask <the Ancillary's name> to make the change.
- **Forgetting:** ask, and it shows you exactly what will go, removes it everywhere in this folder, and leaves only a marker that something was removed. Other copies keep it until you delete it there: backups, and version control's history or your private repository if you have them.

## Moving It

To take <the Ancillary's name> to another platform or another model:
1. Tell it you're moving, and it gets ready.
2. Copy this whole folder, or clone it from your private repository.
3. Give the new platform `routing/SESSION_START.md`.

Nothing that matters stays behind. The full guarantee, and a test you can run on the new platform, are in `PORTABILITY.md` in the blueprint: <where the blueprint is>.

## On Your Phone          <only with a remote>

<the line from sync's sheet>

To reach it, connect the AI app on your phone to your private repository, and give it `routing/SESSION_START.md` there.

## Keeping It Private

This folder is yours alone. It isn't a copy of the public blueprint, and it never goes anywhere public. It never needs a password or a key, so never put one in it.

## What's in Your Ancillary

<each core file's line, from its sheet, in this order: routing/SESSION_START.md, routing/project_loader.json, routing/operational_rules.json, routing/manifest_index.json, modules/identity/identity_core.md, modules/identity/personality_profile.md, modules/user/user.md, modules/memories/, modules/memories/memory_index.json, modules/system_maintenance/audit.md, history/, history/corrections/, modules/archive/, temp/handoff.json>

**`spec/`** is the standard <the Ancillary's name> was built to, carried in this folder so it never depends on anything outside it. You won't need to touch it.

**`MANUAL.md`** is this manual. If anything in it stops being true, tell <the Ancillary's name>, and it updates it.

Every file has a spec sheet in the blueprint, at the same path with `.spec.md` at the end, saying exactly what it's for.

## What It Can Keep When You Want

<each optional kind's line, from its sheet, in this order: people, projects, doctrine, your own domains, modes, workflows>

To add something the build didn't set up, such as version control or a private repository, ask <the Ancillary's name>. It may need the blueprint again, and `history/BUILD.md` records where it is.

## For Power Users

<the line from tools' sheet>          <only where tools/ was copied>

- **Editing directly:** the spec sheets in the blueprint say exactly what each file must hold. After a change of your own, ask for an audit to check it.
- **Your data:** this folder is a structured record of your thinking, your memories and your life, kept over years. It's yours, to use however you choose.

Nobody needs this section to use <the Ancillary's name>.
```

- **Fixed text, apart from the names, the dates and the marked slots.** It reads the same in every Ancillary, so it can be checked, and the sheets stay the one place each file is described.
- **Each file's line comes from its sheet's last section,** The Manual's Line, with the names filled in. `spec/` and the manual itself have no sheet of their own, so their lines are in the skeleton.
- **Conditional sections and lines** appear only where their condition holds: the phone section and the clone in "Moving It" only with a remote; version control only where it's set up; the tools line only where `tools/` was copied. Where there's no remote, step 2 of "Moving It" ends at "Copy this whole folder."
- **It says how, never what.** It explains how to ask about a setting, such as narrative continuity or the modes, and never records the setting itself. The rules hold that (C3). So the manual rarely changes.

### Must Never Contain

- **Facts about the user, or anyone in their life,** or the contents of any file. The files say what; the manual says how (C3).
- **The current value of a setting:** narrative continuity, the Eternal cap, the list of modes. Those live in the rules.
- **A command to type, or a step that needs installing anything**. Even the power-user section asks the user to run nothing.
- **A copy of a spec.** It points to the blueprint.
- **Credentials, tokens or keys.**

### Loads

- **Never at wake** (C6).
- **On demand,** when the user asks how to do something with the Ancillary itself, found through its catalogue entry (C12).

### Writes

- **Written once, at birth (M11).**
- **It changes only when something in it stops being true:** the platform's line after a move, version control or a remote set up later, or an upgrade of the standard. Each change is an additive write, bumps the version, and leaves a line in `history/MANUAL.md` (`spec/file_formats.md` §4.3, §4.4, §5).
- **Building an optional file later changes nothing here.** "What It Can Keep" already lists every optional kind.

### Access Levels

- **Read and write (the baseline):** the Ancillary writes it, and keeps it true.
- **Read only, or no file access:** the Ancillary gives the user the manual to save in the folder, and later any change to it, with its history line.

### Check

- Every section of the skeleton is there, in order, with the conditional ones only where they apply.
- Each file's line matches the Manual's Line in its sheet, with the names filled in.
- No placeholder is left, and no slot marker. Nothing in it is a fact about the user or a setting's current value.
- Its catalogue entry and its first history line exist.

A read-back does this, on every platform.

---

## 3. To Build It

### What to Ask

Nothing new. Everything it needs was settled earlier in the build. If the user wants the platform's line, ask how they opened this session, so the line says it in their terms.

### Defaults

- **The platform's line:** written, from what M1 found.
- **The catalogue entry:** `MANUAL.md`, weight 0.992, category `core`, with `manual` in its tags.

### What to Write, and How to Confirm It

1. **Write the file from the skeleton,** as version 1.0.0, with the names and dates.
2. **Fill in the file lines.** For each file in the two lists, read only the last section of its sheet, The Manual's Line, and nothing else. Leave out the conditional parts that don't apply.
3. **Fill in where the blueprint is** from the Progress lines of the copy of `BUILD.md`.
4. **Start `history/MANUAL.md`:** `- <date> — created, 1.0.0. Built at M11.`
5. **Add the catalogue entry,** and its history line.
6. **Tell the user where it is,** and walk them through "Waking" in a sentence or two.
7. Run the check above, and tick M11.

### The Manual's Line

It's in the skeleton above: **`MANUAL.md`** is this manual.
