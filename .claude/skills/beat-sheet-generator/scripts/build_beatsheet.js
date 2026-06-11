/**
 * beat-sheet-generator / build_beatsheet.js
 *
 * Usage:
 *   node build_beatsheet.js <chapters.json> <output.docx>
 *
 * chapters.json is an array of objects:
 *   { label, title, action, emotion, stakes, pacingFlag }
 */

const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
        AlignmentType, BorderStyle, WidthType, ShadingType,
        PageNumber, Header, Footer } = require('docx');
const fs = require('fs');
const path = require('path');

// ─── colour palette ──────────────────────────────────────────────────────────
const C = {
  brandDark:  '1A2B3C',
  brandMid:   '2E4D6E',
  brandLight: '4A7FA5',
  accent:     'C0392B',   // pacing flag red
  headerBg:   'D6E4F0',
  rowBase:    'FFFFFF',
  pacingBg:   'FFF3F2',
  border:     'B0C8DC',
  textDark:   '1A2B3C',
  textMid:    '3D5A73',
  gray:       '6B7F8E',
};

// ─── helpers ─────────────────────────────────────────────────────────────────
function noBorder()  { return { style: BorderStyle.NONE,   size: 0, color: 'FFFFFF' }; }
function thinBorder(){ return { style: BorderStyle.SINGLE, size: 1, color: C.border }; }
function thickBorder(){ return { style: BorderStyle.SINGLE, size: 3, color: C.border }; }

function spacer(pts) {
  return new Paragraph({ children: [], spacing: { before: pts, after: 0 } });
}

function hr(color) {
  return new Paragraph({
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color, space: 1 } },
    spacing: { before: 0, after: 0 },
    children: [],
  });
}

function beatRow(label, text, bgColor, redText) {
  return new TableRow({
    children: [
      new TableCell({
        width: { size: 1400, type: WidthType.DXA },
        shading: { fill: bgColor, type: ShadingType.CLEAR },
        margins: { top: 80, bottom: 80, left: 140, right: 80 },
        borders: { top: noBorder(), bottom: thinBorder(), left: noBorder(), right: noBorder() },
        children: [new Paragraph({
          children: [new TextRun({
            text: label, bold: true, font: 'Arial', size: 18,
            color: redText ? C.accent : C.brandMid,
          })],
        })],
      }),
      new TableCell({
        width: { size: 7880, type: WidthType.DXA },
        shading: { fill: bgColor, type: ShadingType.CLEAR },
        margins: { top: 80, bottom: 80, left: 80, right: 100 },
        borders: { top: noBorder(), bottom: thinBorder(), left: noBorder(), right: noBorder() },
        children: [new Paragraph({
          children: [new TextRun({
            text, font: 'Arial', size: 18,
            color: redText ? C.accent : C.textDark,
          })],
        })],
      }),
    ],
  });
}

function chapterBlock(ch) {
  const { label, title, action, emotion, stakes, pacingFlag } = ch;
  const bgColor  = pacingFlag ? C.pacingBg : C.rowBase;
  const hdrFill  = pacingFlag ? C.accent   : C.brandMid;

  const tbl = new Table({
    width: { size: 9280, type: WidthType.DXA },
    columnWidths: [1400, 7880],
    borders: {
      top:     thickBorder(),
      bottom:  thickBorder(),
      left:    thickBorder(),
      right:   thickBorder(),
      insideH: noBorder(),
      insideV: noBorder(),
    },
    rows: [
      // Header row
      new TableRow({
        children: [
          new TableCell({
            columnSpan: 2,
            shading: { fill: hdrFill, type: ShadingType.CLEAR },
            margins: { top: 100, bottom: 100, left: 140, right: 140 },
            borders: { top: noBorder(), bottom: noBorder(), left: noBorder(), right: noBorder() },
            children: [new Paragraph({
              children: [
                new TextRun({ text: label + '  ', bold: true, color: 'FFFFFF', font: 'Arial', size: 20 }),
                ...(title
                  ? [new TextRun({ text: title, color: 'FFFFFF', font: 'Arial', size: 18 })]
                  : [new TextRun({ text: '(title TBD)', italics: true, color: 'B8CFDF', font: 'Arial', size: 18 })]),
                ...(pacingFlag
                  ? [new TextRun({ text: '    ⚑ PACING FLAG', bold: true, color: 'FFFFFF', font: 'Arial', size: 16 })]
                  : []),
              ],
            })],
          }),
        ],
      }),
      beatRow('ACTION',  action,  bgColor, false),
      beatRow('EMOTION', emotion, bgColor, false),
      beatRow('STAKES',  stakes,  bgColor, pacingFlag),
    ],
  });

  return [tbl, spacer(120)];
}

// ─── main ────────────────────────────────────────────────────────────────────
const [,, dataPath, outputPath] = process.argv;

if (!dataPath || !outputPath) {
  console.error('Usage: node build_beatsheet.js <chapters.json> <output.docx>');
  process.exit(1);
}

let chapters;
try {
  chapters = JSON.parse(fs.readFileSync(dataPath, 'utf-8'));
} catch (e) {
  console.error('Failed to read/parse chapters JSON:', e.message);
  process.exit(1);
}

const bookTitle = path.basename(outputPath, '.docx').replace(/_Beat_Sheet$/, '').replace(/_/g, ' ');
const totalScenes = chapters.length;
const flaggedScenes = chapters.filter(c => c.pacingFlag);

// ─── document children ───────────────────────────────────────────────────────
const children = [];

// Title
children.push(new Paragraph({
  children: [new TextRun({ text: (bookTitle || 'Manuscript') + ' · Beat Sheet', bold: true, font: 'Arial', size: 52, color: C.brandDark })],
  spacing: { before: 240, after: 60 },
}));
children.push(new Paragraph({
  children: [new TextRun({ text: 'Working reference for read-through — chapter titles TBD', font: 'Arial', size: 20, color: C.gray, italics: true })],
  spacing: { before: 0, after: 100 },
}));
children.push(hr(C.brandLight));
children.push(spacer(80));

// Legend
const legendTable = new Table({
  width: { size: 9280, type: WidthType.DXA },
  columnWidths: [4640, 4640],
  borders: {
    top: thickBorder(), bottom: thickBorder(), left: thickBorder(), right: thickBorder(),
    insideH: noBorder(), insideV: { style: BorderStyle.SINGLE, size: 1, color: C.border },
  },
  rows: [
    new TableRow({
      children: [
        new TableCell({
          width: { size: 4640, type: WidthType.DXA },
          shading: { fill: C.headerBg, type: ShadingType.CLEAR },
          margins: { top: 80, bottom: 80, left: 140, right: 100 },
          borders: { top: noBorder(), bottom: noBorder(), left: noBorder(), right: noBorder() },
          children: [new Paragraph({
            children: [
              new TextRun({ text: 'How to use: ', bold: true, font: 'Arial', size: 18, color: C.brandDark }),
              new TextRun({ text: 'Keep this open alongside your manuscript. One block = one scene.', font: 'Arial', size: 18, color: C.textMid }),
            ],
          })],
        }),
        new TableCell({
          width: { size: 4640, type: WidthType.DXA },
          shading: { fill: C.pacingBg, type: ShadingType.CLEAR },
          margins: { top: 80, bottom: 80, left: 100, right: 140 },
          borders: { top: noBorder(), bottom: noBorder(), left: noBorder(), right: noBorder() },
          children: [new Paragraph({
            children: [
              new TextRun({ text: '⚑ PACING FLAG', bold: true, font: 'Arial', size: 18, color: C.accent }),
              new TextRun({ text: ' = red header + red STAKES row. Look at these scenes first.', font: 'Arial', size: 18, color: C.accent }),
            ],
          })],
        }),
      ],
    }),
  ],
});
children.push(legendTable);
children.push(spacer(160));

// Chapter blocks
for (const ch of chapters) {
  children.push(...chapterBlock(ch));
}

// Footer note
children.push(hr(C.brandLight));
children.push(spacer(80));
const flagLabels = flaggedScenes.map(c => c.label).join(', ');
children.push(new Paragraph({
  alignment: AlignmentType.CENTER,
  children: [new TextRun({
    text: `${totalScenes} scenes · ${flaggedScenes.length} pacing flag${flaggedScenes.length !== 1 ? 's' : ''}` +
          (flaggedScenes.length ? `: ${flagLabels}` : ''),
    font: 'Arial', size: 18, color: C.gray, italics: true,
  })],
  spacing: { before: 40, after: 0 },
}));

// ─── build document ──────────────────────────────────────────────────────────
const doc = new Document({
  styles: { default: { document: { run: { font: 'Arial', size: 20 } } } },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1080, right: 1080, bottom: 1080, left: 1080 },
      },
    },
    headers: {
      default: new Header({ children: [new Paragraph({
        children: [
          new TextRun({ text: (bookTitle || 'Manuscript') + ' Beat Sheet  ', font: 'Arial', size: 16, color: C.gray }),
          new TextRun({ text: '(working reference — titles TBD)', font: 'Arial', size: 16, color: C.gray, italics: true }),
        ],
        border: { bottom: { style: BorderStyle.SINGLE, size: 2, color: C.border, space: 4 } },
      })] }),
    },
    footers: {
      default: new Footer({ children: [new Paragraph({
        alignment: AlignmentType.RIGHT,
        children: [
          new TextRun({ text: 'p. ', font: 'Arial', size: 16, color: C.gray }),
          new TextRun({ children: [PageNumber.CURRENT], font: 'Arial', size: 16, color: C.gray }),
        ],
        border: { top: { style: BorderStyle.SINGLE, size: 2, color: C.border, space: 4 } },
      })] }),
    },
    children,
  }],
});

// Ensure output directory exists
const outDir = path.dirname(outputPath);
if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(outputPath, buf);
  console.log(`Done — ${totalScenes} scenes, ${flaggedScenes.length} pacing flags`);
}).catch(e => {
  console.error('Build error:', e.message);
  process.exit(1);
});
