---
name: romance-writer
description: >
  Turn a romance outline into a complete, publish-ready manuscript. Accepts outlines from the
  Romance Outline Pipeline skill OR any custom outline. Builds a custom style guide from the
  user's own writing sample (and optionally a separate spicy scene sample) so the manuscript
  matches their voice. Full editorial pipeline: AI-ism scrub, developmental edit, beta read,
  and targeted revision. Outputs a single .docx manuscript plus a KDP metadata companion doc.
  MANDATORY TRIGGERS: "write my romance", "write from outline", "romance writer", "turn outline
  into manuscript", "write this story", "manuscript from outline", "write the book", "write
  chapters", "draft manuscript", or any mention of turning a romance outline into a full
  manuscript. Use this skill when the user has a romance outline and wants it written into prose.
---

# Romance Writer

Turn a romance outline into a complete, polished manuscript. This skill takes an outline (from the Romance Outline Pipeline or any custom outline), analyzes the user's writing style from their uploaded samples, and produces a publish-ready .docx manuscript with a full editorial pipeline.

## What This Skill Produces

For each run, exactly 2-3 files:

| File | Description |
|------|-------------|
| `[Title].docx` | Complete manuscript — all chapters as fully written prose |
| `[Title] - KDP Info.docx` | Amazon KDP metadata: description, keywords, categories, comp titles, cover prompt |
| `[Title] - Style Guide.md` | Reusable style guide built from the user's writing sample (saved for future projects) |

## Core Principles

- **The user's voice, not AI voice.** Every manuscript must sound like the user wrote it. The style guide drives everything — sentence patterns, dialogue style, pacing, vocabulary, heat level, narrative quirks.
- **The outline is the blueprint.** Every chapter in the outline gets written. Nothing is skipped, summarized, or condensed. The outline's trope tags, POV assignments, chapter goals, and complications are all honored.
- **Full editorial pipeline.** Raw prose goes through AI-ism scrub → developmental edit → beta read → targeted revision. The final manuscript should read like a polished, published novel.
- **Model routing for quality.** Assessment and analysis tasks (AI-ism identification, dev edit reports, beta reads) use **Sonnet** for speed and critical eye. All prose writing and rewriting (fixes, revisions, chapter rewrites) use **Opus** for maximum prose quality and voice-matching fidelity.
- **Fresh and original.** All names, places, and titles must avoid overused AI patterns. See the bundled Names & Places Avoidance List.

## Names & Places Avoidance List

Read the file `references/ai-names-avoidance.md` bundled with this skill. It contains comprehensive lists of overused AI-generated names, places, businesses, title words, and descriptive cliches. ALL generated content must avoid these throughout the entire workflow.

## Model Routing

Different stages of the pipeline use different models for optimal results. Assessment tasks need a sharp critical eye; prose tasks need the highest-quality writing.

| Step | Task | Model | Why |
|------|------|-------|-----|
| Step 5 | Write chapters | **Opus** | Prose quality and voice-matching require the strongest writing model |
| Step 6a | AI-ism identification & report | **Sonnet** | Analysis task — identifying patterns, flagging issues |
| Step 6b | AI-ism fixes (rewriting) | **Opus** | Prose rewriting must maintain the user's voice at the highest quality |
| Step 7a | Developmental edit report | **Sonnet** | Critical assessment task — structural analysis, genre compliance |
| Step 7b | Dev edit fixes (rewriting) | **Opus** | Chapter rewrites require Opus-level prose quality |
| Step 7c | Beta read report | **Sonnet** | Reader-experience analysis — identifying what doesn't land |
| Step 7d | Beta read fixes (rewriting) | **Opus** | Final prose polish must be the best possible quality |

**How to implement model routing:** When using Task subagents, specify `model: "sonnet"` or `model: "opus"` for each subagent based on the table above. The main conversation can run on any model — the routing matters for the subagent tasks where the heavy lifting happens.

## Step-by-Step Workflow

### Step 1: Outline Intake

Ask the user to upload their outline. This can be:

**From the Romance Outline Pipeline:** A .docx file containing all outline components (story idea, hook/pitch, character bios, trope mapping, romance arc, settings, chapter outline, epilogue). Parse the document and extract all sections.

**A custom outline in any format:** A .docx, .md, .txt, or pasted text containing at minimum:
- Character descriptions for both romantic leads
- A chapter-by-chapter outline (even if brief)
- The subgenre and heat level

If the user provides a custom outline that's missing key elements, ask them to fill in:
- **Subgenre** (if not specified)
- **Heat level**: Sweet/Clean, Moderate (fade to black), Steamy (open door), or Scorching (explicit)
- **POV style**: First person or third person? Present or past tense? Alternating POV or single POV?
- **Target word count per chapter** (default: ~2,500 words for novels, ~1,500 for novellas)
- **Total chapter count** (if not clear from outline)

Once the outline is fully understood, summarize what you'll be writing and confirm with the user before proceeding.

### Step 2: Style Guide — General Writing Sample

Ask the user:

"To make this manuscript sound like YOU, I need a sample of your writing. Upload any piece of fiction you've written — a previous book, a few chapters of a WIP, or even a short story. The longer the sample, the more accurately I can capture your voice."

Use AskUserQuestion:

**Question**: "Do you have a writing sample I can use to match your style?"

**Options**:
- **Yes, I'll upload one** — "I have a sample of my fiction writing to share"
- **No writing sample** — "Write it in a style that fits the genre"

#### If the user uploads a sample:

Read the full uploaded file and analyze their writing style across these dimensions:

**Sentence Structure & Rhythm**
- Average sentence length (short and punchy? Long and flowing? Mixed?)
- Sentence variation patterns (do they follow a long sentence with a short one for effect?)
- Fragment usage (do they use fragments for emphasis?)
- Use of em-dashes, semicolons, parentheticals

**Narrative Voice & POV Depth**
- How deep does the narrator go into internal monologue?
- Is the voice conversational, literary, spare, lush?
- How much does the narrator editorialize vs. observe?
- Self-awareness level (does the character comment on their own behavior?)
- Humor style (dry, self-deprecating, witty, physical comedy, situational?)

**Dialogue Style**
- Dialogue-to-narrative ratio (heavy dialogue? Long narrative stretches?)
- How characters speak (contractions? Slang? Formal? Regional?)
- Dialogue tag usage (minimal "said" only? Action beats? Varied tags?)
- Banter patterns (quick volleys? Longer exchanges? Interruptions?)

**Pacing & Scene Construction**
- Scene length patterns (short scenes? Long immersive scenes?)
- How they handle transitions (hard cuts? Bridging sentences? Time skips?)
- Action vs. reflection balance
- How they handle emotional beats (direct? Subtext? Physical reactions?)

**Descriptive Style**
- Sensory detail density (sparse? Rich? Which senses do they favor?)
- Setting description approach (woven in? Front-loaded? Minimal?)
- Character description approach (detailed? Impressionistic? Compared to objects/feelings?)
- Metaphor/simile usage (frequent? Rare? Style of comparisons?)

**Vocabulary & Word Choice**
- Vocabulary level (accessible? Literary? Genre-specific?)
- Distinctive word preferences or verbal tics
- Profanity usage and level
- Names for body parts, emotions, actions (important for romance)

**Heat Level Execution** (if applicable from general sample)
- How they handle physical attraction descriptions
- Tension-building techniques
- Level of explicitness in romantic/intimate moments

Present the style guide to the user for confirmation. Ask: "Does this capture your voice? Anything I should adjust?"

#### If no writing sample:

Ask what style/tone they want:
- Name 2-3 authors whose style they admire
- Describe the reading experience they want (funny and fast? Emotional and immersive? Dark and atmospheric?)
- Build a lighter style guide from these preferences

### Step 3: Style Guide — Spicy Scene Sample (Heat Level Dependent)

**Skip this step if the heat level is Sweet/Clean or Moderate (fade to black).**

For Steamy or Scorching heat levels, ask:

"Since your story includes open-door intimate scenes, I'd love to see a sample of YOUR spicy writing — a scene or chapter where you've written intimacy before. This helps me match your comfort level, the words you use, how explicit you go, and how you balance the physical with the emotional."

Use AskUserQuestion:

**Question**: "Do you have a sample of your spicy/intimate writing?"

**Options**:
- **Yes, I'll upload one** — "I have a spicy scene sample to share"
- **No spicy sample** — "Match the heat level to the genre standard"

#### If the user uploads a spicy sample:

Read and analyze specifically:
- **Explicitness level** — How graphic? Clinical terms, euphemisms, or somewhere between?
- **Body language vocabulary** — What words do they use for body parts, sensations, actions?
- **Emotional integration** — How much emotional/psychological content is woven into physical scenes?
- **Pacing of intimate scenes** — Fast and intense? Slow and savoring? Building?
- **POV during intimacy** — How deep into the character's head? What do they notice?
- **Scene structure** — How do they enter and exit intimate scenes? Fade in/out points?
- **Tension-building patterns** — What happens before the scene? How is anticipation built?
- **Afterglow handling** — What happens after? Pillow talk? Humor? Vulnerability?
- **Language boundaries** — Any words they avoid? Any they clearly prefer?

Add this as a "Spicy Scene Style" section to the style guide.

#### If no spicy sample:

Ask about their preferences:
- Preferred level of explicitness (tasteful but clear? Highly explicit? Somewhere between?)
- Any words or euphemisms they prefer or want to avoid
- How much emotional content they want during intimate scenes
- Build a lighter spicy style section from these preferences

### Step 4: Save the Style Guide

Compile the full style guide (general + spicy if applicable) and save it as a standalone file:

**`[Author Name or "My"] Style Guide.md`**

Save this to the output folder. Tell the user:

"I've saved your style guide as a separate file. You can upload this for any future writing projects so we can skip the analysis step and go straight to writing."

### Step 5: Write the Manuscript

For each chapter in the outline, write complete prose following:

1. **The style guide** — Every sentence should sound like the user's voice. Match their patterns, vocabulary, pacing, and quirks.
2. **The outline** — Honor the POV assignment, chapter goal, complication, character decision, consequence, and emotional arc specified for each chapter.
3. **Trope delivery** — The trope tags on each chapter tell you which tropes to advance. Make sure the trope-specific scenes land.
4. **The romance arc** — The relationship must progress according to the arc in the outline. Each chapter should move the emotional needle.

**Chapter specifications:**
- Target the word count specified in the outline intake (default ~2,500 for novels, ~1,500 for novellas)
- Every chapter is fully written prose — NOT outlines, summaries, or bracketed placeholders
- POV stays locked to the assigned character for the entire chapter. No head-hopping.
- Intimate moment chapters marked in the outline should be written at the heat level established in the style guide

**CRITICAL — COMPLETENESS REQUIREMENT:** Every single chapter must be fully written prose. No bracketed summaries, no outline notes, no "[Chapter continues with...]" placeholders. If context is limited, break the work into smaller chunks (e.g., chapters 1-5, then 6-10, etc.) rather than summarizing later chapters. A manuscript with summarized chapters is a failed manuscript.

Use Task subagents to write chapters in batches when possible. Give each subagent:
- The full style guide
- The outline for the chapters they're writing
- Character bios and the romance arc
- The trope scene mapping
- The names avoidance list
- Chapters already written (for continuity)

### Step 5b: Structural Quality Checks (Before Revision)

Before moving to the editorial pipeline, verify each chapter against these patterns:

**Romance as A-plot check:**
- Is the love interest present, mentioned, or on the POV character's mind in every chapter?
- Does every chapter advance the romantic relationship?
- Is the climax about the relationship?

**Trope delivery check:**
- Cross-reference each chapter's trope tags from the outline. Are those tropes actually present in the prose?
- Are the must-have trope scenes from the trope mapping all accounted for?

**Style guide compliance check:**
- Read back 2-3 sample chapters and compare to the style guide. Does the prose match the user's voice?
- Check dialogue patterns, sentence rhythm, descriptive density, and humor style.

**Heat level compliance check (if Steamy/Scorching):**
- Do intimate scenes match the spicy style guide?
- Are they at the right explicitness level with the right vocabulary?

**Completeness check:**
- Verify every chapter is full prose — no summaries, outlines, or placeholders anywhere.

Fix any issues before proceeding to the editorial pipeline.

### Step 6a: AI-Ism Identification Report *(Sonnet)*

Read `references/revision-guide.md` for the complete editorial checklist. Use a **Sonnet** subagent to analyze the full manuscript and produce a detailed AI-ism report. The report should flag every instance across every chapter, organized by category:

**Structure, pacing, and flow issues:**
- Philosophical wrap-ups, forced cliffhangers, manufactured dramatic endings
- Chapters ending on tidy emotional summaries instead of mid-scene or forward momentum
- Mechanical chapter structure (setup → conflict → realization → wrap-up)

**AI artifact instances:**
- Connector words: "Additionally," "Furthermore," "Moreover," "It's worth noting," etc.
- Emotional over-labeling (naming emotions instead of showing them through body/behavior)
- Clinical precision ("After approximately forty-five seconds of silence...")
- Meta-commentary or prompt leakage
- POV breaks (narrator knowing things they can't perceive)

**Dialogue problems:**
- Stiff or formal dialogue that doesn't sound like real speech
- Perfect call-and-response patterns (ping-pong exchanges)
- Overuse of surnames when first names would be natural
- Missing natural interruptions, pauses, and conversational messiness

**Narrative authenticity issues:**
- Forced metaphors that don't fit the POV character
- Inflated sentence structures
- Sensory detail not grounded in the active POV character's awareness

**Style guide drift:**
- Any passages where the prose has drifted from the user's voice
- Sentence patterns, vocabulary, or descriptive density that don't match the style guide

The Sonnet subagent should deliver a chapter-by-chapter report with specific passages quoted and specific fixes recommended. This report feeds directly into Step 6b.

### Step 6b: AI-Ism Fixes *(Opus)*

Use an **Opus** subagent to take the AI-ism report from Step 6a and rewrite every flagged passage. Give the Opus subagent:
- The full manuscript text
- The AI-ism report with all flagged passages
- The user's style guide
- The spicy style guide (if applicable)

**CRITICAL: Maintain the user's voice throughout revision.** The AI-ism fixes should remove robotic patterns WITHOUT replacing them with a generic editorial voice. Every rewrite must sound like the user's style guide, not like a different writer. Opus should match the user's sentence rhythms, vocabulary level, and narrative quirks.

Regenerate the .docx with all fixes applied before proceeding.

### Step 7a: Developmental Edit Report *(Sonnet)*

Read `references/dev-edit-prompt.md` for the full developmental edit framework. Use a **Sonnet** subagent to produce a comprehensive dev edit report covering:

1. **Romance as A-plot** — Is the romance central in every chapter?
2. **Heat level & intimate scene assessment** — Does the heat level match? Are intimate scenes well-paced and emotionally integrated?
3. **Subgenre compliance** — Does it deliver what the specific subgenre promises?
4. **Story structure & pacing** — Are beats properly placed? Any sag or rush?
5. **Plot & conflict** — Is the central conflict compelling and sustained?
6. **Character development** — Are arcs earned and paced?
7. **POV & narrative voice** — Is the voice consistent? Does it match the style guide?
8. **Dialogue & banter** — Does it sound real?
9. **Emotional resonance** — Does it deliver the payoff readers expect?

The Sonnet subagent should deliver: Executive Summary, Detailed Notes (with chapter references), Priority Action Items (ranked, top 5-7), and What's Working. This report feeds directly into Step 7b.

### Step 7b: Dev Edit Fixes *(Opus)*

Use an **Opus** subagent to take the top 5 Priority Action Items from the dev edit report and apply them. Give the Opus subagent:
- The full manuscript text
- The dev edit report
- The user's style guide (and spicy style guide if applicable)
- The original outline (for reference on intended structure)

Genre drift (romance not the A-plot, comedy missing if it's a romcom, heat level wrong) is ALWAYS the #1 priority.

For each fix, the Opus subagent should identify which chapters need rewriting and rewrite them as complete prose — maintaining word count and the user's voice. No chapter should lose length during revision.

Regenerate the .docx with all fixes applied before proceeding.

### Step 7c: Beta Read Report *(Sonnet)*

Use a **Sonnet** subagent to run a critical beta read on the revised manuscript. Frame the beta reader as someone who reads heavily in the specific subgenre and writes critical Goodreads reviews.

The beta review must include:
1. **Star rating** (out of 5) — honest, not generous. Most first drafts land 3-3.5 stars. A 4+ means no major structural issues.
2. **The Good** — specific scenes, dynamics, and moments that work. Name chapters and characters.
3. **The Bad** — specific problems with chapter references. Pacing, character, dialogue, plot, and structure issues.
4. **Suggestions for Improving** (ranked by importance) — 3-5 structural fixes with specific chapter references and concrete solutions.

**Beta read calibration:** Judge the book against OTHER ROMANCE in its subgenre, not literary fiction. Focus on problems a targeted chapter rewrite can fix. The most valuable feedback identifies the SINGLE BIGGEST structural problem and explains why it matters.

This report feeds directly into Step 7d.

### Step 7d: Beta Read Fixes *(Opus)*

Use an **Opus** subagent to take the top 3 suggestions from the beta review and apply them. Give the Opus subagent:
- The full manuscript text
- The beta read report
- The user's style guide (and spicy style guide if applicable)

For each fix:
1. Identify which chapters need rewriting
2. Rewrite those chapters as complete prose (maintaining word count — revision means improving, not cutting)
3. Check for continuity: if you restructured chapter 8, make sure chapters 7 and 9 still connect
4. Verify the user's voice is maintained throughout all rewrites

Regenerate the final .docx with all fixes applied.

### Step 8: Create KDP Info Document

Read `references/kdp-template.md` for the full template. Create a companion document including:
- Book title and subtitle suggestion
- Amazon book description (4000 char max, keyword-rich)
- 7 Amazon keyword phrases
- 3 BISAC category suggestions
- Suggested price point
- Series potential notes
- 3-5 comparable real published titles
- Target audience description
- Cover image prompt (detailed, ready for AI image generation)

### Step 9: Generate Final .docx

Use the `docx` npm package to create the manuscript .docx file. Read `references/docx-template.md` for the exact formatting specifications.

The manuscript must include:
- Title page with book title and author name (from outline or user-provided)
- All chapters as fully written, revised prose
- Proper formatting (Times New Roman 12pt, 1.5 line spacing, 1-inch margins)
- Page breaks between chapters

### Step 10: Final Verification

Verify before delivering:
- [ ] Manuscript .docx is non-empty and the correct file size for the word count
- [ ] All chapters are fully written prose — no summaries, outlines, or placeholders
- [ ] KDP Info .docx is complete with all required sections
- [ ] Style Guide .md is saved as a standalone file
- [ ] The prose matches the user's style guide voice
- [ ] Heat level matches what was specified
- [ ] All trope scenes from the outline are present in the manuscript
- [ ] The romance arc follows the outline's emotional beats

Present all files to the user with a brief summary of what was written.

## Important Reminders

- **The style guide is king.** Every sentence should sound like the user wrote it. If there's a conflict between "good writing" and "matching the user's voice," the user's voice wins.
- **The outline is the blueprint.** Don't deviate from the outline unless something genuinely doesn't work narratively — and if so, flag it to the user before changing it.
- **Every chapter must be complete prose.** This is the #1 failure mode. If context runs low, break into smaller batches. Never summarize.
- **The editorial pipeline is not optional.** Raw LLM prose has telltale patterns. The revision passes exist to remove them. Don't skip any step.
- **Heat level must match.** A Scorching outline should produce Scorching prose. A Sweet/Clean outline should have zero explicit content. The spicy style guide (if provided) dictates exactly how to write intimate scenes.
