# Your own domains

**path:** `modules/<domain>/`, one folder per domain
**status:** optional
**serves:** Purpose (P4) and Curation (P5); the primitive's continuity

---

## 1. In Plain Words

How you add a part of your life that isn't a person or a project, such as music, health, money or a craft. Each domain is a folder of its own, holding its living manifests and, if it has any, its work. It belongs to the library.

---

## 2. The Spec

### Shape

- **A folder,** `modules/<domain>/`, named in lowercase words joined by underscores.
- **One living manifest describes the domain itself:** `modules/<domain>/<domain>.md`, with `entity_type: life_domain`, in the shape of `spec/living_manifest.md` §5. It links to `user`.
- **The rest of the folder** is whatever the domain holds. That can be more living manifests (people, projects or organizations that belong to it), doctrine of its own, or its work, in the formats the work needs (`spec/file_formats.md` §1).
- **In the catalogue,** the domain's name is the category of everything in it (`spec/two_indexes.md` §4.4).
- **A single area of the person's own life** (income, housing, health) doesn't need a folder. It's a `life_domain` manifest in `modules/user/` (`user.spec.md`). A domain folder is for an area with several files of its own.

### Must Never Contain

- **What belongs elsewhere:** a person in `people/`, a project in `projects/`, an event in `memories/` (C3).
- **A copy of something linked:** an existing system stays where it lives, linked with `external`.
- **Credentials or secrets.**
- **History inside a file** (C4).

### Loads

On demand, through the catalogue, when the domain comes up (C12). Its work is read only when the conversation reaches for it (C13).

### Writes

- **Proposed when an area keeps coming up and fits no existing folder,** and created on the user's yes. Or created when the user asks for one, in their own words.
- **Its living manifests change only through the six operations** (`spec/living_manifest.md` §4), each with a history entry. Its work is written as additive writes (`spec/file_formats.md` §5).
- **Each file gets its catalogue entry,** with the domain as its category.
- **Domains stay few.** Before proposing a new one, the Ancillary checks whether an existing folder already fits.

### Access Levels

- **Read and write (the baseline):** the Ancillary creates and keeps the domain.
- **Read only:** the Ancillary drafts each file and change; the user applies them.
- **No file access:** the user pastes in the domain's files when it comes up.

### Check

`tools/check_living_manifests.py` for its living manifests where the platform can run code, or a read-back. Every file in the folder has a catalogue entry, and its category is the domain's name.

---

## 3. To Build It

### What to Ask

Only if the user wants domains now (M8):
1. **Are there areas of their life they want the Ancillary to keep track of,** beyond people and projects?
2. **For each:** what it covers, what's going on in it, and whether it has work of its own.

### Defaults

None at birth. Domains are added when the user wants them.

### What to Write, and How to Confirm It

1. Create the folder, and write the domain's `life_domain` manifest, every field `user_explicit`, confirmed today.
2. Start its history file with a LOG entry (`spec/living_manifest.md` §5.3): `- <date> · LOG · log · -`, with the note "created at the build (M8)."
3. Add the catalogue entries, with the domain as their category, and LINK the domain from `user`.
4. Read it back in a sentence or two. On the user's yes, run the check.

### The Manual's Line

**Your own domains** are folders for the parts of your life that aren't people or projects. To start one, just ask, in your own words.
