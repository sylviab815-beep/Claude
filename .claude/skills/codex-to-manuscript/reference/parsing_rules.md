# Parsing Rules — How to Read a Codex + Outline Package

The skill's parser scripts (`skills/codex-to-manuscript/scripts/parse_codex.py` and `skills/codex-to-manuscript/scripts/parse_outline.py`) handle most extraction automatically. This reference is for cases where the parser misses fields or the codex/outline is in an unusual format and you need to extract structure manually.

---

## Codex structure (expected sections, in order)

A standard codex contains these sections, each with consistent labels:

### 1. Story Concept (top of codex)

Labeled fields:
- `Title`
- `Genre/Subgenre`
- `Tropes or Themes`
- `Hook (1 line)`
- `Pitch (short blurb)`
- `Story Summary`

### 2. Structure & Technical Details

Labeled fields:
- `Antagonist` (Type, Goal, Method)
- `Setting` (Primary Setting, Vibe Keywords, Special Rules or Systems)
- `Structure` (Word Count Target, Chapter Count Target, Tense, POV Mode, Alternating POVs?, POV Roster, Beat Template)

### 3. Locked Elements

Labeled lists:
- `Locked Tropes`
- `(Added) Tropes`
- `Key Market Conventions`
- `Mandatories (non-negotiable story elements)`

### 4. Characters

Each character entry begins with `Full Name:` and contains:
- Age
- Gender / Pronouns
- Role in Story
- Physical Description
- Style / Clothing Notes
- Personality Traits
- Strengths and Flaws (sub-list: Strengths, Flaws)
- Internal Conflict (what they want vs. what they need)
- Backstory Summary
- Key Relationships
- Character Arc Summary
- Thematic Tie-In

Characters are usually grouped under `### Main Characters`, `### Secondary Characters`, `### Incidental Characters`.

### 5. Locations

Each location entry begins with `Location Name:` and contains:
- Type of Place
- Physical / Mood Description
- Notable Features or Objects
- Who Uses It and When
- Relevance to Plot or Character Arcs

### 6. Objects

Each object entry begins with `Name of Object:` and contains:
- Description and Use
- Owner or Origin
- Narrative or Emotional Significance

### 7. Lore & Rules

Each lore entry begins with `Topic Name:` and contains:
- Category
- Description
- Impact on Daily Life or Conflict
- Connection to Theme or Main Plot

### 8. Historical Events

Each event entry begins with `Event Name:` and contains:
- Era or Timeframe
- Summary
- Lasting Impact

### 9. Subplots

Each subplot entry begins with `Title:` and contains:
- Involved Characters
- Subplot Summary
- Thematic Connection
- How It Progresses Across the Story (broken down by Act)
- Resolution

---

## Outline structure (expected sections, in order)

The outline is organized by Acts (`### ACT I`, `### ACT II`, `### ACT III`) and Chapters (`#### Chapter N: Title`).

Each chapter entry contains the following labeled fields:
- POV
- Chapter Goal
- Opening Hook
- Key Scenes (numbered list — usually 3 scenes per chapter)
- Romantic/Relationship Development (or Subplot Development)
- Complication or Conflict
- Character Decision and Consequence
- Chapter Tone
- Tropes Advanced
- Intimate Beat (Heat-Gated)
- Cliffhanger (or Closing Line)

---

## When the parser misses a field

If `parse_codex.py` returns an empty value for an expected field, the codex may use a non-standard label. Check for these common variants:

| Standard label | Variant labels seen in the wild |
|---|---|
| Genre/Subgenre | Genre, Subgenre, Category |
| POV Mode | POV, Point of View, Narrative Voice |
| Word Count Target | Target Length, Word Count, Manuscript Length |
| Chapter Count Target | Number of Chapters, Chapter Count |
| Alternating POVs? | Alternating POVs, Multi-POV, POV Structure |

For extracted lists, the parser strips markdown bold/italic and bullet markers. If a list item still has `**Label:** body` formatting, that's a sub-bulleted entry inside a parent bullet (commonly seen in `Mandatories` and `Strengths and Flaws`). Treat the body after the colon as the actual content.

---

## When the codex/outline is a PDF

The PDF parser uses `pdfplumber` first, falling back to `pypdf`. PDF text extraction can introduce:

- **Soft line breaks mid-sentence.** A long line in the original PDF wraps onto the next line in the extracted text, creating spurious sentence breaks. Detect by checking if the next line starts with lowercase or a continuation word.
- **Headers/footers repeated on every page.** If the parser captures repeating "Codex - The Bog Witch's Mistake" headers, strip them in post-processing.
- **Bullet characters lost.** PDFs sometimes encode bullets as `•` (•) which the parser handles, but unusual bullet characters may need normalization.

If extraction is poor, ask the user if they can provide the .docx version instead — DOCX parsing is significantly more reliable.

---

## Pasted-text input

If the user pastes the codex/outline content directly into chat instead of attaching a file, save the pasted content to a temporary `.md` file and run the parser against it. The parser supports `.md` and `.txt` extensions.
