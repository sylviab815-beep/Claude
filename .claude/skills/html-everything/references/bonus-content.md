# Bonus Content Pages

Character pages, family trees, maps, bestiaries, deleted scenes, worldbuilding guides, image galleries, soundtrack pages — the "extras" that live around a book.

## When to use

- "Character page for [Name]"
- "Worldbuilding wiki for [series]"
- "Family tree"
- "Bestiary / monster guide"
- "Map of [setting]"
- "Deleted scene page"
- "Soundtrack page for [book]"
- "Behind-the-scenes / annotation page"
- "Image gallery from [research / mood boards]"

Bonus content is *fan-facing.* The job is to give readers more to live in after they've finished the book.

## Style register

More visual than chapter renders. More personal than promo pages. The reader has already read the book; they want depth, not pitch. Lean into:
- Concrete sensory details (what does Else's cottage smell like?)
- Material specifics (what's in Margery's pocket?)
- The kind of thing that wouldn't make it into the book proper

Avoid:
- Recapping the plot
- Generic "she was strong and brave" character bios
- Long lists of stats

## Pattern 1: Character page

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>[CHARACTER NAME] — [BOOK]</title>
<style>
:root { color-scheme: light; }
* { box-sizing: border-box; }
body {
  margin: 0;
  background: #faf8f4;
  color: #1a1a1a;
  font-family: Georgia, 'Iowan Old Style', serif;
  font-size: 17px;
  line-height: 1.65;
}
.page { max-width: 680px; margin: 0 auto; padding: 48px 24px 80px; }
.character-header {
  text-align: center;
  margin-bottom: 48px;
}
.character-header .role {
  font-family: 'Iowan Old Style', serif;
  font-size: 12px;
  letter-spacing: 0.32em;
  text-transform: uppercase;
  color: #6a6a6a;
  margin: 0 0 12px;
}
.character-header h1 {
  font-size: 48px;
  margin: 0 0 12px;
  font-weight: 500;
  letter-spacing: 0.04em;
}
.character-header .epithet {
  font-style: italic;
  color: #5a2a2a;
  margin: 0;
}
.field-grid {
  display: grid;
  grid-template-columns: 140px 1fr;
  gap: 12px 24px;
  margin: 48px 0;
  font-size: 16px;
}
.field-grid dt {
  font-family: 'Iowan Old Style', serif;
  font-size: 12px;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: #6a6a6a;
  padding-top: 2px;
}
.field-grid dd { margin: 0; }
.body-prose p {
  margin: 0 0 1em;
}
.body-prose blockquote {
  border-left: 3px solid #5a2a2a;
  padding-left: 18px;
  font-style: italic;
  margin: 24px 0;
  color: #4a4a4a;
}
.section-title {
  font-family: 'Iowan Old Style', serif;
  font-size: 12px;
  letter-spacing: 0.28em;
  text-transform: uppercase;
  color: #6a6a6a;
  margin: 48px 0 16px;
  border-bottom: 1px solid #d4cfc5;
  padding-bottom: 8px;
}
@media (max-width: 600px) {
  .character-header h1 { font-size: 36px; }
  .field-grid { grid-template-columns: 1fr; gap: 4px 0; }
  .field-grid dt { margin-top: 12px; }
}
</style>
</head>
<body>
<main class="page">

<header class="character-header">
  <p class="role">[ROLE — e.g., "BONE WOMAN OF ASHENMERE"]</p>
  <h1>[CHARACTER NAME]</h1>
  <p class="epithet">[ONE-LINE EPITHET OR CHARACTER MOTTO]</p>
</header>

<dl class="field-grid">
  <dt>Born</dt>            <dd>[YEAR / PLACE]</dd>
  <dt>Age in book</dt>     <dd>[AGE]</dd>
  <dt>Trade</dt>           <dd>[OCCUPATION]</dd>
  <dt>Carries</dt>         <dd>[OBJECTS / TOOLS — specific items]</dd>
  <dt>Voice tells</dt>     <dd>[ONE OR TWO QUIRKS]</dd>
  <dt>Will not</dt>        <dd>[WHAT THEY REFUSE — character-defining]</dd>
</dl>

<div class="body-prose">

<p class="section-title">Who they are</p>
<p>[Two to three paragraphs of character description — concrete, specific, in your authorial voice. Avoid plot summary.]</p>

<p class="section-title">A line of theirs</p>
<blockquote>[A signature line of dialogue from the book — one that captures their voice.]</blockquote>

<p class="section-title">What they wouldn't say but would think</p>
<p>[A glimpse into their interior — a thought they'd never voice. This is bonus-content territory.]</p>

<p class="section-title">What they smell like</p>
<p>[Concrete sensory detail. Yarrow, ink, wood smoke, leather, sea salt.]</p>

</div>

</main>
</body>
</html>
```

## Pattern 2: Family tree

SVG-based. Simple boxes connected by lines. Click a node to scroll to that character's details below (or open a modal).

```html
<svg viewBox="0 0 800 500" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: Georgia, serif;">
  <!-- Eleanor (mother) -->
  <g class="node">
    <rect x="320" y="40" width="160" height="56" fill="#faf8f4" stroke="#1a1a1a" stroke-width="1.5"/>
    <text x="400" y="68" text-anchor="middle" font-size="14" font-weight="600">Eleanor</text>
    <text x="400" y="84" text-anchor="middle" font-size="11" fill="#888">d. October 1348</text>
  </g>
  <!-- line down to Else -->
  <line x1="400" y1="96" x2="400" y2="180" stroke="#1a1a1a" stroke-width="1"/>
  <!-- Else -->
  <g class="node">
    <rect x="320" y="180" width="160" height="56" fill="#faf8f4" stroke="#5a2a2a" stroke-width="2"/>
    <text x="400" y="208" text-anchor="middle" font-size="14" font-weight="600">Else</text>
    <text x="400" y="224" text-anchor="middle" font-size="11" fill="#888">bone woman</text>
  </g>
  <!-- ... -->
</svg>
```

For complex trees (3+ generations, branching lineages), consider laying out by hand in vector software and exporting as SVG.

## Pattern 3: Map

For book maps, options range from simple to elaborate:

**Simple:** A hand-drawn map saved as an image, with `<img>` and `<figcaption>`. Add `usemap` and `<map>` if you want clickable regions.

**SVG-based:** Hand-drawn paths, regions labeled. Hover effects work.

**Interactive panning:** Use a library like Leaflet (but that breaks the "no dependencies" rule). For most book promo, a static image is fine.

Default approach: static SVG or static image with clear labels. Don't over-engineer.

## Pattern 4: Bestiary / monster catalog

Card-based grid layout. Each "card" is one creature.

```html
<style>
.bestiary {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 24px;
}
.creature {
  background: #fff;
  border: 1px solid #d4cfc5;
  padding: 24px;
}
.creature h2 {
  font-size: 22px;
  margin: 0 0 8px;
  letter-spacing: 0.04em;
}
.creature .type {
  font-family: 'Iowan Old Style', serif;
  font-size: 11px;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: #6a6a6a;
  margin: 0 0 16px;
}
.creature p { margin: 0 0 12px; font-size: 15px; line-height: 1.55; }
.creature .stat {
  font-family: 'Iowan Old Style', serif;
  font-size: 12px;
  color: #6a6a6a;
  letter-spacing: 0.12em;
  margin-top: 16px;
  padding-top: 12px;
  border-top: 1px solid #e4dfd5;
}
</style>

<div class="bestiary">
  <article class="creature">
    <h2>The Hollowed</h2>
    <p class="type">Possession class — physical body retained</p>
    <p>The plague-dead whose bodies are still moving. The ancient thing wears them; the men inside are not entirely gone. They walk because something walks them.</p>
    <p class="stat">FIRST RISEN — October 1348, the field at Ashenmere's eastern edge.</p>
  </article>
  <!-- more creature cards -->
</div>
```

## Pattern 5: Deleted scene page

Frame it as: this was cut from [chapter X] because [reason]. Then the scene itself. Then a short note on what it would have changed.

```html
<article class="deleted-scene">
  <header>
    <p class="meta">DELETED FROM CHAPTER [N] · [BOOK]</p>
    <h1>[SCENE TITLE]</h1>
    <p class="reason">Cut because: [one-line reason — pacing, tone, structure, etc.]</p>
  </header>

  <div class="scene-prose">
    <!-- scene paragraphs -->
  </div>

  <aside class="author-note">
    <p><strong>Author note:</strong> [What this scene would have done if it had stayed. Or what you learned by cutting it.]</p>
  </aside>
</article>
```

## Pattern 6: Soundtrack page

If the user wrote to music. Each track + a sentence about what it meant for the scene.

```html
<article class="soundtrack">
  <h1>The [BOOK] Soundtrack</h1>
  <p class="intro">These are the songs I wrote to. Each one anchored a scene or a character.</p>

  <ul class="tracks">
    <li>
      <p class="track">"[SONG TITLE]" — [ARTIST]</p>
      <p class="note">[CHAPTER REFERENCE]. [What this song was for in your process.]</p>
    </li>
    <!-- more tracks -->
  </ul>

  <p class="cta"><a href="[SPOTIFY_PLAYLIST_URL]">Full playlist on Spotify →</a></p>
</article>
```

Avoid embedding Spotify iframes — they're slow and tracker-heavy. Link out instead.

## Pattern 7: Image gallery / mood board

Grid layout, lightbox optional. Keep it simple — no carousels.

```html
<style>
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 12px;
}
.gallery figure {
  margin: 0;
  background: #fff;
  border: 1px solid #d4cfc5;
  padding: 8px;
}
.gallery img {
  width: 100%;
  height: 240px;
  object-fit: cover;
  display: block;
}
.gallery figcaption {
  font-size: 13px;
  color: #6a6a6a;
  padding: 8px 4px 0;
  text-align: center;
  font-style: italic;
}
</style>

<div class="gallery">
  <figure>
    <img src="[URL_OR_DATA]" alt="[Description]">
    <figcaption>[What this image is / why it's here]</figcaption>
  </figure>
  <!-- more figures -->
</div>
```

## Cross-linking bonus content

If the user has multiple bonus-content pages, give them a small index:

```html
<nav class="bonus-index">
  <p class="section-title">Beneath the Book</p>
  <ul>
    <li><a href="characters.html">The Cast</a></li>
    <li><a href="map.html">Ashenmere and the Roads</a></li>
    <li><a href="bestiary.html">The Hollowed, the Thinned, the Ancient Thing</a></li>
    <li><a href="deleted-scene-margery.html">Cut Scene — Margery at the Convent</a></li>
    <li><a href="soundtrack.html">The Soundtrack</a></li>
  </ul>
</nav>
```

Each page links back to the index in a small nav at the top or bottom.

## What makes bonus content land

- **Specificity.** "Else's hands smell like yarrow and willow bark" is better than "Else is a healer."
- **What the book couldn't say.** Bonus content is the place for the line that didn't fit, the detail that got cut, the question the reader has after closing the book.
- **The author's voice.** Not third-person Wikipedia voice. The voice that wrote the book.
- **One image per beat.** Don't over-illustrate.

## What doesn't work

- Wiki-style stat blocks (height, weight, eye color, "favorite food")
- Plot recap (readers who reached the bonus page already know)
- Generic adjectives ("brave," "loyal," "kind")
- Stock images that don't match the project
