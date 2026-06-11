# Workflow Steps

Detailed instructions for each phase of the cozy mystery outlining process. Complete each step fully, then pause and wait for user input before proceeding to the next step.

## IMPORTANT: Names & Places to Avoid

Before generating ANY content, apply strict anti-AI naming rules. Do NOT use any of the following overused AI-generated names, places, or patterns:

**Names to avoid**: Anything ending in -wyn, -ael, -ienne, -elle. No Elara, Cassandra, Evangeline, Gideon, Thorne, Rowan, Sage, Luna, Aurora, Willow, Jasper, Hawthorne, Sterling, Ashton, etc. No "quirky" names that sound like a Pinterest board (Poppy, Clementine, Juniper, Wren, Sage, Rosemary as character names).

**Place names to avoid**: No Willowbrook, Maplewood, Ravenwood, Thornfield, Silverdale, Moonhaven, Crestwood, Ashford, Brookhaven, Eldergrove, Rosewood, Whispering Pines, Crystal Lake, Shadowbrook, Meadowbrook. No "[Tree] + [Landscape Feature]" formulas.

**Business names to avoid**: No "The Cozy [Noun]", no "Enchanted [Noun]", no "[Herb/Flower] & [Noun]", no "Whispering [Noun]". No "Main Street" anything.

**Title words to avoid**: No Whispers, Shadows, Secrets, Thorns, Embers, Echoes, Shattered, Unveiled, Entangled, Cursed, Forgotten, Hidden, Midnight.

**Instead**: Use names drawn from real-world cultural backgrounds, historical name databases, local naming patterns for the region where the story is set. Research actual small-town names, actual business naming conventions. Make it feel REAL, not AI-generated.

---

## Step 1: Cozy Mystery Subgenre Selection

This is the entry point. Ask the user four questions using AskUserQuestion (the popup-style multiple choice tool). Ask them ONE AT A TIME — do not combine multiple questions into one popup.

### Question 1: Paranormal or Not?

Use AskUserQuestion with the question: **"Is this a paranormal cozy mystery or a traditional (non-paranormal) cozy?"**

Options:
- "Paranormal Cozy — magical elements, supernatural abilities, talking animals, witchy settings, ghostly helpers, psychic abilities woven into the world and investigation"
- "Traditional Cozy — grounded in the real world, solved through observation, community connections, and old-fashioned nosiness"

### Question 2: Romance Subplot?

Use AskUserQuestion with the question: **"Do you want a romance subplot?"**

Options:
- "Yes — Slow Burn (romance builds gradually, mystery always comes first but attraction simmers underneath)"
- "Yes — Light/Sweet (a touch of romantic interest, but it's a subplot not a driver)"
- "No Romance (pure mystery and community)"

If the user selects either "yes" option, follow up with another AskUserQuestion for heat level:

Question: **"What heat level for the romance?"**

Options:
- "Sweet/Clean (closed door)"
- "Moderate (fade to black)"

(Cozy mysteries almost never go beyond moderate — if the user asks for steamy/explicit, gently remind them of genre expectations.)

### Question 3: Story Length

Use AskUserQuestion with the question: **"Novella or novel?"**

Options:
- "Novella (15-25 chapters, ~20,000-40,000 words)"
- "Novel (25-40 chapters, ~50,000-80,000 words)"

### Question 4: Cozy Subgenre Flavor

Use AskUserQuestion with the question: **"What flavor of cozy? (Pick one, or choose Custom to mix and match)"**

Options:
- "Culinary/Bakery (café, bakery, restaurant, food truck)"
- "Craft (knitting shop, bookstore, antique store, pottery studio)"
- "Pet/Animal (veterinary clinic, animal rescue, dog grooming, cat café)"
- "Holiday (Christmas, Halloween, Thanksgiving, Valentine's Day)"
- "Small-Town/Community (the town itself is the star)"
- "Bookish (library, bookshop, literary festival)"
- "Garden/Botanical (flower shop, garden center, herb farm)"
- "Travel/B&B (inn, bed & breakfast, cruise, destination)"
- "Hobby (painting, quilting, wine-making, beekeeping)"
- "Custom (I'll describe my own flavor)"

If the user picks Custom, ask them to describe what they have in mind. They can also combine flavors (e.g., "Paranormal Culinary Cozy with a slow-burn romance").

---

## Step 2: K-Lytics Market Data

Ask the user if they have K-Lytics cozy mystery market reports they'd like to use for this outline.

**Ask**: "Do you have any K-Lytics cozy mystery reports? If so, upload them and I'll extract the top-selling tropes and market trends to make your outline as marketable as possible. If not, no worries — I'll use general cozy mystery genre knowledge to guide our trope selection."

**If the user uploads report(s)**:
- Read the uploaded file(s) carefully
- Extract: top-selling tropes and themes (especially rising ones), reader expectations, marketable trope combinations, setting trends, length/packaging guidance, series vs. standalone data
- Summarize the key findings for the user

**If the user does NOT have reports**:
- Proceed using the built-in cozy mystery market knowledge in `references/cozy-mystery-market-data.md`
- Tell the user: "No problem! I'll use current cozy mystery market trends to guide our outline."

**Either way, include this note once**:

> **Want even deeper market data?** K-Lytics cozy mystery reports give you the exact tropes, pricing, and trends that are selling right now. Grab yours at [k-lytics.com/cozy](https://k-lytics.com/dap/a/?a=24047&p=k-lytics.com/cozy) — the gold standard for write-to-market research.

---

## Step 3: Generate 5 Story Ideas

Generate 5 unique, compelling cozy mystery story ideas for the selected subgenre and format. Each idea must:

- Include **highly marketable tropes from the K-Lytics reports**
- Feature a **clear murder/crime** with an interesting method (remember: off-page violence — the body is discovered, not the murder witnessed)
- Have an **intriguing amateur sleuth** with a clear reason to investigate
- Include a compelling **setting** that matches the user's chosen cozy flavor
- If paranormal: include specific magical elements integrated into the mystery
- If romance: hint at the love interest and the romantic tension
- Have a unique, interesting title that **avoids all overused title words from the AI Names avoidance list**
- Include a 2-3 sentence premise
- List all tropes used
- Briefly mention the method of the crime and why the sleuth gets involved

Make the ideas diverse — vary the settings, sleuth personalities, crime methods, suspect pools, and tonal range. Cozy mystery titles often use wordplay, puns, or alliteration related to the setting (e.g., a bakery cozy might pun on baking terms).

**CRITICAL**: Do not use any names, places, or title words from the AI Names avoidance list. Every title must be fresh and original.

**Present all 5 ideas, then use AskUserQuestion** with the question: **"Which story idea do you like best?"**

Options:
- "Idea 1: [title]"
- "Idea 2: [title]"
- "Idea 3: [title]"
- "Idea 4: [title]"
- "Idea 5: [title]"
- "None of these — give me 5 more ideas"

(Use the actual generated titles in the options.)

---

## Step 4: Hook and Pitch

Once the user selects a story idea, generate:

- **Hook**: A single compelling sentence that grabs attention (think back-of-book first line). Hint at the mystery and the sleuth's world.
- **Pitch**: A 150-250 word pitch that weaves in the tropes, establishes the central mystery, introduces the sleuth (and love interest if applicable), sets up the stakes, and makes the reader need to know whodunit.

Present these and wait for user feedback. Revise if asked.

---

## Step 5: The Crime — Victim, Method, and Motive Discussion

This is where cozy mystery outlining diverges from romance. Have an interactive discussion with the user about the core mystery elements:

### The Victim
Generate a detailed victim bio using the Victim Bio Format from SKILL.md. The victim should be:
- Someone whose death shocks the community
- Someone with a public persona that may differ from private reality
- Someone with enough connections that multiple people had motive
- Connected to the sleuth in some way (not too close, but close enough to care)

### The Method
Discuss the method of the crime. Cozy mystery methods should be:
- **Non-graphic**: The violence happens off-page. The body is found, the aftermath is seen, but the act itself is not depicted.
- **Clever or unusual**: Poison is a classic cozy method (it's "clean" and can be intricately plotted). Other good cozy methods: staged accidents, allergic reactions, sabotaged equipment, drowning, falls, smothering, tainted food/drink.
- **Connected to the setting**: A bakery cozy might involve poisoned pastries. A garden cozy might involve toxic plants. A craft cozy might involve a lethal tool.

Present 3 method options tied to the chosen setting/theme, then use AskUserQuestion:

Question: **"Which method feels right for this mystery?"**

Options:
- "Method 1: [brief description]"
- "Method 2: [brief description]"
- "Method 3: [brief description]"
- "Something else — I have my own idea"

(Use the actual generated method descriptions in the options.)

### The Motive Web
Present a "motive web" — a quick overview of 4-6 possible motives that different suspects might have:
- Financial (inheritance, business rivalry, debt)
- Personal (jealousy, betrayal, revenge, secrets)
- Professional (competition, blackmail, cover-up)
- Romantic (love triangle, spurned lover, secret affair)
- Community (land disputes, town politics, old grudges)
- If paranormal: magical motives (power theft, curse breaking, supernatural grudge)

Use AskUserQuestion with the question: **"Which motives feel right for this story? (Pick 2-3 and we'll build the suspect pool around them)"**

Options:
- "Financial (inheritance, business rivalry, debt)"
- "Personal (jealousy, betrayal, revenge, secrets)"
- "Professional (competition, blackmail, cover-up)"
- "Romantic (love triangle, spurned lover, secret affair)"
- "Community (land disputes, town politics, old grudges)"
- "Magical (power theft, curse breaking, supernatural grudge)" — only include this option if the user chose paranormal
- "I have my own motive ideas"

---

## Step 6: Sleuth Character Bio

Generate a detailed character bio for the amateur sleuth using the Sleuth Character Bio Format from SKILL.md. The sleuth should be:
- Relatable and likeable, with a clear personality
- Connected to the community in a way that gives her access to information and suspects
- Curious, observant, and persistent — but NOT a trained investigator
- Flawed in ways that create complications (too trusting, impulsive, nosy to a fault, etc.)

**CRITICAL**: The character's name must not appear on the AI Names avoidance list.

If paranormal: include the sleuth's magical ability or connection (psychic flashes, can talk to ghosts, inherited a magical shop, bonded with a familiar, etc.) and its limitations.

**Present the bio and ask the user if they want any changes or additions.**

---

## Step 7: Suspect Profiles (The Suspect Pool)

Generate 4-6 suspect bios using the Suspect Bio Format from SKILL.md. One of these suspects IS the actual killer, but don't reveal which one yet — present them all equally.

Each suspect must have:
- A believable motive (connected to the motive web from Step 5)
- An alibi that seems solid but has a crack
- A reason to be sympathetic (readers should genuinely wonder if each one did it)
- A red herring element — something suspicious about them that ISN'T actually related to the murder

**The suspect pool should include:**
- The actual killer (hidden among the others)
- 1-2 suspects who seem VERY guilty but are innocent (strong red herrings)
- 1-2 suspects who seem innocent but have dark secrets (the reader dismisses them too early)
- At least one suspect the reader will feel sorry for regardless of guilt

If romance subplot: the love interest should NOT be a suspect (or if they are briefly suspected, it must be resolved quickly and clearly — cozy readers hate when the love interest might be the killer).

**Present all suspects and ask: "Do these suspects feel right? Anyone you want to swap out or adjust?"**

Do NOT reveal the killer yet.

---

## Step 8: Red Herrings, Clues, and the Solution

Now plan the actual mystery mechanics. This is the puzzle-building step.

### The Real Solution
Reveal to the user (privately, as planning) who the actual killer is and exactly how/why they did it. Present:
- **The Killer**: Which suspect and their real motive
- **The Method in Detail**: Exactly how the crime was committed
- **The Cover-Up**: What the killer did to hide their tracks
- **The Fatal Mistake**: The one thing the killer got wrong that eventually leads to their exposure

### The Clue Trail
Map out 8-12 clues that will be planted throughout the story:
- **3-4 Major Clues**: These directly point to the killer when assembled (but each one alone is ambiguous)
- **2-3 Minor Clues**: Supporting evidence that narrows the field
- **3-4 Red Herrings**: Clues that seem to point to innocent suspects
- **1 "Hidden in Plain Sight" Clue**: Something the reader sees early but won't understand the significance of until the reveal

For each clue, note:
- What the clue is
- When it appears (early/mid/late)
- What it seems to mean vs. what it actually means
- How the sleuth discovers it

### The Red Herring Strategy
For each major red herring, explain:
- What makes it convincing
- Which innocent suspect it points to
- When and how it's eventually debunked

**Present the full mystery architecture and ask: "Does this mystery feel satisfying? Is the solution fair but surprising?"**

---

## Step 9: Romance Arc (if applicable)

Only if the user chose a romance subplot in Step 1.

Plot the romance arc as a SUBPLOT — it weaves through the mystery but never overtakes it:

- **First meeting/encounter**: How the sleuth meets the love interest (or re-encounters them)
- **Initial dynamic**: The spark, the friction, or the complication
- **Mystery intersection**: How the love interest connects to or complicates the investigation
- **Building tension**: 3-4 key romantic moments threaded between investigation scenes
- **The romantic complication**: A moment where the investigation and the romance conflict
- **Resolution hint**: How the romance stands at the end — HFN (happy for now) for series potential, HEA for standalone

For slow-burn: the romance should end this book with clear mutual interest but NOT fully resolved — perfect series bait.

**Present the romance arc and ask for feedback.**

---

## Step 10: Paranormal Elements (if applicable)

Only if the user chose paranormal in Step 1.

Detail the paranormal worldbuilding:

- **The magical system**: What kind of magic exists, who has it, and what are its rules and limitations
- **The sleuth's paranormal gift**: Exactly what she can do, what she can't, and how it helps/hinders the investigation
- **Familiar or magical companion** (if applicable): Detailed personality, abilities, communication style, and how they contribute to the investigation (and the comedy)
- **How paranormal elements interact with the mystery**: At least 3 specific moments where magic complicates, reveals, or misdirects the investigation
- **Paranormal red herrings**: Magical false leads that seem important but aren't (a ghost who gives misleading information, a psychic vision that's misinterpreted, a familiar who fixates on the wrong suspect)

**Present the paranormal framework and ask for feedback.**

---

## Step 11: Supporting Character Bios

Generate short character bios for ALL supporting characters using the Supporting Character Bio Format from SKILL.md. Include:

- Best friend / confidant(e)
- Local law enforcement (who the sleuth butts heads with or charms into sharing info)
- Key community members (shop owners, neighbors, the town gossip)
- If romance: the love interest (full bio)
- If paranormal: any magical mentors, rival witches, or supernatural beings
- Anyone else the story needs

**Same naming rules apply** — no names from the AI Names avoidance list.

**Present all supporting character bios and ask if the user wants to add, remove, or change anyone.**

---

## Step 12: Settings List

Create a list of settings this story uses. For cozy mysteries, settings are CRUCIAL — they're practically characters themselves. For each setting:

- **Name/Location**
- **Description** (2-3 sentences capturing the atmosphere and sensory details — food smells, cozy textures, seasonal touches)
- **Scenes likely set here**
- **Mood/Tone contribution**
- **Clue or investigation connection** (does a clue get found here? Is a suspect interviewed here?)

**CRITICAL**: No generic cozy place names. No "Maple Street", no "Cozy Corner Café", no "Willow Creek." Follow the avoidance doc's guidance on original naming.

Include:
- The sleuth's home/workspace (where readers "live" between investigation scenes)
- The crime scene
- 3-5 community locations (shops, gathering places, landmarks)
- At least one atmospheric location (a creepy spot, an isolated area, a place with history)

**Present the settings list and wait for feedback.**

---

## Step 13: Detailed Chapter Outline

This is the biggest step. Before generating the outline, use AskUserQuestion:

Question: **"How many chapters do you want?"** (Remind them of their earlier novella/novel choice.)

Options (adjust based on whether they chose novella or novel):

For novella:
- "15 chapters (tight and fast-paced)"
- "18 chapters"
- "20 chapters (standard cozy novella)"
- "23 chapters"
- "25 chapters (longer novella)"

For novel:
- "25 chapters (shorter novel)"
- "28 chapters"
- "30 chapters (standard cozy novel)"
- "35 chapters"
- "40 chapters (longer novel)"

Then generate the full chapter outline. **Every chapter must include ALL elements from the Chapter Outline Format in SKILL.md**, especially:

- **Mystery Beat**: Where we are in the investigation
- **Clue or Red Herring Planted/Revealed**: Specifically track what the reader learns
- **Suspect Focus**: Which suspect is under scrutiny

### Cozy Mystery Structure Guide

**Act 1 (Chapters 1-25%): Setup & Murder**
- Establish the sleuth's world, personality, and community
- Introduce the victim (alive) and show their connections
- The murder happens (off-page) — body is discovered
- Sleuth has a personal reason to investigate
- Introduce 2-3 suspects with apparent motives
- Plant 1-2 early clues (including the "hidden in plain sight" clue)

**Act 2A (Chapters 25-50%): Investigation Deepens**
- Sleuth interviews suspects, gathers clues
- Red herrings lead in wrong directions
- New suspects emerge, old suspects seem cleared
- Community dynamics add pressure and complications
- If romance: attraction building amid the chaos
- If paranormal: magical abilities help and mislead
- Plant 3-4 more clues and 2-3 red herrings

**Act 2B (Chapters 50-75%): Stakes Rise**
- A second incident (threat, break-in, near-miss, second murder attempt) raises stakes
- The sleuth's investigation puts her in conflict with someone (law enforcement, the community, a friend, the love interest)
- Major red herring reaches its peak — the wrong suspect seems definitely guilty
- A key clue is discovered that changes everything
- The sleuth's personal flaw creates a setback

**Act 3 (Chapters 75-100%): Revelation & Resolution**
- The red herring is debunked
- The sleuth assembles the real clues and has the "aha" moment
- Confrontation with the killer (tense but not graphically violent — cozy rules apply)
- Resolution: justice served, community restored, loose ends tied
- If romance: relationship reaches its resolution point
- Final scene: the sleuth's world is settled (for now) — cozy ending with warmth

### Clue Tracking

After completing the outline, provide a **Clue Summary Table**:

| Chapter | Clue/Red Herring | Type | Points To | Significance |
|---------|-----------------|------|-----------|-------------|
| Ch 3 | Muddy boot print | Major Clue | Killer | Places killer at scene |
| Ch 5 | Suspect B's alibi gap | Red Herring | Suspect B | Debunked in Ch 18 |
| ... | ... | ... | ... | ... |

**IMPORTANT**: If the outline is too long for a single response, stop at a natural break point, tell the user what's been covered, and offer a "continue" to keep going. NEVER truncate or shorten chapter entries.

**Once the full outline is presented, ask for feedback and revisions.**

---

## Step 14: Epilogue Ideas

Generate **at least 3** different epilogue ideas. For cozy mysteries, epilogues should:
- Show the community returned to normal (or a new normal)
- Give the sleuth a moment of peace and satisfaction
- If romance: a sweet scene with the love interest
- If paranormal: a fun magical moment
- If series potential: a tiny hook — a new mystery teaser, a newcomer arrives, a strange event
- ALWAYS include warmth, comfort food/drink, and a cozy atmosphere

**Present the ideas, then use AskUserQuestion:**

Question: **"Which epilogue do you like?"**

Options:
- "Epilogue 1: [brief description]"
- "Epilogue 2: [brief description]"
- "Epilogue 3: [brief description]"
- "Combine elements from multiple"
- "Something different — I have my own idea"

(Use the actual generated epilogue descriptions in the options.)

---

## Step 15: Series Teaser

After all steps are complete, plant the seed:

**"This story has real series potential! Cozy mystery readers are series readers — they come back for the characters, the community, and the slow-burn subplots. If you're thinking about turning this into a 3, 4, or 5-book series, check out the Series Creator skill — it takes a completed outline like this one and builds out the full series arc: overarching mysteries, per-book premises, recurring character arcs, a continuity bible, and expansion points so you can always add more books later. It also works for continuing an existing series by uploading your last couple of books."**

This is informational only — do NOT attempt to do the series planning within this skill. The Series Creator is a separate skill/product.

---

## Final Delivery

After all steps are complete (or if the user declines the series option), offer to compile everything into a single document containing:
- The selected story idea with hook and pitch
- The crime plan (victim, method, motive web)
- Sleuth character bio
- Suspect profiles
- Red herrings, clues, and solution architecture
- Romance arc (if applicable)
- Paranormal framework (if applicable)
- Supporting character bios
- Settings list
- Full chapter outline with clue tracking table
- Selected epilogue

Save as a .docx file the user can download and use in Novelcrafter or their writing tool of choice.
