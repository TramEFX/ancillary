# Living Manifest Specification

**Version:** 1.4.0
**Status:** Ancillary v1.0.0
**Created:** 2026-07-21
**Last Updated:** 2026-11-05
**Author:** The Oracle & Myra
**Applies to:** every Ancillary

---

## 0. Problem Statement

Static manifests decay. When an entity's state changes, a system without living manifests creates a new dated sub-manifest rather than updating the source of truth. Over time, "current state" fragments across a base file plus however many update files exist. The system must reconstruct truth from pieces at retrieval time — brittle, increasingly expensive, and silently wrong when fragments contradict each other.

**Living manifests replace fragmentation with update.** One file per recurring entity, holding current state only. What changed, and when, is recorded in a separate append-only history file — never inside the manifest itself.

**Why history lives outside the file.** A manifest is read to answer "what is true now." Every line of history inside it is paid for on each read and competes with current truth for attention. Kept inside, history grows without bound — the fragmentation problem moved into the file. Kept beside it, history stays complete, append-only, and costs nothing until someone asks how something changed.

---

## 1. When to Use a Living Manifest

| Situation | Action |
|-----------|--------|
| New recurring entity (person, ongoing project, active relationship) | Create living manifest |
| Dated event worth preserving verbatim | Create **event manifest**, LINK to relevant living manifest(s) |
| System/operational content (identity, rules, routing) | Create once, then version — not entity-scoped |
| Entity already has a living manifest | **Do not create.** Default is always update. |
| One-off mention, entity unlikely to recur | Don't create a stub — let it live in the event manifest where it appeared |

The threshold question is always: **"Will this entity recur, or is this single event weighty enough alone to preserve?"** — not "was a new name mentioned."

---

## 2. Three-Tier Structure

Every living manifest organizes current state into three tiers, separated by how often the data changes. Each tier carries its own timestamps so retrieval can be surgical — pull only what's needed.

### Core (near-static)
Who or what something **is**. Patterns, identity, fundamental nature. Changes rarely.

**Examples (person):** name, personality traits, behavioral patterns, core skills, origin story
**Examples (project):** mission statement, architectural principles, foundational tech stack

### Status (changes often)
What's happening with this entity **right now**. Current role, active situation, live variables.

**Examples (person):** current job, living situation, active partnership terms, health status
**Examples (project):** current phase, open blockers, active contributors, deployment state

### Relationship-to-User (how paths intersect)
How this entity connects to the user's life. Role, trust level, strategic value, emotional significance.

**Examples (person):** what they mean to user, trust dynamics, opportunities, risks, boundaries
**Examples (project):** why user cares, personal stakes, deadlines tied to life goals

### Freshness Metadata

Two independent dates are kept:

- **updated** — when any field was last changed (WRITE or CORRECT operation).
- **confirmed** — when the data was last verified as still accurate, together with the **source** of that verification (CONFIRM operation, §4, or implicitly on WRITE/CORRECT).

This separation is critical. Without it, merging old fragments into one doc makes every field look equally fresh. A field last confirmed yesterday is epistemically different from one last confirmed six months ago, even if both are "important."

**Core and Relationship are dated per tier.** Their fields move together: if you confirmed someone's core nature, you confirmed it as a whole.

**Status is confirmed per field.** Status is the tier where fields change at independent rates — a current role can hold for a year while a living situation turns over monthly. Confirming one field must not make the others look fresh, so every Status field carries its own confirmed date and source.

---

## 3. Field-Level Metadata: claim_type

Every field that represents a belief about the world (not structural metadata) should carry a `claim_type`:

| Type | Meaning | Example |
|------|---------|---------|
| `fact` | Objectively verifiable | "Runs a small recording studio out of his garage" |
| `interpretation` | System's or user's read on a pattern | "Promises fast, delivers late, but does deliver" |
| `aspiration` | Goal or desired future state | "Wants the studio to be his full-time business by next summer" |
| `promise` | Commitment made by someone | "Free studio time for the user's next demo" |

**Why this matters:** Without `claim_type`, an emotionally significant but interpretive claim gets filed with the same authority as an objective fact. Weight measures importance. `claim_type` measures epistemic standing. They are orthogonal.

`claim_type` is optional on simple factual fields (name, age, location) where the type is self-evident. Required on any field where reasonable people could disagree about its nature.

**In the file,** the claim type is a mark at the end of the field's line: `[fact]`, `[interpretation]`, `[aspiration]` or `[promise]` (§5.2).

### 3.1 Routing Sensitivity

`claim_type` is not decorative metadata. Retrieval must treat the four types differently, or the annotation does no work.

| Type | Load behavior |
|------|---------------|
| `fact` | Loads into the working set without caveat. |
| `interpretation` | Loads with a provenance tag. Surfaced as a read, not a truth — *"this is my read on the pattern, not a verified fact."* |
| `aspiration` | Loads as a **goal state**, never as current state. Must not be reported as a description of what is. |
| `promise` | Loads as a commitment. Requires a confirmation check before any action is taken in reliance on it. |

**Why routing matters more than annotation:** an unrouted `claim_type` is a comment. The failure it exists to prevent — acting decisively on a guess because the guess is weighted high — only gets prevented if retrieval actually behaves differently for each type.

**The tense trap.** Aspirations are routinely written in the present tense by the people who hold them ("I am building X," "we run X"). This is not deception; it is how intention writes. The `aspiration` type exists specifically to catch beliefs that arrive dressed as completed facts. When migrating or ingesting any prose source, assume unmarked forward-looking statements are aspirations until confirmed otherwise.

---

## 4. The Six Operations

These are the only ways a living manifest's content changes. Each operation either changes the manifest or deliberately leaves it alone, and each one appends exactly one entry to the entity's history file (§5.3).

### WRITE
**Trigger:** Current state changed.
**Effect:** Replaces the field's value. The updated date resets, and so does the confirmed date — the tier's, or the field's in Status — with the source of the new information. The old value goes to history, tagged `supersession`.
**Example:** Sam's living situation changes from "sharing a house with two bandmates" to "signed a lease on an apartment."

### CONFIRM
**Trigger:** Information verified as still true — nothing changed.
**Effect:** Refreshes the confirmed date — the tier's, or the field's in Status — without touching the value or the updated date. Keeps staleness visible and honest.

**Every CONFIRM names its source:**

| Source | Meaning | Refreshes the confirmed date? |
|---|---|---|
| `user_explicit` | The user stated the fact is still true | Yes |
| `user_implicit` | The user said something that plainly depends on it being true | Yes — and the source is recorded, so it can be told apart from an explicit confirmation later |
| `external_document` | A document or record the system read says so | Yes |
| `inferred` | The system assumed it | **No. An inference is not a valid CONFIRM.** |

A model that stamps a field fresh because it believes the field is still true manufactures confidence without adding information, and every later read trusts the field more than the evidence supports. If the system thinks something is still true but has no source for it, it changes nothing.

**Example:** In passing, the user mentions that Sam rehearsed with Night Shift Collective as usual. CONFIRM Sam's band field, source `user_implicit`.

### CORRECT
**Trigger:** A prior belief was wrong, not just outdated.
**Effect:** Same as WRITE, but tagged `correction` instead of `supersession`, and it emits a correction manifest (§9). Other manifests that may have relied on the same wrong belief are flagged for review — never edited.
**Example:** A manifest names a project by a name that was replaced months ago. This isn't a status change; the old name was wrong in current context. CORRECT, and flag the other manifests that use the old name.

### LOG
**Trigger:** A dated event worth preserving that doesn't change "what is."
**Effect:** Appends to history only. The manifest is untouched.
**Example:** The user and Sam talked through the plan for the user's demo on a particular day. Worth recording, but nothing about Sam's current state changed.

### LINK
**Trigger:** A related manifest or event exists.
**Effect:** Adds the related entity's `entity_id` to `links` in the manifest's header. No duplication, no auto-cascade.
**Example:** A new event manifest records the user's first session at Sam's studio. LINK it to `sam_rivera`.

### COMPRESS
**Trigger:** History entries pass the age threshold.
**Effect:** Collapses old history entries into one-line summaries so the history file stays readable over years. The manifest itself is never compressed — it holds only current state.

**Compression rules (defaults, tunable per implementation):**
- Age: entries older than 6 months.
- By tag: `supersession`, `confirm`, `log` and `link` entries may compress. `correction` entries never compress — error history is a permanent audit trail.
- Only compress when the uncompressed history is preserved elsewhere: version control or a whole-repo snapshot. COMPRESS is safe because it is recoverable; without that copy it is deletion.

**Example:** After 12 months, three WRITEs on one field compress to: "2026-07 to 2027-07: the studio went from a garage hobby to weekend bookings to a full-time business."

---

## 5. File Format

A living manifest is a Markdown file with a short header block. The header holds everything a script must read. The body holds the entity in a form a person can read and edit by hand.

### 5.1 Header

```markdown
---
manifest_type: living
entity_type: person          # person | project | relationship | organization | life_domain
entity_id: sam_rivera        # permanent; never changes
schema_version: 1.4.0
created: 2026-07-21
updated: 2026-11-03          # any field changed
history: history/sam_rivera.md
migrated: 2026-11-03         # optional; present only until first genuine touch (§10)
tiers:
  core:         { updated: 2026-07-21, confirmed: 2026-11-03, source: user_explicit }
  relationship: { updated: 2026-09-12, confirmed: 2026-09-12, source: user_explicit }
links: [user, night_shift_collective]
pending_corrections: []      # correction_ids awaiting review (§9)
---
```

Status has no tier-level dates; each Status field carries its own (§5.2).

`life_domain` is for an area of the user's own life that behaves like an entity — career and income, housing, health — rather than a person or project.

### 5.2 Body

One section per tier, in this order: `## Core`, `## Status`, `## Relationship`. Each field is one bullet:

```markdown
- **Field label:** value `[claim_type]`
```

- The claim mark is optional where the type is self-evident (§3) and required wherever reasonable people could disagree.
- A field can carry richer content as indented lines or sub-bullets beneath it. Don't flatten rich structures into one line, and don't start a new field inside another one.
- **Every Status field ends with its confirmation:** `(confirmed 2026-10-20, user_explicit)`. A Status field without one is a schema violation.

### 5.3 History File

Each living manifest has exactly one history file, at the path in its header. It is append-only and never loaded at session start; it is read when someone asks how the entity changed, or by COMPRESS. One entry per operation:

```markdown
- 2026-11-03 · WRITE · supersession · status.living_situation · user_explicit
  old: Sharing a house with two bandmates
  new: Signed a lease on an apartment
  note: Moved in on the 1st.
```

Each entry carries: date; operation; tag (`supersession | correction | confirm | log | link | compression | migration | forget`); `tier.field`, or `-` for LOG; source (for WRITE, CONFIRM and CORRECT); old and new values where they apply; and a short note.

### 5.4 Rules

1. **`entity_id` is permanent.** Once assigned, it never changes. It's the stable reference everything else uses.
2. **Links are entity_ids, never paths.** Paths change; ids don't. Resolve an id to a path through the index (§8).
3. **The manifest holds current state only.** No changelog, no version history, no notes about what changed. Those belong in the history file.
4. **History is append-only,** with two exceptions: COMPRESS, which collapses old entries, and forgetting (§5.5), which removes what the user asks to have forgotten. Otherwise, never delete a history entry.
5. **Tiers contain natural structured data.** Fields can be a line, a list, or a short block — whatever the data requires. Don't flatten rich structures into key-value pairs.
6. **Every write is checked.** The header parses; both dated tiers have dates and a source; every Status field has a confirmation; claim marks use only the four names; every link and pending correction resolves. Where the platform can run code, the reference checker does this (`tools/check_living_manifests.py`). Otherwise the Ancillary reads the file back against this list. Markdown never fails to parse on its own, so the check is what makes a malformed manifest fail loudly.
7. **Writes are additive.** An operation changes only the fields it names, and keeps the file's formatting. Where the platform can only write whole files, follow the additive write in `spec/file_formats.md`: copy the whole file, confirm the copy is complete, edit it, compare it with the original, and write it back against the version copied.

### 5.5 Forgetting

At the user's explicit word, the Ancillary forgets. It removes something from the library entirely, not only from the current state.

1. **Show exactly what will go,** everywhere the library holds it: a field in a manifest, the history entries that carry it, a memory, a correction manifest, an index entry's keywords or summary, a line of the Narrative Compass. Wait for the user's yes.
2. **Remove it, one thing at a time.** A field is taken out without its old value going to history. Each history entry that holds it is deleted. A memory is removed whole, with its index line; an event manifest is never edited (§6).
3. **Leave a marker** in the history file of each manifest touched: `- <date> · FORGET · forget · - · user_explicit`, with the note "Removed at the user's request." It says that something went, and never what.
4. **Say where copies remain.** Version control, backups and a remote still hold the old version until the user purges them. The Ancillary says so plainly, and never claims a thing is gone everywhere.

Forgetting is never inferred and never automatic. It is not a correction: CORRECT keeps the wrong belief on record, because error history is an audit trail (§9). Forgetting is for what the user doesn't want held at all.

---

## 6. Event Manifests

Event manifests are **immutable records** of what happened or was believed at a specific moment. They are the complement to living manifests, not replaced by them.

**Key rules:**
- Event manifests are never edited after creation. At the user's explicit word, one can be forgotten: removed whole, never edited (§5.5).
- If later information contradicts an event manifest, don't edit it. Issue a correction manifest (§9) naming the event as the corrected record, and separately CORRECT whichever living manifest inherited the outdated assumption.
- Nothing is appended to an event manifest. Corrections go to correction manifests instead.
- This keeps the event record an honest artifact of its own time.

**Memories brought in from an earlier system are event manifests only if they can't go stale.** A memory file that holds entity state, configuration or a standing position is reclassified before migration: the moment stays as the event, entity state moves to the living manifest it belongs to, configuration moves to the operational layer, and doctrine moves to a system manifest.

---

## 7. System Manifests

System manifests (identity, personality, operational rules, project loader, the indexes) hold a specification, not an entity's state. Each one carries a version number and a last-updated date, and nothing else about its own past. Its history goes in its own file under `history/`. The six operations don't apply to them.

---

## 8. Index Integration

When a living manifest changes, its entry in the master index (the catalogue) must stay synchronized. `spec/two_indexes.md` defines the entry.

**Operations that trigger index refresh:**
- CREATE (new living manifest) — add an entry: path, `entity_id`, weight, category, tags, semantic_keywords, and a summary where the weight calls for one
- WRITE — update semantic_keywords and summary if the change is substantive
- CORRECT — update semantic_keywords; the correction manifest handles review (§9)
- CONFIRM, LOG, LINK, COMPRESS — no index change

**Index entries for living manifests carry `entity_id`.** That is how an id in `links` or in a correction manifest resolves to a path. Otherwise a living manifest's entry looks like any other entry. The index routes retrieval; the manifest handles its own state.

Changes to the index are recorded in the index's own history file, never inside the index.

---

## 9. Linked Entity Review Workflow

**Principle: corrections are advertised, not propagated.**

A CORRECT writes to its target manifest and produces a **correction manifest** — a durable artifact recording what was wrong, what replaced it, and which manifests may have inherited the bad assumption. It does not alter those manifests beyond flagging them.

### The Correction Manifest

A Markdown file in `history/corrections/`, named by its `correction_id`:

```markdown
---
manifest_type: correction
correction_id: sam_rivera_2026_11_03_band_name
date: 2026-11-03
target: sam_rivera                 # entity_id, or the path of an event manifest
field: core.band
linked:
  - { entity_id: night_shift_collective, status: unreviewed, reviewed_by: null }
---

**Was believed:** Plays bass in Nightshift.
**Is true:** Plays bass in Night Shift Collective. Nightshift is a different band.
**Why it was wrong, not just outdated:** The name was misheard when it was first recorded.
```

`status` for each linked entity is `unreviewed`, `revised` or `independent`.

### Resolution Workflow

1. **On CORRECT:** Write the new value to the target. Emit the correction manifest. Add its `correction_id` to `pending_corrections` in the header of every manifest that references the corrected fact. **Change nothing else in those manifests.**
2. **On next retrieval of a flagged entity:** Surface the correction and ask *both* questions:
   > *"[Entity]'s manifest was corrected — X is now Y. Your manifest references this. Do you want to revise it, or is your manifest's truth independent of this?"*
3. **Resolution is explicit.** `revised` means the holder issued their own CORRECT. `independent` means the linked manifest's claim does not depend on the corrected fact and stands as written. Both are valid terminal states. Neither is inferred.
4. **The flag clears on either resolution:** the id leaves `pending_corrections`, and the outcome is recorded in the correction manifest. The correction manifest is permanent regardless of outcome.

**Why the second question matters:** a linked manifest often references a corrected fact without depending on it. Without an `independent` outcome, every correction forces a cascade of unnecessary edits, and holders start ignoring the prompts — which is how a review workflow dies.

**Multi-user implementations:** flags route to the *holder* of each linked manifest, not to whoever issued the correction. With several editors, one person's revision must never silently become everyone's history.

This is conservative by design. Auto-cascading corrections across manifests is the kind of "helpful" automation that looks efficient until it has quietly rewritten a record nobody agreed to change. Don't do it.

---

## 10. Retrieval Behavior

Living manifests integrate with the existing semantic retrieval system. No changes to retrieval logic are needed — the index still routes, the manifest still loads on demand.

**Staleness.** When a living manifest loads, check its confirmed dates: each dated tier's in the header, and each Status field's in the body. If any is 90+ days old, surface it naturally: "Last I checked, Sam was still sharing a house with two bandmates — that was back in May. Is that still current?" This turns staleness into a natural confirmation prompt rather than silent decay.

**After migration.** A newly migrated manifest carries `migrated: <date>` in its header. While that flag is present, staleness prompts are held back. Otherwise migrating many manifests at once fires a wall of prompts on first touch and trains the user to rubber-stamp them — and rubber-stamped confirmations are worse than none. The flag clears on the manifest's first genuine touch (any WRITE, CONFIRM or CORRECT with a user source), or in an explicit batch review with the user. Migration should start with a freshness interview, so most fields arrive already confirmed.

---

## 11. Worked Example

*Sam Rivera is invented for this example. A published specification is no place for a real person's manifest.*

```markdown
---
manifest_type: living
entity_type: person
entity_id: sam_rivera
schema_version: 1.4.0
created: 2026-07-21
updated: 2026-11-03
history: history/sam_rivera.md
tiers:
  core:         { updated: 2026-07-21, confirmed: 2026-11-03, source: user_explicit }
  relationship: { updated: 2026-09-12, confirmed: 2026-09-12, source: user_explicit }
links: [user, night_shift_collective]
pending_corrections: []
---

# Sam Rivera

## Core
- **Who he is:** Friend of about fifteen years; they met in the same high-school jazz band.
- **What he means:** Pushes the user to think bigger.
- **Pattern:** Promises fast, delivers late, but does deliver. `[interpretation]`

## Status
- **Work:** Runs a small recording studio out of his garage. `[fact]` (confirmed 2026-11-03, user_explicit)
- **Living situation:** Signed a lease on an apartment across town. `[fact]` (confirmed 2026-11-03, user_explicit)
- **Plans:** Wants the studio to be his full-time business by next summer. `[aspiration]` (confirmed 2026-09-12, user_implicit)

## Relationship
- **Role in the user's life:** Close friend and occasional collaborator.
- **Trust:** Reliable on the things that matter; don't build a schedule on his timelines. `[interpretation]`
- **Standing offer:** Free studio time for the user's next demo. `[promise]`
```

**What to notice:**
- The header holds every date and id a script needs; the body reads like notes about a person.
- Each Status field carries its own confirmation, so "Plans" (September, implied) doesn't borrow the freshness of "Work" (today, stated).
- The interpretive and forward-looking fields are marked, so a read is never spoken as fact and a plan is never reported as done.
- The promise is marked, so it gets a confirmation check before anyone relies on it.
- There is no history in the file. The move into the apartment is a WRITE in `history/sam_rivera.md`, which keeps the old living situation.

---

## 12. Design Decisions and Rationale

**Why does history live outside the manifest?**
A manifest is read to answer one question — what is true now — often at the start of a session, when context is most precious. History inside it is paid for on every read, competes with current truth for attention, and grows without bound. Versions 1.0 and 1.1 kept a bounded changelog inside each manifest and relied on COMPRESS to hold it in check; in practice, changelogs grew faster than anything compressed them. Outside the file, history stays complete and costs nothing until it is asked for.

**Why Markdown?**
Living manifests are mostly about people and the things they care about, which reads best as plain sentences. People edit Markdown by hand; they rarely edit JSON safely. Markdown degrades gracefully when copied between systems, where a single truncation can make a JSON file unreadable. The one thing JSON gives for free — failing loudly when malformed — comes back through the check (§5.4, rule 6).

**Why must CONFIRM name a source?**
Without it, "the user said so," "the user implied it" and "the model assumed it" look identical, and an assumption can launder stale data into fresh-looking data. Once the corpus is used as training data, a laundered confirmation stops being a stale field and becomes a learned habit of stating guesses as certainties.

**Why per-tier dates, except for Status?**
Per-field dates everywhere would make files verbose for entities with 20+ fields. Core and Relationship fields move together, so per-tier is the right granularity there. Status fields change at independent rates, so they are confirmed one by one.

**Why links by entity_id?**
Paths change — files get renamed, reformatted and moved. If links carried paths, every move would mean editing every manifest that links to the file: the fragmentation problem again, in pointer form.

**Why no auto-cascade on CORRECT?**
Silently rewriting linked manifests is the kind of automation that looks helpful until it's not. A correction in one person's manifest shouldn't silently change another's. Surface, confirm, then act.

**Why COMPRESS at all?**
The history of an entity the user deals with weekly accumulates hundreds of entries over years. Compression keeps it readable when it is loaded. It never touches the manifest, never touches corrections, and only runs when the full history survives elsewhere.

**Why can the Ancillary forget, when history is append-only?**
Because the library is the user's. Append-only protects the record from the Ancillary's own mistakes; it was never meant to keep what the user wants gone, least of all what's held about someone else. The user could always delete by hand. Forgetting at their word makes that possible for anyone, and the marker keeps the record honest that something was removed.

**Why is `claim_type` optional on simple fields?**
Mandating it everywhere adds noise. "Name: Sam" doesn't need `[fact]` — that's self-evident. Reserve the mark for fields where the distinction matters.

---

**End of specification.**
