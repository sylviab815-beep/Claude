# AI Tell Library

Universal AI-tell patterns that drift into LLM-generated prose regardless of voice. A profile opts in by setting Section 8 to "yes" or by listing specific categories.

These are the patterns that show up in every voice's editorial pass when LLM-assisted drafting is involved. Catching them at draft time saves cleanup later.

## Category A — Trope tags and stage directions

- **"a shiver ran down [her] spine"** — banned. The body either does something specific or it doesn't.
- **"[she] let out a breath [she] hadn't realized [she] was holding"** — banned. Capital-T trope.
- **"[his] heart pounded / hammered / thundered"** — banned as default. Allowed only if the POV character is genuinely tracking heart rate as data.
- **"[his] breath caught"** — banned as default.
- **"[her] eyes widened"** — banned as default. Use a specific reaction or none.
- **"[he] swallowed hard"** — banned as default.
- **"[her] knees went weak"** — banned.
- **"[he] couldn't help but [verb]"** — banned. Either he did it or he didn't.

## Category B — Filler intensifiers

- **suddenly** — banned. The prose should make the suddenness audible without naming it.
- **finally** — banned as a stage direction. _He finally turned_ → _He turned._
- **simply** — banned as filler. _He simply walked away_ → _He walked away._
- **just** — handle with care. Frequent in dialogue, banned as narration filler. _It was just so much_ → cut or rewrite.
- **really** — banned as intensifier. _She was really angry_ → render the anger.
- **very** — banned as intensifier. Find the specific word.
- **literally** — banned outside of dialogue.
- **basically** — banned outside of dialogue.

## Category C — Hedging tells

- **"a sense of [emotion]"** — banned as filler. _A sense of unease_ → render the unease or cut.
- **"something like [emotion]"** — handle with care. Allowed when the POV character is genuinely groping for the right name; banned as default hedging.
- **"a hint of [emotion]"** — banned.
- **"a flicker of [emotion]"** — banned. Either rendered or cut.
- **"a wave of [emotion]"** — banned.
- **"a pang of [emotion]"** — banned.
- **"a feeling of [emotion]"** — banned. Find the rendering.

## Category D — Atmospheric clichés

- **"the air seemed to [verb]"** — banned. Air doesn't seem.
- **"the silence was [adjective]"** as an opener — banned. _The silence was deafening._ → cut or render specifically.
- **"palpable [noun]"** — banned. _Palpable tension._ Find the rendering.
- **"thick with [noun]"** — banned. _The room was thick with tension._ → cut or render.
- **"hung in the air"** — banned. _The question hung in the air._ → cut.
- **"deafening silence"** — banned.
- **"pregnant pause"** — banned.

## Category E — Comparator constructions

- **"the way [X] [verbs]"** as simile/comparator — banned. _The way the light caught his face._ Allowed: literal idioms — _the way home, the way back, the way down._ Rule of thumb: if it can be replaced with _like_ or _as_, it's the banned form.
- **"the kind of [noun] that [verbs]"** — banned as comparator. _The kind of silence that swallows sound._ → rewrite.
- **"like a [noun]"** as default simile — handle with care. Allowed when the simile is fresh; banned when it's a stock comparison.
- **"as if [clause]"** — handle with care. Frequent and load-bearing in some voices; lazy hedging in others. Profile decides.

## Category F — Stacks and lists

- **Adjective stacks of three or more** — banned as default. _The cold, dark, empty house_ → find the one adjective that does the work.
- **Not-X stacks** _(three short denials in a row)_ — banned. _Not air. Not water. Not blood._ → rewrite as a single sentence with _or_.
- **Tricolon emotional escalation** _(three rising emotional adjectives)_ — banned. _She was angry, furious, livid._ → pick one.

## Category G — Telegraphed emotion

- **Naming the emotion before showing it** — banned as default. _She was sad. She started to cry._ → render.
- **"[He] felt [emotion]"** — banned as default. Render or cut.
- **"a part of [him] [verbed]"** — banned. _A part of him wanted to leave._ → either he wanted to or he didn't.
- **"deep down, [he] knew"** — banned.

## Category H — Camera moves and cinematic tells

- **"the camera pans"** — banned (literally never write this).
- **"the scene shifts"** — banned.
- **Aerial-shot openings** — banned. _The town sat nestled in the valley._ → start in the body of the scene.

## Category I — Therapy-speak

- **processing** — banned as emotional verb. _I'm processing this._ → render.
- **holding space** — banned.
- **boundaries** in the modern emotional sense — banned unless the character is explicitly and on-page someone who would use that vocabulary.
- **"sit with [feeling]"** — banned.
- **"unpack [topic]"** — banned outside of dialogue.

## Category J — Authorial tells

- **Genre-aware winks** — banned. No nodding at the reader. No _of course, in a story like this._
- **"little did [she] know"** — banned. No flagged foreshadowing.
- **"if only [she] had known"** — banned.
- **Stage-directing the reader** — banned. _Pay attention to this detail._

---

## How the profile uses this library

The profile's Section 8 (AI-tell guardrails) opts in. Default: yes, all categories. The profile can:

- Opt in to all categories (the default).
- Opt in to specific categories by letter (e.g., "A, B, F, G, I").
- Opt out entirely (rare; only voices that genuinely use one of these patterns as signature should opt out).
- Override individual rules — if a profile says "the way [X] verbs" is a signature comparator in this voice, the profile wins.

When drafting, the skill applies the opted-in categories during generation and runs the post-draft grep pass against the patterns above plus the profile's own banned-vocab list.
