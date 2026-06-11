# DOCX Manuscript Template — Cozy Mystery

Use this Node.js script structure to generate each manuscript. The `docx` npm package is installed globally.

## Script Structure

```javascript
const fs = require("fs");
const { Document, Packer, Paragraph, TextRun, AlignmentType, PageBreak, HeadingLevel } = require("docx");

// Chapter content arrays — each element is a paragraph of text
const chapters = [
  {
    title: "Chapter 1: [Chapter Title]",
    content: [
      "First paragraph of the chapter...",
      "Second paragraph...",
      // ... ~1,250 words total per chapter (novella) or ~1,650 words (novel)
    ]
  },
  // ... 16 chapters (novella) or 30 chapters (novel)
];

// Build document sections
const children = [];

// Title page
children.push(
  new Paragraph({ spacing: { before: 4000 }, children: [] }), // spacer
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 200 },
    children: [new TextRun({ text: "BOOK TITLE", bold: true, size: 56, font: "Times New Roman" })]
  }),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 200 },
    children: [new TextRun({ text: "A [Subgenre] Cozy Mystery", size: 28, font: "Times New Roman" })]
  }),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: "by [Author Name]", size: 32, font: "Times New Roman", italics: true })]
  }),
  new Paragraph({ children: [new PageBreak()] })
);

// Chapters
chapters.forEach((chapter, index) => {
  // Chapter heading
  children.push(
    new Paragraph({
      heading: HeadingLevel.HEADING_1,
      spacing: { before: 600, after: 400 },
      alignment: AlignmentType.CENTER,
      children: [new TextRun({ text: chapter.title, bold: true, size: 32, font: "Times New Roman" })]
    })
  );

  // Chapter paragraphs
  chapter.content.forEach((para) => {
    children.push(
      new Paragraph({
        spacing: { after: 200, line: 360 }, // 1.5 line spacing
        children: [new TextRun({ text: para, size: 24, font: "Times New Roman" })] // 12pt
      })
    );
  });

  // Page break after each chapter (except last)
  if (index < chapters.length - 1) {
    children.push(new Paragraph({ children: [new PageBreak()] }));
  }
});

const doc = new Document({
  styles: {
    default: {
      document: {
        run: { font: "Times New Roman", size: 24 }
      }
    },
    paragraphStyles: [
      {
        id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 32, bold: true, font: "Times New Roman" },
        paragraph: { spacing: { before: 600, after: 400 }, alignment: AlignmentType.CENTER }
      }
    ]
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 }, // US Letter
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } // 1 inch
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

- **Page size**: US Letter (12240 x 15840 DXA)
- **Margins**: 1 inch all around (1440 DXA)
- **Body font**: Times New Roman, 12pt (size: 24 in half-points)
- **Chapter headings**: Times New Roman, 16pt bold, centered
- **Line spacing**: 1.5 (line: 360)
- **Paragraph spacing**: 200 DXA after each paragraph
- **Page breaks**: Between every chapter
- **Title page**: Book title, subgenre label, author name

## Content Guidelines

Each chapter's `content` array contains the full prose, broken into natural paragraphs. Dialogue gets its own paragraph.

- **Novella**: ~1,250 words per chapter, 16 chapters, ~20,000 words total
- **Novel**: ~1,650 words per chapter, 30 chapters, ~50,000 words total

## Important Notes

- Do NOT use `\n` for line breaks — use separate Paragraph elements
- Always include the title page with the page break after it
- Validate the file was created and check its size (novella: 35-55 KB, novel: 70-110 KB)
- The author name on the title page should match whatever the user specifies (they may use a pen name)
