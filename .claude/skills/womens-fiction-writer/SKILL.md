---
name: womens-fiction-writer
description: >
  Turn a women's fiction outline into a complete, publish-ready manuscript.
  Accepts outlines from the Women's Fiction Outline skill OR any custom outline.
  Builds a custom style guide from the user's writing sample so the manuscript
  matches their voice. The protagonist's transformation arc — not a romance — is
  the A-plot. Full editorial pipeline: AI-ism scrub, developmental edit, beta
  read, and targeted revision. Outputs a manuscript .docx plus a KDP metadata
  companion doc. MANDATORY TRIGGERS: "write my women's fiction", "women's fiction
  writer", "write from outline", "turn outline into manuscript", "write this
  story", "manuscript from outline", "write the book", "write my novel", or any
  mention of writing a women's fiction manuscript from an outline.
---

# Women's Fiction Writer

Turn a women's fiction outline into a complete, polished manuscript. This skill takes an outline (from the Women's Fiction Outline skill or any custom outline), analyzes the user's writing style from their uploaded sample, and produces a publish-ready .docx manuscript with a full editorial pipeline.

## What This Skill Produces

For each run, 2-3 files:

| File | Description |
|------|-------------|
| `[Title].docx` | Complete manuscript — all chapters as fully written prose |
| `[Title] - KDP Info.docx` | Amazon KDP metadata, keywords, categories, cover prompt |
| `[Title] - Style Guide.md` | Reusable style guide built from user's writing sample |

## Core Principles

- **The user's voice, not AI voice.** Every manuscript sounds like the user wrote it. The style guide drives everything — sentence patterns, dialogue style, pacing, interiority, vocabulary, and narrative quirks.
- **The protagonist's transformation is the A-plot.** In women's fiction, the central story is the protagonist's inner journey. The love interest (if any) supports rather than drives the narrative. Every chapter should advance who she is becoming.
- **The outline is the blueprint.** Every chapter gets written in full. Nothing is skipped, summarized, or condensed. POV assignments, chapter goals, complications, key relationship moments, and emotional landing points are all honored.
- **Full editorial pipeline.** Raw prose goes through AI-ism scrub → developmental edit → beta read → targeted revision. The final manuscript should read like a polished, published novel.
- **Model routing for quality.** Assessment tasks use **Sonnet**. All prose writing and rewriting uses **Opus** for maximum quality and voice-matching fidelity.
- **Fresh and original.** All names, places, and titles avoid overused AI patterns. See the bundled Names & Places Avoidance List.

## Names & Places Avoidance List

Read `references/ai-names-avoidance.md` before generating any content. It contains comprehensive lists of overused AI-generated names, places, businesses, title words, and descriptive clichés. ALL generated content must avoid these throughout the entire workflow.

## Model Routing

| Step | Task | Model |
|------|------|-------|
| Step 5 | Write chapters | **Opus** |
| Step 6a | AI-ism identification report | **Sonnet** |
| Step 6b | AI-ism fixes (rewriting) | **Opus** |
| Step 7a | Developmental edit report | **Sonnet** |
| Step 7b | Dev edit fixes (rewriting) | **Opus** |
| Step 7c | Beta read report | **Sonnet** |
| Step 7d | Beta read fixes (rewriting) | **Opus** |

When using Task subagents, specify `model: "sonnet"` or `model: "opus"` accordingly.

## Step-by-Step Workflow

### Step 1: Outline Intake

Ask the user to upload their outline. This can be:

**From the Women's Fiction Outline skill:** A .docx file containing story idea, hook/pitch, protagonist bio (with wound/lie/truth), transformation arc, ensemble cast bios, settings, and chapter outline. Parse all sections.

**A custom outline in any format:** A .docx, .md, .txt, or pasted text. At minimum, it should include:
- Protagonist description and her core wound/lie/truth (or equivalent)
- A chapter-by-chapter outline (even if brief)
- The story's central themes and emotional arc

If the outline is missing key elements, ask the user to fill in:
- **Story category** (midlife reinvention, grief & healing, family saga, sisterhood, etc.)
- **POV style**: First person or third person? Past or present tense? Single protagonist POV or small rotating ensemble?
- **Target word count per chapter** (default: ~2,500 for novels, ~1,500 for novellas)
- **Total chapter count** (if not clear)
- **Romance present?** (If yes: Is it a significant subplot or a light thread? How does it resolve?)

Once the outline is fully understood, summarize what you'll be writing and confirm with the user before proceeding.

### Step 2: Style Guide — Writing Sample

Ask the user:

"To make this manuscript sound like YOU, I need a sample of your writing. Upload any piece of fiction you've written — a previous book, chapters from a WIP, or even a short story. The longer the sample, the more accurately I can capture your voice."

Use AskUserQuestion:

**Question**: "Do you have a writing sample I can use to match your style?"

**Options**:
- **Yes, I'll upload one** — "I have a sample of my fiction writing to share"
- **No writing sample** — "Write it in a style that fits the genre"

#### If the user uploads a sample:

Read the full uploaded file and analyze:

**Sentence Structure & Rhythm**
- Average sentence length (short and punchy? Long and flowing? Mixed?)
- Variation patterns, fragment usage, em-dashes, semicolons

**Narrative Voice & Interiority**
- How deep does the narrator go into internal monologue?
- Is the voice conversational, literary, spare, lush?
- How much does the narrator editorialize vs. observe?
- Self-awareness level — does the character comment on her own behavior?
- Humor style (dry, self-deprecating, wry, absent?)

**Dialogue Style**
- Dialogue-to-narrative ratio
- How characters speak (contractions, register, regional touches)
- Dialogue tag preferences (minimal "said"? Action beats?)
- Banter patterns — quick or slow?

**Pacing & Scene Construction**
- Scene length, how they handle transitions, interiority-to-action balance
- How emotional beats are handled (direct, subtext, physical reaction?)

**Descriptive Style**
- Sensory detail density, setting approach, metaphor and simile usage

**Vocabulary & Word Choice**
- Vocabulary level and distinctive verbal tics
- Profanity level
- How they describe internal emotional states

Present the style guide for user confirmation: "Does this capture your voice? Anything to adjust?"

#### If no writing sample:

Ask what style/tone they want:
- Name 2-3 authors whose style they admire
- Describe the reading experience they want (funny and fast? Quiet and immersive? Raw and emotional?)
- Build a lighter style guide from these preferences

### Step 3: Save the Style Guide

Compile the full style guide and save as:

**`[Author Name or "My"] Style Guide.md`**

Tell the user: "I've saved your style guide as a separate file. You can upload this for any future writing projects to skip the analysis step."

### Step 4: Write the Manuscript

For each chapter in the outline, write complete prose following:

1. **The style guide** — Every sentence should sound like the user's voice.
2. **The outline** — Honor the POV, chapter goal, complication, key relationship moment, inner state, and emotional landing point for each chapter.
3. **The transformation arc** — The protagonist's inner journey must progress visibly across chapters. Each chapter should move the emotional needle in some direction.
4. **Ensemble authenticity** — Supporting characters should feel like full people, not just satellites to the protagonist. Their relationships should be specific and lived-in.

**Chapter specifications:**
- Target the word count specified in the outline intake (default ~2,500 for novels, ~1,500 for novellas)
- Every chapter is fully written prose — NOT outlines, summaries, or bracketed placeholders
- POV stays locked to the assigned character for the entire chapter. No head-hopping.

**CRITICAL — COMPLETENESS REQUIREMENT:** Every chapter must be fully written prose. No bracketed summaries, no outline notes, no "[Chapter continues...]" placeholders. If context is limited, break the work into smaller batches rather than summarizing later chapters.

Use Task subagents to write chapters in batches. Give each subagent:
- The full style guide
- The outline for their assigned chapters
- The protagonist bio (wound/lie/truth)
- The transformation arc
- The ensemble cast bios
- The names avoidance list
- Previously written chapters (for continuity)

### Step 4b: Structural Quality Checks (Before Revision)

Before moving to the editorial pipeline, verify:

**Transformation arc check:**
- Is the protagonist's inner journey advancing in every chapter?
- Can you trace her wound → resistance → cracks → shift → transformation through the chapters?
- Is the ending earned from who she's been throughout — not a sudden change?

**Ensemble relationship check:**
- Are the key relationships (daughter, mother, best friend, etc.) distinct and emotionally specific?
- Do supporting characters feel like real people or like plot functions?
- Are the relationship dynamics changing as the protagonist changes?

**Theme delivery check:**
- Cross-reference each chapter's theme tags from the outline. Are those themes actually present in the prose?
- Are themes woven in organically or stated explicitly (which would be a problem)?

**Style guide compliance check:**
- Read 2-3 sample chapters against the style guide. Does the prose match the user's voice?

**Completeness check:**
- Verify every chapter is full prose — no summaries, outlines, or placeholders.

Fix any issues before proceeding.

### Step 5a: AI-Ism Identification Report *(Sonnet)*

Read `references/revision-guide.md` for the complete editorial checklist. Use a **Sonnet** subagent to analyze the full manuscript and produce a detailed AI-ism report flagging instances across every chapter:

**Structure, pacing, and flow:**
- Philosophical wrap-ups, forced dramatic endings, tidy emotional summaries
- Mechanical chapter structure (setup → conflict → realization → bow-tied conclusion)

**AI artifact instances:**
- Connector words: "Additionally," "Furthermore," "Moreover," "It's worth noting," etc.
- Emotional over-labeling (naming emotions instead of showing them)
- Clinical precision ("After approximately forty-five seconds...")
- Meta-commentary or prompt leakage

**Dialogue problems:**
- Stiff or formal dialogue
- Perfect ping-pong exchanges
- Missing interruptions, pauses, and conversational messiness

**Narrative authenticity issues:**
- Forced metaphors that don't fit the POV character
- Sensory detail not grounded in the POV character's awareness
- Style guide drift

Deliver a chapter-by-chapter report with specific passages quoted and specific fixes recommended.

### Step 5b: AI-Ism Fixes *(Opus)*

Use an **Opus** subagent to rewrite every flagged passage from Step 5a. Give it:
- The full manuscript text
- The AI-ism report
- The user's style guide

Every fix must sound like the user's voice, not a generic editorial voice. Regenerate the .docx with all fixes applied.

### Step 6a: Developmental Edit Report *(Sonnet)*

Read `references/dev-edit-prompt.md` for the full framework. Use a **Sonnet** subagent to assess:

1. **Protagonist's transformation as A-plot** — Is her inner journey central to every chapter?
2. **Story category compliance** — Does it deliver what its specific type of women's fiction promises?
3. **Ending integrity** — Does the ending feel earned and honest (not saccharine)?
4. **Structure & pacing** — Are transformation beats properly placed?
5. **Ensemble relationships** — Are the key relationships emotionally authentic?
6. **Character arcs** — Is the protagonist's growth paced and credible?
7. **POV & narrative voice** — Consistent and matching the style guide?
8. **Dialogue & subtext** — Does it sound real? Is subtext doing work?
9. **Theme & emotional resonance** — Are themes woven in organically?

Deliver: Executive Summary, Detailed Notes (chapter-specific), Priority Action Items (ranked), What's Working.

### Step 6b: Dev Edit Fixes *(Opus)*

Use an **Opus** subagent to apply the top 5 Priority Action Items. Give it:
- The full manuscript
- The dev edit report
- The user's style guide
- The original outline

For each fix: identify chapters needing rewriting, rewrite as complete prose maintaining word count and the user's voice. Regenerate the .docx.

### Step 7a: Beta Read Report *(Sonnet)*

Use a **Sonnet** subagent to run a critical beta read. Frame the beta reader as someone who reads heavily in women's fiction / book club fiction and writes thoughtful Goodreads reviews.

The beta review must include:
1. **Star rating** (out of 5) — honest, not generous. Most first drafts land 3-3.5 stars.
2. **The Good** — specific scenes and dynamics that work. Name chapters and characters.
3. **The Bad** — specific problems with chapter references.
4. **Suggestions for Improving** (ranked) — 3-5 structural fixes with chapter references and concrete solutions.

**Calibration:** Judge against published women's fiction in its specific category, not literary fiction. The most valuable feedback identifies the single biggest structural problem and why it matters.

### Step 7b: Beta Read Fixes *(Opus)*

Use an **Opus** subagent to apply the top 3 suggestions from the beta review. Give it:
- The full manuscript
- The beta read report
- The user's style guide

For each fix: identify chapters, rewrite as complete prose maintaining word count, check continuity across adjacent chapters, maintain the user's voice throughout. Regenerate the final .docx.

### Step 8: Create KDP Info Document

Read `references/kdp-template.md` for the full template. Create a companion document including:
- Book title and subtitle suggestion
- Amazon book description (keyword-rich, max 4000 characters)
- 7 Amazon keyword phrases
- 3 BISAC category suggestions
- Suggested price point
- Series potential notes
- 3-5 comparable published titles
- Target audience description
- Cover image prompt (detailed, ready for AI image generation)

### Step 9: Generate Final .docx

Use the `docx` npm package. Read `references/docx-template.md` for exact formatting specs. The manuscript must include:
- Title page with book title and author name
- All chapters as fully written, revised prose
- Proper formatting (Times New Roman 12pt, 1.5 line spacing, 1-inch margins)
- Page breaks between chapters

### Step 10: Final Verification

Before delivering:
- [ ] Manuscript .docx is the correct file size for the word count
- [ ] All chapters are fully written prose — no summaries, outlines, or placeholders
- [ ] KDP Info .docx is complete with all required sections
- [ ] Style Guide .md is saved as a standalone file
- [ ] The prose matches the user's style guide voice
- [ ] The protagonist's transformation arc is traceable across the manuscript
- [ ] The ending feels earned — not sudden or saccharine
- [ ] Ensemble relationships are distinct and emotionally specific

Present all files with a brief summary.

## Important Reminders

- **The style guide is king.** If there's a conflict between "good writing" and "matching the user's voice," the user's voice wins.
- **The protagonist's transformation is the A-plot.** Romance (if present) supports her arc — it does not replace it. If the romance is crowding out the protagonist's inner journey, that's a genre problem.
- **Every chapter must be complete prose.** Never summarize. Break into smaller batches instead.
- **The editorial pipeline is not optional.** Raw LLM prose has telltale patterns. Every step exists to remove them.
- **The ending must be earned and honest.** Women's fiction readers can feel a false note. The protagonist's resolution should emerge from who she's been throughout the book — not arrive as a sudden gift.
