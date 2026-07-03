# DOCX Manuscript Template — Thriller

Use this Node.js script structure to generate each manuscript. The `docx` npm package is installed globally.

## Script Structure

```javascript
const fs = require("fs");
const { Document, Packer, Paragraph, TextRun, AlignmentType, PageBreak, HeadingLevel } = require("docx");

const chapters = [
  {
    title: "Chapter 1: [Chapter Title]",
    pov: "Character Name", // if multi-POV — include POV indicator
    content: [
      "First paragraph...",
      "Second paragraph...",
      // ~1,250 words (novella), ~1,600 words (standard), or ~1,800 words (extended)
      // Thriller chapters can be SHORT — some may be 800-1,000 words for pacing
    ]
  },
  // ... 16 (novella), 30-38 (standard), or 45-55 (extended)
];

const children = [];

// Title page
children.push(
  new Paragraph({ spacing: { before: 4000 }, children: [] }),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 200 },
    children: [new TextRun({ text: "BOOK TITLE", bold: true, size: 56, font: "Times New Roman" })]
  }),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 200 },
    children: [new TextRun({ text: "A [Subgenre] Thriller", size: 28, font: "Times New Roman" })]
  }),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: "by [Author Name]", size: 32, font: "Times New Roman", italics: true })]
  }),
  new Paragraph({ children: [new PageBreak()] })
);

// Chapters
chapters.forEach((chapter, index) => {
  children.push(
    new Paragraph({
      heading: HeadingLevel.HEADING_1,
      spacing: { before: 600, after: 400 },
      alignment: AlignmentType.CENTER,
      children: [new TextRun({ text: chapter.title, bold: true, size: 32, font: "Times New Roman" })]
    })
  );

  if (chapter.pov) {
    children.push(
      new Paragraph({
        spacing: { after: 300 },
        alignment: AlignmentType.CENTER,
        children: [new TextRun({ text: chapter.pov.toUpperCase(), size: 20, font: "Times New Roman", italics: true, smallCaps: true })]
      })
    );
  }

  chapter.content.forEach((para) => {
    children.push(
      new Paragraph({
        spacing: { after: 200, line: 360 },
        children: [new TextRun({ text: para, size: 24, font: "Times New Roman" })]
      })
    );
  });

  if (index < chapters.length - 1) {
    children.push(new Paragraph({ children: [new PageBreak()] }));
  }
});

const doc = new Document({
  styles: {
    default: { document: { run: { font: "Times New Roman", size: 24 } } },
    paragraphStyles: [{
      id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
      run: { size: 32, bold: true, font: "Times New Roman" },
      paragraph: { spacing: { before: 600, after: 400 }, alignment: AlignmentType.CENTER }
    }]
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
      }
    },
    children: children
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync("/path/to/output.docx", buffer);
  console.log("Created: output.docx");
});
```

## Key Specifications

- **Page size**: US Letter
- **Margins**: 1 inch all around
- **Body font**: Times New Roman, 12pt
- **Chapter headings**: Times New Roman, 16pt bold, centered
- **POV indicator**: 10pt italic small caps, centered (multi-POV only)
- **Line spacing**: 1.5
- **Page breaks**: Between every chapter

## Content Guidelines

- **Novella**: ~1,250 avg words/chapter, 16 chapters, ~20,000 total
- **Standard**: ~1,600 avg words/chapter, 30-38 chapters, ~50,000-70,000 total
- **Extended**: ~1,800 avg words/chapter, 45-55 chapters, ~80,000-100,000 total

Thriller chapters can vary MORE in length than other genres — short, punchy chapters (800 words) are effective for high-tension moments. Variation in chapter length IS a pacing tool.

## Important Notes

- No chapter under 600 words
- Validate file was created and check size
- Author name matches user specification
