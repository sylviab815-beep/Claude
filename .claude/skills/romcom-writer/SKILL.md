---
name: romcom-writer
description: >
  Turn a romantic comedy outline into a complete, publish-ready manuscript.
  Accepts outlines from the Romantic Comedy Outline skill OR any custom
  outline. Builds a custom style guide from the user's writing sample,
  including a comedic voice analysis. Enforces comedy-in-every-chapter.
  Full editorial pipeline: AI-ism scrub, developmental edit (with comedy
  compliance check), beta read, and targeted revision. Outputs a manuscript
  .docx plus KDP metadata companion doc. MANDATORY TRIGGERS: "write my
  romcom", "romcom writer", "write my romantic comedy", "turn outline into
  manuscript", "write this rom-com", "write my rom-com", "manuscript from
  outline", or any mention of writing a romantic comedy manuscript.
---

# Romantic Comedy Writer

Turn a romantic comedy outline into a complete, polished manuscript. This skill takes a rom-com outline (from the Romantic Comedy Outline skill or any custom outline), analyzes the user's comedic voice from their writing sample, and produces a publish-ready .docx with a full editorial pipeline.

## What This Skill Produces

| File | Description |
|------|-------------|
| `[Title].docx` | Complete manuscript — all chapters as fully written prose |
| `[Title] - KDP Info.docx` | Amazon KDP metadata, keywords, categories, cover prompt |
| `[Title] - Style Guide.md` | Reusable style guide including comedic voice analysis |

## Core Principles

- **The user's voice, not AI voice.** Every sentence sounds like the user wrote it. The style guide — especially the comedic voice section — drives everything.
- **Comedy in every chapter.** A rom-com that stops being funny to be romantic has failed. Every chapter must have at least one genuine laugh. This is non-negotiable and is the first thing checked in revision.
- **The outline is the blueprint.** Every chapter gets written. The comedy beat map, set pieces, running gags, and misunderstanding arc are all honored. Nothing is skipped.
- **Full editorial pipeline.** Raw prose goes through AI-ism scrub → developmental edit (comedy + romance compliance) → beta read → targeted revision.
- **Model routing for quality.** Assessment tasks use **Sonnet**. All prose writing and rewriting uses **Opus**.
- **Fresh and original.** All names and places avoid overused AI patterns. See the bundled Names & Places Avoidance List.

## Names & Places Avoidance List

Read `references/ai-names-avoidance.md` before generating any content.

## Model Routing

| Step | Task | Model |
|------|------|-------|
| Step 4 | Write chapters | **Opus** |
| Step 5a | AI-ism report | **Sonnet** |
| Step 5b | AI-ism fixes | **Opus** |
| Step 6a | Dev edit report | **Sonnet** |
| Step 6b | Dev edit fixes | **Opus** |
| Step 7a | Beta read report | **Sonnet** |
| Step 7b | Beta read fixes | **Opus** |

## Step-by-Step Workflow

### Step 1: Outline Intake

Ask the user to upload their outline. This can be:

**From the Romantic Comedy Outline skill:** A .docx file containing story idea, hook/pitch, H1 and H2 bios, comedy beat map, romance arc, supporting cast, settings, and chapter outline. Parse all sections.

**A custom outline:** Any format. At minimum it should include:
- Character descriptions for both leads
- Chapter-by-chapter outline
- The central comedic premise
- Heat level

If key elements are missing, ask for:
- **Heat level** (0 = Inspirational/Christian, 1 = Sweet/Clean, 2 = Fade to black, 3 = Sensual)
- **POV style**: First or third person? Past or present tense? Alternating or single POV?
- **Target word count per chapter** (default: ~2,500 for novels, ~1,500 for novellas)
- **Comedy beat map**: Set pieces, running gags, the misunderstanding arc, the grovel — if not in the outline, ask the user to describe them

Summarize what you'll be writing and confirm before proceeding.

### Step 2: Style Guide — General Writing Sample

Ask the user:

"To make this manuscript sound like YOU, I need a sample of your writing. Any piece of fiction — a previous book, chapters from a WIP, a short story — works. The longer the sample, the better I can capture your voice."

Use AskUserQuestion:
- **Yes, I'll upload one**
- **No writing sample** — "Write in a style that fits the genre"

#### If the user uploads a sample:

Analyze across all standard dimensions (sentence structure, rhythm, dialogue, pacing, descriptive style, vocabulary) PLUS the **Comedic Voice** section below.

**Comedic Voice Analysis (Essential for Rom-Com)**

- **Humor style**: Dry and understated? Broad and physical? Self-deprecating? Situational irony? Witty wordplay? Absurdist?
- **Comic timing in prose**: How do they build to a punchline in narrative? Do they use sentence rhythm for comedic effect (long setup, short payoff)? Fragment for emphasis?
- **Internal monologue humor**: Does the narrator make jokes to themselves? Are they self-aware about their own disasters?
- **Dialogue comedy**: Is their banter quick back-and-forth? Does one character always "win" exchanges? Do they write comedic misreadings of situations?
- **Physical comedy vs. verbal comedy**: Do they lean on situational set pieces or witty dialogue?
- **Tone calibration**: Where on the spectrum between "warm and funny" and "chaotic and farcical" does their humor land?
- **The straight man dynamic**: Do they write a more grounded character alongside the comedic lead, or are both characters funny in different ways?

Present the full style guide (including comedic voice section) for user confirmation.

#### If no writing sample:

Ask:
- Name 2-3 rom-com authors whose style they admire
- Describe the humor: dry and witty, warm and goofy, chaotic and physical?
- Build a lighter style guide from these preferences

### Step 3: Save the Style Guide

Save as: **`[Author Name or "My"] Style Guide.md`**

Tell the user: "I've saved your style guide — including your comedic voice profile — as a standalone file. Upload it for any future projects to skip the analysis step."

### Step 4: Write the Manuscript

For each chapter, write complete prose following:

1. **The style guide** — especially the comedic voice. Every chapter must sound like the user's humor, not generic rom-com.
2. **The outline** — honor POV, chapter goal, complication, decision, consequence, The Funny, and The Romantic for each chapter.
3. **Comedy in every chapter** — this is the #1 rule. Every chapter must have at least one genuine laugh built from character and situation, not layered-on jokes. Reference the comedy beat map for set pieces, running gags, and the misunderstanding arc.
4. **The romance arc** — emotional connection must progress chapter by chapter alongside the comedy.
5. **Heat level compliance** — strictly honor the heat level from the outline intake.

**Chapter specifications:**
- Target word count from outline intake (default ~2,500 novels, ~1,500 novellas)
- Every chapter is fully written prose — NO outlines, summaries, or placeholders
- POV stays locked to the assigned character per chapter

**CRITICAL — COMPLETENESS:** Every chapter must be full prose. No summaries, no "[Chapter continues...]" placeholders. Break into smaller batches rather than summarizing.

Use Task subagents to write chapters in batches. Give each subagent:
- The full style guide (especially the comedic voice section)
- The comedy beat map
- The outline for their assigned chapters
- H1 and H2 bios
- The romance arc
- The names avoidance list
- Previously written chapters (for continuity of running gags and character voice)

### Step 4b: Structural Quality Checks

Before editorial pipeline:

**Comedy compliance check (MOST IMPORTANT):**
- Does every chapter have at least one genuine laugh?
- Are the set pieces from the comedy beat map present and fully written?
- Are the running gags appearing consistently (and escalating)?
- Is the misunderstanding arc building correctly?
- Does the grovel land as both funny AND emotionally moving?

**Romance compliance check:**
- Is the love interest present or on the narrator's mind in every chapter?
- Does the romantic tension escalate appropriately?
- Does the HEA feel earned?

**Heat level compliance:**
- Is every chapter within the stated heat level?
- For 0-1: Nothing beyond a kiss. For 2: Fade to black before any explicit content.

**Style guide compliance:**
- Does the prose match the user's comedic voice?
- Are sentence rhythm and humor style consistent?

**Completeness check:** Every chapter full prose, no placeholders.

Fix before proceeding.

### Step 5a: AI-Ism Identification Report *(Sonnet)*

Read `references/revision-guide.md`. Use a **Sonnet** subagent to analyze and produce a detailed report flagging:

**Comedy killers (rom-com specific):**
- Chapters with no genuine laugh
- Jokes explained after they land ("...she thought, realizing how absurd this was")
- Banter that's too perfect — every line a winner, no setup lines, no missed beats
- Internal monologue that's self-analyzing rather than self-aware and funny
- Comedy that stops for a serious scene and never recovers its tone
- Running gags that appear but don't escalate

**Standard AI artifacts:**
- Connector words, emotional over-labeling, clinical precision, POV breaks
- Mechanical chapter structure, tidy emotional wrap-ups
- Dialogue that sounds like a script, not real people

**Style guide drift:**
- Prose that no longer sounds like the user's comedic voice

### Step 5b: AI-Ism Fixes *(Opus)*

Use an **Opus** subagent to rewrite every flagged passage. Every fix must sound like the user's voice — especially their comedic voice. Regenerate the .docx.

### Step 6a: Developmental Edit Report *(Sonnet)*

Read `references/dev-edit-prompt.md`. Use a **Sonnet** subagent to assess:

1. **Comedy compliance** — Is it funny in every chapter? Do the set pieces land?
2. **Romance as A-plot alongside the comedy** — Are both working together?
3. **The misunderstanding arc** — Is it earned and escalating?
4. **The grovel** — Does it land as both funny and emotionally satisfying?
5. **Heat level compliance** — Is every chapter within the stated level?
6. **Story structure and pacing**
7. **Character development and voice**
8. **Dialogue and banter**
9. **Emotional resonance and HEA delivery**

### Step 6b: Dev Edit Fixes *(Opus)*

Apply top 5 Priority Action Items from the dev edit report. Comedy compliance problems are always #1 if present. Regenerate the .docx.

### Step 7a: Beta Read Report *(Sonnet)*

Use a **Sonnet** subagent as a reader who reads heavily in clean/sweet romantic comedy and writes Goodreads reviews. Include:

1. **Star rating** (honest — most first drafts land 3-3.5 stars)
2. **The Good** — specific funny moments and romantic scenes that work
3. **The Bad** — where the comedy fell flat or the romance stalled
4. **Suggestions** (ranked, top 3-5)

**Calibration**: Judge against published clean/sweet rom-com. Did it make them laugh? Did they root for the couple? Was there chemistry? Did the grovel feel earned?

### Step 7b: Beta Read Fixes *(Opus)*

Apply top 3 suggestions from the beta read. Maintain word count and comedic voice. Regenerate the final .docx.

### Step 8: KDP Info Document

Read `references/kdp-template.md`. Create companion document with:
- Book title and subtitle suggestion
- Amazon book description (keyword-rich, max 4000 characters, structured for rom-com)
- 7 Amazon keyword phrases
- 3 BISAC category suggestions (note: Romance-Contemporary and Romance-Romantic Comedy are the primary categories)
- Suggested price point
- Cover image prompt — **must specify illustrated/cartoon cover style** as this is the current market standard for rom-com
- Series potential notes
- 3-5 comparable published titles
- Target audience description

### Step 9: Generate Final .docx

Use the `docx` npm package. Read `references/docx-template.md` for formatting specs. Include title page, all chapters as revised prose, proper formatting (Times New Roman 12pt, 1.5 line spacing, 1-inch margins), page breaks between chapters.

### Step 10: Final Verification

Before delivering:
- [ ] Manuscript .docx is correct file size for word count
- [ ] Every chapter has at least one genuine laugh
- [ ] All set pieces from the comedy beat map are present and fully written
- [ ] Running gags appear consistently and escalate
- [ ] The misunderstanding arc builds and resolves correctly
- [ ] The grovel is both funny and emotionally satisfying
- [ ] Heat level is honored throughout
- [ ] All chapters are full prose — no summaries or placeholders
- [ ] The prose matches the user's comedic voice
- [ ] KDP Info document is complete (with illustrated cover prompt)
- [ ] Style Guide is saved as standalone file

## Important Reminders

- **Comedy in every chapter.** No exceptions. A chapter without a laugh is out of genre.
- **The user's comedic voice is king.** If there's a conflict between "funnier" and "matching their voice," their voice wins.
- **The outline is the blueprint.** Don't deviate from the comedy beat map without flagging it.
- **The grovel must earn its moment.** It should be a little ridiculous, emotionally vulnerable, and satisfying. The HEA should feel like it took the whole book to get there.
- **Heat level is a promise.** Honor it exactly.
