# Text Overlay Style Profiles

Each genre maps to a style profile the Python builder uses. The profile controls font family, weight, color, stroke, shadow, and positioning logic.

When writing `slideshow_plan.json`, set `text_style` to the profile key below and `text_position` to either `"top"` or `"bottom"`. Alternate top/bottom across slides for feed rhythm, unless a specific image demands one side.

## Profile Keys

| text_style | Genres | Font stack | Color | Stroke | Shadow |
|---|---|---|---|---|---|
| `dark_romance` | dark romance, dark MM | Bold condensed serif (Playfair Display 900 / Cormorant Garamond 700) | #FFFFFF | 2px black | Soft dark drop |
| `monster_romance` | monster romance | Bold display serif (Cinzel 900 / UnifrakturCook) | #F5E9C8 (cream) | 2px #2B1A0F | None |
| `paranormal_romance` | paranormal romance | Serif italic (Italiana / Great Vibes mixed) | #E8DCC4 | 2px #1A1A2E | Glow |
| `romantic_suspense` | romantic suspense, thriller | Bold sans condensed (Oswald 700 / Bebas Neue) | #FFFFFF | 3px black | Hard shadow |
| `spicy_romcom` | romcom spicy | Handwritten + bold serif combo (Caveat Bold + Playfair) | #FFF8F0 | 2px #C97B63 | Soft |
| `clean_romcom` | clean romcom, cozy fantasy | Rounded sans (Quicksand 700 / Nunito 800) | #3A2E2A | 1px #FFFFFF | None |
| `cozy_mystery` | cozy mystery | Vintage serif (Libre Baskerville Bold) | #3A2E2A | 1px #FFF8E7 | Soft cream |
| `dark_stays` | psychological horror, dark stays | Thin condensed serif (EB Garamond Italic 500) | #E8E2D4 | 1px #0A0A0A | Heavy dark |
| `sci_fi` | sci-fi | Monospace or techno sans (Space Mono Bold / Orbitron 700) | #00E5FF or #FFFFFF | 2px #0A0A0F | Neon glow |
| `thriller` | pure thriller | Impact-style sans (Anton / Bebas Neue) | #FFFFFF | 3px black | Hard |

## Layout rules

All 1024×1792 canvas:

- **Top position**: text vertical center at y = 320 (upper fifth), padding 64px left/right
- **Bottom position**: text vertical center at y = 1472 (lower fifth), padding 64px left/right
- **Max text width**: 896px (1024 - 2×64)
- **Font size auto-fits** between 72px and 140px based on character count, preferring the largest size that fits within 3 lines
- **Line spacing**: 1.15× font size
- **Alignment**: center

## Safe zones

- **Instagram Reels / TikTok UI**: bottom 240px is often covered by UI chrome. If `text_position = "bottom"`, the baseline sits at y ≈ 1472 which leaves ~320px clearance — safe.
- **Top UI (profile/time)**: top 160px. A top-position baseline at y ≈ 320 clears this by ~160px — safe.

## Gradient plates (optional)

For very busy images, the builder can drop a subtle gradient behind the text. Set `"text_plate": true` in the slide entry. The plate is:

- Top position: black gradient from 0 opacity at 25% down to 45% opacity at the top
- Bottom position: mirrored — 0 opacity at 75% up to 45% at the bottom

Use a plate by default for `dark_romance`, `dark_stays`, `thriller`, and any other profile where legibility risk is high.
