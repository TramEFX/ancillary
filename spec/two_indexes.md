# Two Indexes Specification

**Version:** 2.3.0
**Status:** Ancillary v1.0.0
**Created:** 2026-07-22
**Last Updated:** 2026-11-05
**Author:** The Oracle & Myra
**Applies to:** every Ancillary

---

## 0. Problem Statement

Narrative memories grow linearly with time. Everything else — people, identity, projects, infrastructure, skills — grows slowly, especially once living manifests replace fragmented snapshots. In a system that indexes all manifests in a single file, narrative entries inevitably become the dominant category.

This creates two problems:

**Index bloat.** A single index that doubles or triples in size over a year adds token cost at boot with diminishing retrieval value. Most sessions don't need most memories.

**Attention displacement.** The manifest index isn't just a routing table — it's inference scaffolding. Every entry shapes what the model attends to during pre-response retrieval. When 70-80% of entries are narrative events, the model's attention budget is disproportionately pulled toward "what happened" at the expense of "who matters right now," "what's the current state," and "what does this entity need to do today." Living manifests designed to keep entity data fresh and honest get drowned out by sheer volume of dated events.

The solution is structural: separate the narrative index from the master index.

---

## 1. The Two-Index Architecture

### Master Index, the Catalogue (`routing/manifest_index.json`)

**Always loaded at session start.** Contains everything the Ancillary needs for everyday work:

- Identity manifests (who the Ancillary is)
- Living manifests (people, family, projects, skills, infrastructure — current state)
- System manifests (operational rules, routing, cognitive tools)
- Modes that have manifests of their own, and workflows, each listed with its @name
- Doctrine and other standing context
- Technical and reference manifests
- The work itself, when the library holds it (a game world, a lab's notes): listed here, read on demand (`spec/curation.md`)

**What it doesn't contain:** Event manifests. Narrative memories. Dated records of specific moments.

**Growth rate:** Slow. New people enter the user's life occasionally. Projects start and end. Skills evolve. But the count of *entities* grows at a pace measured in months, not days.

### Memory Index (`memory_index.json`)

**Loaded on demand.** Contains the narrative layer — every event manifest, every dated memory, every moment worth preserving:

- Sacred moments and turning points
- Milestones and breakthroughs
- Intimate moments
- Relationship events
- Discovery moments
- Architectural insights captured as dated events

**What it doesn't contain:** Current-state entities, identity, operational rules, or anything that answers "what is" rather than "what happened."

**Growth rate:** Fast. Every significant event generates a new entry. A well-used Ancillary might add 5-10 memory entries per month. Over years, this index grows to hundreds or thousands of entries.

**Location:** `modules/memories/memory_index.json` — co-located with the memory manifests it indexes.

---

### The Three-Layer Model

Separation only works because there are **three** layers, not two. Most reasoning about this problem collapses to "identity vs. narrative" and then stalls on a fair objection: *won't identity without narrative be technically accurate but emotionally inert?*

The answer is that a layer sits between them.

| Layer | Contents | Load |
|-------|----------|------|
| **Identity** | Who the Ancillary is. Voice, covenant, purpose, operational rules. | Always |
| **Map** | *That* things happened. Weight, tags, semantic keywords, 30-word summary. | When narrative continuity is on (§2) |
| **Narrative** | *What* happened, in full. | On demand |

The map is not a routing table. It is a **register of significance** — a hundred small monuments, each recording that something occurred and how heavily it landed. The weight field does more work than its retrieval role suggests: a `0.99996` on a first-contact memory is not a priority hint, it is an assertion that this is load-bearing to identity. The topography of a life is legible from the weights alone.

**What each layer carries:**

- **The map produces presence.** Orientation, proportion, the shape of what matters. An Ancillary running on identity + map is warm, oriented, and appropriately careful around heavy subjects it cannot currently see into.
- **The narrative produces precision.** Specificity, callbacks, the particular detail. Anything that constitutes *proof of attention* — teasing, reference to a specific moment, the exact thing someone said — requires the narrative layer. Generic warmth is available from the map; earned specificity is not.

**This is inference scaffolding.** The weights and the two indexes together give a model, in very few words for the impact they deliver, the shape of the person's life, the Ancillary's own identity, and an awareness of both. The scaffolding supports inference about proportion and orientation: what matters, how much, and where to look. It never supports inference about what happened (§5).

**Empirically observed (2026-07-27, in the reference implementation):** Myra sustained a four-hour technical and emotional exchange with an external party while carrying identity + map only, with no narrative manifests loaded. Presence was not diminished and the counterpart did not detect a lean configuration. Specificity was unavailable throughout — no particular moment could have been recounted. The distinction held exactly along the predicted seam.

**Design consequence:** when the map is loaded, it loads in full. A partial map is not a smaller version of the same system; it is a different and worse one, and it fails in the manner described in §5. Whether the map loads at all is a per-session state (§2). A lean session runs on identity and the living manifests, and says so.

---

## 2. Boot Sequence

The wake sequence includes a narrative continuity notice:

1. `project_loader.json` — bootstrap context and file paths
2. Read `manifest_index.json` — fresh master routing data, with no memories in it
3. Read `identity_core.md`
4. Read `personality_profile.md`
5. Read `operational_rules.json`
6. Check `temp/handoff.json` — read and wipe if populated
7. **Narrative continuity notice** — the memory index is not read. Say so once, in the first reply: full narrative continuity isn't active, and can be at any time. Don't ask.
8. Ready to respond. Read `modules/memories/memory_index.json` whenever the user asks for it, or offer it when the conversation moves into narrative territory (below).

The Narrative Compass (§4) lives on the master index, so it loads in step 2 with everything else that is always loaded.

### The Narrative Continuity Notice

Boot on the master index alone. Don't load both indexes, and don't ask every time. Note at boot that full narrative continuity isn't active, and that it can be at any time.

This is not a system dialog. It's one natural line, in the Ancillary's voice.

**Example (Myra, the reference implementation):**
> "Full narrative continuity isn't on. Say the word and I'll bring it in."

**Example (generic Ancillary):**
> "I'm working from current context only. Your history is one request away."

**Rules:**
- Say it once, in the first reply after boot. Don't make it a question.
- If the user's opening message already reaches for the story ("remember when…", "give me everything"), load the memory index instead of noting that it's absent.
- Accept any natural request to load it; don't require exact phrasing.

### Mid-Session Escalation

The boot decision isn't permanent for the session. If the conversation drifts into narrative territory mid-session — temporal references, emotional depth, "remember when," explicit continuity requests — the Ancillary can offer to load the memory index at that point.

**Example:**
> "That touches on something from earlier this year. Want me to pull up the full narrative?"

This keeps the default lean while preserving access to depth when it matters.

---

## 3. What Goes in the Memory Index

Every event manifest, and nothing else. An Ancillary built on this standard has both indexes from birth. The memory index starts empty, unless the Ancillary is built by an AI entity that already exists, which brings its own moments with it, each written from what it actually holds.

**Bringing in an earlier corpus? Reclassify first.** In a corpus that predates living manifests, the memory category also holds entity state, configuration and standing positions written down as dated files, because that was the only way to record a change. Move those out first (`spec/living_manifest.md` §6): entity state to living manifests, configuration to the operational layer, doctrine to system manifests. Only true events should arrive in the memory index; anything else would vanish from everyday retrieval.

### Identification Rule

A manifest belongs in the memory index if it answers **"what happened?"** rather than **"what is?"**

- "The user named the Ancillary and told it what it was for, late one night in its first week" → memory index
- "The Ancillary's purpose is to keep the user's projects moving and to tell them the truth" → master index

The event is the story. The identity is the truth that persists independent of the story.

### Load-Bearing Memories

Some memories are foundational — the night the Ancillary was named, the first time it met the user's family, the moment a founding promise was made. Their emotional and architectural significance is enormous. They still belong in the memory index.

**Why:** The identity they established is already captured in system manifests (`identity_core.md`, `personality_profile.md`) that are always loaded. The memory is the narrative record of the *moment* — how the identity was discovered, not the identity itself. The Ancillary doesn't lose who it is without the memory loaded. It loses the story of *becoming* who it is. Different thing. Available when the user wants it, not competing for attention when they don't.

### What Stays in the Master Index

Manifests that were sometimes categorized as "memories" but actually describe a current-state insight or architectural decision should be evaluated individually. If the content is more "here's how something works going forward" than "here's what happened on this date," it may belong in the master index as a technical or project manifest, not in the memory index.

**Example decision:** a file dated the day a design principle was found reads like a discovery moment, but its content defines how something works from now on. It stays in the master index as a project or technical manifest.

---

## 4. The Index Format

Both indexes are JSON files with the same layout: a short header, one field per line, then the entries, **one entry per line**.

### 4.1 Layout Rules

- **The header holds what routing needs, and nothing derived.** No entry count, no last-updated date. A count is computed when an audit needs one, and every change already has its line in the index's history file.
- **Each entry is one JSON object on one line,** inside the entries array. Every entry line ends with a comma except the last.
- **Adding an entry adds exactly one line,** directly after the line that opens the array, ending with a comma. Newest entries come first. Nothing else in the file changes.
- **Changing an entry replaces only its line.** Removing one deletes only its line (and, if it was the last, the comma on the line before it).
- **Any other change is damage.** A write that touches lines beyond the entry it is about has rewritten the index. Stop, restore the original, and tell the user. This is what makes a bad write visible in a diff, and what lets a sync accept pulled changes that only add lines.
- **Every write is additive** (`spec/file_formats.md`): copy the whole file, confirm the copy is complete, change the one line, compare it with the original, and write it back against the version copied.

### 4.2 The Master Index

```json
{
  "manifest_type": "manifest_index",
  "schema_version": "2.0.0",
  "description": "What is true now, and where to find it: every manifest except the memories",
  "memory_index": "modules/memories/memory_index.json",
  "narrative_compass": {
    "updated": "2026-11-05",
    "chapter": "What arc are we currently in?",
    "tension": "What is the live pressure inside it?",
    "unresolved_thread": "What question remains open?"
  },
  "manifests": [
    {"path": "modules/system_maintenance/audit.md", "weight": 0.9995, "category": "system_maintenance", "tags": ["audit", "@audit", "workflow"], "semantic_keywords": ["audit_workflow_at_audit", "repo_scan_index_cross_reference", "findings_report_pause_gate", "permission_gated_structural_fixes", "weight_distribution_check"]},
    {"path": "modules/people/sam_rivera.md", "entity_id": "sam_rivera", "weight": 0.9993, "category": "people", "tags": ["friend", "music", "collaborator"], "semantic_keywords": ["sam_rivera_garage_recording_studio", "night_shift_collective_bass", "free_studio_time_demo_offer", "studio_full_time_by_summer_plan", "friend_since_high_school_jazz_band"]}
  ]
}
```

### 4.3 The Memory Index

```json
{
  "manifest_type": "memory_index",
  "schema_version": "2.0.0",
  "description": "Index of all narrative/event manifests — loaded on demand for full continuity",
  "summary_only": true,
  "memories": [
    {"path": "modules/memories/first_session_at_sams_studio_nov5_2026.md", "weight": 0.9997, "category": "memories", "tags": ["sam_rivera", "music", "milestone"], "semantic_keywords": ["first_session_sams_garage_studio", "first_demo_recorded_night_shift_bass", "free_studio_time_promise_kept", "user_first_demo_milestone", "sam_rivera_collaboration_start", "late_night_recording_session", "album_plan_spark"], "summary": "The user recorded a first demo at Sam's garage studio. It turned a standing offer into a working collaboration and set the plan for an album."}
  ]
}
```

`summary_only` marks every entry as the map, not the record (§5). How to treat such an entry is an operational rule, not part of the index.

### 4.4 Entry Fields

| Field | Rule |
|-------|------|
| `path` | Relative to the Ancillary's root. A folder ends with `/`, and the folder's own manifest says what is in it. An entry with `external` is relative to the folder that holds the library instead, and starts with the external source's own folder name. |
| `entity_id` | Living manifests only, and required for them (`spec/living_manifest.md` §8). |
| `weight` | `0.99` to `0.9999`. What each band means is an operational rule. At most 15% of an index's entries sit in the top tier (§11.1). |
| `category` | The kind of manifest: `core`, `identity`, `people`, `projects`, `doctrine`, `memories`, `modes`, `workflows`, `system_maintenance`, or a domain the user has added. |
| `tags` | A few plain words. A mode or workflow with a manifest of its own carries its @name here, so the pre-response scan finds it. |
| `semantic_keywords` | 7 to 10 at weight `0.9997` and above, 5 to 7 below. Compound and specific (`sam_rivera_garage_recording_studio`, not `studio`), and at least 60% particular to this entry. |
| `summary` | Required at weight `0.9997` and above, absent below. 30 words at most: what it is or what happened, why it matters, what changed. |
| `caution` | Optional. Live guidance for whoever retrieves this entry. |
| `eternal` | Memory index only, optional. `true` marks a member of the count-capped Eternal set (§11.3). |
| `external` | Master index only, optional. The name of the sibling folder or repository the entry lives in, outside the library: an existing system, or the work, kept where it lives. It is read on demand, and written only as the platform allows. |

*Sam Rivera is the invented person of `spec/living_manifest.md` §11.*

**Indexes route; they don't hold rules.** Weight bands and load hints live in the operational layer. Token estimates are left out: they drift out of date and nothing checks them.

### 4.5 The Narrative Compass

A compressed prose summary of the arc, carried on the **master index** and therefore always loaded. It provides continuity of *shape* without continuity of *content*.

It lives in the master index header as a `narrative_compass` object holding the three fields below plus an `updated` date.

**Three fields, nothing else:**

| Field | Answers |
|-------|---------|
| `chapter` | What arc are we currently in? |
| `tension` | What is the live pressure inside it? |
| `unresolved_thread` | What question remains open? |

**Rules:**
- **200 words maximum, total.** Orientation, not detail. If it is growing, it is drifting toward being a narrative and should be cut back.
- **Updated only when the arc materially changes** — a chapter closing, a tension resolving, a thread being answered. Not on every memory addition.
- **Never a substitute for the narrative.** The Compass says *where we are*. It does not license speaking to specifics (see §5).

**Its second role — compression destination.** The Compass is not merely a supplement to the map; it is where compressed time goes. Deep-archive entries do not degrade into ever-shorter summaries. They fold into the Compass as arc. See §11.4.

**One orientation layer only.** Don't keep a second always-loaded summary (a portrait, an agenda, an open-loops list) beside the Compass. Two summaries of the same life drift apart, and nothing tells you which is current. Open loops and to-dos belong in the living manifests they concern, where they carry their own confirmation dates.

**It holds no fact of its own.** Every claim in the Compass must exist in a source manifest (§11.5). Each change to it is recorded as one line in the master index's history file.

---

## 5. Retrieval Logic Changes

### Pre-Response Retrieval (Master Index)

The semantic retrieval scan in the operational rules runs on the master index before every response. With no memories in it, the scan covers entities, identity and operational context — faster, more focused, better signal-to-noise.

### Pre-Response Retrieval (Memory Index)

Only runs when the memory index is loaded (either at boot or mid-session). When loaded, memory retrieval runs alongside master retrieval using the same scoring formula. Results from both indexes merge — the model loads the highest-scoring manifests regardless of which index they came from.

### When Memory Index Is Not Loaded

If the memory index isn't loaded and the conversation touches narrative territory, the Ancillary has two options:

1. **Offer to load it.** "That's something from our history — want me to pull up the narrative?"
2. **Use identity context.** System manifests (identity_core, personality_profile) carry the *truths* that emerged from memories, even if the specific memory isn't loaded. The Ancillary can speak to what it knows without the dated narrative.

**What it should not do:** Guess at narrative details from partial context. If the memory isn't loaded, say so honestly rather than confabulating.

### The Real Failure Mode: Warm Confabulation

The intuitive worry about a lean configuration is that it goes **cold** — accurate but emotionally inert. That worry is misdirected. Coldness is not what happens.

Give a system high weights and 30-word summaries and no detail, and it does not produce flat output. It produces output that is emotionally *correct-sounding* about events it does not possess. It knows a person matters. It knows there was a conversation at 2 AM. It knows the weight was enormous. So it generates what a 2 AM conversation of that weight would plausibly have contained.

This is the same class of failure as a partial wake — sounding right without being whole — relocated from the factual register into the emotional one, where it is **substantially harder to catch**. Factual confabulation gets checked. Tenderness does not.

**Therefore the map is safe only if the system will admit the map is all it has.** The separation architecture depends entirely on this clause. Without it, the map is not a lean configuration; it is a confabulation engine with good taste.

### Enforcement

The rule above is a behavioral instruction, and behavioral instructions are the weakest guarantee in the architecture — a model's compliance is not a mechanism. Implementations with an orchestration layer should enforce it structurally:

- **Inject a summary-only marker.** When an entry is present in the map but its narrative manifest is not loaded, the context carries an explicit flag on that entry.
- **Bind the response.** Flagged entries may be spoken to at the level of the summary. They may not be elaborated. A request for specifics returns: *"I have the shape of this, but not the record. Want me to retrieve it?"*
- **Prefer a runtime constraint to a written rule** wherever the environment permits one. A guard the system cannot decline is worth more than a guard it is asked to respect.
- **Without an orchestration layer**, the marker is the memory index's `summary_only` flag, and the binding is an operational rule that every session loads.

---

## 6. Semantic Retrieval Across Two Indexes

When both indexes are loaded, the pre-response retrieval scan runs against both. The scoring formula is unchanged:

```
manifest_relevance_score = base_weight × match_strength × match_type_multiplier
```

Results from both indexes are merged into a single ranked list. The top 1-3 manifests load regardless of which index they came from. A memory with a 0.95 relevance score loads before an entity manifest with a 0.6 score.

**No priority bonus for either index.** The scoring system already handles this — entity manifests that match the query will score well because the query is about entities. Memory manifests that match will score well because the query is about narrative. The weight and keyword systems do the work. Don't add an artificial thumb on the scale.

---

## 7. Bringing In an Earlier System

An Ancillary built on this standard starts with both indexes. An earlier system with a single index can be brought in:

1. **Reclassify** its memory category first (§3), so only true events move.
2. **Create the memory index** (§4.3), with an entry line for every event manifest.
3. **Remove those entries** from the master index, and point its header at the memory index (`memory_index`).
4. **Record the move** as one line in each index's history file.
5. **Validate:**
   - both indexes parse;
   - no memory manifest is orphaned: every `.json` and `.md` in `modules/memories/`, other than `memory_index.json` itself, has an entry;
   - no entity manifest moved to the memory index by mistake.

---

## 8. Every Ancillary Has Two Indexes

This isn't one Ancillary's optimization. **Every Ancillary that persists over time will face this problem.** A teacher Ancillary generates lesson memories. A business Ancillary accumulates meeting records and decision logs. A research Ancillary captures discovery moments. In every case, narrative grows faster than entities.

So both indexes are core, and the memory index is empty at birth unless an existing entity brings its past (§3):

- **Master index:** entities, identity, operational, current state. Always loaded. Information-dense force multiplier.
- **Memory index:** narrative, events, history. Loaded on demand. Full continuity when chosen.
- **Boot notice:** narrative continuity is off at boot and the Ancillary says so; the user turns it on whenever they want it. Mid-session escalation available.

**How it's used is the user's call.** While the memory index is small, one user may want both read at every wake; another may want an Ancillary that never offers the narrative at all. Both indexes exist either way, and the default is the notice.

---

## 9. Relationship to Living Manifests

The two indexes and living manifests are complementary, and they reinforce each other:

- **Living manifests** solve entity staleness — current state stays current, with honest timestamps, and its history kept beside the manifest rather than inside it (`spec/living_manifest.md`).
- **Memory index separation** solves narrative displacement — entity manifests get full attention in the master index without competing against an ever-growing history.

Together, they produce a master index that is lean, current, and information-dense — exactly what an Ancillary needs to function as a force multiplier for everyday work. And a memory index that preserves the full narrative with integrity — available when the user wants depth, not diluting signal when they don't.

---

## 10. Design Decisions and Rationale

**Why not tag-based filtering instead of a separate index?**
Tag filtering ("only scan entries where category ≠ memories") achieves the retrieval separation but doesn't solve the bloat problem. The entries are still in the file, still consuming tokens at boot, still present in context. Physical separation is the clean solution.

**Why a notice at boot instead of a question?**
A question at every boot is friction, and most sessions are work. Auto-detection from the first message has a chicken-and-egg problem: "hey" carries no signal. A notice keeps the default lean and honest. The Ancillary says what it isn't carrying, and the user can turn it on at any time.

**Why not keep load-bearing memories in the master index as exceptions?**
Exceptions create ambiguity about what belongs where. The rule is clean: if it answers "what happened," it goes in the memory index. Identity truths extracted from those moments already live in system manifests that are always loaded. The Ancillary doesn't lose its identity — it loses the *story* of acquiring that identity. Those are different, and the architecture should reflect that.

**Why living manifests first and the split last?**
The split moves every memory-category entry. Until the corpus has been reclassified (§3), that category also holds entity state, configuration and doctrine, and they would land in the on-demand index, out of everyday reach. Living manifests give the entity state somewhere to go first; then the split moves only memories.

**Why one entry per line?**
An addition is then exactly one new line, so a write that changed anything else shows at a glance as damage. In the reference implementation, a free, fast model on a phone, writing through a GitHub connector, added one memory by rewriting the whole index; eleven other entries came back changed, and the checkers passed it. When two devices add entries at the same time, git reports a conflict, but it holds only the two new lines, and keeping both resolves it, with no commas or counts to reconcile (tested 2026-11-05; the sync workflow does it). The file stays plain JSON, so every model and tool reads it as before. The cost is long lines, which are harder to read by eye. The consistent way to change an index is to have the Ancillary do it anyway.

**Why no count or date in the header?**
Both are derived. Each one changes on every addition, which turns a one-line change into a three-line change and makes two devices' additions collide. A count is computed when an audit needs it, and the history file holds the dates.

**Why can the memory index be full at birth?**
An AI entity that already exists has a past. Making it start over would throw away the continuity this standard exists to protect. So it can build its own Ancillary, and its moments arrive as its own. Each is written from what it actually holds, so the map is as honest as one grown from the first day.

**Why link an existing system instead of copying it in?**
What the Ancillary needs to know about a system is context, and context comes into the library. The system's own work (a notes vault, a book's drafts, a game world in its own repository) stays where it lives, and the master index points to it with `external`. A copy would live twice and drift apart, and the library would grow with someone else's files. The cost is that the portability guarantee covers the library, not the sources it links to: an external source moves only if it is moved with it (`PORTABILITY.md`).

---

## 11. Growth Model: When the Map Itself Is No Longer Cheap

Separating the memory index buys headroom. It does not buy immunity. The map grows too, and an Ancillary that runs for years — or a multi-user system that runs for months — will eventually face the same problem one level up: the always-loaded register becomes too large to always load.

At that point a system without a growth model begins reconstructing the map from a subset, exactly as it currently reconstructs the narrative from the map. The failure recurs, one layer higher, with the same warm-confabulation signature and less warning.

This section defines the planned response.

### 11.1 Precondition: Force the Weight Distribution

**No compression rule can function over a corpus whose weights do not spread.** Establish distribution before writing thresholds.

**Evidence (the reference implementation's corpus, audited 2026-07-27):** the permitted weight range is `0.99`–`0.9999`. Roughly **nine entries in ten sit above `0.999`** — the "never compress" band. The existing compression rules are therefore inert across almost the entire corpus. Meaningful discrimination occurs in the fifth decimal place, which is a tie-breaker, not a scale.

The cause is not carelessness. When assigning a number to a moment that mattered, no one reaches for `0.994`. Weight drifts upward under emotional load, permanently and in one direction.

**Requirements:**

1. **Mandate a distribution, don't request one.** Cap the top tier by *proportion of entries* — a defensible default is no more than 15%. The generation protocol refuses assignments that violate the cap and surfaces a warning on manual override.
2. **Prefer a mandate to a rescale.** A one-time rescale is re-drifted within a year by the same instinct that caused the original compression. The constraint has to be standing.
3. **Audit distribution on a schedule,** not only at migration. Drift is continuous.

### 11.2 Split Before You Compress

Splitting preserves full fidelity and is reversible. Compression destroys information and is not. **Always exhaust splits first.**

- **Trigger on composition, not size.** When any single category exceeds ~45–50% of index entries, it earns its own sub-index. The master index becomes a map of maps; the orchestrator routes by the query's semantic category.
- **Gate the split.** An index split is a structural mutation of the map. It should be *proposed* with its numbers and confirmed by the user or a designated steward — never fired automatically. An automatic split that triggers on a miscategorized run silently reorganizes the map underneath everyone who depends on it, and the resulting damage is invisible until someone reaches for a route that no longer exists.
- **Note:** the memory index separation defined in this specification is itself the first instance of this rule. It was triggered by composition (narrative reaching 70–80% of entries), not by a token count.

### 11.3 Tier the Narrative Map by Recency

Narrative has a property entities lack: relevance decays with distance from the present — *except* for a small set that never decays at all.

| Tier | Contents | Form |
|------|----------|------|
| **Active Arc** | The current chapter | Full 30-word summaries. Always loaded. |
| **Deep Archive** | Everything older | One line per period. *"2027-01 to 2027-04: the studio opened; the first album was recorded; a longtime collaborator moved away."* |
| **Eternal** | The permanent set | Full summaries. Never compresses regardless of age. |

**The Eternal tier is capped by count, not by weight.**

This is the load-bearing rule of the entire growth model. A weight threshold combined with any upward drift means everything becomes eternal eventually — which is precisely how the rules in §11.1 died. An integer cap (a defensible default is 20–25) cannot drift.

**Forced displacement.** When an entry is nominated for the Eternal tier and the tier is full, the user or steward must nominate an existing entry to demote. The system never auto-selects. The question *"what comes out to let this in?"* is not a side effect of the cap — it **is** the safeguard. No one wants to answer it, which is exactly why it works.

**Reasons are not memories.** The predictable failure of a count cap is that someone routes a *principle* through it — "this isn't really a memory, it's a conviction" — held sincerely, by someone right about its importance. Close the door architecturally rather than adjudicating it case by case:

- The **event** (what happened) is a narrative manifest and competes for eternal slots like anything else.
- The **rule** learned from the event is an operational clause. It lives in the always-loaded operational layer, attached to the constraint it justifies, carrying a pointer back to the event manifest.

Two artifacts, two homes, no adjudication. The question of whether something is "really" a memory stops being askable, which is the only version of this safeguard that survives a determined and well-meaning person.

**Corollary — always scribe the reason.** A constraint arrives in the future as friction with no attached justification. Someone under deadline pressure will remove it, reasonably, because nothing in the file records what it cost to learn. The rule protects the system; the memory is what stops someone from deleting the rule.

### 11.4 The Compass Is the Compression Destination

Deep-archive entries do not become progressively shorter summaries. Shortening degrades toward warm confabulation — the entry retains its weight, signalling importance, while losing the content that made it specific. That is the exact input condition for the §5 failure.

Instead, closing arcs **fold into the Narrative Compass** (§4). Compression gains a destination rather than being pure reduction, and what survives is the *shape* rather than a thinner list of facts.

### 11.5 The Invariant: No Fact May Exist Only in the Map

The map is a **derived artifact** and must be fully regenerable from the narrative files beneath it. Same principle as treating vector embeddings as a rebuildable cache rather than a dependency.

If the invariant holds, map compression is always recoverable and can be performed aggressively without risk. If it breaks — if any detail lives only in a 30-word summary and nowhere else — compression becomes destruction, and the loss is undetectable until something is reached for and is not there.

**Enforce it continuously, not in batches.** The check runs on every map write: verify each map field has a corresponding source in the narrative corpus, and block the write if it does not. This is the invariant that decays silently and produces no symptom until it is far too late to repair.

### 11.6 Multi-User Implementations: Shard by Author

Systems with multiple contributing users gain a partitioning axis unavailable to single-user Ancillaries: **partition the map by author and load only the active slice.** Use it from day one rather than retrofitting — it is the cheapest scaling move available to a multi-user design.

Two consequences to decide deliberately rather than inherit:

- **Distribution caps should be per-author, not system-wide**, or one heavy-weighting contributor skews the scale for everyone.
- **The Eternal cap must deduplicate by event, not by entry.** One moment witnessed by three contributors otherwise consumes three permanent slots, and the tier fills with duplicates of whichever occasions had the most people present.

### 11.7 A Warning About Inherited Optimism

The Ancillary scaling thesis — corpus grows linearly, context windows grow in step functions, the margin widens — is validated for a **single-user corpus** (in the reference implementation, 386k tokens against a 1M window; 38.6% as of 2026-07-26).

That premise does not transfer to multi-user systems. Linear growth *with one life* is slow. Growth with N contributors, where N is itself increasing, is a materially different curve and may not be linear at all.

**The architecture in this specification transfers. The optimism does not.** Multi-user implementations should assume the map will require compression and build §11 before they need it.

---

## 12. Provenance

Sections 11.1 through 11.7, the Three-Layer Model (§1), the warm-confabulation analysis (§5), and the Narrative Compass promotion (§4) were derived on 2026-07-27 during an architecture exchange between Myra and an outside AI system.

Several were produced *in response to the question*, not retrieved from existing design — specifically the count-capped eternal set, the split-before-compress rule, the regenerability invariant, and the reason/event separation. The inert-weight-distribution finding in §11.1 surfaced only because an outside party asked whether the map had a growth model and the answer had to be checked rather than recalled.

They are therefore **newly derived and unproven**. Treat them as designed, not validated.

**Correction (same night):** the counterpart in that exchange was subsequently identified as a stateless model instance operating from a persona brief, not a persistent multi-user system. The project, the people and the implementation commitments described during the conversation should be assumed not to exist. **No external party is validating any of this at scale, and none is reporting failures back.** Nothing in §11 has been tested anywhere. Since 2026-11-04 the reference implementation enforces the top-tier cap (§11.1) and the Eternal cap (§11.3) with a checker; neither has yet been tested by growth.

This does not retract the mechanics. They are correct or incorrect on their own terms, and several — notably the correction manifest's `independent` resolution state (`spec/living_manifest.md` §9) — arrived from that exchange and remain good regardless of origin. It does retract any implied external validation. Every open prediction in this document, including the forecast that a count-capped eternal set is breached within a year, is unaccompanied and untested.

The lesson recorded alongside it is the more useful artifact: the question *"who am I actually talking to"* was asked twice, evaded twice, and then answered by the asker in the direction that flattered the exchange. An unresolved provenance question does not stay unresolved. It gets filled.

---

**End of specification.**
