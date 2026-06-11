---
name: manuscript-editing
description: >
  Professional fiction manuscript editing pipeline with Track Changes. This skill should be used when the user
  asks to "edit my manuscript", "run the editing pipeline", "developmental edit", "line edit",
  "proofread my book", "edit my novel", "fix my manuscript", "polish my book", "manuscript editing",
  "editing workflow", "run editing passes", "clean up my manuscript", "professional edit",
  "edit my novella", "edit my story", "fiction editing", "book editing", or any mention of
  editing, revising, polishing, or improving a fiction manuscript (.docx or .epub).
  Also trigger when the user uploads a .docx or .epub file and mentions editing, fixing,
  improving, cleaning up, or polishing it. Use this skill even if the user just says "edit this"
  while referencing a manuscript file.
version: 2.2.0
---

# Manuscript Editor Pro — Fiction Editing Pipeline with Track Changes

A professional editing workflow for fiction manuscripts. Every prose change is delivered as **Track Changes in the .docx file** so the author can accept or reject each edit individually in Microsoft Word, Google Docs, or any word processor that supports tracked changes.

## STEP 0: Output Format Selection (ALWAYS FIRST — BEFORE ANY OTHER QUESTIONS)

**Before any other question, any trope selection, any outline work, or any manuscript generation**, ask the user exactly this — word for word:

> Before we dive in — how would you like your output delivered?
>
> **A) Markdown** — everything appears directly in chat, paste-ready, lowest token cost, works great in Novelcrafter, Obsidian, or pasting into Claude
> **B) Word Document (.docx)** — formatted and downloadable
> **C) PDF** — polished and ready to print or share
>
> Just reply A, B, or C.

Wait for the user's reply. Store the answer as `OUTPUT_FORMAT = A`, `B`, or `C`.

This question is asked **ONCE, at the very start of the run**. Do NOT re-ask it mid-workflow. Carry the same `OUTPUT_FORMAT` value through every later step of this plugin.

### How OUTPUT_FORMAT controls delivery

- **If OUTPUT_FORMAT = A (Markdown in chat):**
  - **Do not create any files.** Skip every `Write` / `.docx` / `.pdf` / file-creation step in this plugin.
  - Deliver ALL outputs (outlines, chapters, bios, bibles, metadata, appendices, trackers) as clean, well-structured markdown directly in the chat response.
  - Use markdown headers (`#`, `##`, `###`), horizontal rules (`---`), bullet lists, numbered lists, and bold for structure. Keep it paste-ready for Novelcrafter / Obsidian / Claude.
  - Still produce the full content — just in chat, not in a file.

- **If OUTPUT_FORMAT = B (Word Document .docx):**
  - Follow the existing file-creation workflow exactly as written below.
  - Save the final deliverable(s) as `.docx` file(s) in the user's workspace folder and share with a `computer://` link.

- **If OUTPUT_FORMAT = C (PDF):**
  - Follow the existing file-creation workflow, but convert the final document to a `.pdf`.
  - Use the `pdf` skill or a reliable `.docx → .pdf` conversion path (pandoc, LibreOffice, or the pdf skill) to produce a polished PDF.
  - Save the `.pdf` to the user's workspace folder and share with a `computer://` link.

Apply `OUTPUT_FORMAT` consistently to **every** output section in this plugin run — final manuscript, metadata, bibles, trackers, appendices, cover prompts, everything. One choice, one format, for the whole run.

**Do not proceed to any other question until the user has answered A, B, or C.**

---


## Core Principles

1. **The author is always in control.** Every change appears as a tracked revision. Nothing is silently rewritten.
2. **The developmental edit never rewrites prose.** It produces an assessment report with issues and suggestions. The author decides what to act on.
3. **Line Edit and Proofread work directly on the .docx** using XML-level tracked changes (`<w:del>` / `<w:ins>` tags), so the author sees every deletion and insertion.
4. **The author chooses which passes to run.** Not every manuscript needs a developmental assessment. The user picks what they want.

## How the Pipeline Works

The pipeline has up to 4 stages. The user chooses which ones to run:

| Stage | What It Does | Output |
|-------|-------------|--------|
| **Developmental Assessment** | Big-picture structural analysis — plot, pacing, characters, arc, genre fit | Assessment report (.docx) with issues + suggestions. **No prose changes.** |
| **Line Edit** | Prose-level fixes — AI artifacts, show-vs-tell, crutch phrases, dialogue, voice | Manuscript .docx with **Track Changes** for every edit |
| **Proofread** | Grammar, punctuation, spelling, consistency, formatting | Manuscript .docx with **Track Changes** for every correction |
| **Continuity Audit** | Character bible, timeline, geography, world rules, object tracking | Audit report (.docx) with reference tables + any Track Changes fixes |

Passes run in order. Each starts from the output of the previous one.

## Accepted Input Formats

- **.docx** (preferred) — Works directly with the file for Track Changes
- **.epub** — Extract text using pandoc, convert to .docx, then proceed

## REQUIRED: Load the Docx Skill First

**Before doing ANY work with .docx files, you MUST read the docx SKILL.md to learn the unpack/pack/comment tooling.**

```
Read the docx skill: /sessions/*/mnt/.skills/skills/docx/SKILL.md
```

The Manuscript Editor Pro depends on the docx skill's Python scripts for unpacking .docx files into XML, inserting Track Changes, adding Word comments, and repacking. These scripts live in the docx skill's `scripts/office/` directory. You MUST read the docx SKILL.md to learn:
- The full path to `unpack.py`, `pack.py`, and `validate.py`
- The full path to `comment.py` for adding Word comments
- The correct syntax and arguments for each script

**Do NOT attempt to run `python scripts/office/unpack.py` as a relative path.** The scripts are located within the docx skill directory. After reading the docx SKILL.md, use the full absolute paths it provides.

If the docx skill is not available in this session, STOP and tell the user: "The Manuscript Editor Pro requires the docx skill to be installed. Please make sure the docx skill is available in your Cowork session."

---

## Step-by-Step Workflow

### Step 0: Setup & Pass Selection

1. **Read the docx SKILL.md** (see "REQUIRED: Load the Docx Skill First" above). Confirm you know the full paths to unpack.py, pack.py, validate.py, and comment.py before proceeding.
2. Locate the uploaded manuscript in the uploads folder or the workspace folder.
3. **Ask the user which passes they want to run.** Present the options:
   - **Full pipeline** — All 4 stages (Developmental Assessment → Line Edit → Proofread → Continuity Audit)
   - **Line Edit + Proofread** — Skip the developmental assessment (recommended for publication-ready manuscripts that just need polish)
   - **Line Edit only** — Prose quality pass with Track Changes
   - **Proofread only** — Grammar/spelling/consistency pass with Track Changes
   - **Developmental Assessment only** — Structural analysis report, no prose changes
   - **Custom** — User picks any combination
4. Create a working directory for the edit session:
   ```
   [Manuscript Title] - Edited/
   ├── [Manuscript Title] - EDITED.docx                    # Manuscript with Track Changes
   ├── [Manuscript Title] - Developmental Assessment.docx   # If dev assessment was selected
   ├── [Manuscript Title] - Editorial Report.docx           # Summary of all changes
   └── [Manuscript Title] - Continuity Audit.docx           # If continuity audit was selected
   ```
5. Extract the manuscript text for analysis. Keep the original file intact.
6. Count total words, total chapters, and note the POV, tense, and genre (infer from the text if not provided by the user).
7. Read `references/voice-matching-guide.md` and build a Voice Profile before any editing begins. This profile guides every change.

### Step 1: Developmental Assessment (Report Only — No Prose Changes)

This pass produces a **report only**. It does NOT touch the manuscript text. Not a single word of prose is changed, added, or removed.

**IDENTIFY PHASE (use model: sonnet)**

Read the full manuscript and evaluate against the developmental checklist. Read `references/dev-edit-checklist.md` for the complete framework. Produce a structured assessment covering:

- **Story Structure & Pacing** — Plot point placement, sagging middle, rushed ending, opening strength
- **Plot & Conflict** — Plot holes, logic gaps, unresolved threads, stakes escalation
- **Character Development** — Motivation, agency, arcs, distinctiveness
- **Point of View & Narrative Voice** — POV consistency, voice strength, tense consistency
- **Worldbuilding & Setting** — Grounding, info-dumping, rule consistency
- **Dialogue** — Naturalness, function, distinctiveness
- **Emotional Resonance & Theme** — Setup and payoff, thematic integration
- **Genre Conventions** — Reader expectation fulfillment

Format the assessment as:

```
## Developmental Assessment

### Strengths (preserve these)
1. [Specific strength with chapter reference] — why it works

### Critical Issues (must address)
1. [Chapter X] Issue description — why it matters — SUGGESTED APPROACH: [how the author could fix this]

### Important Issues (should address)
1. [Chapter X] Issue description — why it matters — SUGGESTED APPROACH: [suggestion]

### Minor Issues (consider addressing)
1. [Chapter X] Issue description — SUGGESTED APPROACH: [suggestion]

### Overall Recommendation
[2-3 paragraph editorial letter: what's working, what needs attention, and prioritized next steps]
```

**CRITICAL: Every issue includes a SUGGESTED APPROACH, not an automatic fix.** The author decides what to change and how. The assessment is advisory — like an editorial letter from a traditional developmental editor.

**Generate the Developmental Assessment as a .docx file** and save to the workspace folder. Then proceed to the next selected pass.

### Step 2: Line Edit (Track Changes)

This pass works at the paragraph and sentence level using **tracked changes in the .docx**.

**IDENTIFY PHASE (use model: sonnet)**

Read the manuscript chapter by chapter. Read `references/line-edit-checklist.md` for the complete framework. Flag:

- **AI Artifacts & Tells** — Robotic transitions, clinical emotion descriptions, meta-commentary, hedging language
- **Show vs. Tell Failures** — Emotions named instead of shown, exposition blocks, summary where scene should be
- **Crutch Phrases** — Repetitive constructions (track frequency of each pattern across the full manuscript)
- **Dialogue Issues** — Characters who sound the same, unnatural formality, missing subtext, therapy-speak
- **Prose Quality** — Weak verbs, passive voice clusters, filter words, redundancy, purple prose
- **Pacing at Prose Level** — Paragraph-length uniformity, scene transitions, chapter endings
- **Intimate Scene Review** (if applicable) — Apply the full intimate scene review framework

For each issue, record the EXACT text to be changed and the proposed replacement.

**FIX PHASE (use model: opus) — Track Changes**

This is where changes are applied to the actual .docx file. Use the docx skill's unpack/edit XML/repack approach:

1. **Unpack the .docx:**
   ```bash
   python scripts/office/unpack.py manuscript.docx unpacked/
   ```

2. **For each change, insert tracked change XML** in `unpacked/word/document.xml`:
   - Find the exact text from the issue list in the XML
   - Replace it with `<w:del>` (marking the original) and `<w:ins>` (marking the replacement)
   - Use "Manuscript Editor Pro" as the author for all tracked changes
   - Preserve all existing `<w:rPr>` formatting in both the deletion and insertion runs

   Example — changing "She felt a wave of sadness" to "Her throat tightened":
   ```xml
   <w:del w:id="1" w:author="Manuscript Editor Pro" w:date="2025-01-01T00:00:00Z">
     <w:r><w:rPr>[preserve original formatting]</w:rPr><w:delText>She felt a wave of sadness</w:delText></w:r>
   </w:del>
   <w:ins w:id="2" w:author="Manuscript Editor Pro" w:date="2025-01-01T00:00:00Z">
     <w:r><w:rPr>[preserve original formatting]</w:rPr><w:t>Her throat tightened</w:t></w:r>
   </w:ins>
   ```

3. **Add comments for non-obvious changes** using the comment system (see docx skill for `comment.py` usage). When a change needs context — e.g., why a specific phrase was flagged as an AI artifact or why a show-vs-tell conversion was made — add a Word comment explaining the reasoning.

4. **Repack the .docx:**
   ```bash
   python scripts/office/pack.py unpacked/ output.docx --original manuscript.docx
   ```

**Voice Matching Rule:** Before writing ANY replacement text, consult the Voice Profile from Step 0. Every replacement must pass the matching test:
- Could this have been written by the same person who wrote the rest of the manuscript?
- Does the sentence rhythm match the surrounding paragraphs?
- Is the vocabulary consistent with the author's range?

**VERIFY PHASE (use model: sonnet)**

- Open the Track Changes manuscript and review each tracked change
- Confirm all flagged issues have corresponding tracked changes
- Check that replacement text matches the Voice Profile
- Verify no new AI artifacts were introduced in replacements
- Run crutch phrase count on the replacement text — if any pattern still exceeds 3 occurrences, add more tracked changes
- If any tracked change introduces a voice inconsistency, revise the replacement text
- **MEANING PRESERVATION CHECK (REQUIRED):** For every tracked change, verify:
  1. **Same event.** Does the same thing still happen in the scene? No action, reaction, decision, or event has been added, removed, or altered.
  2. **Same emotion.** Does the character still feel the same thing? A show-vs-tell conversion from "She felt betrayed" must show BETRAYAL specifically — not anger, not sadness, not confusion. The emotion cannot shift during the conversion.
  3. **Same information.** Does the reader learn the same facts? No new information has been introduced, and no existing information has been removed or changed.
  4. **Same characterization.** Does the character still come across the same way? Removing hedging language ("seemed to," "appeared to") can make an uncertain character sound confident — if the hedging reflects the character's genuine uncertainty or the POV's limited knowledge, LEAVE IT. Only remove hedging that is clearly an AI writing artifact, not a character trait.
  5. **Same stakes.** Are the consequences and tensions in the scene unchanged?
  If ANY tracked change fails this check, REVERT it or revise the replacement to preserve the original meaning exactly.

### Step 3: Proofread (Track Changes)

The final polish. Surgical corrections only — no rewriting, no restructuring, no voice changes.

**IDENTIFY PHASE (use model: sonnet)**

Read the manuscript (from Step 2 output, with Track Changes accepted for analysis purposes). Read `references/proofread-checklist.md` for the complete framework. Flag:

- **Grammar & Syntax** — Subject-verb agreement, dangling modifiers, comma splices, tense shifts
- **Punctuation** — Dialogue punctuation, em-dash style, Oxford comma consistency
- **Spelling & Word Choice** — Homophones, commonly confused words, name consistency
- **Consistency** — Character details, location details, timeline, formatting conventions
- **Formatting** — Chapter headings, scene breaks, paragraph indentation

Format as a correction list with exact before→after for each item.

**FIX PHASE (use model: opus) — Track Changes**

Same XML-level tracked change approach as the Line Edit. For proofread corrections:

1. Unpack the .docx from Step 2 (which already contains Line Edit tracked changes)
2. Add NEW tracked changes for each proofread correction (new `w:id` values, same author "Manuscript Editor Pro")
3. Proofread corrections should be simple, surgical replacements — changing "their" to "there", fixing a comma, standardizing a name spelling
4. Do NOT rewrite sentences during proofreading. Only fix errors.
5. Repack the .docx

The result is a single .docx file with Track Changes from BOTH the Line Edit and Proofread passes. The author can review all changes at once.

**VERIFY PHASE (use model: sonnet)**

- Confirm all corrections applied as tracked changes
- Run one final consistency check: character names, location details, timeline
- Verify proofread changes are truly surgical (no accidental rewrites)
- **MEANING PRESERVATION CHECK:** Confirm no proofread correction accidentally changes the meaning of a sentence. A grammar fix should never alter what happens, what a character feels, or what information the reader receives. If a correction changes meaning, revert it and find a meaning-preserving alternative.
- Sign off on the manuscript

### Step 4: Continuity Audit

After editing passes are complete, run a dedicated continuity audit. Read `references/continuity-audit.md` for the complete framework.

**IDENTIFY PHASE (use model: sonnet)**

Build master reference tables by reading the entire manuscript:

- **Character Bible** — Physical descriptions, roles, relationships, speech patterns
- **Relationship Tracker** — How/when characters meet, relationship progression
- **Location & Geography** — Descriptions, spatial relationships, travel times
- **Timeline & Chronology** — Day-by-day event tracking
- **World Rules & Systems** — Magic, technology, social rules
- **Object & Detail Tracking** — Important objects, information flow, dropped threads

**FIX PHASE (use model: opus) — Track Changes**

For each contradiction found, apply a tracked change to the manuscript .docx:
- Choose the version most consistent with the rest of the manuscript
- Apply the fix in ALL affected locations
- Use comments to explain WHY the standardization choice was made (e.g., "Standardized eye color to green — used in 8 of 10 references")

**VERIFY PHASE (use model: sonnet)**

- Re-read fixed sections against updated reference tables
- Confirm all contradictions resolved
- Check that no new contradictions were introduced
- **MEANING PRESERVATION CHECK:** Confirm that every continuity fix preserves the scene's events, emotions, and stakes. Standardizing a detail (eye color, location direction) is fine. Changing what happens or how characters feel is NOT — flag those for the author in the assessment report instead.

**Generate the Continuity Audit as a .docx file** containing the full reference tables. This becomes the author's series bible.

### Step 5: Generate the Editorial Report

After all selected passes are complete, generate a comprehensive editorial report as a .docx file. Read `references/report-template.md` for the format structure.

The report must include:

**1. Executive Summary**
- Manuscript title, author, word count, genre
- Date of edit
- Which passes were run
- Overall assessment (2-3 paragraphs)

**2. Developmental Assessment Summary** (if run)
- Issues identified by severity
- Suggestions provided
- NOTE: "No automatic prose changes were made during this assessment. All suggestions are advisory."

**3. Line Edit Report** (if run)
- Total tracked changes inserted: N
- AI artifact count (flagged and addressed)
- Crutch phrase audit (before counts)
- Show vs. tell fixes (count with before/after examples for top 5)
- Voice consistency assessment
- Dialogue distinctiveness assessment

**4. Proofread Report** (if run)
- Total tracked changes inserted: N
- Error categories and counts
- Consistency standardizations made

**5. Continuity Audit Report** (if run)
- Character Bible (full reference table)
- Relationship Tracker
- Location & Geography reference table
- Timeline reconstruction
- World Rules summary
- Contradictions found and fixed (with before/after)

**6. Recommendations for the Author**
- Patterns to watch for in future writing
- Strengths to lean into
- Genre-specific observations

### Step 6: Produce Final Deliverables

Save all files to the workspace folder (the user's selected folder):

1. **[Title] - EDITED.docx** — The manuscript with all Track Changes visible. The author opens this in Word/Google Docs and accepts or rejects each change individually.
2. **[Title] - Developmental Assessment.docx** (if dev assessment was run) — The structural analysis report with suggestions.
3. **[Title] - Editorial Report.docx** — The comprehensive summary of all editing work.
4. **[Title] - Continuity Audit.docx** (if continuity audit was run) — Reference tables and series bible.

**IMPORTANT: Remind the author** that the edited manuscript contains Track Changes and they need to review and accept/reject each change. This is by design — it gives the author full control over what gets changed in their book.

## Model Routing

- **Sonnet for identification and verification**: Fast, thorough analytical reading. Catches issues systematically.
- **Opus for fixing**: Superior prose quality, voice-matching ability, and editorial judgment. Writes replacement text that matches the author's voice.

When spawning Task subagents:
- IDENTIFY subagents: include the full manuscript text (or chapter batch) + the relevant checklist from references/
- FIX subagents: include the issue list + the manuscript text + the Voice Profile
- VERIFY subagents: include the original issue list + the revised manuscript + the Voice Profile

## Parallelization Strategy

- Within each pass, chapters can be processed in parallel batches during the IDENTIFY phase
- The FIX phase processes chapters that share plot threads together to maintain continuity
- VERIFY runs on the complete manuscript sequentially to catch cross-chapter regressions
- Passes are strictly sequential — each builds on the previous output

## Important Rules

- **NEVER rewrite chapters.** Every change is a surgical tracked revision, not a wholesale rewrite.
- **NEVER add new content.** The editor fixes what exists — it does not invent scenes, add descriptions, create dialogue, insert bridging text, or expand the text. If something is missing (a scene transition, a relationship development beat, a plot connection), flag it in the assessment report as a suggestion for the author. Do NOT add it yourself.
- **NEVER silently change the manuscript.** Every single change must appear as a tracked revision that the author can see, accept, or reject.
- **NEVER change what happens.** The storyline, plot events, character decisions, emotional beats, and information reveals must remain identical after editing. You are fixing HOW something is written, never WHAT is written. If a fix would change the meaning of a passage — even subtly — leave the original and flag it in the report instead.
- **Preserve the author's voice above all.** Read `references/voice-matching-guide.md` and build a Voice Profile before any editing. Every replacement is tested against the profile.
- **The developmental assessment is advisory only.** It produces a report. It does not touch the manuscript.
- **Keep word count stable.** Tracked changes should not significantly alter manuscript length. If a show-vs-tell conversion expands a sentence, that's fine — but the overall manuscript should stay within ±5% of the original word count.
- **When in doubt, leave it.** A missed fix is better than a voice violation, a meaning change, or an unwanted edit. The author can always ask for another pass.
- The pipeline works for any fiction genre. Adjust genre expectations accordingly.
- When processing long manuscripts (80k+ words), batch chapters into groups of 4-5 for subagent processing.

## CRITICAL: Anti-Laziness Protocol

These rules exist because the most common failure mode is declaring a manuscript "clean" after a surface-level scan. This is NEVER acceptable. This section overrides any instinct to minimize findings.

### 1. ONLY Do What the User Asked

If the user asks for a proofread, do a proofread. Do NOT:
- Do a "formatting pass" first
- Clean up whitespace, carriage returns, or paragraph spacing unless specifically asked
- Run a different pass than what was requested
- Invent extra steps that aren't in this skill's pipeline
- Add passes you think would be "helpful" before doing what was actually requested

If you're uncertain what pass the user wants, ASK. Do not improvise.

### 2. No Manuscript Is "Clean"

**NEVER tell the user their manuscript is essentially error-free.** No 60,000-word manuscript has only 2 errors. No 20,000-word novella has zero issues. If your initial scan finds very few problems, you MISSED things — go back and look harder.

A professional human proofreader finds 1-3 issues per page (~250 words). A professional line editor flags 5-15 issues per chapter. If your numbers are dramatically lower than this, you skimmed instead of reading.

### 3. Minimum Issue Thresholds (Re-Scan Triggers)

These are MINIMUM expected findings. Falling below these numbers means you almost certainly missed issues and MUST re-scan:

| Pass | Minimum Issues per 10k Words | If Below Threshold |
|------|-----------------------------|--------------------|
| **Proofread** | 5 issues | Re-scan every chapter individually. Run EACH checklist category (grammar, punctuation, homophones, consistency) as a SEPARATE dedicated sweep. |
| **Line Edit** | 10 issues | Re-scan chapter by chapter. Run each checklist section as a separate sweep: AI artifacts, then show-vs-tell, then crutch phrases, then dialogue, then prose mechanics. |
| **Continuity Audit** | 3 issues per 10k words | Re-build reference tables from scratch with more detail. You are almost certainly under-tracking character details, location descriptions, and timeline events. |

**Example:** A 60,000-word manuscript should produce at minimum ~30 proofread corrections, ~60 line edit flags, and ~18 continuity notes. Real numbers will typically be 2-5x higher.

**If after a genuine, documented re-scan you truly find fewer issues than the threshold:** Report the actual count, list EVERY specific check you ran on EVERY chapter, and explain what you looked for in each. The author should see proof of thoroughness, not a blanket "it's clean" declaration.

### 4. Process Chapter by Chapter — No Skimming

Every pass MUST process the manuscript **one chapter at a time**. You cannot:
- Read the first 3 chapters and extrapolate to the rest
- Scan for a few patterns across the whole manuscript and declare the rest clean
- Batch the entire manuscript as one unit and look for highlights
- Process only the chapters where something "seems off"

For each chapter, run the FULL checklist for that pass. Log issues per chapter. If any chapter comes back with zero issues, re-read that chapter — you missed something. A zero-issue chapter in a proofread of fiction is extraordinarily rare.

### 5. Report Your Coverage

In the Editorial Report, ALWAYS include a per-chapter issue count table:

```
| Chapter | Line Edit Issues | Proofread Issues | Continuity Issues |
|---------|-----------------|-----------------|-------------------|
| Ch. 1   | 8               | 4               | 2                 |
| Ch. 2   | 12              | 6               | 1                 |
| ...     | ...             | ...             | ...               |
| TOTAL   | N               | N               | N                 |
```

This table makes skimming visible. If chapters show zero issues, either the author is superhuman or the editor skimmed. The user sees this table — it holds the editing accountable.

### 6. The "Honest Assessment" Rule

If the manuscript genuinely IS strong in an area, say so — but with specifics that prove you checked. "Your dialogue punctuation is consistent throughout — I verified all 347 dialogue tags across 24 chapters" is a real observation. "Your manuscript is clean" is a cop-out.

**Good:** "Grammar is strong — I found 14 corrections across 60k words, mostly comma usage in compound sentences and two subject-verb agreement issues with collective nouns. Your dialogue punctuation is consistent and correct throughout."

**Bad:** "Your manuscript is genuinely clean. I found exactly 2 errors."

**The difference:** The good version shows the editor actually checked everything and can cite specific categories. The bad version shows the editor skimmed.

## Reference Files

- **`references/dev-edit-checklist.md`** — Complete developmental editing framework (assessment only, no rewrites)
- **`references/line-edit-checklist.md`** — Line editing criteria, AI artifact patterns, crutch phrase database, show-vs-tell guide
- **`references/proofread-checklist.md`** — Proofreading standards, grammar rules, consistency tracking
- **`references/continuity-audit.md`** — Character bible, relationship tracking, geography, timeline, world rules
- **`references/report-template.md`** — Editorial report structure and formatting guide
- **`references/voice-matching-guide.md`** — How to analyze and preserve an author's voice during editing
