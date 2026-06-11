# Workflow Steps — Romantic Suspense Writer

Complete step-by-step pipeline. Do not skip steps. Pause for user input where indicated.

---

## Step 1: Outline Intake

Ask the user to upload their outline. Parse all sections:

- Both leads' character bios (including their wound, their blind spot, what they stand to lose)
- The external threat/suspense arc (what the danger is, who the antagonist is, what the stakes are)
- The romance arc beats (where they fall together, the trust break, the black moment, the HEA)
- The information architecture (what the reader knows when — the reveal schedule)
- Chapter-by-chapter structure (goals, complications, which track is primary each chapter)

After parsing, summarize:
- The dual-plot in one sentence for each track
- The thematic spine (what trust issue connects both tracks)
- Any gaps in the outline that need filling before writing begins

Use AskUserQuestion: "Does this summary capture your story correctly? Any adjustments before I start writing?"

---

## Step 2: Series / World Continuity Check

Use AskUserQuestion:

**"Is this book part of a series or interconnected world?"**
- Book 1 of a new series — I'll start building the world bible
- Continuing an existing series — please share a world bible or previous book
- Interconnected standalone — same world, new couple; share any world notes you have
- True standalone

If continuing a series or interconnected standalone:
- Read any provided world bible, previous books, or series notes
- Extract: recurring character names/roles, location details, established world facts, unresolved threads
- Note which secondary characters in this book are slated for future books — write them with enough dimensionality to earn their own story
- Save a `[Series Name] - World Bible.md` or update the existing one

---

## Step 3: Series Position and POV Confirmation

Use AskUserQuestion for each question ONE AT A TIME:

**"What is this book's position in the series/reading order?"**
- Standalone (complete story, no prior reading needed)
- Book 1 (entry point to the world)
- Book 2+ (assumes familiarity with prior books)
- Interconnected standalone (can be read independently, but rewards series readers)

**"What is the POV structure?"**
- Single first-person (deep inside one protagonist's head — intimate, immediate)
- Single third-person close (tight on one character, slight distance)
- Dual POV (alternating between both leads — reader knows more than either character)
- Other (specify)

---

## Step 4: Style Guide

Ask the user:

"To make this manuscript sound like YOU, I need a sample of your writing. Upload any piece of your fiction — a previous book, a chapter of a WIP. The longer the sample, the better."

Use AskUserQuestion:
- Yes, I'll upload a sample
- No sample — match genre conventions

#### If sample uploaded:

Read and extract:
- **Voice & Tone**: Sentence length patterns, narrative distance, how conversational or literary, humor level
- **Tension Style**: How dread and unease are built — implication, detail, dialogue, pace
- **Romantic Tension Style**: How attraction is communicated in clean content — internal monologue, physical awareness, near-miss construction
- **Dialogue Patterns**: Banter style, how subtext works, how secrets and lies sound
- **Pacing Style**: Chapter length preferences, how action and quieter scenes balance
- **Description Density**: How much sensory detail, how settings are used
- **Distinctive Voice Markers**: Fragments, em-dashes, characteristic phrases, POV depth

Present the style guide to the user: "Does this capture your voice?"

#### If no sample:
Ask for 2-3 author comparisons plus a brief description of the feel they want (warm and fast? Slow burn and atmospheric? Wry humor? High tension?). Build a lighter style guide from these.

Save the guide as `[Title] - Style Guide.md`.

---

## Step 5: Ticking Clock and Twist Confirmation

Use AskUserQuestion:

**"What kind of ticking clock drives the external threat?"**
- Literal deadline (a specific date, event, or countdown)
- Escalating pattern (the threat escalates on a schedule — another attack, another victim)
- Soft deadline (a general sense that time is running out — no specific moment, just pressure)
- No clock — the tension comes from cumulative escalation, not time pressure

**"How complex is the suspense reveal?"**
- One major reveal (a single identity/truth that recontextualizes the story)
- Two-layer (a mid-book twist that changes the game, then a final reveal)
- Straightforward (suspense through escalation, the reader knows the threat — tension is in the chase)

---

## Step 6: Write the Manuscript

For each chapter, write complete prose following:

1. **The dual-track mandate**: Every chapter must advance both the romance and the suspense track. Read `references/dual-track-architecture.md` before writing Chapter 1 and keep it open throughout.

2. **The style guide**: Every sentence should sound like the user's voice.

3. **The outline**: Honor POV assignment, chapter goal, complication, character decision, and consequence. The outline is the blueprint — don't deviate without flagging it.

4. **The information budget**: Check the outline's information release schedule before writing each chapter. What does the reader learn here? What stays hidden? Is there active misdirection? No early reveals.

5. **Sweet/clean standards**: Full romantic tension through proximity, near-misses, charged dialogue, and specific physical awareness. No explicit content. Read `references/prose-craft.md` for how to write clean heat at full intensity.

6. **Chapter hooks**: Every chapter ends on a hook that pulls at least one track, ideally both.

**Chapter specifications:**
- Target ~2,000–2,500 words per chapter for novels; ~1,500 for novellas (confirm from outline)
- Every chapter is fully written prose — no summaries, outlines, or bracketed placeholders
- POV locked to the assigned character — no head-hopping

**CRITICAL — COMPLETENESS**: A manuscript with summarized chapters is a failed manuscript. If context is limited, write chapters 1–5, then 6–10, etc. Never summarize a chapter to cover more ground.

Use Task subagents to write chapters in parallel batches when possible. Give each subagent:
- The full style guide
- The outline for the chapters they're writing
- Character bios and the romance arc beat map
- The dual-track architecture rules
- Chapters already written (for continuity and information budget tracking)
- The information release schedule from the outline

---

## Step 6b: Structural Quality Check (Before Revision)

Before running the editorial pipeline, verify:

**Dual-Track Check:**
- [ ] Every chapter advances both the romance and the suspense track
- [ ] Love interest is present, mentioned, or on the protagonist's mind in every chapter
- [ ] Romance arc beats all appear on-page: Alliance, First Connection, Deepening Stakes, Almost, Trust Break, Black Moment, Turn, HEA
- [ ] Black moment breaks BOTH tracks simultaneously
- [ ] HEA is delivered AFTER the external resolution, not before or alongside

**Suspense Track Check:**
- [ ] Information budget matches the outline for each chapter — no early reveals
- [ ] Tension ratchets upward — baseline rises even with brief dips
- [ ] Protagonist draws wrong conclusions before right ones
- [ ] Twists have planted clues (3+ per twist)
- [ ] External threat is felt in every chapter

**Sweet/Clean Compliance:**
- [ ] No explicit content anywhere
- [ ] Romantic tension is delivered through proximity, near-misses, charged dialogue, specific physical awareness
- [ ] Near-miss moments are written at full emotional intensity before the interruption

Fix any issues before proceeding to the editorial pipeline.

---

## Step 7a: AI-Ism Identification Report (Sonnet)

Read `references/revision-guide.md` for the complete checklist. Use a Sonnet subagent to analyze the full manuscript and produce a chapter-by-chapter report flagging:

- AI connector words (Additionally, Furthermore, Moreover, etc.)
- Emotional over-labeling (naming emotions instead of showing them)
- Mechanical chapter structure and tidy wrap-ups
- Clinical precision ("After approximately forty-five seconds...")
- POV breaks
- Romantic suspense-specific AI patterns: near-miss scenes that don't build to the edge, danger that evaporates between chapters, romance-suspense tracks that aren't braided

Report feeds directly into Step 7b.

---

## Step 7b: AI-Ism Fixes (Opus)

Use an Opus subagent to rewrite every flagged passage. Give the Opus subagent:
- The full manuscript
- The AI-ism report
- The style guide
- The dual-track architecture rules (to verify every rewrite serves both tracks)

Every rewrite must sound like the user's style guide, not generic editorial voice.

---

## Step 8a: Developmental Edit Report (Sonnet)

Use a Sonnet subagent to produce a comprehensive dev edit covering:

1. **Dual-track integrity** — Is every chapter advancing both tracks? Where do they decouple?
2. **Black moment assessment** — Does it break both tracks simultaneously?
3. **HEA delivery** — Is it fully satisfying? Does it come after the external resolution?
4. **Tension escalation** — Does the ratchet work? Where does it flatten?
5. **Information control** — Any early reveals? Any skipped plant points?
6. **Character arc** — Do both leads have internal arcs that earn the HEA?
7. **Sweet/clean compliance** — Full romantic tension within clean standards?
8. **Series consistency** — Is the world and recurring cast consistent?
9. **Voice** — Does the prose sound like the style guide?

Output: Executive Summary, Detailed Notes (with chapter references), Top 5-7 Priority Action Items, What's Working.

---

## Step 8b: Dev Edit Fixes (Opus)

Use an Opus subagent to apply the top 5 Priority Action Items. Dual-track failure (romance or suspense not the A-plot) is always priority #1 if present.

For each fix: identify which chapters need rewriting, rewrite as full prose, verify continuity.

---

## Step 9a: Beta Read Report (Sonnet)

Use a Sonnet subagent framed as a heavy romantic suspense reader (reads 3+ RS books a month, writes honest Goodreads reviews):

1. **Star rating** (out of 5) — honest, not generous. Most first drafts land 3–3.5 stars.
2. **The Good** — specific scenes and dynamics that work
3. **The Bad** — specific problems with chapter references
4. **Top 3–5 suggestions for improvement** — ranked by importance, with specific chapter references and solutions

Beta reader calibration: judge against published romantic suspense, not literary fiction. Focus on whether the book delivers the dual-track promise.

---

## Step 9b: Beta Read Fixes (Opus)

Apply the top 3 suggestions from the beta read. Maintain word count — revision means improving, not cutting.

---

## Step 10: KDP Info Document

Read `references/kdp-template.md`. Create a companion document with:
- Book title and subtitle (for romantic suspense: subtitle should signal BOTH romance and danger)
- Amazon description (hooks the reader on the romance AND the threat)
- 7 keyword phrases (mix romantic suspense broad + trope-specific + audience-specific)
- 3 BISAC categories (always include "FICTION / Romance / Romantic Suspense")
- Suggested price point
- Series information
- 3–5 comparable published titles (must be actual romantic suspense, recently published)
- Target audience
- Cover image prompt (should signal both danger and romance — two people, atmospheric threat)

---

## Step 11: Generate Final .docx Files

Read `references/docx-template.md`. Generate:
1. The manuscript .docx
2. The KDP Info .docx

---

## Step 12: Final Verification and Delivery

Before delivering:
- [ ] Manuscript .docx is non-empty, correct file size for word count
- [ ] All chapters are fully written prose — no summaries or placeholders
- [ ] KDP Info .docx is complete
- [ ] Style Guide .md is saved
- [ ] World Bible updated if series
- [ ] Dual-track compliance confirmed (romance + suspense both present throughout)
- [ ] Black moment breaks both tracks
- [ ] HEA delivered after external resolution
- [ ] Sweet/clean — zero explicit content
- [ ] Voice matches style guide

Present all files to the user with a brief summary.

---

## Names & Places to Avoid

**Hero names to avoid**: Ryan, Chase, Liam, Connor, Ethan, Aiden, Grayson, Hunter, Cole
**Heroine names to avoid**: Emma, Sophia, Ava, Olivia, Isabella, Madison, Lily, Grace
**Thriller-style names to avoid**: Sarah, Jack, Kate, Tom, Marcus (villain), Elena (brilliant anything)
**Estate/setting names to avoid**: Blackwood, Ravenwood, Thornfield, Hawthorne, Graystone, Silverlake
**Title words to avoid**: Hidden, Dark, Silent, Secret, Deadly, Dangerous, Perfect, Last, Gone, Missing, Broken, Shattered

**Instead**: Use names that feel specific to the characters' demographics, regions, and time period. The more grounded the names, the more real the world feels.
