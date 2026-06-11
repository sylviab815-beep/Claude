# Cozy Mystery Author — Workflow Steps

Complete each step fully. Present output and WAIT for user input before proceeding.

---

## Phase 1: Interactive Setup

Use AskUserQuestion (popup-style multiple choice) for each question. Ask them ONE AT A TIME.

### Question 1: Subgenre

**"What kind of cozy mystery are we writing?"**

Options:
- "Paranormal Cozy — magical elements, familiars, supernatural worldbuilding"
- "Traditional Cozy — grounded, real-world, no magic"
- "Culinary Cozy — food-themed, bakery/restaurant/café setting"
- "Craft Cozy — knitting, quilting, bookshop, gardening"
- "Pet Cozy — animal sidekicks, veterinary, rescue"

### Question 2: Romance

**"Romance subplot?"**

Options:
- "Yes — slow-burn romance thread woven through the mystery"
- "No — pure mystery, no romance"

### Question 3: Heat Level

**"What heat level?"**

Options:
- "Sweet/Clean — closed door, fade to black"
- "Mild Spice — tasteful open door, not explicit"

### Question 4: Length

**"How long should the book be?"**

Options:
- "Novella — ~20,000 words (16 chapters, great for rapid release)"
- "Full Novel — ~50,000 words (30 chapters, standard cozy length)"

### Question 5: Series Position

**"Is this a standalone or part of a series?"**

Options:
- "Standalone — one and done"
- "Book 1 — first in a new series (plant seeds for future books)"
- "Book 2-5 — continuing a series (I'll provide context from previous books)"
- "Not sure yet — write it so it works either way"

If user chooses "Book 2-5," ask them to upload or paste context from previous books (character names, town details, unresolved threads, romance status). Read this material carefully and extract all continuity details before proceeding.

### Question 6: Style Guide

**"Would you like me to match your existing writing style?"**

Options:
- "Yes — I'll upload 1-2 previous manuscripts for you to study"
- "No — use the default cozy mystery voice"

If yes: Ask the user to upload their manuscripts. Read them thoroughly and build a Style Guide document capturing their voice, dialogue patterns, pacing, description style, chapter structure, and mystery craft approach. Save as `[Book Title] - Style Guide.md`. Present the style guide summary to the user and ask for confirmation before proceeding.

### Question 7: Outline Source

**"Do you have a completed outline, or should I generate one?"**

Options:
- "I have an outline — I'll upload or paste it"
- "Generate an outline for me (I'll approve it before you write)"
- "I have a concept but no outline — help me develop it"

If they upload an outline: Read it carefully. Verify it contains: chapter-by-chapter breakdown, mystery beats, clue schedule, suspect pool, killer identity, red herring strategy. If any of these are missing, ask the user to fill the gaps before proceeding.

If generating an outline: Follow the outline generation process below, then present it for approval.

---

## Phase 2: Outline Generation (if needed)

Skip this phase if the user provided their own outline.

### Step 2a: Concept Development

Based on the user's subgenre and preference choices, generate 3 unique story concepts. Each includes:
- Title (avoid AI name patterns)
- One-line hook
- The victim (who and why they matter)
- The killer (identity, motive, method — kept hidden from the reader)
- 4-5 suspects with motives
- The sleuth (who she is, why she investigates)
- Setting (specific, vivid, cozy)
- If paranormal: the magical element and how it complicates the mystery
- If romance: the love interest and the obstacle

Present all 3 concepts. Use AskUserQuestion:

**"Which concept do you want to develop? (Or combine elements from multiple)"**

Options:
- "Concept 1: [title]"
- "Concept 2: [title]"
- "Concept 3: [title]"
- "Mix and match — I'll tell you what I want from each"

### Step 2b: Full Outline

Build a complete chapter-by-chapter outline including:

For each chapter:
- Chapter number and working title
- Summary (3-5 sentences)
- Mystery beat (where we are in the investigation)
- Clue or red herring planted/revealed (SPECIFIC — what exactly the reader learns or is misdirected by)
- Suspect focus (which suspect is in the spotlight)
- If romance: romantic beat for this chapter
- If paranormal: magical element in this chapter
- Chapter tone and goal

The outline must also include:
- **Clue Schedule**: A numbered list of every real clue, the chapter it appears in, and how it connects to the solution
- **Red Herring Map**: Each false trail, which chapters it runs through, and when/how it's debunked
- **Suspect Tracker**: For each suspect — motive, alibi, alibi weakness, chapters where they're featured, and when they're eliminated or confirmed
- **The Solution Logic**: How the sleuth puts it together — which clues connect, what the "aha" trigger is, and why it's fair

**Present the full outline and ask for approval before writing.**

---

## Phase 3: Manuscript Writing

### Step 3a: Pre-Writing Setup

Before writing Chapter 1:

1. Read `references/outline-adherence.md` — internalize the anti-spoiler rules
2. Read `references/prose-craft.md` — internalize the show-don't-tell standards
3. If a style guide exists, read it and keep it active throughout writing
4. Construct the Knowledge State for Chapter 1 (what does the sleuth know at the start? Almost nothing.)

### Step 3b: Write Each Chapter

For each chapter:

1. **Build the Knowledge State** — list what the sleuth knows and doesn't know at this point
2. **Check the outline** — what happens in this chapter? What clue or red herring appears? Which suspect is featured?
3. **Write the chapter** following:
   - The outline's beats for this chapter — do not deviate
   - The Knowledge State — do not include information the sleuth doesn't have yet
   - Equal Suspect Treatment — if the killer appears, write them with the same register as all other suspects
   - Prose Craft rules — show don't tell, dialogue as behavior, sensory immersion
   - Style Guide (if one exists) — match voice, pacing, and patterns
4. **Apply the Backward Writing Test** — "If I didn't know who the killer was, would I have written this chapter differently?" If yes, fix it.
5. **Verify clue placement** — if a clue was scheduled for this chapter, verify it's on-page and properly buried

Write chapters sequentially — do NOT skip ahead or write out of order. The Knowledge State must build naturally.

### Step 3c: Completeness Verification

After all chapters are written:
- Every chapter must be fully written prose — no brackets, summaries, or placeholders
- Each chapter hits the target word count (~1,250 for novellas, ~1,650 for novels)
- No chapter under 1,000 words
- Total manuscript within 10% of target length

---

## Phase 4: Editorial Pipeline

### Step 4a: Outline Adherence Audit

BEFORE any other editing, run the full audit from `references/outline-adherence.md`:
1. Knowledge State verification per chapter
2. Suspect treatment scan (compare language used for killer vs innocents)
3. Clue timing check (every clue in the right chapter)
4. Red herring quality check (each one written with conviction)
5. Backward writing scan (phrases that only work if you know the ending)
6. Reveal integrity check (no new information in the reveal chapter)

Fix all flagged issues before proceeding.

### Step 4b: AI-Ism Revision Pass

Read `references/revision-guide.md` and apply all fixes:
- Remove robotic phrasing and AI artifacts
- Fix POV breaks and perspective slips
- Sharpen dialogue — make it natural and character-specific
- Improve chapter endings — mid-scene momentum, no manufactured cliffhangers
- Replace telling with showing throughout

### Step 4c: Developmental Edit

Analyze the full manuscript for:
- Mystery fairness (are all clues on-page before the reveal?)
- Pacing (does the investigation have momentum? any chapters that drag?)
- Character consistency (does the sleuth sound the same throughout? does each suspect have a distinct voice?)
- Genre compliance (is the cozy tone maintained even during tense moments?)
- Romance pacing (if applicable — does it fit the book's series position?)
- Paranormal consistency (if applicable — are the magical rules followed?)

Produce a ranked Priority Action Items list. Apply the top 5 fixes.

### Step 4d: Beta Read

Read the revised manuscript as a critical beta reader who reads a lot of cozy mysteries:
- Star rating (honest — 3-3.5 is normal for a first draft)
- The Good (specific scenes and dynamics that work)
- The Bad (specific problems with page references)
- Suggestions for Improving (ranked, 3-5 structural fixes)

Apply the top 3 fixes from the beta review.

### Step 4e: Final Outline Adherence Check

One last pass specifically checking:
- The killer isn't telegraphed through descriptive language
- The reveal uses only previously established information
- All suspects received fair narrative treatment
- Clues are in the right chapters

---

## Phase 5: KDP Metadata & Delivery

### Step 5a: Create KDP Info Document

For the completed book, generate:
- Book title and subtitle suggestion
- Amazon book description (4000 char max, keyword-rich)
- 7 Amazon keyword phrases optimized for the cozy mystery subgenre
- 3 BISAC category suggestions
- Suggested price point
- 3-5 comparable real published titles
- Target audience description
- Cover image prompt (illustrated cozy style, specific to the book's subgenre and content)

### Step 5b: Generate .docx Files

Create the manuscript and KDP info as .docx files using the `docx` npm package. Read `references/docx-template.md` for formatting specs.

### Step 5c: Final Delivery

Save all files to the user's workspace folder. Present:
- The manuscript .docx
- The KDP info .docx
- The style guide (if one was created)
- A brief summary: title, word count, chapter count, and whether the outline adherence audit passed clean
