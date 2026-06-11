# Ebook-Style Pages

HTML chapter pages that LOOK like ebook pages — dropcap on first letter, justified or near-justified text, page-style proportions, sometimes used as standalone "first chapter preview" pages for promo, or as a Vellum-replacement workflow.

## When to use

- "Make me an ebook-style HTML page of [chapter]"
- "Pretty version of [chapter] that looks like Vellum"
- "First chapter preview as a webpage"
- "Replace-Vellum-by-hand HTML workflow"
- "Standalone reading page for [scene]"

Different from `chapter-renders.md` — that's for *editing/proofing* (clean, no flourishes, Vellum-paste-friendly). This is for *display* (dropcap, polished, presentation-ready).

## Anatomy of an ebook-style page

1. **Chapter header** — centered, small caps for "CHAPTER," large for the number, optional title
2. **Dropcap** — first letter of first paragraph, large, decorative
3. **Body prose** — serif, well-spaced, near-justified or fully-justified
4. **Scene breaks** — centered glyph or spaced asterisks
5. **End-of-chapter ornament** — optional centered glyph
6. **Maybe a back-to-top or next-chapter nav** — minimal

## Starter HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>[CHAPTER TITLE]</title>
<style>
:root {
  color-scheme: light;
  --bg: #fbf8f3;
  --text: #1f1d1a;
  --muted: #8a8478;
  --accent: #5a2a2a;
  --rule: #d8d2c4;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font-family: Georgia, 'Iowan Old Style', 'Palatino Linotype', Palatino, serif;
  font-size: 19px;
  line-height: 1.7;
  -webkit-font-smoothing: antialiased;
}
.book {
  max-width: 640px;
  margin: 0 auto;
  padding: 80px 36px 120px;
}
.chapter-header {
  text-align: center;
  margin: 0 0 56px;
}
.chapter-header .label {
  font-family: 'Iowan Old Style', Georgia, serif;
  font-size: 12px;
  letter-spacing: 0.32em;
  color: var(--muted);
  margin: 0;
}
.chapter-header .number {
  font-size: 32px;
  letter-spacing: 0.18em;
  margin: 12px 0 0;
  color: var(--text);
  font-weight: 400;
}
.chapter-header .title {
  font-family: 'Iowan Old Style', Georgia, serif;
  font-size: 14px;
  font-style: italic;
  letter-spacing: 0.06em;
  color: var(--muted);
  margin: 20px 0 0;
}
.chapter-rule {
  border: 0;
  border-top: 1px solid var(--rule);
  width: 80px;
  margin: 32px auto 56px;
}
p {
  margin: 0 0 1em;
  text-indent: 1.6em;
  text-align: justify;
  hyphens: auto;
  -webkit-hyphens: auto;
}
p.first { text-indent: 0; }
p.first::first-letter {
  font-family: 'Iowan Old Style', Georgia, serif;
  font-size: 4.2em;
  line-height: 0.86;
  float: left;
  padding: 6px 10px 0 0;
  font-weight: 500;
  color: var(--text);
}
em, i { font-style: italic; }
.scene-break {
  text-align: center;
  text-indent: 0;
  margin: 2.2em 0;
  letter-spacing: 0.8em;
  color: var(--muted);
  font-size: 16px;
}
.end-ornament {
  text-align: center;
  margin: 64px 0 0;
  color: var(--muted);
  font-size: 20px;
  letter-spacing: 0.4em;
}
::selection { background: #f3ead4; }

@media (max-width: 600px) {
  body { font-size: 18px; line-height: 1.65; }
  .book { padding: 56px 24px 80px; }
  .chapter-header .number { font-size: 26px; }
  p { text-align: left; }  /* mobile reads better left-aligned */
  p.first::first-letter { font-size: 3.6em; padding: 4px 8px 0 0; }
}
</style>
</head>
<body>

<div class="book">

<header class="chapter-header">
  <p class="label">CHAPTER</p>
  <p class="number">[ROMAN OR SPELLED]</p>
  <p class="title">[OPTIONAL ITALIC TITLE]</p>
</header>

<hr class="chapter-rule">

<p class="first">[Opening sentence — first letter becomes the dropcap.]</p>

<p>[Body paragraphs.]</p>

<p class="scene-break">✦ ✦ ✦</p>

<p>[Continued.]</p>

<p class="end-ornament">⁂</p>

</div>

</body>
</html>
```

## Notes

**Dropcap caveats:**
- `::first-letter` doesn't work well with opening quotation marks. If the first paragraph starts with a quote (`"`), the dropcap will be applied to the quote, which looks wrong.
- Workaround: wrap the first letter manually in a `<span class="dropcap">`:
  ```html
  <p class="first"><span class="dropcap">T</span>he yarrow had gone to seed.</p>
  ```
  Then style `.dropcap` instead of `::first-letter`.

**Justified text:**
- Desktop: justified looks good (especially with `hyphens: auto`).
- Mobile: justified often creates "rivers" of whitespace at narrow widths. The media query above falls back to left-aligned on mobile.

**Roman numerals:** Use uppercase Roman ("XXIV") or spelled-out caps ("TWENTY-FOUR") per the project's convention. Reliquary Duet uses spelled-out caps.

**Scene break glyphs:** Common options:
- `✦ ✦ ✦` (three diamonds, spaced)
- `* * *` (classic asterisks)
- `⁂` (asterism — single character, good for end-of-chapter)
- `❦` (floral heart — feminine/literary)
- `※` (Japanese reference mark — minimalist)

**End-of-chapter ornament:** Use a single centered glyph. Asterism (`⁂`) is the standard literary mark. Plain horizontal rule also works.

## Multi-chapter ebook-style site

If the user wants a whole book in ebook style:

1. One HTML file per chapter (`chapter-01.html`, `chapter-02.html`, …)
2. A `toc.html` index with chapter links
3. Optional: a tiny "Previous / Next" nav at the bottom of each chapter

Don't try to bundle everything in one giant file. Browsers can handle it but it's bad UX.

## Print preview / PDF export

If the user wants this to also work as a printable PDF (for ARC distribution, for example), add print CSS:

```css
@media print {
  body { background: #fff; color: #000; }
  .book { padding: 0.5in; max-width: 100%; }
  @page {
    size: 5.5in 8.5in;
    margin: 0.75in 0.6in;
  }
}
```

Then "Print to PDF" from the browser gives a reasonable proof.

## What to leave OUT of ebook-style pages

- Ads, newsletters, signup boxes (this is presentation, not promo)
- Nav menus, headers (each page is just the chapter)
- Cover images on the chapter page itself (cover goes on a separate title page if there is one)
- Comments / engagement widgets

The whole point of ebook-style is *quiet, immersive, distraction-free.* Anything that breaks immersion goes elsewhere.
