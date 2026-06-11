# Author Pages

Landing pages, book release pages, "what I'm working on" pages, simple author-bio pages.

## When to use

- "Make me a landing page for [book title]"
- "Build a release-day page for [book]"
- "What I'm working on" page
- "Mailing list signup page"
- "Author bio page"
- "Pre-order page"

## Common page jobs

1. **Single-book launch page** — cover + blurb + retailer links + email capture
2. **Series page** — multiple books in a duet/trilogy with reading order
3. **Universe page** — all series cross-linked
4. **"What I'm writing" page** — work-in-progress, expected releases
5. **Mailing-list landing** — single CTA, minimal distraction

## Section pattern for a book launch page

1. **Hero**: cover image, title, byline, one-line tagline
2. **Blurb**: 80-150 words of back-cover copy
3. **Retailer buttons**: Amazon, Apple, Kobo, Google Play, B&N, Audible if applicable
4. **Audio narrator** (if applicable): "Narrated by [Name]" with a one-line note on why
5. **A pull quote or "first lines"**: pulls the reader into the prose
6. **Mailing list capture** (optional): "Join the [list name]"
7. **About the author** (short — 2-3 sentences)
8. **Also by** (if part of a series or larger catalog)

## Starter HTML — single-book launch

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>[BOOK TITLE] — [AUTHOR NAME]</title>
<style>
:root {
  color-scheme: light;
  --bg: #faf8f4;
  --text: #1a1a1a;
  --muted: #6a6a6a;
  --accent: #5a2a2a;
  --border: #e4dfd5;
  --body: Georgia, 'Iowan Old Style', 'Palatino Linotype', Palatino, serif;
  --ui: system-ui, -apple-system, 'Segoe UI', sans-serif;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font-family: var(--body);
  font-size: 18px;
  line-height: 1.65;
}
.page { max-width: 720px; margin: 0 auto; padding: 48px 24px; }
.hero { text-align: center; margin-bottom: 56px; }
.hero img.cover {
  max-width: 280px;
  width: 100%;
  height: auto;
  box-shadow: 0 12px 36px rgba(0,0,0,0.18);
  margin-bottom: 32px;
}
h1 {
  font-size: 36px;
  margin: 0 0 8px;
  letter-spacing: 0.02em;
  font-weight: 600;
}
.byline {
  font-family: var(--ui);
  font-size: 14px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
  margin: 0 0 24px;
}
.tagline {
  font-style: italic;
  font-size: 20px;
  color: var(--text);
  margin: 0 auto;
  max-width: 480px;
}
.blurb { margin-bottom: 40px; }
.blurb p { margin: 0 0 1em; }
.retailers {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  justify-content: center;
  margin: 48px 0;
}
.retailer-btn {
  font-family: var(--ui);
  font-size: 14px;
  letter-spacing: 0.06em;
  padding: 12px 24px;
  background: var(--text);
  color: var(--bg);
  text-decoration: none;
  border-radius: 2px;
  transition: background 0.15s;
}
.retailer-btn:hover { background: var(--accent); }
.pull-quote {
  font-size: 22px;
  font-style: italic;
  line-height: 1.5;
  border-left: 3px solid var(--accent);
  padding: 0 0 0 24px;
  margin: 48px 0;
  color: var(--text);
}
.section-title {
  font-family: var(--ui);
  font-size: 13px;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--muted);
  margin: 56px 0 16px;
  text-align: center;
}
.also-by ul {
  list-style: none;
  padding: 0;
  text-align: center;
}
.also-by li {
  font-style: italic;
  margin: 8px 0;
}
hr.rule {
  border: 0;
  border-top: 1px solid var(--border);
  margin: 56px auto;
  max-width: 120px;
}
@media (max-width: 600px) {
  body { font-size: 17px; }
  h1 { font-size: 28px; }
  .page { padding: 32px 18px; }
  .pull-quote { font-size: 18px; padding-left: 18px; }
}
</style>
</head>
<body>
<main class="page">

  <section class="hero">
    <img class="cover" src="[COVER_IMAGE_URL_OR_DATA]" alt="[BOOK TITLE] cover art">
    <h1>[BOOK TITLE]</h1>
    <p class="byline">[AUTHOR NAME]</p>
    <p class="tagline">[ONE-LINE TAGLINE]</p>
  </section>

  <hr class="rule">

  <section class="blurb">
    <p>[BLURB PARAGRAPH 1]</p>
    <p>[BLURB PARAGRAPH 2]</p>
    <p>[BLURB PARAGRAPH 3 — CLOSE]</p>
  </section>

  <div class="retailers">
    <a class="retailer-btn" href="[AMAZON_URL]">Amazon</a>
    <a class="retailer-btn" href="[APPLE_URL]">Apple Books</a>
    <a class="retailer-btn" href="[KOBO_URL]">Kobo</a>
    <a class="retailer-btn" href="[GOOGLE_URL]">Google Play</a>
    <a class="retailer-btn" href="[AUDIBLE_URL]">Audible</a>
  </section>

  <blockquote class="pull-quote">
    "[A LINE FROM THE BOOK THAT PULLS THE READER IN]"
  </blockquote>

  <hr class="rule">

  <section class="also-by">
    <p class="section-title">Also by [AUTHOR NAME]</p>
    <ul>
      <li>[BOOK 1]</li>
      <li>[BOOK 2]</li>
    </ul>
  </section>

</main>
</body>
</html>
```

## Notes per common scenario

**Book release day:** Lead with cover, retailer buttons high on the page (above the fold on desktop), the blurb compact (under 150 words). Add a "Read the first chapter" link if available. Email-capture optional but worth offering.

**Pre-order:** Same as release-day but emphasize the release date as a countdown or a clear "Releases [DATE]" line in the hero. Retailer buttons should link to pre-order pages.

**Audiobook release:** Lead with the narrator name in the hero ("Narrated by [Name]"). Include a Libro.fm link alongside Audible if it's wide-distributed. A short note on the narrator-author fit lands well.

**Series page:** Each book is its own section with cover + one-paragraph blurb + retailer buttons. Reading order should be visually clear. End with a "What's next" section for forthcoming books.

**"What I'm working on":** Less commercial, more conversational. A short paragraph per project. Optional ETA. Newsletter signup at the bottom (low-pressure).

## Cover image handling

If the user gives you a cover image as an attachment, base64-encode it and embed as a `data:` URL so the page is fully self-contained. If they give you a hosted URL, use that, but note that the page is no longer fully offline. If they don't give a cover, leave a placeholder with clear `[COVER_IMAGE]` brackets and ask them to add it.

## Mailing list capture pattern

Most authors use ConvertKit, MailerLite, or Substack. Each platform gives an embed code. For the launch page, leave a clear placeholder:

```html
<section class="newsletter">
  <p class="section-title">Join the [LIST NAME]</p>
  <!-- PASTE CONVERTKIT/MAILERLITE/SUBSTACK EMBED CODE HERE -->
</section>
```

Don't try to build a custom form — it won't capture emails into the user's actual mailing list.
