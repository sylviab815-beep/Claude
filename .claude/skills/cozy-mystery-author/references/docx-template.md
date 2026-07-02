# Cozy Mystery Manuscript Formatting (.docx)

Generate the manuscript as a .docx using Node.js with the `docx` npm package. If `docx` isn't installed, install it (`npm install docx`) before generating.

## Length Tiers & Chapter Targets

- **Novella (20,000-50,000 words):** ~1,000-2,500 words/chapter, ~16-24 chapters
- **Standard / cozy novel (60,000-90,000 words):** ~2,200-3,500 words/chapter, ~22-32 chapters

Trust the outline's chapter count. No chapter should run under ~1,000 words (rushing) or balloon far past the tier target.

## Formatting Standards

- **Font:** Times New Roman, 12pt
- **Line spacing:** 1.5 (manuscript standard)
- **Margins:** 1 inch all sides
- **Paragraphs:** first-line indent 0.5", no extra space between paragraphs; no indent on the first paragraph after a chapter header or scene break
- **Chapter headers:** `Chapter [N]` (optionally with a title), starting on a new page
- **Scene breaks:** a centered `* * *` with one blank line before and after
- **Chapter starts:** each chapter begins on a new page (page break before)

## Document Order

1. **Title page (centered):** Book Title / "by [Author Name]" (the name from setup — never assumed) / series name + number if applicable
2. **Copyright page:** auto-generate with the current year and the author name; standard fiction disclaimer
3. **Table of contents** (optional for novella; recommended for novel)
4. **Chapters** — full prose, page break before each
5. **Back matter:** "About the Author" (100-150 words, supplied or templated), "Also by [Author]" if applicable, and an optional "Recipes" / bonus section if the subgenre calls for it (culinary cozy convention)

## Generation Notes

- Build the doc with `docx`'s `Document`, `Paragraph`, `TextRun`, `HeadingLevel`, `AlignmentType`, and a `PageBreak` before each chapter.
- Write the script to a temp location, run it with Node, and save the output .docx into the user's working subfolder.
- After generating, verify the file is non-empty and the chapter count matches the outline.
- Regenerate the .docx after any editorial stage that changes prose.

## Sample Script Skeleton

```javascript
const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, PageBreak } = require('docx');

// chapters = [{ number, title, paragraphs: [ "para text", ... ] }, ...]
// Build title page, copyright, then map chapters to sections with a PageBreak before each.
// Apply Times New Roman 12pt, 1.5 spacing, 0.5" first-line indent via paragraph/run styles.
// Packer.toBuffer(doc).then(buf => fs.writeFileSync(outPath, buf));
```
