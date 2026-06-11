# Chapter Renders

Manuscript-style HTML for proofing chapters, sharing with beta readers, or copy-pasting into Vellum / Word / wherever.

## When to use

- "Render this chapter in HTML"
- "HTML version of [chapter] so I can read it on my phone"
- "Beta-reader copy of [chapter]"
- "Pretty version of this for proofing"
- "Copy-paste-into-Vellum HTML"

## Three modes — pick based on the user's job

### Mode 1: Manuscript-style (for proofing / beta readers)

Clean, readable, distraction-free. Italics preserved. Smart quotes. Em-dashes intact. Single column, comfortable line length. No dropcap (Vellum handles that later). Mobile-friendly.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>[CHAPTER TITLE]</title>
<style>
:root { color-scheme: light; }
body {
  background: #faf8f4;
  color: #1a1a1a;
  font-family: Georgia, 'Iowan Old Style', 'Palatino Linotype', Palatino, serif;
  font-size: 18px;
  line-height: 1.7;
  margin: 0;
  padding: 0;
}
.page { max-width: 680px; margin: 0 auto; padding: 48px 28px 80px; }
.chapter-header {
  text-align: center;
  margin: 24px 0 56px;
  letter-spacing: 0.18em;
  font-size: 14px;
  color: #555;
}
.chapter-header .num {
  display: block;
  margin-top: 8px;
  font-size: 22px;
  letter-spacing: 0.22em;
  color: #1a1a1a;
}
.chapter-header .title {
  display: block;
  margin-top: 14px;
  font-size: 13px;
  letter-spacing: 0.08em;
  color: #888;
  font-style: italic;
}
p {
  margin: 0 0 1.1em;
  text-indent: 1.6em;
}
p.first { text-indent: 0; }
em, i { font-style: italic; }
::selection { background: #f0e8d4; }
@media (max-width: 600px) {
  body { font-size: 17px; }
  .page { padding: 32px 20px 60px; }
}
</style>
</head>
<body>
<div class="page">

<div class="chapter-header">
  CHAPTER<span class="num">[NUMBER]</span><span class="title">[CHAPTER TITLE]</span>
</div>

<p class="first">[First paragraph — no indent.]</p>

<p>[Subsequent paragraphs — indented.]</p>

<!-- ... chapter content ... -->

</div>
</body>
</html>
```

Notes:
- First paragraph has no indent (`p.first`); rest are indented.
- Italics: use `<em>` tags around italic spans.
- Smart quotes: use `&ldquo;` / `&rdquo;` for double, `&lsquo;` / `&rsquo;` for single. Em-dashes: `&mdash;`.
- Scene breaks: a centered glyph or three dots — `<p style="text-align: center; text-indent: 0; margin: 2em 0;">* * *</p>`

### Mode 2: Vellum-paste-ready (no formatting that fights Vellum)

When the user wants to write/edit in HTML and then paste into Vellum:

- **No CSS text-indent** — Vellum applies its own paragraph indentation.
- **No CSS dropcap** — Vellum has dropcap settings per book.
- **No chapter header styling** — Vellum has chapter title fields.
- **Italics preserved** — use `<em>` (Vellum reads it).
- **Smart quotes preserved** — use the entities or actual smart-quote characters.

The pattern is the same as Mode 1 but with `text-indent: 0` and no dropcap. Add a button to the page that copies just the body (no header) to clipboard with formatting preserved:

```html
<button id="copyBtn">Copy chapter body</button>
<div id="body">
  <!-- chapter paragraphs -->
</div>

<script>
document.getElementById('copyBtn').addEventListener('click', async function() {
  const html = document.getElementById('body').innerHTML;
  const text = Array.from(document.querySelectorAll('#body p'))
    .map(p => p.textContent.trim()).join('\n\n');
  try {
    await navigator.clipboard.write([
      new ClipboardItem({
        'text/html': new Blob([html], { type: 'text/html' }),
        'text/plain': new Blob([text], { type: 'text/plain' })
      })
    ]);
    this.textContent = 'Copied — paste into Vellum.';
  } catch (err) {
    this.textContent = 'Copy failed — select manually.';
  }
});
</script>
```

### Mode 3: Running-headers, print-preview style

When the user wants a closer-to-final preview (page numbers, running headers). This is more elaborate; use `@page` CSS for print. Note: many browsers ignore `@page` for screen, so this mode is mostly useful for "Print to PDF" preview.

```css
@page {
  size: 5.5in 8.5in;  /* US digest */
  margin: 0.75in 0.6in;
  @top-center {
    content: string(book-title);
    font-family: Georgia, serif;
    font-size: 10px;
    letter-spacing: 0.18em;
    color: #888;
  }
  @bottom-center {
    content: counter(page);
    font-family: Georgia, serif;
    font-size: 10px;
    color: #888;
  }
}

h1.book-title { string-set: book-title content(); }
```

Use sparingly — print-CSS support is browser-dependent.

## Italics conversion

Markdown source like `*the resting*` should become `<em>the resting</em>` in HTML. Single-asterisk pairs around text → italic. Double-asterisks → bold (rare in fiction prose).

If chapter source is .md, convert `\*([^*]+)\*` to `<em>$1</em>` before wrapping in `<p>` tags.

## Smart quote conversion

Raw .md often has straight quotes (`"` and `'`). For polished HTML:

| Character | Entity | When |
|---|---|---|
| ` " ` opening double | `&ldquo;` | Before a word/letter |
| ` " ` closing double | `&rdquo;` | After punctuation or word |
| ` ' ` opening single | `&lsquo;` | Before a word (rare) |
| ` ' ` apostrophe / closing | `&rsquo;` | Inside or after a word |
| ` -- ` em-dash | `&mdash;` | Between clauses |

A simple regex pass:
- ` "` (space-then-quote) → ` &ldquo;`
- `" ` (quote-then-space) and `"` at end of clause → `&rdquo; `
- `'s`, `'t`, `'re`, etc. → `&rsquo;`
- `--` → `&mdash;`

Or just use actual Unicode smart quote characters in the HTML source (they survive copy-paste).

## Scene break convention

The Reliquary Duet uses paragraph-break-only scene shifts (no `* * *`). For other projects, the user may want centered glyphs:

```html
<p style="text-align: center; text-indent: 0; margin: 2em 0; letter-spacing: 0.6em; color: #888;">✦ ✦ ✦</p>
```

Default: paragraph break only. Ask if the user wants visual scene breaks.

## What NOT to include in chapter renders

- Ads, popups, signup boxes (let proofing be pure prose)
- Cover images (chapter is text-only)
- Footnotes unless the chapter has them in source
- "Next chapter" navigation (one chapter per file is the convention)

## Multi-chapter rendering

If the user asks for "the whole book in HTML," default to one chapter per file with a simple index file linking them. Don't put a whole novel in one HTML file unless they explicitly ask — browsers handle it but it's awkward to navigate.

```html
<!-- index.html -->
<ul>
  <li><a href="chapter-01.html">CHAPTER ONE — [TITLE]</a></li>
  <li><a href="chapter-02.html">CHAPTER TWO — [TITLE]</a></li>
  ...
</ul>
```
