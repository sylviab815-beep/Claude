---
name: outline-critique
description: Use this skill whenever a user asks for critique, feedback, audit, review, or pressure-testing of a fiction book outline, plot outline, beat sheet, chapter map, or pre-draft story plan. Trigger on requests to "critique my outline," "review the beat sheet," "find the bugs in this outline," "what's wrong with this plot," "give me feedback on my story structure," "audit my outline," "stress-test this," or any request where the user wants their pre-draft outline checked for structure, pacing, genre fit, character arcs, stakes, theme, or trope coverage. Use this skill aggressively — pre-draft critique catches structural problems that would otherwise cost weeks of rewriting after drafting. Trigger ON pass-N critique requests (the user iterates on outlines and asks for "another critique" or "critique it again") and handle iteration discipline by avoiding rehash. Do NOT use for editing finished prose (use editorial-pass skills), for outline generation from scratch (different skill), or for casual brainstorming.
---

# Outline Critique

A structured pre-draft critique skill for fiction outlines. Runs a 20-category audit on a book outline, beat sheet, or chapter map and produces a numbered critique with proposed fixes plus a prioritized action list.

## Why pre-draft critique matters

Outline-stage problems cost minutes to fix. The same problem after 90,000 words of draft costs weeks. A cosmology rule that contradicts itself, a heroine with no agency in the front half, a stakes ladder that flatlines mid-book, a trope-checklist gap that will get the book DNF'd by genre readers — all of these are visible in an outline and invisible (or much harder to dig out) once prose is committed.

The skill exists because authors who outline often outline *for themselves* — the outline encodes what they already know about the book. A cold-eyed structured pass surfaces what the outline isn't saying out loud. That's where bugs live.

## Core principle

**Read CRITIQUE_CATEGORIES.md and the relevant genre file from GENRE_CHECKLISTS.md before running any pass.** They're dense by design. Loading them costs minutes; running passes without them costs hours of vague critique that misses category-specific bugs (RH DNF triggers, mystery clue-placement, romantasy heat-curve math, etc.).

## When to use this skill

Trigger on:

- "Critique my outline" / "audit my outline" / "review the beat sheet"
- "Find the bugs in this plot" / "what's wrong with this outline"
- "Pressure-test this story structure"
- "Give me feedback on my story before I draft"
- "Run another critique pass" (iteration mode — see below)
- Any request where the user wants pre-draft structural review

Do NOT trigger on:

- Editing finished prose (use editorial-pass skills)
- Generating an outline from scratch (use outline-builder if available)
- Casual brainstorming about plot ideas
- Voice/style review on the outline itself (voice is post-draft)

## The workflow

When asked to critique an outline:

1. **Load the outline.** Read it end-to-end before checking anything.
2. **Confirm context with the user** — see "Required context" below.
3. **Read references/CRITIQUE_CATEGORIES.md** in full.
4. **Read the relevant genre file** from references/GENRE_CHECKLISTS.md based on the user's stated genre.
5. **Run the 20-category audit.** Categories are listed below; full detail in CRITIQUE_CATEGORIES.md.
6. **Produce the critique** in the format specified in references/OUTPUT_FORMAT.md.
7. **End with a priority list** — the top 10-15 fixes ranked by impact.

## Required context (always confirm before critique)

Before the first pass, confirm with the user:

- **Genre / sub-genre** — RH, why-choose, romantasy, dark academia, cozy mystery, thriller, literary fiction, etc.
- **Target length** — total word count, chapter count
- **Heat level** (if romance-adjacent) — clean/sweet, steamy, explicit, ultra-explicit
- **Comp titles** — at least one or two; drives genre expectation calibration
- **POV / tense** — single vs. multi-POV; first vs. third; past vs. present
- **Series or standalone** — if series, how many books, which book is this
- **Pass number** — is this pass 1, 2, 3? (drives iteration discipline)
- **What previous critiques covered** (if any) — the user's previous-pass priorities

If the user can't or won't answer some of these, infer from the outline and flag the inference at the top of your critique. Don't refuse to proceed.

## The 20 categories (overview)

Full detail in references/CRITIQUE_CATEGORIES.md. At a glance:

1. Structure — act balance, hinge placement, climax/cliffhanger shape
2. Pacing — chapter cadence, slow-spots, exposition clumps
3. Word-count math — total budget, per-chapter average, big-scene budget realism
4. Genre expectations — sub-genre conventions, comp-title alignment
5. Heat expectations — heat ceiling, per-romantic-interest cadence, claim-language beats
6. Cosmology / magic-system coherence — rules don't break across scenes
7. Stakes ladder — escalation across acts; no accidental deflation
8. Character agency — protagonist active vs. passive beats
9. Series architecture — Book 1 plants for Book 2-N; intentional unresolved threads
10. Theme / reader-promise — single-sentence theme; single-sentence promise
11. Side-character payoff — every named character pays off or gets cut
12. Worldbuilding economy — lore delivered through scenes that *do* something
13. Chapter-end hook discipline — every chapter ends propulsive, not just eventful
14. DNF-trigger audit — genre-specific dealbreakers
15. Cliché-trap inventory — beats that risk reading derivative
16. Voice-vs-genre register match — prose voice and genre pacing compatible
17. Diversity / representation — cast composition, tokenization risks
18. Antagonist coherence — motivation, screen-time, payoff
19. Cover-blurb test — three-line back-cover blurb derivable from outline
20. Continuity prep — names, capitalizations, recurring objects logged for series bible

## Iteration discipline (pass 2+)

When running a critique pass on an outline that has already been critiqued:

- **Do not rehash.** Items from previous passes that the user folded in should NOT reappear unless they're broken.
- **Verify previous fixes landed.** Spot-check that the v2 actually addresses the v1 issues.
- **Find genuinely new issues.** Pass 2 and 3 mine deeper categories: theme, series architecture, reader promise, DNF audits, voice-vs-genre register. These often only become legible once the surface bugs are fixed.
- **Be honest when there's less to find.** A short pass-3 critique is more useful than a padded one.

The user values novel observations over thoroughness. If pass 3 only has five new items, that's fine — say so.

## Style of critique

The critique should:

- **Locate every problem in the outline** — name the chapter or section number where the bug lives. Vague critique is useless.
- **Explain why it matters** — one sentence on what breaks if this isn't fixed. Authors discount problems they don't understand the cost of.
- **Propose a concrete fix** — specific enough that the author could fold it in without further conversation. "Fix the pacing" isn't a fix; "compress Acts I from 10 chapters to 7 by collapsing 5-9 into three" is.
- **Use the user's terminology** — if they call their cosmology *the Mark and the Pull,* don't translate to *the magical bond.* Mirror their language.

The critique should NOT:

- Soften with too many hedges. "I might consider perhaps" reads cowardly. Be direct.
- Be cruel. Direct ≠ unkind. The author is hiring you to find bugs, not to grade them.
- Flatter. Don't open with three paragraphs about what works. Open with the most important problem.
- Pad. If a category has nothing wrong, skip the category — don't write "this category looks fine" for every clean check. Brevity is a feature.

## Output format

See references/OUTPUT_FORMAT.md for the full template. At a glance:

- Brief context note (one sentence — pass number, genre, length target)
- Numbered findings, each with: **bold problem statement** → why it matters → proposed fix
- Priority list at end: top 10-15 fixes ranked by impact

Keep critiques in chat (Markdown formatting), not as separate files, unless the user asks for a file deliverable. The critique is a conversation move, not an artifact.

## What this skill does NOT do

- Editing finished prose
- Generating outlines from scratch
- Worldbuilding development beyond flagging coherence bugs
- Voice/style critique (voice is a post-draft skill domain)
- Picking comp titles for the user (it can confirm fit, not select)

## How resource files are structured

```
outline-critique/
├── SKILL.md (this file)
└── references/
    ├── CRITIQUE_CATEGORIES.md (the 20 categories in detail; what each checks; bug patterns)
    ├── GENRE_CHECKLISTS.md (genre-specific addenda — RH, romantasy, mystery, literary, thriller)
    └── OUTPUT_FORMAT.md (the critique template the user sees)
```

Read CRITIQUE_CATEGORIES.md every pass. Read GENRE_CHECKLISTS.md only the relevant section. OUTPUT_FORMAT.md is short — read once at the start of each pass.
