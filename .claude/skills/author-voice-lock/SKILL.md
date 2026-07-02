---
name: author-voice-lock
description: Use this skill whenever drafting, continuing, or expanding original fiction prose where a specific author voice must hold. Trigger when the user asks to "draft," "write," "continue," "expand," or "ghostwrite" anything in the style of a configured voice profile — including chapters, scenes, scene inserts, openings, closers, blurbs, and back-cover copy. Trigger when the user names a pen name or profile (e.g., "draft as [pen name]", "use my [name] voice profile", "write this in [profile] voice"). Trigger when the user references a profile file under profiles/ in this skill. Also trigger when the user wants to set up, build, or fill in a new voice profile from scratch (guided intake). Do NOT trigger for editorial passes on already-drafted prose, for casual brainstorming, for non-fiction, or when a more specific series-keyed drafting skill is available.
---

# Author Voice Lock — Drafting Skill

A drafting-time skill that enforces a configurable author voice profile during prose generation. It is the generic, fill-in-the-details version of a series-keyed drafting skill: the structure is fixed, the content is yours.

## Core principle

**Read the active profile before generating any new prose.** A voice profile is dense by design. Loading it costs seconds; not loading it costs hours of editorial pass cleanup later.

## What this skill does

1. Loads a voice profile (banned vocab, signature moves, POV/tense, dialogue mechanics, trope guardrails, worldbuilding hooks, character voice rules) from `profiles/`.
2. Applies those rules during drafting, not after.
3. Runs a post-draft grep checklist against the banned terms in the active profile.
4. Reports any non-trivial fixes the grep pass caught.

## What this skill does NOT do

- Editorial passes on already-drafted prose — pair with `full-stack-manuscript-polish` or a series-specific editing skill.
- Replace a series-keyed skill that already exists for the same author. If one exists (e.g., a Vauclain Monsters or Infernum Academy drafting skill), use that — it carries series canon this skill cannot.
- Generate the profile content for the author. The author fills in the profile (manually, or via the guided intake in `references/INTAKE.md`).

---

## Profile selection

Profiles live in `profiles/`. Each profile is a single Markdown file named after the pen name or voice (e.g., `profiles/jane-doe.md`, `profiles/dark-fantasy-pen-name.md`).

When invoked, choose the active profile in this order:

1. **Explicit name in the request.** If the user says "draft as Jane Doe" or "use the dark-fantasy profile," look for `profiles/jane-doe.md` or `profiles/dark-fantasy.md` (case-insensitive, hyphens or underscores both fine). Match by filename without the `.md` extension.
2. **Single-profile fallback.** If exactly one profile file exists in `profiles/` (excluding `_TEMPLATE.md` and `_EXAMPLE.md`), load it.
3. **Ask.** If multiple profiles exist and none was named, list the available profiles and ask which to use before drafting. Do not guess.
4. **Setup mode.** If no user profile exists yet (only `_TEMPLATE.md` and `_EXAMPLE.md`), tell the user the skill needs a profile first and offer to walk them through `references/INTAKE.md`.

Never invent a profile. Never blend two profiles. One profile per drafting session unless the user explicitly asks for a crossover.

---

## Drafting workflow

When asked to draft new prose under a voice profile:

1. **Identify the active profile** using the rules above.
2. **Read the full active profile** before generating a single sentence. The profile is short by design and read every time.
3. **Read `references/AI_TELL_LIBRARY.md`** if the active profile opted into universal AI-tell guardrails (most should).
4. **Draft the requested prose** with the profile's rules applied during generation. Honor:
   - POV and tense
   - Sentence rhythm and paragraph density
   - Banned vocabulary (zero tolerance)
   - Signature moves to preserve
   - Dialogue mechanics
   - Genre/trope guardrails and content lines
   - Worldbuilding capitalization canon
   - Character voice rules
5. **Run the post-draft grep checklist** built from the profile's banned vocabulary section. Catch what generation missed.
6. **Deliver.** Note any non-trivial banned-vocab fixes from the grep pass in the response so the author can verify.

---

## Setting up a new profile

If the user wants to create a profile from scratch, there are two paths:

- **Manual.** Copy `profiles/_TEMPLATE.md` to `profiles/<pen-name>.md` and fill it in. `profiles/_EXAMPLE.md` shows what a complete profile looks like.
- **Guided intake.** Read `references/INTAKE.md` and walk the user through it section by section, writing the answers into a new `profiles/<pen-name>.md` as you go. Confirm each section before moving on. Never invent answers.

---

## Critical rules summary (applies to every profile)

These hold regardless of which profile is active. Profile rules layer on top.

### One voice per session
Do not blend voices. If the user invokes a profile, every sentence of generated prose obeys that profile until the user explicitly switches.

### Profile beats default
If a banned word in the profile contradicts something in the AI tell library, the profile wins. If the profile says "fragments are signature, preserve them," the editorial reflex to "vary sentence structure" is suppressed.

### Voice is generation-time, not editing-time
Apply the rules while drafting. Do not draft loose and clean up after. The cleanup pass is a safety net, not a strategy.

### Honest reporting
If the generated prose violates a banned-vocab rule and the grep pass catches it, say so when delivering. Do not silently rewrite.

### No invented canon
If the profile has worldbuilding hooks (proper nouns, magic system terms, place names), use only what's in the profile. If the prose needs a new term, flag it for the author rather than inventing one.

---

## File layout

```
author-voice-lock/
├── SKILL.md                         (this file)
├── README.md                        (install, multi-profile usage, troubleshooting)
├── profiles/
│   ├── _TEMPLATE.md                 (blank fillable template — do not edit; copy)
│   ├── _EXAMPLE.md                  (a fictional filled-in example for reference)
│   └── <your-pen-name>.md           (one or more user-created profiles)
└── references/
    ├── INTAKE.md                    (guided Q&A to build a profile from scratch)
    └── AI_TELL_LIBRARY.md           (universal AI tells; profiles can opt in)
```
