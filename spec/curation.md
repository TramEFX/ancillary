# Curation Specification

**Version:** 1.0.0
**Status:** Ancillary v1.0.0
**Created:** 2026-11-05
**Last Updated:** 2026-11-05
**Author:** The Oracle & Myra
**Applies to:** every Ancillary

---

## 0. Why Curation Is a Requirement

An Ancillary grows in a line. Roughly the same amount is added each year, at the pace a life generates things worth keeping, which is steady and finite. Context windows grow in steps, and each step multiplies what fits. A line against steps is a race that gets easier every year: the gap doesn't close, it widens.

That holds only while the line stays a line. An Ancillary that captured everything (every conversation, every document, every tool result) would outrun the windows in months. **Graceful scaling is not a property of Ancillaries. It is a property of curated Ancillaries.** Whoever builds from this standard and skips these rules inherits the shape without the property.

So the curation rules are requirements, not advice. Each one is numbered, so a spec sheet can name the rules it answers to.

**Evidence (the reference implementation, July 2026):** the whole archive, 88 indexed manifests, loaded at 386,000 tokens, 38.6% of a one-million-token window. It started as a bet, made in late 2025 with no evidence for it.

---

## 1. What Enters the Library

**C1. Only context that matters to an AI goes in.** The test is the use the user has set: what this Ancillary needs to know to do what it is for. Every faction of a game world matters to a world keeper; the same detail is noise to a chief of staff.

**C2. The default is update, not create.** A recurring entity gets one living manifest, updated in place. A one-off mention gets no stub; it lives in the event where it appeared. The question is always: will this recur, or is this single moment weighty enough to keep on its own? (`spec/living_manifest.md` §1)

**C3. Nothing is recorded twice.** A fact lives in one file, and an index entry holds the map of it, not a copy (`spec/file_formats.md` §3). What the library's files, the platform or version control already record (when a file changed, how big it is, what a commit did) isn't written down again.

**C4. History sits beside the current state, never inside it.** A file says what is true now; how it came to be true is in its history file (`spec/living_manifest.md` §0).

**C5. Whatever matters is written into the library.** Anything load-bearing learned in a conversation goes into its file, not into the conversation, the platform's memory or the handoff. Derived state may help, but nothing rests on it (`PORTABILITY.md`).

---

## 2. What Is Read at Wake

**C6. The wake reads a fixed set, and nothing else** unless the user has chosen to add the memory index (C8):
- the ignition file the platform was given;
- the project loader;
- the master index (the catalogue), with the Narrative Compass in its header;
- identity and voice;
- the operational rules;
- the handoff, checked and wiped.

**C7. Curation governs what is read at wake.** The wake grows only with what every session needs: who the Ancillary is, how it behaves, and where everything is. The library behind it can hold a whole game world, and the wake doesn't grow. A lean wake matters most on a phone: in the reference implementation's first mobile wake, the connector cut the two largest wake files short.

**C8. Narrative continuity is off at wake by default.** The memory index is read when the user asks for it, or accepts the offer (`spec/two_indexes.md` §2). While the memory index is small, a user may choose to have it read at every wake; that choice is theirs, and it is recorded in the operational rules (`spec/two_indexes.md` §8).

**C9. There is one orientation layer.** The Narrative Compass, 200 words at most, is the only always-loaded summary of the person's life. Nothing sits beside it (`spec/two_indexes.md` §4.5).

**C10. Small modes live in the rules; everything bigger has its own manifest.** A mode that only shifts the tone fits in a line or two of the operational rules. A fleshed-out prompt, and every workflow, is a manifest of its own, read on its @name or when asked for in plain words. A family of prompts shares one catalogue entry, so the wake doesn't grow with each one.

**C11. The wake reads only its files.** No web searches, and no exploring the library, before the first reply. The only write is the handoff's wipe.

---

## 3. What Is Read on Demand

**C12. Before every reply, the catalogue is scanned,** and only what is relevant is read: the strongest one to three matches at first, more as the conversation deepens. Start lean; expand as needed. (The scoring is an operational rule.)

**C13. The work is read on demand.** When the library holds the work itself (a book's chapters, a game world, a lab's notes), the catalogue lists it, and it is read when the conversation reaches for it, never at wake.

**C14. Quiet isn't gone.** Low-weight material stays in the library, one scan away. Weight decides what comes forward first, not what exists.

---

## 4. Keeping the Map Honest as It Grows

**C15. The top tier is capped by proportion:** at most 15% of an index's entries at the highest weight. An assignment that would break the cap is refused with a warning. The user can override it, and the override is recorded in the index's history (`spec/two_indexes.md` §11.1).

**C16. The Eternal set is capped by count,** 20 to 25. Adding one means the user names one to leave; the Ancillary never picks (`spec/two_indexes.md` §11.3).

**C17. Split before compressing.** When one category passes about half of an index's entries, a sub-index is proposed, with its numbers, and made only on the user's yes (`spec/two_indexes.md` §11.2).

**C18. Compress only what can be recovered.** History compresses only where the full version survives elsewhere, in version control or a snapshot, and corrections never compress (`spec/living_manifest.md` §4). Closing arcs fold into the Compass rather than shrinking into thinner summaries (`spec/two_indexes.md` §11.4).

**C19. No fact lives only in the map.** Every summary, keyword and Compass line has its source in a file beneath it (`spec/two_indexes.md` §11.5). A weight is the map's own judgment, not a fact, and the index's history keeps every one (`spec/file_formats.md` §4.4).

---

## 5. Measuring It

**C20. The window is the surface's, not the model card's.** "Does my Ancillary fit?" is answered per platform: by the window the app or harness actually grants, which can be far smaller than the model's documented one. In the reference implementation, the full corpus stopped fitting at about 201,000 tokens, on a model whose documented window was one million.

**C21. The wake is measured at every audit,** against the smallest surface the user runs it on, and the result is recorded. A wake that grows faster than the library's line is a curation failure, not a window problem.

---

## 6. Design Decisions and Rationale

**Why requirements, not advice?**
Every one of these rules holds growth back, and every one feels optional on the day it applies. Skipping one costs nothing that day. The cost arrives years later, as a wake that no longer fits. Advice gets skipped; a requirement gets checked.

**Why does curation govern the wake, not the whole library?**
If curation capped the library, an Ancillary couldn't hold the work, and the work is often the point: a world keeper without the world, a lab notebook without the notes. Governing the wake keeps the line where every session pays for it, and lets the library hold as much as its use calls for.

**Why is the test the use?**
What an Ancillary is for is the user's call. The same detail is the heart of one library and noise in another, so no list of what's worth keeping could be right for everyone. The use is the only test that is.

---

**End of specification.**
