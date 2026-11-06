# audit.md

**path:** `modules/system_maintenance/audit.md`
**status:** core
**serves:** Curation (P5) and Legibility (P3); the primitive's connectivity

---

## 1. In Plain Words

The checkup your Ancillary runs on its own library: is every file where the catalogue says, are the maps honest, and is the wake still small. It finds and reports first, and fixes nothing without your yes, one thing at a time. It runs when you ask for it.

---

## 2. The Spec

### Shape

```markdown
# Audit

**Version:** 1.0.0
**Created:** <the date of the build>
**Last Updated:** <the date of the last change>
**Name:** @audit

---

Checks that the library is whole, its maps are honest, and the wake is still small. It runs when <the name the user goes by> asks for it, in any words. Suggest one after a heavy session, or when something seems wrong; never start one unasked. It runs best at the start of a fresh session: say so once, then go on.

## 1. Look

Nothing changes in this part.

1. **Walk the library.** List every file and folder. `history/`, `modules/archive/`, `tools/`, the handoff, and version control's own files are never findings.
2. **Hold both indexes against the files** (spec/two_indexes.md §4, §7). Find:
   - every entry whose file is missing;
   - every file that should have an entry and has none: everything but the ignition file, the loader, the two indexes and what step 1 leaves out;
   - a memory in the catalogue, or anything but a memory in the memory index;
   - an entry that breaks spec/two_indexes.md §4.4.
   An external entry whose source isn't on this platform is reported, not a finding.
3. **Check the weights** (C15, C16). In each index, at most 15% of the entries are in the top tier, or the override is in its history. The Eternal set is within its cap. Report how the entries spread across the bands, because weight drifts upward (spec/two_indexes.md §11.1).
4. **Check the living manifests** against spec/living_manifest.md §5.4, rule 6: every link and pending correction resolves. List the ones with a confirmation 90 days old or more, unless they carry the migrated flag.
5. **Check the composition.** If one category holds about half of an index's entries, a split is proposed, with its numbers (C17).
6. **Measure the wake** (C21): the size of the files the wake reads, against the smallest surface <the name the user goes by> runs it on.
7. **Look in temp/.** Anything but the handoff is left over.

Where the platform can run code, the reference checkers do steps 3 and 4, and a few lines of script do step 2. Otherwise, read them back.

## 2. Report, and Wait

Write the findings: each problem, the fix proposed for it, and the wake's size. Then stop until <the name the user goes by> has read them.

## 3. Fix, One at a Time

Propose each fix and wait for a yes before making it. Never batch them. Each fix is an additive write with its history line (spec/file_formats.md §5).

## 4. Record

Add one line to history/audit.md: the date, the findings, what was fixed, and the wake's size. Where version control is set up, commit the audit as one commit.
```

- **Fixed text, apart from the names and dates.** It changes with a new version of the standard, not by the Ancillary's own judgment.
- **Every fix is gated.** The only writes the audit makes on its own are its record and its commit. Even what's left over in `temp/` is cleared on a yes, so a weak model's misreading can't remove a file.
- **The record goes in the audit's own history file,** beside the lines for changes to the audit itself. A run's line is `- <date> — run: <the findings, in a few words>; fixed <what was fixed>; wake <its size>.`
- **The wake's size** is the total size of the wake files in bytes, by script where code runs, or from the platform's report of each file's size. A quarter of the byte count is a fair estimate of tokens. Each run's line makes the wake's growth visible against the library's own.

### Must Never Contain

- **A fix made without the user's yes.**
- **Findings about the archive, `history/` or `tools/`** (`spec/file_formats.md` §4.5).
- **A step that writes a count, a hierarchy or other derived numbers into an index** (C3). The report holds them.
- **A particular tool's name, or one platform's paths** (P2).
- **Credentials, tokens or keys.**

### Loads

On demand, in full, when the user asks for an audit (the rules' MODES.at_names). Never at wake.

### Writes

- **Written once, at birth (M9).** Its catalogue entry, with `@audit` in `tags`, is added at M9 (`manifest_index.spec.md`).
- **Each run** writes only the fixes the user approves, its record line, and its commit.
- **The fixed text changes with a new version of the standard** (an upgrade). That bumps the version and leaves a history line (`spec/file_formats.md` §4.3).

### Access Levels

- **Read and write (the baseline):** the Ancillary runs the whole audit.
- **Read only:** the Ancillary runs the look and the report, and hands back each fix for the user to apply.
- **No file access:** the user pastes in both indexes and the files they want checked. The Ancillary reports on what it was given, and says what it couldn't see.

### Check

- The file matches the skeleton, and no placeholder is left.
- Every spec and C-rule it points to is in the Ancillary's `spec/`.
- Its catalogue entry carries `@audit`.

Where the platform can run code, a few lines of script do this. Otherwise the Ancillary reads it back.

---

## 3. To Build It

### What to Ask

1. **What's the smallest place you'll run your Ancillary?** For example, a phone app. The wake is measured against it.

### Defaults

- **The smallest surface:** the platform the build runs on.
- **Its catalogue entry:** weight 0.9995, category `system_maintenance`.

### What to Write, and How to Confirm It

1. Write the file from the skeleton, as version 1.0.0.
2. Start `history/audit.md`: `- <date> — created, 1.0.0. Built at M9.`
3. Add its catalogue entry and that history line.
4. Run the audit's look once, as its first run, and record it. That first wake measurement is the line the library grows from.
5. Run the check above and tick M9.

### The Manual's Line

**`modules/system_maintenance/audit.md`** is your Ancillary's checkup. Ask for an audit after a busy stretch, or whenever something seems off. It reports first and changes nothing without your yes.
