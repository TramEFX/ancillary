# tools/

**path:** `tools/`
**status:** optional (above the baseline)
**serves:** Legibility (P3) and Curation (P5); the primitive's continuity

---

## 1. In Plain Words

Two short scripts that check your Ancillary's files, and version control, which keeps every past version as a backup and an undo. They need a platform that can run code, so nothing depends on them: where they can run, your Ancillary runs them itself, and where they can't, it reads each file back against its sheet. You never install anything or type a command.

---

## 2. The Spec

### Shape

The blueprint's `tools/` folder, copied whole at M1, and only where the platform can run code.

| Script | What it checks |
|---|---|
| `check_living_manifests.py` | Every living manifest against `spec/living_manifest.md` §5.4, rule 6: the header parses; both dated tiers have dates and a source; every Status field has its confirmation; claim marks use only the four names; every link and pending correction resolves. Also its history file exists, its three tier sections are there in order (§5.2), and its catalogue entry carries its `entity_id` (§8). It lists every confirmation 90 days old or more, unless the manifest is flagged migrated (§10). |
| `check_index_weights.py` | Both indexes: every weight from 0.99 to 0.9999; at most 15% of each index's entries in the top tier, apart from any the index's history records as the user's override (C15, `spec/file_formats.md` §4.4); the Eternal set only in the memory index, within the cap the operational rules set, and every member with a summary (C16). It reports how each index spreads across the weight bands the rules name. |

- **Reference code.** It's Python, standard library only, short enough to read.
- **The sheets are the authority.** The code adds no rule of its own. Where it and a sheet disagree, the sheet wins, and the code is what gets fixed.
- **It reads its numbers from the library,** such as the Eternal cap from the operational rules, rather than holding its own.
- **What the scripts don't cover** (paths that exist, keyword counts, one entry per line, the forget marker) is a few lines of script, or a read-back, as each sheet's check says. The build's own checks at M10 fold into these two.

**Version control** is optional too, and set up at M1 where the platform can run git:

- **A backup and an undo, never the record.** `history/` is the record, and git is never a check at wake.
- **Set up with two rules:** `* text=auto eol=lf` in `.gitattributes` (`spec/file_formats.md` §2), and `temp/` ignored (§4.6).
- **Every change is committed,** with a short message naming what changed. A forget's message says only "forget" and the date.
- **Pushing:** only when the user says to. Where the user has a remote, the sync pushes after each write instead (`system_maintenance/sync.spec.md`).
- **Git keeps every old version,** including anything the user later asks to forget. The user is told once at setup, and again at every forget (`spec/living_manifest.md` §5.5).

### Must Never Contain

- **A rule the sheets don't hold.**
- **Anything outside the standard library,** or an install step.
- **The user's data, paths or credentials (P2).** The tools are the same in every Ancillary.
- **A step that force-pushes or rewrites history.**

### Loads

Never at wake. The Ancillary runs a checker after each write the checker covers, at every audit, and at M10.

### Writes

- **Copied whole at M1,** with the first line of `history/tools.md`: `- <date> — copied, version <the standard's version>. Built at M1.`
- **Replaced whole by an upgrade of the standard,** and recorded the same way.
- **Never edited by the Ancillary.** A checker that seems wrong is reported to the user, and its sheet is followed.

### Access Levels

- **Where code runs:** the Ancillary runs the checkers and reports in plain words. It runs git, where the user wants version control.
- **The baseline without code** (a filesystem connector in a chat app): no tools. Every check is a read-back, and M1 says nothing about tools.
- **Read only, or no file access:** no tools.

### Check

- The copy matches the blueprint's `tools/`, file for file.
- Both scripts run on the library as built at M10, and pass.
- Where version control is set up: both rules are in place, and the working copy is clean after each commit.

---

## 3. To Build It

### What to Ask

Only where the platform can run code, at M1. The checkers need no question: the Ancillary simply uses them.
1. **Do you want version control?** It keeps every version of every file, as a backup and an undo.
2. **Do you want to reach your Ancillary from your phone or another computer?** If yes, see `system_maintenance/sync.spec.md`.

### Defaults

- **The checkers:** copied wherever code runs.
- **Version control:** offered, and set up on the user's yes.
- **A remote:** none.

### What to Write, and How to Confirm It

1. Copy `tools/` whole, and start `history/tools.md`.
2. On a yes to version control: set up git with both rules, and make the first commit.
3. On a yes to a remote: follow `system_maintenance/sync.spec.md` for M1.
4. At M10, run both checkers over the whole library.

### The Manual's Line

In the section for power users: **`tools/`** holds two checkers your Ancillary runs on its own files. If you chose version control, it keeps every past version as a backup. You never need to run anything yourself.
