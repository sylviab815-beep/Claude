---
name: html-everything
description: Use this skill whenever the user asks for HTML — author landing pages, book release pages, newsletter/email templates, Substack-paste-ready posts, chapter renders for proofing or sharing, interactive promo pages (quizzes, calculators, character widgets), ebook-style chapter pages, character or worldbuilding bonus-content pages, image galleries, or any other web-renderable page. Trigger on "make me an HTML…", "build a landing page", "newsletter template", "Substack post", "HTML version of this chapter", "interactive page about…", "character page", "render this in HTML", "single-page site for…", or any request where the deliverable is HTML. Do NOT use this skill for Cowork artifacts that need live MCP data — those use the artifact tool's own conventions.
---

# HTML Everything

A general-purpose skill for producing clean, attractive, single-file HTML for an author's needs — landing pages, newsletter templates, chapter renders, interactive promo, ebook-style pages, and bonus content (character pages, worldbuilding sketches, deleted scenes).

## Core principles

**Single file, self-contained.** Every page is one `.html` file. Inline all CSS. Inline all JS unless explicitly told otherwise. Use `data:` URLs for small images. No build process. No external dependencies the user has to install.

**Light mode default.** Unless the user asks for dark or gothic-dark. Add `:root { color-scheme: light; }` at the top of every stylesheet.

**Mobile-responsive.** Always include `<meta name="viewport" content="width=device-width, initial-scale=1">` and design for 360px-wide screens first. Use CSS that doesn't break at narrow widths.

**Accessible by default.** Semantic HTML (`<article>`, `<header>`, `<nav>`, `<main>`, `<footer>`). Proper heading hierarchy (one `<h1>` per page, then `<h2>`, then `<h3>`). Alt text on every image. Sufficient color contrast (WCAG AA minimum: 4.5:1 for body text).

**Serif body type for prose.** Default body font: `Georgia, 'Iowan Old Style', 'Palatino Linotype', Palatino, 'Times New Roman', serif`. UI elements (buttons, nav, captions) can use system-ui: `system-ui, -apple-system, 'Segoe UI', sans-serif`. Body font-size: 18px on desktop, 17px on mobile. Line-height: 1.6-1.7 for body prose.

**No framework dependencies.** Plain HTML, plain CSS, plain JS. The user should be able to open the file in any browser. No React, no Vue, no build steps, no npm install. If interactivity needs more than 100 lines of JS, ask first.

**Save to user's selected folder.** Default save location is `/Users/kateseger/Documents/Claude/Projects/[current project]/` or wherever the user's working. Use clear filenames: `bone-covenant-launch.html`, not `page.html`.

---

## When to invoke this skill

| User says… | Use this skill |
|---|---|
| "Make me a landing page for [book]" | Yes — see `author-pages.md` |
| "Build a newsletter template" | Yes — see `email-and-newsletter.md` |
| "Render this chapter in HTML" | Yes — see `chapter-renders.md` |
| "Make a quiz / calculator / widget" | Yes — see `interactive-pages.md` |
| "Ebook-style HTML version of this" | Yes — see `ebook-pages.md` |
| "Character page / deleted scene / map / bestiary" | Yes — see `bonus-content.md` |
| "Make me an HTML artifact" | Use Cowork's artifact tool instead — different format |
| "I need a Word document / PDF / spreadsheet" | Use the corresponding skill (docx, pdf, xlsx) |

## Workflow

1. **Clarify scope.** Ask only what you can't infer:
   - What's the page's job? (Sell a book, capture emails, share a chapter, entertain.)
   - Where is it going? (Website, email-pasted, Substack-pasted, ebook export.)
   - Any specific aesthetic? (Default is clean literary; gothic-flavored if the project is dark.)
   - What images/text does the user already have, vs. what do you need to draft?
2. **Pick the right reference file.** Each `references/*.md` has concrete starter HTML and platform-specific notes. Read the relevant one before building.
3. **Build the page.** Use the starter HTML from the reference as a base. Customize content. Tune typography and color to project. Validate at 360px and 1200px widths mentally before saving.
4. **Save with a clear filename.** Project-related stuff goes in the project folder. Use kebab-case: `bone-covenant-character-map.html`.
5. **Surface it cleanly.** Give the user a `computer://` link to view. Mention the file's purpose in one sentence. Don't post-amble.

## Reference files

| File | Covers |
|---|---|
| `author-pages.md` | Landing pages, book release pages, "what I'm working on" pages, simple author bio pages |
| `email-and-newsletter.md` | Email-safe HTML (tables, inline styles), Substack-paste-ready posts, MailerLite/ConvertKit templates |
| `chapter-renders.md` | Manuscript-style HTML for proofing or sharing with betas; copy-paste-into-Vellum format; running headers |
| `interactive-pages.md` | Quizzes, calculators, "which character are you" widgets, simple games, promo widgets |
| `ebook-pages.md` | Vellum-style ebook chapter pages, dropcap rendering, proper page breaks for print-style |
| `bonus-content.md` | Character pages, family trees, maps, bestiaries, deleted scenes, worldbuilding guides, image galleries |

## Common patterns across all HTML output

### Typography defaults

```css
:root {
  color-scheme: light;
  --body-font: Georgia, 'Iowan Old Style', 'Palatino Linotype', Palatino, 'Times New Roman', serif;
  --ui-font: system-ui, -apple-system, 'Segoe UI', sans-serif;
  --color-bg: #faf8f4;
  --color-text: #1a1a1a;
  --color-muted: #6a6a6a;
  --color-accent: #5a2a2a;  /* deep oxblood — adjust per project */
  --color-border: #e4dfd5;
  --max-prose-width: 680px;
}

body {
  font-family: var(--body-font);
  font-size: 18px;
  line-height: 1.65;
  color: var(--color-text);
  background: var(--color-bg);
  margin: 0;
  padding: 0;
}

@media (max-width: 600px) {
  body { font-size: 17px; }
}
```

### Page skeleton

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>[Page Title]</title>
<style>
  /* inline CSS here */
</style>
</head>
<body>
  <main>
    <!-- content here -->
  </main>
</body>
</html>
```

### Responsive image pattern

```html
<figure>
  <img src="data:image/..." alt="Descriptive alt text" loading="lazy" style="max-width: 100%; height: auto; display: block;">
  <figcaption>Optional caption</figcaption>
</figure>
```

### Project-specific aesthetic notes

- **Gothic / dark fantasy projects** (Reliquary Duet, Cathedral of Crows): Cream paper background (`#faf8f4`), warm-black text (`#1a1a1a`), oxblood or rust accent (`#5a2a2a`), serif body type, optional candle/flame emoji as decoration (sparingly).
- **Paranormal romance** (Monsters of Ahi'koa, Veil Keepers): Slightly more saturated; teal/seafoam accents okay; can lean a bit more visual.
- **Romantasy / academic** (Infernum Academy, Zenith Hall): Library-feeling — burgundy/ivory, parchment textures okay, more ornamental.

If the project's aesthetic isn't documented, default to the literary-gothic palette above and ask if a different feel is wanted.

## Final-check protocol

Before sharing the file, mentally walk through:

- [ ] Opens in a browser as a single file with no missing dependencies
- [ ] Looks right at 360px (mobile) and 1200px (desktop) widths
- [ ] All images have alt text
- [ ] One `<h1>` per page; heading hierarchy is logical
- [ ] No `localStorage` / `sessionStorage` calls unless explicitly requested
- [ ] No external network requests unless the user knows
- [ ] No leftover placeholder text (`Lorem ipsum`, `TODO`, etc.)
- [ ] Filename is descriptive and kebab-case
- [ ] If email-safe / Substack-pasteable, run through the email-safe checklist in `email-and-newsletter.md`

## What this skill does NOT do

- Cowork artifacts (use the `create_artifact` tool — different format, persists in sidebar)
- Word/PDF/Excel deliverables (use the docx/pdf/xlsx skills)
- Multi-page sites with build processes (this skill is for single-file pages; if the user needs a full site, ask whether a static-site generator would be better)
- JavaScript-framework apps (React, Vue, etc.) — ask for explicit confirmation if the request seems to need one
