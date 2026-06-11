# Chapter-by-Chapter Edit

A voice-locked editorial skill for fiction authors. You hand it one chapter; it runs eleven editorial passes against your voice profile and delivers the result in whichever format you want — flagged report, marked-up chapter, or cleaned replacement.

Pairs with `author-voice-lock`. Same profile system. Drafting skill enforces voice during generation; this skill enforces voice during revision.

---

## What's in the box

```
chapter-by-chapter-edit/
├── SKILL.md                           The skill itself — workflow, profile lookup, pass pipeline
├── README.md                          This file
└── references/
    ├── EDITORIAL_PASSES.md            The eleven passes, with what each looks for
    └── OUTPUT_FORMATS.md              The three delivery formats with examples
```

This skill carries no profiles of its own — it reads from `author-voice-lock/profiles/`.

---

## Setup

1. Install `author-voice-lock` first if you haven't. This skill needs at least one voice profile to work, and the profiles live in `author-voice-lock/profiles/`.
2. Install `chapter-by-chapter-edit` (this skill) the same way: **+** → **Manage Skills** → add the `.skill` file.
3. Confirm at least one profile exists at `author-voice-lock/profiles/<your-pen-name>.md`. If not, run the guided intake from `author-voice-lock` to build one.

---

## Using the skill

Hand the skill a chapter and name your profile (or let the skill use your only profile if you have one):

> Edit chapter 3 as Jane Doe.
>
> Run a chapter pass on this — use my Marian Holt profile.
>
> Polish chapter 5 in my dark-fantasy voice and give me a flagged report.
>
> Clean up the attached chapter as J.D. Cole.

The skill will:

1. Find the matching profile.
2. Read the full profile before reading the chapter.
3. Read the chapter end-to-end.
4. Ask which output format you want for this chapter (unless you specified one).
5. Run the eleven passes in order.
6. Deliver in the chosen format.

---

## The eleven passes

1. **Voice integrity** — banned vocab, AI tells, out-of-voice phrasing.
2. **POV & tense consistency** — head-hops, tense slips, POV drift.
3. **Sentence rhythm preservation** — protect signature moves (fragments, parallels, three-beat closers).
4. **Dialogue mechanics** — tags, adverbs, action beats, character voice consistency.
5. **Filter words & show-don't-tell** — _watched, noticed, felt, started to_, etc.
6. **Tone consistency** — flag therapy-speak, romance-novel cadence, clinical detachment, anything off-register.
7. **Repetition & tic words** — echo flags within paragraph and chapter span.
8. **Continuity (within chapter)** — names, timeline, positions, established facts.
9. **Structure & shape** — does the chapter open, escalate, button?
10. **Opening & closer audit** — first paragraph hooks, last paragraph lands.
11. **Worldbuilding canon** — capitalization rules from the profile.

Full spec in `references/EDITORIAL_PASSES.md`.

---

## The three output formats

You pick per chapter:

- **Flagged issues report** — markdown with sections per pass, each issue listing location, current text, suggested fix, and rule. Non-destructive. You apply what you want. Best for line edits and chapters with lots of small issues.
- **Marked-up chapter** — the full chapter with inline strikethroughs and bracketed suggestions. Easy to scan. Best for sentence-level cleanup.
- **Cleaned replacement chapter** — the rewritten chapter plus a change summary. Fast. Author-decision flags surface separately for things that need your call (POV shifts, structural changes, new proper nouns). Best when you trust the rules and want the work done.

You can also ask for all three if you want to compare formats; the skill will warn that it's 3× the output.

Full spec in `references/OUTPUT_FORMATS.md`.

---

## Multiple pen names

Same model as `author-voice-lock` — drop a profile per pen name in `author-voice-lock/profiles/` and name the profile when you invoke this skill:

> Edit chapter 3 as Jane Doe.
> Edit the same chapter as J.D. Cole.

Two clean passes, one profile each, no bleed.

---

## Tuning the workflow over time

When a pass misses something the editorial pass should have caught, the right fix is usually in the profile, not the skill:

- A word you keep finding in your prose that wasn't in the banned-vocab list → add it to profile Section 6.
- A signature move the skill kept "fixing" → add it to profile Section 7.
- A character voice tic the skill flattened → add it to profile Section 11.
- A repeated tone slip → add it to profile Section 13.

The skill plus a tuned profile holds tighter every cycle.

---

## When to use this vs. other skills

- **Use this skill when:** you want a deep editorial pass on one chapter at a time, calibrated to a voice profile.
- **Use `author-voice-lock` when:** you're drafting new prose, not editing existing prose.
- **Use `full-stack-manuscript-polish` when:** you're running a whole-manuscript workflow with cross-book continuity, dangling threads, and final assembly.
- **Use a series-keyed editing skill when:** one already exists for your series. Series-keyed skills carry canon (cast, magic system, dangling threads) this generic skill cannot. If your series doesn't have one yet, this skill plus a tuned profile gets you most of the way.

---

## Limits

This skill enforces voice and runs an eleven-pass copyedit pipeline. It does not:

- Catch cross-chapter continuity. The continuity pass is within-chapter only. Names, timelines, and facts established in earlier chapters can't be cross-checked without reading the rest of the book.
- Replace developmental editing. Plot holes, character arc problems, theme drift — out of scope.
- Carry world canon. The worldbuilding pass uses what's in profile Section 10; if your world has more rules, those need to live in the profile or in a series-keyed skill.

---

## Troubleshooting

**The skill can't find my profile.** Confirm the file exists at `author-voice-lock/profiles/<pen-name>.md`. Filename match is case-insensitive and hyphen/underscore-tolerant. If you only have one profile, the skill should pick it up automatically without being named. If you have multiple, name the one you want.

**The skill ran all eleven passes but the report feels light.** The profile is probably thin. Check Section 6 (banned vocab) and Section 7 (signature moves). Five concrete bans beat fifty vague preferences. Five named signature moves beat zero.

**The skill flagged something that's actually a signature move.** Two possibilities. Either Section 7 of the profile doesn't list it (add it), or Section 7 lists it but the rule is too vague to grip on (be more specific — example passages help).

**The skill flagged a pass for "constraint."** That means the profile lacked a section the pass needed. The flag will name which section. Fill it in for next time.

**The cleaned replacement applied a change I didn't want.** Switch to the flagged report or marked-up format for that chapter. The cleaned replacement is the most aggressive format; use it when you trust the rules. The other two formats give you per-issue control.

**My chapter has a deliberate POV/tense shift the skill keeps flagging.** Add it to profile Section 2 (e.g., "tense slips into present for memory passages — preserve") or Section 12 (things the voice does). The skill will stop flagging it.
