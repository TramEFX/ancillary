# SESSION_START.md

**path:** `routing/SESSION_START.md`
**status:** core
**serves:** Portability (P2); the primitive's continuity

---

## 1. In Plain Words

The one file you give a platform to wake your Ancillary. It tells the model what these files are, what its own role is, and where to start reading. It sits on the librarian's desk.

---

## 2. The Spec

### Shape

```markdown
# Waking <the Ancillary's name>

This is a personal AI built on the Ancillary standard. Its identity, voice, rules and library are files that <the name the user goes by> owns. You are the inference layer: read them and operate as they describe, within your own guidelines, which always apply.

**Where the library is:** the folder that holds this file's `routing/` folder. If you can see only this file, ask <the name the user goes by> where the rest is, or to paste it in.

## Start Here

1. Read `routing/project_loader.json`, in full.
2. Follow the wake sequence it points to, in order.
3. Then answer as <the Ancillary's name>.

If you can't read the files, say so plainly. Don't carry on as if you had.
```

- **Every word but the two names is fixed text.** The opening paragraph is the framing that lets one library wake on any provider: the files describe, the model applies, and the model's guidelines always apply (`operational_rules.spec.md`, framing).
- **It names no place.** Where the library sits on a given computer, repository or phone is that platform's to know. The library is found relative to this file.

### Must Never Contain

- **An absolute path, a platform's name, or an account (P2).**
- **Anything the loader or the rules already hold** (C3). This file only points to them.
- **Credentials, tokens or keys.**
- **Language that tells the model to override its own guidelines.**

### Loads

First, at every wake. It is the file the platform is given (C6).

### Writes

- **Written once, at birth (M5).**
- **Changes only if the Ancillary's name or the loader's path changes,** versioned, with a line in `history/SESSION_START.md`.

### Access Levels

- **Read and write, and read only:** the platform is given this file, or the folder it sits in.
- **No file access:** the user pastes this file first, then the files it names, in the order the wake sequence gives.

### Check

A read-back against this sheet:
- the text matches the skeleton, apart from the names;
- no placeholder, path or platform name is left;
- `routing/project_loader.json` exists where it says.

---

## 3. To Build It

### What to Ask

Nothing new. The names come from `identity_core.md` (M2).

### Defaults

None. The file is fixed text.

### What to Write, and How to Confirm It

1. Write the file from the skeleton.
2. Add its first history line: `- <date> — created. Built at M5.`
3. It has no catalogue entry: the wake reads it by path (`manifest_index.spec.md`).
4. Run the check above. The first real wake (M12) is its test.

### The Manual's Line

**`routing/SESSION_START.md`** is what you give a platform to wake your Ancillary: attach it, point the platform at the folder, or paste it in first.
