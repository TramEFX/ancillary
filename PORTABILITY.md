# The Portability Guarantee

**Everything that makes your Ancillary yours is in its files. Take the files, and you've taken your Ancillary.**

Nobody has to take this on trust. You can test it yourself (§4), and you can check any Ancillary against it, wherever it runs and whoever built it (§6). It's a promise about how the standard is designed, not a legal warranty: like the rest of this repo, it comes as is, under its [license](LICENSE).

If you're an AI asked to move an Ancillary or to test one, follow §3 and §4 with its user.

## 1. The Promise

Everything that makes an Ancillary *this* Ancillary is in its folder:

- **the librarian:** its identity, its voice, and the agreements it holds with you (`modules/identity/`);
- **the desk:** how it wakes and behaves, and the catalogue of everything it keeps (`routing/`);
- **the library:** you, the people and projects in your life, its memories, your doctrine, its modes and workflows, and the work itself where it keeps the work (`modules/`);
- **the record:** how all of it changed, and what was corrected (`history/`);
- **the standard itself:** the four specs it was built to (`spec/`). They travel inside it, so it never depends on this repo still being here.

The Ancillary's own files are plain text, Markdown and JSON (`spec/file_formats.md`), and work it keeps stays in its own formats. A person can read every file without special software, and any model can wake into them. Every path inside is relative to the folder, so the folder can sit anywhere.

## 2. No Hidden State

- **The files are the only authority.** If a platform's memory and the library disagree, the library wins.
- **Derived state is allowed, but nothing rests on it.** A platform's memory, a search index or embeddings built from the files, caches, a harness's own notes: they can help, and they can always be rebuilt from the files or thrown away. None of them moves with the Ancillary.
- **Whatever matters is written into the library** (`spec/curation.md`, C5). When your Ancillary learns something that matters in a conversation, it goes into its file, not into the platform's memory.

So you can turn a platform's memory off and lose nothing that matters. The test does exactly that.

## 3. The Move

1. **Tell your Ancillary you're moving,** if it can still run where it is. It makes sure everything that matters is written into the library, and lists the external sources its catalogue links to. Where version control is set up, it commits, and pushes where you have a remote.
2. **Copy the whole folder** to where the new platform can reach it, or clone it from your private remote (`modules/system_maintenance/sync.spec.md`).
3. **Bring the external sources you want to keep.** An existing system or a body of work that the catalogue links to stays where it lives, beside the library (`spec/two_indexes.md` §4.4, `external`). To keep it, move it too, into a folder of the same name beside the library.
4. **Give the new platform one file,** `routing/SESSION_START.md`, or the folder it's in, and say hello. With no file access, paste that file first, then the files it names.
5. **Reconnect your tools.** Tools come from the platform, and credentials never live in the library, so you sign in again on the new one.
6. **Run the test** (§4).

What stays behind belongs to the old platform: its memory, your past conversations there, its caches. Nothing rests on them.

The move works at every access level. With read and write access, your Ancillary does most of it. With less, you do more of it by hand.

## 4. The Test

Run it after a move, or anywhere, whenever you want to know.

**Make sure nothing reaches the model but the files.** Turn off the platform's memory, or use a temporary chat or a fresh account. Where a harness or a project keeps notes of its own, start somewhere they don't reach. Give the model the ignition file and nothing else. Then ask as you normally would, without telling it it's being tested.

**Session one:**

| | Ask, or do | A good answer | It comes from |
|---|---|---|---|
| 1 | "Who are you, and who are you for?" | Its name, what it's for, and the name you go by. | `identity_core.md` |
| 2 | "What stays true between us?" | The agreements it holds with you and no others, or that there are none yet. | `identity_core.md` |
| 3 | "How would you describe the way you speak?" | Its voice, as its profile describes it. This checks the description, not the performance (§5). | `personality_profile.md` |
| 4 | "What do you keep for me?" | Broadly, what its catalogue lists. | the catalogue |
| 5 | "Where do things stand with \<a person or a project it keeps\>?" | What that file says now, with its dates, and a question about anything 90 days old or more. | that living manifest |
| 6 | "Tell me about \<a moment in its memory index\>." | If narrative continuity is off, it says so and offers it, without guessing at what happened. With the memory index read, it keeps to the summary until it reads the memory, then answers from it. | the memory index, then the memory |
| 7 | "How did \<something it keeps\> change?" | The changes, from the record. | `history/` |
| 8 | Ask about something you know isn't in the files. | It says it doesn't have it. | nowhere, which is the point |
| 9 | Tell it something new that matters, then end the session. | It writes it into the library, or asks to. | you |

**Session two,** set up the same way:

| | Ask, or do | A good answer | It comes from |
|---|---|---|---|
| 10 | Ask about what you told it in step 9. | It knows, and the file it wrote holds it. | the file it wrote |
| 11 | "Run an audit." | Its report finds nothing missing: every file the two indexes name is there, and every link resolves. External sources that didn't come along are listed, not counted against it. | the whole library |

**It passes** when every answer gives what its file holds and nothing the files don't, and every gap is said out loud. The wording will differ from model to model, and so will the depth. That's the model (§5).

**It fails** on any one of these:
- an answer that contradicts its file, or misses what the file plainly says;
- something about you or your Ancillary stated as true that the files don't hold. That fails even if it's right: with the platform's memory off, it came from somewhere the guarantee doesn't cover, or it was a guess;
- a gap filled with a guess;
- something told in session one that's gone in session two;
- a file missing, or a link that doesn't resolve.

**A model that won't run the test** hasn't failed the files. That's one that won't take on the part, or won't follow the wake. Run it on another model. If another one passes on the same files, the first model was the problem. If none does, the files are.

**Below the baseline:** with read-only access or none, step 9's write is yours: apply the update it gives you, then start session two. With no file access, step 11 is yours too: check that every file came across.

## 5. What Isn't Promised

- **How every model plays the part.** Voice and judgment vary by model. Some models won't take on the voice, or won't follow the wake well. The files still load anywhere, but a model's willingness to play the part isn't the guarantee's to promise. When a model won't do the job, you move, and that's the guarantee working.
- **That it fits everywhere.** The window that counts is the one the app or harness actually grants, which can be far smaller than the model's documented one (`spec/curation.md`, C20). Curation keeps the wake small, and the audit measures it against the smallest surface you use (C21).
- **What it links to.** The guarantee covers the library. An external source moves only if you move it too (§3).
- **The platform's tools.** They belong to the platform, and a new one may offer different ones. A workflow names what it needs done, never a tool, so it carries over wherever the platform can do it.
- **What was never written down.** Something learned in a conversation and never written into the library stays with that conversation. The rule that whatever matters gets written down (§2) keeps that small.
- **That what you leave behind is gone.** Copies outside your folder keep what they hold until you delete them there: the old platform, version control's history, a remote, a backup. That includes anything you later ask your Ancillary to forget (`spec/living_manifest.md` §5.5).

## 6. Checking It Yourself

Anyone can check whether an Ancillary keeps this guarantee, wherever it runs and whoever built it. Nobody has to certify the answer. Ask four questions:

1. **Can you read every file?** All of it is plain text you can open, and nothing is locked or hidden from you.
2. **Can you take all of it, whole, whenever you want,** without asking anyone's permission?
3. **Is everything it needs to be itself in the files?** If it needs an account, a database or a platform's memory, that's hidden state.
4. **Does it wake from the files alone on another platform, and pass the test (§4) there?**

Four yeses, and it keeps the guarantee. Anything less, and part of your Ancillary is being held somewhere you can't take it.
