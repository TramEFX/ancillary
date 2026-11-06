# sync.md

**path:** `modules/system_maintenance/sync.md`
**status:** optional
**serves:** Portability (P2) and Ownership (P1); the primitive's continuity

---

## 1. In Plain Words

How your Ancillary keeps one library across your devices, through a private repository that you own: it pulls before it writes, pushes after, and checks everything it pulls. A phone app that reaches the repository directly needs no sync; a computer running git does. It's optional, and nothing else depends on it.

---

## 2. The Spec

### Shape

```markdown
# Sync

**Version:** 1.0.0
**Created:** <the date it was set up>
**Last Updated:** <the date of the last change>
**Name:** @sync

---

Keeps this copy of the library and its private remote the same. It runs wherever git runs. A platform that reaches the remote through a connector reads and writes it directly, with additive writes against the version it copied, and needs no sync.

## Always

- The remote stays private, and nothing secret goes into it.
- Pull before the session's first write to the library. Push after each write.
- Never force-push and never rewrite history. Purging old history is <the name the user goes by>'s own act, never this workflow's.
- temp/ never leaves this copy (spec/file_formats.md §4.6).

## Pulling

1. **Fetch, and look before taking anything.** Every pulled change must look like a write the standard allows:
   - in an index: whole entry lines added, changed or removed, each with its history line (spec/two_indexes.md §4.1);
   - in a living manifest: only the fields an operation changed, each with its history entry (spec/living_manifest.md §4);
   - a memory: added whole, never changed;
   - doctrine, a mode, a workflow or a system manifest: its version bumped, with its history line;
   - a history file: lines added at the end, or a forget's marker.
   Anything else is shown to <the name the user goes by> before it's taken.
2. **A removal is taken only as a whole forget:** the removal, every index line and history line it touches, and the marker, together (spec/living_manifest.md §5.5). Any other removal is shown first.
3. **Nothing a forget removed comes back.** If a pulled change would restore something removed by a forget (git's own record of the forget shows what it was), hold it back. Tell <the name the user goes by> that a pull would bring back something they asked to forget, without saying what, and let them decide.
4. **Merge.**
   - A conflict where both sides only added lines, as two new index entries or two history lines, is resolved by keeping both: newest first in an index, in date order in a history file.
   - A conflict over the same fact in a living manifest is resolved from the dates and sources. When they can't settle it, ask.
   - Any other conflict is <the name the user goes by>'s call.
5. **Check what came in,** with the reference checkers where code runs. If a file already read this session changed, read it again before relying on it.

## Pushing

1. **Look at what's staged:** nothing outside the library, nothing secret, no stray file. Anything unexpected is shown, not committed.
2. **Commit each write** with a short message that names what changed. A forget's message says only "forget" and the date, never what.
3. **Push.** If the remote has moved on, pull first, then push.
```

- **Untested in v1.** No v1 Ancillary has synced yet. The rules rest on tests in the reference implementation: a plain push can't erase an entry that exists only on the remote, and phone apps can read and write a private repository. One phone write there damaged the index; the additive write (`spec/file_formats.md` §5) and one entry per line (`spec/two_indexes.md` §4) are designed to prevent that, and haven't been tested on a phone since.
- **Fixed text, apart from the names and dates.** It changes with a new version of the standard.
- **Version control comes first.** Git, the line-ending rule (`* text=auto eol=lf` in `.gitattributes`, `spec/file_formats.md` §2) and the private remote are set up at M1, where the platform can run git (`tools.spec.md`). The build follows this sheet from then on, and the file itself is written at M9.
- **The rules point here.** Where the file exists, the Ancillary reads it before the session's first write to the library (the rules' WRITING.sync). The handoff's wipe isn't one: `temp/` never syncs.
- **Why the review comes before the merge:** checkers pass a damaged file that still meets every rule they check. A comparison against what was there before catches it (`spec/file_formats.md` §7).
- **Why conflicts over added lines are resolved by hand:** two devices adding an index entry at the same time make git report a conflict, even though keeping both lines is always right. Git's union merge would keep both on its own, but where both sides changed the same line it keeps both versions too and breaks the file (tested 2026-11-05). So the Ancillary resolves these, and the rule above is all it takes.

### Must Never Contain

- **The remote's address, an account name or a token.** Git keeps the remote; the platform keeps the credentials (P2).
- **A step that force-pushes, rewrites history or purges.**
- **A particular tool's name.** Git is the standard's one named tool, because the remote is a git remote.
- **Its own change history, or a weight** (C3, C4).

### Loads

Before the session's first write to the library, wherever the file exists (the rules' WRITING.sync). When the user asks for a sync (@sync), in full. Never at wake (C11).

### Writes

- **Written at M9,** after the remote was set up at M1, with its catalogue entry (`@sync` in `tags`) and the first line of `history/sync.md`.
- **Its runs write only what they pull and merge,** and nothing of their own.
- **The fixed text changes with a new version of the standard.** That bumps the version and leaves a history line (`spec/file_formats.md` §4.3).

### Access Levels

- **Where git runs:** the Ancillary runs the sync, and nobody types a command.
- **Through a connector, as on a phone:** there's no sync. The Ancillary reads and writes the remote directly, every write additive against the version copied (`spec/file_formats.md` §5). The next sync on a computer reviews those writes.
- **Read only, or no file access:** there's no remote to keep. The user's copy is the one they hold.

### Check

- The file matches the skeleton, and no placeholder is left.
- `.gitattributes` holds the line-ending rule, and `temp/` is ignored.
- The remote is private, where the platform can tell; where it can't, the user has confirmed it.
- After each sync, this copy and the remote match, and the checkers pass.

---

## 3. To Build It

### What to Ask

At M1, only where the platform can run git:
1. **Do you want to reach your Ancillary from your phone or another computer?** That takes a private repository on a service like GitHub, under the user's own account.
2. **Is the repository private?** If the Ancillary can't create it, the user does, and it checks before the first push.

Explain the privacy point plainly: a private repository still sits on someone else's servers, and git keeps every old version of every file, including anything the Ancillary was asked to forget, until the user purges it.

### Defaults

- **Off.** No remote unless the user wants one.
- **Its catalogue entry:** weight 0.9995, category `system_maintenance`.

### What to Write, and How to Confirm It

1. At M1: set up git, the line-ending rule, the ignore rule for `temp/`, and the remote. Push the first commit.
2. At M9: write the file from the skeleton, as version 1.0.0, start `history/sync.md` (`- <date> — created, 1.0.0. Built at M9.`), and add its catalogue entry.
3. Run one sync. When this copy and the remote match, run the check above and tick it with M9.

### The Manual's Line

**`modules/system_maintenance/sync.md`** keeps your Ancillary the same on every device, through a private repository. That repository still sits on someone else's servers, and git keeps every old version, including anything you've asked your Ancillary to forget, until you purge it. It never purges for you.
