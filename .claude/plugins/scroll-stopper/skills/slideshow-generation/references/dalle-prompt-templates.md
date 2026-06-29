# DALL-E 3 / Flux Prompt Templates by Genre

## CRITICAL: Always specify pairing for romance

Romance covers nearly every variant — MM (male/male), FF (female/female), MF (male/female), reverse harem, why-choose, polyamory, monster/human, etc. Image generators DEFAULT TO MF if you don't specify, which produces the wrong content for ~40% of indie romance subgenres (especially MM, which is huge on BookTok).

**Every romance image prompt MUST explicitly state the pairing**, including when the subject is a single character — specify gender unambiguously.

### Required pairing tokens (use in every romance prompt):

| Detected pairing | Tokens to inject |
|---|---|
| **MM** (male/male) | "two men", "a man and another man", "his hand on the other man's chest", "two male figures", "M/M couple" |
| **FF** (female/female) | "two women", "a woman and another woman", "her hand on the other woman", "two female figures", "F/F couple" |
| **MF** (male/female) | "a man and a woman", "his hand on her waist", "M/F couple" |
| **Reverse harem** (1F + multiple M) | "one woman, three men", "a woman flanked by three men", "RH why-choose" |
| **MMF** / triad | "two men and a woman", "throuple", explicit count |
| **Monster × human** | specify gender of human + monster type ("a man and a male orc", "a woman and a male demon") — never leave species OR gender ambiguous |
| **Single character / non-romance** | specify gender clearly ("a man", "a woman", "a non-binary figure") — avoid pronouns alone |

### Apply pairing in image AND hooks

- **Images:** prepend the pairing tokens before the subject description
- **Hooks:** use pronouns and labels matching the pairing ("He's mine. He's mine. He's mine." for MM, NOT "She's his.")
- **Single-character hooks:** still match pronouns to the actual romance lead's gender

### Detection rule

Before any image generation, the plugin must confirm the pairing with the user. Auto-detect from the manuscript by counting pronoun pairs in romantic/intimate scenes — but **never assume.** Always confirm:

> "I'm reading this as an **MM (male/male)** dark romance. Should I generate hooks and images with two men? Or is this MF / FF / RH / something else?"

---

Every prompt ends with this shared negative tail:

> ", no text, no letters, no words, no watermarks, no logos, no typography, no signage, cinematic composition, clear negative space in {upper/lower} third for text overlay"

Pick the text overlay zone (upper vs lower third) and build the image around leaving that zone visually calm.

## Dark Romance / Dark MM

**Palette:** deep blacks, blood red, bruised blues, candle-warm amber. High contrast.

**Subjects:** hands, silhouettes, a man's back, gripping objects (doorframes, wrists, glass), spilled wine, broken things, luxury interiors at night, leather, chains, pearls, smoke.

**Template:**
> "Cinematic moody photograph, {subject} in a {luxury dim interior / rain-slick alley / candle-lit bedroom}, {low-key dramatic lighting / single amber light source}, shallow depth of field, film grain, desaturated with blood red accents, {no face / silhouette / from behind}, aesthetic: A24 dark romance thriller, clear negative space in {upper third}, no text, no letters, no words, no typography, no watermarks"

**Example:**
> "Cinematic moody photograph, a man's tattooed hand gripping a crystal whiskey glass, dim amber candlelight, blood red wine spilled on white sheets, shallow depth of field, film grain, A24 aesthetic, clear negative space in upper third, no text, no letters, no words, no typography, no watermarks"

## Monster Romance

**Palette:** saturated jewel tones — emerald, violet, sapphire. Can go cosmic (nebula purples) or earthy (forest greens, orc skin).

**Subjects:** clawed hand holding human hand, massive silhouette in a doorway, horns in shadow, tail curling, fangs at rest, a human-scale room that reveals something huge is in it.

**Template:**
> "Fantasy illustrated digital painting, {huge monstrous figure / clawed hand / horned silhouette}, interacting with a human-scale element, {jewel-tone palette}, painterly, romantic fantasy cover art style, atmospheric, clear negative space in {lower third}, no text, no letters, no words, no typography"

## Paranormal Romance

**Palette:** moonlit blue-silver, blood red, forest green, cathedral gold. Moody and magical.

**Subjects:** full moon, fog, ancient library, blood on snow, a pendant, a crescent scar, cathedral architecture, forests at night.

**Template:**
> "Cinematic fantasy photograph, {moonlit forest / cathedral at night / fog-shrouded moor}, moody blue-silver palette with blood red accent, mystical atmosphere, dramatic lighting, shallow depth of field, clear negative space in {upper third}, no text, no letters, no words, no typography"

## Romantic Suspense

**Palette:** desaturated urban — slate, concrete, steel blue, muzzle flash orange. Grit.

**Subjects:** rain on a window, a handgun on a nightstand, a blurred figure through glass, a hallway at night, a hotel room, city skyline from a car window.

**Template:**
> "Cinematic thriller photograph, {rain-streaked window / dim hotel corridor / handgun on bedside table}, desaturated cool palette, single warm light source, film noir lighting, shallow depth of field, clear negative space in {upper/lower third}, no text, no letters, no words, no typography"

## Romcom (Spicy)

**Palette:** warm pastels, cream, blush, butter yellow, sage, terracotta. Sunlit.

**Subjects:** two coffee cups, a rumpled bed with one shirt on the floor, a kitchen at golden hour, lipstick on a wine glass, overlapping hands on a table, a messy bedside table with a sexy book.

**Template:**
> "Warm cinematic lifestyle photograph, {coffee cups on a sunlit counter / rumpled bed in morning light / two wine glasses and a messy kitchen}, warm pastel palette, golden hour lighting, playful composition, clear negative space in {upper third}, no text, no letters, no words, no typography"

## Romcom (Clean / Closed-Door)

**Palette:** even warmer, softer. Hallmark-adjacent but elevated.

**Subjects:** small-town storefronts, string lights, a front porch swing, autumn leaves, a dog on a welcome mat, a coffee shop window.

**Template:**
> "Cozy lifestyle photograph, {small town main street / porch swing with blanket / coffee shop at golden hour}, warm soft palette, string lights, dreamy bokeh, wholesome aesthetic, clear negative space in {upper/lower third}, no text, no letters, no words, no typography"

## Cozy Mystery

**Palette:** autumnal, warm reds/oranges/creams, or seaside blue-whites. Teacup vibes.

**Subjects:** teacup on a book, a cat on a windowsill, a crime scene with a knitted cardigan on the chair, a pie with one slice missing, a vintage library.

**Template:**
> "Cozy mystery illustration or photograph, {teacup and open book on antique table / cat beside a wool cardigan / vintage library corner}, warm autumnal palette, soft window light, slightly whimsical, clear negative space in {upper third}, no text, no letters, no words, no typography"

## Psychological Horror / Dark Stays

**Palette:** cold, desaturated, single-lamp warmth in an ocean of dark. Almost monochrome.

**Subjects:** a cabin door, an empty chair facing a window, a long hallway, a bathtub half-filled, a single lit lamp in a dark room, mirrors, locks, keys.

**Template:**
> "Unsettling cinematic photograph, {empty chair by a rain-soaked window / long dark hallway with one open door / cabin interior with single lit lamp}, cold desaturated palette with single warm light source, oppressive atmosphere, slow-burn horror aesthetic, clear negative space in {upper/lower third}, no text, no letters, no words, no typography"

## Sci-Fi (Non-Romance)

**Palette:** neon cyan + magenta, or clinical white, or deep-space blacks with starlight.

**Subjects:** a corridor of a spaceship, a visor reflecting stars, a planet from orbit, a holographic interface, a single astronaut figure, a server room.

**Template:**
> "Cinematic sci-fi photograph, {spaceship corridor / planetary surface / holographic interface}, {neon cyan and magenta / deep space black with starlight}, atmospheric, moody, clear negative space in {upper third}, no text, no letters, no words, no typography"

## Cozy Fantasy / LitRPG

**Palette:** warm fantasy pastels — lavender skies, mint, peach, gold.

**Subjects:** a witch's bakery, a dragon on a teapot, a glowing enchanted plant, a cozy fantasy shop interior, a pet familiar.

**Template:**
> "Cozy fantasy illustration, {enchanted bakery / tiny dragon on a teapot / mushroom cottage interior}, warm pastel palette, studio ghibli-inspired, whimsical, clear negative space in {upper/lower third}, no text, no letters, no words, no typography"

## Thriller / Suspense

**Palette:** high-contrast blacks and sodium-orange streetlight yellows. Urban.

**Subjects:** rear-view mirror at night, headlights on wet road, a phone on a kitchen table, a door left open, running shoes in a doorway.

**Template:**
> "Cinematic thriller photograph, {rear-view mirror at night / wet road under streetlights / phone on empty kitchen table}, high contrast, sodium-orange and deep black palette, tense atmosphere, clear negative space in {upper third}, no text, no letters, no words, no typography"
