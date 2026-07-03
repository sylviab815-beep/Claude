# Pulp Adventure Romance Manuscript Formatting

## Word Count Targets

- **Novella:** 25,000–40,000 words total. 1,500–2,500 words per chapter. 12–20 chapters.
- **Standard Novel:** 60,000–80,000 words total. 2,500–4,000 words per chapter. 22–32 chapters.
- **Extended Novel:** 90,000–120,000 words total. 3,500–5,000 words per chapter. 32–45 chapters.

Final word count must land within ±5% of the target range. Pad-words and fluff are not acceptable; reduce the chapter count if a chapter cannot legitimately reach target length.

## Chapter Header Format

```
Chapter [Number]
[Title]
```

Both lines centered. One blank line above and below. Use Heading 1 style for the number line and Heading 2 for the title line. Page break before each new chapter.

## Body Formatting

- **Font:** Times New Roman or Garamond, 12pt
- **Line spacing:** 1.5
- **Margins:** 1 inch on all sides
- **Paragraph indent:** 0.5 inch first line (no indent on first paragraph after a heading or scene break)
- **Justification:** Left-aligned, ragged right (NOT full-justified)
- **Scene break:** `* * *` centered, one blank line before and after

## Title Page

Centered, vertically and horizontally:

```
[BOOK TITLE]

[BY]

[AUTHOR NAME]

[GENRE: Pulp Adventure Romance]

[YEAR]
```

Page break after.

## Front Matter (in order)

1. Title page
2. Copyright page (auto-generated; year is current year, author name from setup)
3. Optional: Dedication
4. Optional: Author's Note
5. Optional: Content notes (especially relevant for Spicy heat level — list any sensitive content)
6. Table of Contents (auto-generated from chapter headings)

## Back Matter (in order)

1. About the Author (100–150 words; placeholder if not provided)
2. Other Books by [Author] (if applicable)
3. Optional: Acknowledgments

## Chapter Body Conventions

- Open every chapter with a strong sensory or action anchor (no "[Protagonist] woke up" openings unless plot-justified)
- Close every chapter on a forward pull (cliffhanger, reveal, raised stakes, emotional shift)
- Scene breaks marked with `* * *` for clean POV/time/location shifts
- Italics for thoughts (sparing; show through prose rather than using italicized internal monologue)
- Italics for emphasis (very sparing — let the prose carry weight)
- No bold body text
- No emoji or non-standard symbols

## Dialogue Conventions

- Standard double quotation marks
- Em dashes for interrupted speech: "I told you—"
- Ellipses for trailing speech: "I just thought..."
- New paragraph for new speaker
- Action beats integrated within paragraphs, not on separate lines

## Generation

The manuscript is generated as a single .docx file using a Python `python-docx` script or equivalent. The file:

1. Includes all front matter
2. Includes all chapters with proper page breaks
3. Includes back matter
4. Has a working Table of Contents
5. Saves to the user's specified output folder
6. Filename format: `[BookTitle].docx` (no spaces — use underscores or hyphens; no special characters except `-` and `_`)

A second file, `[BookTitle]_KDP_Metadata.docx`, is generated from the kdp-template.md spec.

A third file, `[BookTitle]_ARIS_Log.docx`, contains the per-chapter ARIS log produced during Phase 4.
