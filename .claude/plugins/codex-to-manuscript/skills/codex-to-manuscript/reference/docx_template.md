# DOCX Output Template

The final manuscript is delivered as a single `.docx` file with publish-ready formatting. Use `python-docx` to assemble it from the chapter prose generated during the writing pipeline.

---

## File layout

The output folder contains:

```
[Book Title]/
├── [Book Title].docx           — the manuscript
├── [Book Title] - KDP Info.docx — Amazon metadata, blurb, cover prompt
└── [Book Title] - Edit Log.md   — chapter-by-chapter edit notes
```

---

## Manuscript document structure

In order, top to bottom:

1. **Title page** — book title (centered, large), author name placeholder
2. **Copyright placeholder** — single line: `Copyright © [Year] [Author Name]. All rights reserved.`
3. **Dedication placeholder** — single italicized line, customer can edit
4. **Chapter 1**
5. **Chapter 2**
6. ...
7. **The End** — centered, single line at the very end

---

## Chapter formatting

Each chapter starts on a new page (insert a page break before the chapter heading).

Chapter heading format:

```
                        Chapter 1
                  The Weight of Water and Time
```

(Centered, "Chapter N" on one line, chapter title on the next.)

Body text follows two blank lines after the heading.

---

## Body text formatting

| Property | Value |
|---|---|
| Font family | Georgia (or Times New Roman if Georgia unavailable) |
| Font size | 12pt |
| Line spacing | 1.5 |
| Paragraph spacing | 0pt before, 0pt after |
| First-line indent | 0.3" (for body paragraphs) |
| Alignment | Left (not justified) |

First paragraph of each chapter and first paragraph after a scene break: **no first-line indent**.

---

## Scene breaks

Use a centered dingbat row between scenes within a chapter:

```
                            * * *
```

(Three asterisks, single line, centered, with one blank line above and below.)

---

## Quote characters

All quotation marks must be smart quotes (curly), not straight. python-docx will preserve whatever you write — convert before insertion if needed.

Em-dashes are em-dashes (—), not double hyphens (--). En-dashes (–) for ranges only.

---

## Python-docx reference snippets

```python
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.text import WD_BREAK

doc = Document()

# Set default style
style = doc.styles['Normal']
style.font.name = 'Georgia'
style.font.size = Pt(12)
style.paragraph_format.line_spacing = 1.5
style.paragraph_format.first_line_indent = Inches(0.3)
style.paragraph_format.space_before = Pt(0)
style.paragraph_format.space_after = Pt(0)

# Title page
title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = title.add_run(book_title)
run.font.size = Pt(28)
run.font.name = 'Georgia'

# Page break before each chapter
def add_chapter(doc, number, title):
    doc.add_page_break()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(f"Chapter {number}")
    r.bold = True
    r.font.size = Pt(16)
    p.paragraph_format.first_line_indent = Inches(0)

    p2 = doc.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r2 = p2.add_run(title)
    r2.italic = True
    r2.font.size = Pt(14)
    p2.paragraph_format.first_line_indent = Inches(0)

    doc.add_paragraph()  # blank line

def add_body_paragraph(doc, text, first_in_chapter=False):
    p = doc.add_paragraph(text)
    if first_in_chapter:
        p.paragraph_format.first_line_indent = Inches(0)

def add_scene_break(doc):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Inches(0)
    p.add_run("* * *")

# At the end
end = doc.add_paragraph()
end.alignment = WD_ALIGN_PARAGRAPH.CENTER
end.add_run("The End").italic = True

doc.save(output_path)
```

---

## KDP Info document

Generate `[Book Title] - KDP Info.docx` containing:

1. **Title** — full title
2. **Subtitle** (if applicable) — usually genre-specific
3. **Series** — series name (if applicable, ask user)
4. **Author Name** — placeholder
5. **Genre** — primary
6. **Categories** — three Amazon categories matching the codex's genre/tropes
7. **Keywords** — seven Amazon keyword phrases (mix of trope, audience, vibe)
8. **Back Cover Blurb** — 150-200 words derived from `concept.pitch` + `concept.story_summary`, polished to read as marketing copy
9. **Amazon Long Description** — 400-500 words, formatted for Amazon (with bold-style emphasis on hooks, single-paragraph readable blocks)
10. **Cover Prompt** — a 3-4 sentence Ideogram/Midjourney/DALL-E-ready prompt describing the book's cover art direction, drawn from the codex's vibe keywords, primary setting, and tone
11. **Production Notes** — the model used to write the manuscript (recorded from the Phase 0 choice — e.g., "Claude Opus 4.8"), the plugin version, and the date the manuscript was generated. This is for the customer's records and for series consistency across books.

Format the KDP Info doc with clear headings (Heading 2 style) for each section. The Production Notes section can be in smaller text (Heading 3 or just italic body) at the bottom of the doc.

Example Production Notes section:

```
Production Notes

Written with: Claude Opus 4.8
Plugin: Codex to Manuscript v1.3.1
Generated: [date]

For series consistency, future books should be written with the same Claude model.
```

---

## Edit Log

`[Book Title] - Edit Log.md` is a plain markdown file. The structure is defined in `editorial_pipeline.md` Loop 1 Step 5. One section per chapter, plus a final section for the end-of-book pipeline notes.
