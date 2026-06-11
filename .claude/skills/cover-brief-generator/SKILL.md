---
name: cover-brief-generator
description: >
  Generate a designer-ready cover brief by researching current bestselling and trending book covers in any genre. Use this skill whenever an author wants to know what's working visually on Amazon right now, needs a cover brief for a designer, wants to see comp covers for a specific genre/subgenre/trope combination, or asks what their cover should look like. MANDATORY TRIGGERS: "cover brief", "comp covers", "what should my cover look like", "cover direction", "what's trending on covers", "book cover research", "cover for my [genre] book", "cover designer brief", "what covers are selling", "cover mood board", or any mention of generating, researching, or briefing a book cover. Also trigger when the user uploads a cover image and asks how it compares to what's selling.
---

# Cover Brief Generator

Research current bestselling book covers in the user's genre, analyze visual patterns, and produce a designer-ready cover brief as a .docx file — including direct links to comp covers on Amazon so the designer (or the author) can see exactly what's selling right now.

---

## What This Skill Produces

A Word document (.docx) containing:

1. **Comp Cover Gallery** — 4–6 current bestselling covers with Amazon links and visual descriptions
2. **Visual Pattern Analysis** — what the bestselling covers in this niche share (color palette, typography style, imagery type, mood)
3. **Genre Signal Checklist** — what elements must be present for readers to instantly recognize the genre
4. **Cover Direction** — specific, actionable direction for a designer: color palette, typography, imagery, mood, composition
5. **What to Avoid** — visual patterns that are dated, overcrowded, or signaling the wrong genre
6. **If a sample cover was provided** — a comparison against current comps with specific notes on what's working and what to reconsider

---

## Step 1: Intake

Gather this information before researching. Some may already be in the conversation — extract what you can, ask only for what's missing.

**Required:**
- Genre and subgenre (e.g., "contemporary romance," "sweet/clean romantic suspense," "cozy mystery — paranormal," "psychological thriller")
- Tropes (e.g., "forced proximity," "small-town romance," "amateur sleuth with a cat")
- Heat level / tone (clean/sweet/spicy OR warm/dark/funny/gritty)
- Pen name (if provided — affects brand alignment section)

**Optional but powerful:**
- An existing cover or cover idea (uploaded image — use it for comparison)
- Series information (standalone vs. series — affects typography/spine consistency notes)
- Target Amazon category or comp author they already have in mind

If any required fields are missing, ask for them before proceeding to research.

---

## Step 2: Research — Find Current Bestselling Covers

Search for 4–6 real, currently selling books whose covers represent the visual language of the user's specific genre/subgenre/trope combination. Prioritize:

- Books in the **top 100** of the relevant Amazon category (not just genre — go to the subgenre level)
- Books published or with covers updated in the **last 2–3 years** (cover trends move fast)
- Books with **strong visual identity** that clearly signal the genre — not outliers

**Search strategy (run multiple searches to triangulate):**
1. Search Amazon for the genre + subgenre + heat level (e.g., "sweet clean romantic suspense bestsellers")
2. Search for the specific tropes on Amazon and Goodreads (e.g., "forced proximity romance bestsellers 2024")
3. Search for known comp authors and look at their recent releases
4. Search BookBub, Publisher's Weekly new releases, or "top [genre] books 2024/2025" if needed

For each comp cover found, capture:
- **Title and Author**
- **Amazon URL** (direct link to the book page)
- **Visual description** — what does the cover actually look like? (color palette, imagery, typography placement, model/no model, mood)
- **Rank or status** — why this cover is a comp (bestseller rank, award, high visibility)

If you can retrieve the cover image URL from the Amazon page, include it. If not, the Amazon link is sufficient — the designer will open it.

---

## Step 3: Analyze Visual Patterns

After gathering comps, identify the patterns across them. This is the most valuable part of the brief — the designer needs to understand not just one cover, but the visual DNA of the whole category.

Analyze and report on:

**Color Palette:**
- What colors dominate the category? (e.g., "navy and gold are everywhere in clean romantic suspense right now")
- Are backgrounds dark or light?
- Is there a signature accent color for the subgenre?

**Typography:**
- Script vs. serif vs. sans-serif — what's dominant?
- Where does the title sit (top/center/bottom)?
- How large is the author name relative to the title?
- Any distinctive type treatments (outline fonts, metallic effects, shadowing)?

**Imagery & Composition:**
- Couple on cover vs. no couple?
- Full-body figures vs. close crop?
- Illustrated vs. photographic?
- Setting/location on cover vs. people-focused?
- What props or symbols are recurring (flowers, weapons, keys, animals, specific objects)?

**Mood & Atmosphere:**
- What feeling does the category's cover aesthetic project? (cozy/warm, dark/edgy, romantic/soft, action/tense)
- How does that mood align with what the user's book needs to convey?

**Genre Signals:**
- What elements are absolutely required for readers to recognize the genre at a glance?
- What would make a cover look like it belongs to the wrong genre?

---

## Step 4: Pen Name Brand Alignment

If a pen name was provided, note any brand considerations:

- **Julie Fontaine** (Women's Fiction / Romantic Suspense): Clean, emotionally resonant, faith-friendly aesthetic. Warmer color palettes. Should feel literary without being cold. No overt sensuality.
- **Other pen names**: Apply whatever is known about the pen name's visual brand. If unknown, note that brand consistency should be considered if this is a series or part of a catalog.

---

## Step 5: Existing Cover Comparison (if image provided)

If the user submitted an existing cover or a cover concept, compare it against the comps:

- What's working? (What aligns with the current visual language of the category?)
- What might signal the wrong genre, wrong heat level, or wrong era?
- What's the single most important change to consider?

Be specific and constructive — not "the cover looks dated" but "the script font and pastel palette are associated with 2019-era sweet romance; the current category has moved toward bolder typography and higher-contrast palettes."

---

## Step 6: Generate the Cover Brief (.docx)

Produce the cover brief as a Word document using the docx skill (read the docx SKILL.md at the skills/docx path for exact implementation).

### Document Structure

**Page 1 — Header**
- Title: "[Book Title or Genre] Cover Brief"
- Subtitle: "Prepared for [Pen Name] — [Date]"

**Section 1: Your Comp Covers**
For each comp (4–6 total):
- Book title + Author (bold)
- Amazon link (clickable hyperlink — label it "View on Amazon")
- 3–4 sentence visual description of the cover
- One sentence on why it's a relevant comp

**Section 2: Visual Pattern Analysis**
Prose summary of the patterns across the comps. Organized by: Color Palette → Typography → Imagery → Mood. Keep it concrete and specific — a designer should be able to use this without looking anything up.

**Section 3: Genre Signal Checklist**
Bullet list: "Your cover must signal [genre] by including..."
Second bullet list: "Avoid these patterns — they signal the wrong genre or era..."

**Section 4: Your Cover Direction**
The actionable brief. Write this as if you're giving instructions to a cover designer who has never read the book:

- **Overall Mood:** [one sentence]
- **Color Palette:** [specific colors or palette description — e.g., "Deep teal, warm gold, and cream. Dark background."]
- **Typography Style:** [specific type direction — e.g., "Elegant serif title, medium weight. Script author name below. Gold foil treatment if budget allows."]
- **Imagery:** [exactly what the cover should show — e.g., "Woman in silhouette against a city at dusk. No full-face shots. Atmospheric, not character-specific."]
- **Composition:** [layout — e.g., "Full-bleed image. Title at top, author name at bottom. No tagline needed."]
- **What to Avoid:** [specific things — e.g., "Avoid: clinch couples, hot pink, stock-photo-obvious imagery, overly busy layouts"]

**Section 5: Existing Cover Notes** (only if image was provided)
Comparison of submitted cover against comps, with specific notes.

---

## Docx Implementation Notes

- Use the docx skill for all Word document creation
- Use a clean, professional layout: navy or dark teal header bar, white body, readable 12pt font
- Comp covers section: use a simple two-column table (Title/Author | Link + Description) for readability
- All Amazon links must be actual clickable hyperlinks using ExternalHyperlink
- If cover images can be retrieved (direct image URLs from Amazon pages), embed them at ~200px wide next to the description
- Save to the user's Cowork folder and present with `mcp__cowork__present_files`

---

## Quality Check Before Delivering

Before saving the document, verify:
- [ ] 4–6 real comp covers with working Amazon links (not made-up titles)
- [ ] Visual analysis is specific, not generic ("warm and inviting" is too vague — describe the actual colors and what they're doing)
- [ ] Cover direction section gives a designer everything they need without further questions
- [ ] Genre signal checklist is honest — if this genre requires elements the user might not want, say so
- [ ] Document is clean and professional — a designer should be able to use it as a client brief

---

## Reference Files

- `references/genre-visual-guide.md` — Visual conventions and current trends by genre/subgenre. Read this before analyzing comps to calibrate your pattern recognition.
