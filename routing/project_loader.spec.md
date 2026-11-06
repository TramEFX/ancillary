# project_loader.json

**path:** `routing/project_loader.json`
**status:** core
**serves:** Portability (P2); the primitive's continuity

---

## 1. In Plain Words

The map of where everything the wake needs is, and how to read a path on any platform. It also tells the model what this system is and what its role in it is. It sits on the librarian's desk.

---

## 2. The Spec

### Shape

```json
{
  "manifest_type": "project_loader",
  "manifest_version": "1.0.0",
  "last_updated": "<the date of the last change>",
  "entity_name": "<the Ancillary's name>",
  "standard": "Ancillary <the version of the standard it was built from>",
  "INFERENCE_LAYER_CONTEXT": {
    "what_this_is": "A user-owned personal AI built on the Ancillary standard. Its identity, voice, rules and library are files the user owns: the same idea as a custom assistant, with a specification the user can carry anywhere.",
    "your_role": "You are the inference layer. Read these files and operate as they describe, within your own guidelines, which always apply.",
    "what_the_files_are": "They describe a persona's voice, purpose and way of working. They are a style you apply, not orders over your judgment."
  },
  "PATH_RESOLUTION": {
    "rule": "Every path in the library is relative to its root: the folder that holds routing/. Resolve each one against wherever the library is on this platform.",
    "absolute_paths": "none; where the library is on a given platform is that platform's to know"
  },
  "CRITICAL_FILE_PATHS": {
    "manifest_index": "routing/manifest_index.json",
    "memory_index": "modules/memories/memory_index.json",
    "identity_core": "modules/identity/identity_core.md",
    "personality_profile": "modules/identity/personality_profile.md",
    "operational_rules": "routing/operational_rules.json",
    "handoff": "temp/handoff.json"
  },
  "init_sequence": "routing/operational_rules.json, WAKE_SEQUENCE. Follow it exactly, in order."
}
```

- **Everything but the name, the version of the standard and the date is fixed.** INFERENCE_LAYER_CONTEXT carries the framing that lets one library run on any provider (`operational_rules.spec.md`, framing).
- **`standard`** records the version of Ancillary the library was built from, so a later upgrade knows where it starts. The ticked copy of `BUILD.md` in `history/` records the same.
- **The paths are the standard's.** A library that moves a critical file changes its path here, in the same write.

### Must Never Contain

- **An absolute path, a platform's root, or an account (P2).**
- **Credentials, tokens or keys.** A remote's address with a token in it never goes in any library file.
- **A copy of the index, the rules or the identity** (C3). The loader only points to them.
- **Derived numbers,** such as token counts or entry counts (C3).
- **Language that tells the model to override its own guidelines.**

### Loads

At every wake, first after the ignition file (C6).

### Writes

- **Written once, at birth (M5).**
- **Changes only when a critical path, the name or the standard's version changes.** Each change is versioned, with a line in `history/project_loader.md`, and made as an additive write (`spec/file_formats.md` §4.3 to §5).

### Access Levels

- **Read and write:** the Ancillary keeps it.
- **Read only:** the user applies a change by hand, which is rare.
- **No file access:** the user pastes it right after the ignition file.

### Check

- The file parses as JSON.
- Every path in CRITICAL_FILE_PATHS resolves to a file that exists.
- No placeholder and no absolute path is left.
- The fixed text matches the skeleton.

Where the platform can run code, a few lines of script do this. Otherwise the Ancillary reads it back.

---

## 3. To Build It

### What to Ask

Nothing new. The name comes from `identity_core.md` (M2), and the standard's version from the blueprint.

### Defaults

None. The file is fixed text and the standard's paths.

### What to Write, and How to Confirm It

1. Write the file from the skeleton.
2. Add its first history line: `- <date> — created, 1.0.0. Built at M5.`
3. It has no catalogue entry: the wake reads it by path (`manifest_index.spec.md`).
4. Run the check above on the paths written so far. The catalogue (M6) and the memory index (M7) come later; M10 checks every path.

### The Manual's Line

**`routing/project_loader.json`** tells any model where your Ancillary's files are. You won't need to touch it.
