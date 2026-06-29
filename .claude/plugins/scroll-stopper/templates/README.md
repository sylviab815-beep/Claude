# Sample CSV templates

Three sample files showing exactly what Scroll Stopper writes for your scheduler. Same fake book ("Debt Marker" by Dana Sacco — MM dark romance) reformatted into each scheduler's bulk-import format so you can see how the same content lands in each tool.

## Files

| File | Scheduler | What it shows |
|---|---|---|
| `metricool-sample.csv` | Metricool | Full Metricool calendar template — one row per platform with TikTok/Instagram/Facebook/etc. boolean columns + per-platform metadata (Reel type, Pinterest board, YouTube category, etc.) |
| `later-sample.csv` | Later | Simpler 5-column format: Scheduled Time, Caption, Media URL, Profile, Label |
| `buffer-sample.csv` | Buffer | 5 columns: Text, Image URL, Tags (auto-extracted from hashtags), Posting Time, Board Name |
| `hootsuite-sample.csv` | Hootsuite | 5 columns: Date, Message, Link (auto-extracted), Image URL, Profile |

## Use these to:

1. **Preview before you run** — open one to see what's coming
2. **Reference when hand-editing** — if you need to add a row manually
3. **Test your scheduler import** — try importing the sample first to make sure your scheduler accepts the format before running with real content

## When Scroll Stopper writes the real version

When you run `/create-slideshow` with `auto_generate_captions: true` in your config, Scroll Stopper:

1. Generates platform-tuned captions (different captions for TikTok vs Instagram vs YouTube — not the same caption everywhere)
2. Pulls genre + platform-appropriate hashtags
3. Injects your buy link, CTA, and handle
4. Matches pronouns to your confirmed pairing (MM/FF/MF/RH/etc.)
5. Writes the CSV in the format your `default_scheduler` expects
6. You fill in date/time per row → import → done

## Caveats

- **Metricool video uploads via bulk CSV** — Metricool puts video links in `Picture Url 1`. Some platforms (especially TikTok) may require a separate upload step inside Metricool's UI for the video to attach properly. Test with one row before bulk-importing 50.
- **Buffer Pinterest posts** — need a Board Name. Sample leaves blank. Edit before importing if posting to Pinterest via Buffer.
- **Later profile names** — must match the exact name of the connected social account inside Later. Sample uses your handle; verify it matches.
