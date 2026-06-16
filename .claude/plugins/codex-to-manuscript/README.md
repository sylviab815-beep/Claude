# Codex to Manuscript

Turn a complete Codex + Outline package into a publish-ready first-draft manuscript.

## What This Plugin Does

You upload your Codex (story bible) and your chapter-by-chapter Outline — typically as PDFs from a story-pack purchase. The plugin:

1. **Parses both files** into structured data (characters, locations, lore, subplots, per-chapter beats).
2. **Shows you a summary** of everything it found.
3. **Asks if you want to change anything** — character names, gender, places, POV, tense, heat level, length target, or supply your own writing sample for voice matching.
4. **Auto-detects the genre** and applies a matching guardrail system (Supernatural Consequence for paranormal romance, Comedy Architecture for romcom, Darkness Calibration for dark romance, Clue Disclosure for mystery, etc.).
5. **Writes the entire manuscript** chapter-by-chapter with **edit-as-you-go** editorial passes. After every chapter, it scans for AI-isms, voice drift, and genre rule violations before moving on.
6. **Runs structural integrity gates every 3 chapters** — catches narrator future-leak ("I would later learn…"), telegraphed clues, premature antagonist reveals, and outline drift before they compound.
7. **Runs a six-pass end-of-book editorial pipeline** — AI-ism scrub, developmental edit, beta read, line edit, proofread, and a holistic whole-book polish pass.
8. **Holistic Manuscript Polish** — final whole-book pass that strips artificial chapter endings, removes AI artifacts, fixes stiff dialogue, locks all sense-detail to POV, and ensures continuous narrative momentum from chapter to chapter (without shortening anything).
9. **Final integrity sweep** before delivery — must pass before the manuscript is finalized.
10. **Delivers a publish-ready `.docx` manuscript**, a companion **KDP Info** document (Amazon metadata, blurb, cover prompt), and an **Edit Log** of every change made.

## Usage

```
/write-from-codex
```

Then upload your codex and outline files when prompted, confirm the output folder, answer the revision questions, and let the pipeline run.

## Supported Input Formats

- `.pdf` (primary — what most story packs ship as)
- `.docx` (editable version)
- `.txt` / `.md` (pasted text or markdown)

## What You Get

```
[Book Title]/
├── [Book Title].docx           ← the manuscript
├── [Book Title] - KDP Info.docx ← Amazon metadata + cover prompt
└── [Book Title] - Edit Log.md   ← chapter-by-chapter edit notes
```

## Time

A 50,000-word manuscript takes several hours with the full edit-as-you-go pipeline. A 30k novella takes 2-3 hours. Faster modes are offered if you need quicker turnaround:

- **Draft-only** — skip per-chapter editing; run only the end-of-book pipeline
- **No editorial** — produce the first draft and stop; you can edit separately later

## What This Plugin Doesn't Do

- It does not generate the codex or the outline. Use the matching outline-builder plugin for that.
- It does not produce a print-formatted PDF or upload to KDP.
- It does not generate cover art (but does include a cover prompt you can feed to Ideogram, Midjourney, or your designer).

## Files

```
codex-to-manuscript.plugin/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── write-from-codex.md       ← main pipeline command
│   ├── check-integrity.md        ← structural integrity scan (standalone)
│   ├── check-outline-drift.md    ← outline-drift scan (standalone)
│   └── polish-manuscript.md      ← holistic whole-book polish (standalone)
└── skills/
    └── codex-to-manuscript/
        ├── SKILL.md              ← the orchestrator
        ├── scripts/
        │   ├── parse_codex.py            ← parses any codex (PDF or DOCX)
        │   ├── parse_outline.py          ← parses any outline (PDF or DOCX)
        │   ├── integrity_check.py        ← future-leak / telegraph / antagonist density / clear-speed
        │   └── outline_drift_check.py    ← compares draft to outline beats
        └── reference/
            ├── genre_guardrails.md   ← genre-to-guardrail routing
            ├── editorial_pipeline.md ← edit-as-you-go + end-of-book pipeline
            ├── integrity_checks.md   ← integrity + outline-drift gates
            ├── manuscript_polish.md  ← holistic whole-book polish spec
            ├── ai_ism_scrub.md       ← banned AI phrases
            ├── parsing_rules.md      ← codex/outline format reference
            ├── user_revisions.md     ← how to apply user edits
            └── docx_template.md      ← final document formatting
```
