---
name: beat-sheet-generator
description: |
  Generates a chapter-by-chapter beat sheet as a Word document (.docx) from any fiction manuscript. Each scene gets a color-coded block showing ACTION (what physically happens), EMOTION (the keynote feeling), and STAKES (what changed). Scenes with flat arcs, passive protagonists, or repeated emotional loops are highlighted in red as pacing flags. Use this skill whenever an author says "make a beat sheet", "map my chapters", "I need a read-through reference", "show me my story structure", "beat map my manuscript", "what's happening in each chapter", "give me a chapter overview", "create a structural map", or wants a compact overview before a read-through or revision pass. Also trigger when an author uploads a manuscript and asks about pacing, structure, or where their story slows down. The output is always a Word document — never just a chat response — so trigger this skill any time the author wants a structural map rather than a quick answer.
---

# Beat Sheet Generator

Reads a fiction manuscript and produces a compact Word document mapping every scene in reading order. Three lines per scene: ACTION / EMOTION / STAKES. Pacing problems get red headers and a ⚑ flag so the author can spot them at a glance during their read-through.

## What this produces

A single .docx file with:
- A legend explaining how to use the document
- One color-coded table block per chapter/scene in reading order
- Each block: a dark header (chapter label + existing title if any) + three rows
- Pacing-flagged scenes: red header, red STAKES row, ⚑ marker in the header
- Header with document title; page numbers in footer

---

## Step 1: Extract the manuscript text

**For .docx files** (including ones with tracked changes — strip all of that):
```bash
pandoc "<input.docx>" -t plain -o /tmp/manuscript_clean.txt 2>/dev/null
```
If pandoc fails, use the unpack approach from the docx skill to extract document.xml and strip XML tags with a quick Python script.

**For .epub:**
```bash
pandoc "<input.epub>" -t plain -o /tmp/manuscript_clean.txt
```

**For .txt files:** read directly — no extraction needed.

---

## Step 2: Map the chapter and scene structure

Read through the clean text and identify every chapter/scene break. Look for:
- `Chapter X`, `Chapter X: Title`, `Chapter X - Scene Y`, `Prologue`, `Epilogue`, `Forward`, `Afterword`
- Any line that functions as a chapter divider (author's convention may vary — use context)

Record each break's exact label and any existing title. Don't renumber or rename — capture exactly what's in the manuscript, since the author or an editor will assign final titles.

For long manuscripts (60,000+ words), read in sections of 10–15 chapters at a time rather than trying to hold everything at once.

---

## Step 3: Write the beat data for each scene

For each chapter or scene, determine three things:

**ACTION** — What physically happens? What do characters do, discover, decide, or fail to do? 2–4 sentences. Focus on events that move the story — not backstory, not description. If the scene is mostly internal, say so honestly.

**EMOTION** — What is the keynote feeling of the scene? Not the plot — the emotional register. What does the reader feel as they finish this scene? One sentence, specific rather than generic ("Helplessness giving way to grim resolve" beats "sad but determined").

**STAKES** — What changed? What does the reader know, fear, or hope at the end of this scene that they didn't at the start? If nothing changed, say so directly — that's the most important thing to know about a scene.

---

## Pacing flag criteria

Set `"pacingFlag": true` when any of these apply. The author will use these flags as priorities during their read-through, so flag honestly — being too conservative is the same as being unhelpful.

1. **Flat stakes** — The scene ends with the same stakes as it began. No escalation, no reversal, no new revelation that reframes what came before. The STAKES line will naturally say something like "no change" or "status quo maintained."

2. **Emotional loop** — The same emotional beat repeats 2+ times within this scene without breaking to something new. The character circles the same fear, doubt, or grief without arriving anywhere different. The scene ends where it started emotionally.

3. **Passive protagonist** — The POV character accepts a mission, assignment, or situation without any friction, pushback, or active costly choice. They're moved by the plot rather than moving through it.

4. **Frictionless briefing** — A scene whose sole purpose is delivering information — a briefing, an explanation, an exposition dump — with no complication, no interruption, no cost to anyone present. Pure frictionless information transfer.

5. **Urgency gap** — A high-stakes event is established in this scene (character missing, major threat revealed, betrayal discovered) but the consequences don't land for 2 or more scenes afterward. Flag the scene where the gap opens, not where it closes.

---

## Step 4: Build the JSON data file

Write the chapter array to `/tmp/beatsheet_data.json`. Each entry follows this structure:

```json
[
  {
    "label": "Ch 1",
    "title": "Forward",
    "action": "Author frames the book as the series' darkest act...",
    "emotion": "Anticipation laced with warning...",
    "stakes": "Reader context established; the full weight of the series named.",
    "pacingFlag": false
  },
  {
    "label": "Ch 15 · Scene 2",
    "title": null,
    "action": "Shadow finds the clone's sabotage footage...",
    "emotion": "Catastrophic — the clone has gone active...",
    "stakes": "Clone has taken violent action. Chuck locked out. Shadow missing.",
    "pacingFlag": true
  }
]
```

**Label conventions:**
- Use `Ch X` rather than `Chapter X` to keep headers compact
- Normalize `Chapter X - Scene Y` → `Ch X · Scene Y`
- Use `Prologue`, `Epilogue`, `Forward`, `Afterword` as-is

**Title:** Use the title exactly as it appears in the manuscript, or `null` if the scene has no title yet.

---

## Step 5: Run the build script

Determine the skill's base directory (shown as "Base directory for this skill" when this skill loaded). Then run:

```bash
NODE_PATH=/usr/local/lib/node_modules_global/lib/node_modules \
node "<skill-base-dir>/scripts/build_beatsheet.js" \
  /tmp/beatsheet_data.json \
  "<outputs-folder>/<BookTitle>_Beat_Sheet.docx"
```

The script reads the JSON from argument 1 and writes the .docx to argument 2. It will print `Done` on success or an error message on failure.

---

## Step 6: Deliver

Present the .docx file to the author using `mcp__cowork__present_files` or a `computer://` link.

Tell them:
- How many scenes were mapped total
- How many pacing flags were found and which chapters carry them (so they know what to look at first)
- That red blocks in the document = pacing flags = the ones to read critically

---

## Notes on manuscript conventions

- Some authors use scene breaks within chapters (often marked with `* * *` or `---`). If these contain distinct plot beats, treat each as a separate block.
- Chapter numbering is often messy in raw drafts — trust what the manuscript says, not what the numbering "should" be.
- Some manuscripts have placeholder titles or "TBD" — note those as-is in the title field.
- If the manuscript has a codex, character list, or other front/back matter that isn't story, skip it or summarize it briefly as a single block.
