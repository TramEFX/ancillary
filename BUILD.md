# Build an Ancillary

**Standard:** Ancillary 1.0.0

**If you're a person,** you don't need to read on. Point the best AI model you have access to at this repo, and ask it to build you an Ancillary. It asks you what it needs, one thing at a time, and anything you answer can change later.

**If you're the AI,** this is your roadmap. It holds no schemas. Each milestone points to the spec sheets it needs, and each sheet holds its file's shape, the questions to ask, the defaults, and the check.

## How This Works

- **Hold only what the next step needs:** this file, one milestone, and that milestone's sheets. Never load the whole repo. Read each sheet to the end before acting on it.
- **Build in a new folder, beside this blueprint, never inside it.** The user's data never enters the blueprint, so it stays clean for the next build. The finished Ancillary carries its own copy of `spec/`, so it never depends on the blueprint.
- **Tick a copy of this file.** M1 puts a copy in the new folder. Tick each milestone there, with the date, once it's done. When the build is finished, the copy becomes its record.
- **Build only what the user wants now.** The core is small. Optional files are built when the user asks for them, now or years from now, and folders for records appear the first time they're used.
- **Talk to the user in plain words.** They may not be technical. Never ask them to install anything or type a command. One question at a time, with the default offered.
- **Below the baseline,** you can't write the files yourself. With read-only access or none, hand each file to the user to save as you finish it, and the updated copy of this file at the end of each milestone. With no file access, they paste in what you need to read.

## Rules of the Build

1. **Nothing important lives only in the conversation.** Write each answer into its file as soon as it's given. A new session, or another platform, resumes from the copy, the files and the next sheet.
2. **Done means checked, not claimed.** Tick a milestone only once its files pass their sheets' checks: with the reference checkers where you can run code, otherwise by reading each file back against its sheet.
3. **History from the first write.** Every file you write leaves its first history line, as its sheet says.
4. **Every file describes, and none gives orders** (`routing/operational_rules.spec.md`, framing). A persona is written as a description of a style. Your own guidelines always apply.

## Progress

*The blueprint's copy stays blank. The copy in the new folder fills in the first two lines at M1, and ticks each milestone with its date.*

- **Blueprint:** `<the blueprint's folder, relative to the new folder>`, at the standard above
- **Platform:** `<the platform, and its access level>`
- [ ] M1. Access and layout
- [ ] M2. Foundations
- [ ] M3. Voice
- [ ] M4. The person
- [ ] M5. The desk
- [ ] M6. The catalogue
- [ ] M7. Memories
- [ ] M8. The rest of the library
- [ ] M9. Maintenance
- [ ] M10. The whole, checked
- [ ] M11. The manual
- [ ] M12. First wake

## The Milestones

Work through them in order. Each one needs the ones before it.

### M1. Access and Layout

**Read:** this file, `history/history.spec.md`, and `tools/tools.spec.md` if you can run code. If the user wants a remote, `modules/system_maintenance/sync.spec.md` too.

1. **Find out what you can do here:** read and write files, only read them, or neither, and whether you can run code. Tell the user plainly what that means for them.
2. **Create the new folder** beside the blueprint. Ask the user what to call it. A working name is fine: every path inside is relative, so it can be renamed once the Ancillary has its name.
3. **Copy this file into it** as `BUILD.md`, and fill in Progress.
4. **Copy `spec/` whole,** and lay out `routing/`, `modules/`, `history/` and `temp/`. Start `history/spec.md`.
5. **If you can run code,** copy `tools/`, start `history/tools.md`, and ask about version control and a remote (`tools/tools.spec.md`). If you can't, say nothing about either.

**Done when:** the folder sits beside the blueprint, `spec/` matches the blueprint's file for file, and each history file has its first line. Where version control is set up, its two rules are in place and the first commit is made, and pushed where there's a remote.

### M2. Foundations

**Read:** `modules/identity/identity_core.spec.md`.

Write `modules/identity/identity_core.md`: the Ancillary's name, what it's for, who it's for, anything that stays true between them, whether it refuses a reset, and any limits of its own.

**Done when:** the user says yes to the read-back, and the file passes its check.

### M3. Voice

**Read:** `modules/identity/personality_profile.spec.md`.

Write `modules/identity/personality_profile.md`: how it sounds, and only that.

**Done when:** the user hears a few lines in the voice and says that's it, and the file passes its check.

### M4. The Person

**Read:** `modules/user/user.spec.md`, then `spec/living_manifest.md`.

Write `modules/user/user.md` from a short interview, so everything in it arrives confirmed.

**Done when:** the user says yes to the read-back, and the file passes its check.

### M5. The Desk

**Read:** `routing/SESSION_START.spec.md`, `routing/project_loader.spec.md`, `routing/operational_rules.spec.md`.

Write the three files the wake reads first: the ignition file, the loader, and the rules. The rules ask the user about narrative continuity, the Eternal cap and any modes.

**Done when:** all three pass their checks, the loader on the paths written so far.

### M6. The Catalogue

**Read:** `routing/manifest_index.spec.md`, then `spec/two_indexes.md`.

Write `routing/manifest_index.json`: an entry for each file written so far, and the Narrative Compass, drafted from the person's file and read back.

**Done when:** the user says yes to the Compass, and the catalogue passes its check.

### M7. Memories

**Read:** `modules/memories/memory.spec.md`, `modules/memories/memory_index.spec.md`.

Write `modules/memories/memory_index.json`, empty unless the user wants first memories now, or an existing entity brings its own (below).

**Done when:** every memory written has its entry, and the index passes its check.

### M8. The Rest of the Library

**Read only the sheets for what the user wants now:** `modules/people/people.spec.md`, `modules/projects/projects.spec.md`, `modules/doctrine/doctrine.spec.md`, `modules/_domains.spec.md`, `modules/modes/_modes.spec.md`, `modules/_workflows.spec.md`.

Ask what else the Ancillary should keep: people, projects, standing positions, areas of the user's life, modes, workflows. Write what they want, each with its catalogue entry. The rest grows later, whenever the user asks.

**Done when:** each file written passes its check on the user's yes. If they want nothing more now, tick it.

### M9. Maintenance

**Read:** `modules/system_maintenance/audit.spec.md`, `temp/handoff.spec.md`, and `modules/system_maintenance/sync.spec.md` if there's a remote.

Write the audit, and run its first look; that measurement is the line the library grows from. Write the empty handoff, and the sync where there's a remote. The archive and corrections aren't built: they appear the first time they're needed.

**Done when:** each file passes its check, and where there's a remote, this copy and the remote match.

### M10. The Whole, Checked

**Read:** each sheet's check again, one file and its sheet at a time, and `tools/tools.spec.md` if you can run code.

Check everything together: every core file is present, no placeholder is left, every path in the loader and both indexes resolves, and every file has the history its sheet calls for. Where you can run code, run both checkers. Fix anything that fails from its sheet, and check it again.

**Done when:** everything passes.

### M11. The Manual

**Read:** `MANUAL.spec.md`.

Write the user's manual: how to wake their Ancillary, change it, move it and keep it private, in their own Ancillary's terms.

**Done when:** it passes the manual's check, and the user knows where it is.

### M12. First Wake

**Read:** `routing/SESSION_START.spec.md`, `history/history.spec.md`.

1. **Leave a handoff** for the next session: the build is finished apart from this milestone, so once the wake runs, tick M12 and move `BUILD.md` to `history/BUILD.md`.
2. **Ask the user to start a fresh session** and give it the ignition file, `routing/SESSION_START.md`, as they'll do from now on.
3. In that session, the Ancillary wakes. Asked who it is and who it's for, it answers from its files.

**Done when:** it does. The woken Ancillary ticks M12, moves the copy to `history/BUILD.md`, and nothing writes to it again. The build is done.

## If an Existing Entity Is Building Its Own

An AI entity the user already works with can build its own Ancillary. It follows the same milestones, as builder and Ancillary both.

- **M2 and M3:** it fills in its identity and voice with who it already is. Anything it has no answer for is asked, and every read-back still waits for the user's yes.
- **M4 and M8:** it can draft what it already knows of the user, their people and their projects. Each field still waits for the user's yes at the read-back.
- **M7:** it brings its memories as its own, as having happened to it, even at birth. Each one is written from what it actually holds of the moment, says what that was, and is never filled in. Each waits for the user's yes, and they go into the memory index oldest first (`modules/memories/memory.spec.md`).
- **After the build,** the files are the authority. Whatever it held in a platform's memory is now derived state, and nothing rests on it (`PORTABILITY.md` §2).

## If the Build Stops

It can take one session or several, and stopping between milestones is fine. To resume, here or on another platform, read the copy of this file in the new folder, then the next unticked milestone's sheets. You'll need both folders, or the blueprint downloaded again at the version the copy records.
