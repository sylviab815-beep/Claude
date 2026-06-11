# Author Voice Lock

A configurable drafting skill for fiction authors who want their LLM-assisted prose to hold a specific voice — without keying the skill to a single series.

If you've ever drafted a chapter, gotten back something that *sounds* technically correct but reads like every other LLM scene on the internet, this is the fix. You fill in a profile once. The skill reads it before generating a sentence. The voice holds.

---

## What's in the box

```
author-voice-lock/
├── SKILL.md                         The skill itself — workflow and triggering rules
├── README.md                        This file
├── profiles/
│   ├── _TEMPLATE.md                 Blank fillable template — copy this for each voice
│   └── _EXAMPLE.md                  Fictional filled-in example (Marian Holt) for reference
└── references/
    ├── INTAKE.md                    Guided Q&A — the skill walks you through filling in a profile
    └── AI_TELL_LIBRARY.md           Universal AI-tell patterns; profiles opt in
```

---

## Setup

### Option A — Fill in the template yourself

1. Copy `profiles/_TEMPLATE.md` to `profiles/<your-pen-name>.md`. Use lowercase and hyphens for the filename: `profiles/jane-doe.md`, `profiles/dark-fantasy-pen.md`.
2. Open `profiles/_EXAMPLE.md` for reference. Marian Holt is fictional — she shows what a complete, useful profile looks like.
3. Fill in every section. Be specific. _"Punchy prose"_ produces nothing useful. _"Average sentence 12-20 words; fragments earned at action peaks; em-dashes for self-correction only"_ produces consistent voice.
4. Save.

### Option B — Guided intake

Ask the skill:

> Build me a voice profile from scratch.

The skill will run the interview in `references/INTAKE.md` — it asks one section at a time, writes your answers into a new profile file, reads each section back, and confirms before moving on. Takes 10–20 minutes for a well-tuned profile.

---

## Using the skill

Once you have a profile, invoke the skill by naming it:

> Draft chapter 3 as Jane Doe.
>
> Continue this scene in the dark-fantasy voice.
>
> Use my Marian Holt profile and write a 500-word opening.

The skill will:

1. Find `profiles/jane-doe.md` (or whichever profile you named).
2. Read the full profile before drafting.
3. Read `references/AI_TELL_LIBRARY.md` if your profile opted in.
4. Draft the prose with the rules applied during generation.
5. Run a post-draft grep pass against your banned-vocab list.
6. Note any non-trivial fixes when delivering.

If you have only one profile, the skill loads it automatically without needing to be named.

If you have multiple profiles and don't name one, the skill will list them and ask.

---

## Multiple pen names

This is what the skill is built for. Drop a profile per pen name into `profiles/`:

```
profiles/
├── _TEMPLATE.md
├── _EXAMPLE.md
├── jane-doe.md             ← cozy mystery
├── j-d-cole.md             ← grimdark fantasy
└── jdoe-romance.md         ← contemporary romance
```

Invoke whichever voice you need:

> Draft as J.D. Cole.
> Use my jdoe-romance profile.

Each profile is self-contained. They don't bleed into each other. You can write a cozy chapter in the morning and a grimdark chapter in the afternoon and the voices don't cross.

---

## Tuning a profile over time

Treat the profile as a living document. Every editorial pass that catches a tic the skill missed during drafting is a tic you should add to the profile so the next session catches it during generation. Add to:

- **Section 6** if the tic is a banned-vocab item.
- **Section 7** if you discover a signature move you want preserved.
- **Section 13** if it's a pattern that drifts in from default LLM prose.
- **Section 14** if it should be in the post-draft grep pass.

A profile that's tuned over five or ten drafting sessions will hold voice as well as a series-keyed skill.

---

## When to use this vs. a series-keyed skill

- **Use this skill when:** you write under multiple pen names, you write standalone novels, you write across multiple genres, or you write in a voice that doesn't have its own dedicated skill yet.
- **Use a series-keyed skill when:** one already exists for your series. A series-keyed skill carries world canon, recurring character bibles, and dangling threads that this generic skill cannot. If you don't have one and want one, ask the skill-creator skill to build one off your filled-in profile plus your series bible.

---

## Limits

This skill enforces voice. It does not:

- Replace editorial passes on already-drafted prose. Pair with a manuscript-polish skill for that.
- Carry series canon. Worldbuilding hooks in the profile are light by design — recurring proper nouns, setting type, recurring motifs. For deep canon (cast, magic system, timeline), use a series-keyed skill.
- Generate the profile content. You fill in the profile. The skill cannot write your voice into existence; it can only protect a voice that already exists.

---

## Troubleshooting

**The drafted prose still sounds generic.** The profile is too vague. Open it and check Section 6 (banned vocab) — if you have fewer than ten items, the skill has nothing to grip on. Add the words you find yourself fixing in editorial passes. Five concrete bans beat fifty vague preferences.

**The skill picked the wrong profile.** Name it explicitly: _"Use my <pen-name> profile"_ or _"Draft as <pen-name>"_. Filename match is case-insensitive and hyphen/underscore-tolerant.

**The skill loaded a profile but the prose violated a rule.** Tell it. The grep pass should have caught it; if it didn't, the rule may need to move from a description into the post-draft grep checklist (Section 14) with a regex that catches the pattern.

**I don't know what to put in Section X.** Read `profiles/_EXAMPLE.md`. If you're still stuck, run the guided intake — it asks the right questions and offers concrete examples without putting words in your mouth.
