---
name: genre-group-finder
description: Finds active Facebook groups and Goodreads groups for a given book genre or subgenre so an author can grow readership and place promo. Use this skill whenever the user wants to discover reader/author communities to join or promote in — triggers include "find Facebook groups for [genre]", "Goodreads groups for [genre]", "where can I promote my [genre] book", "find reader groups", "find author groups", "what communities should I join for [subgenre]", "FB groups for cozy mystery / romance / thriller etc.", "build me a list of groups to promote in", or any request to locate, list, or vet genre-specific Facebook or Goodreads communities. Use it even if the user just says "find me groups" in a publishing/marketing context. This is for community discovery — NOT for newsletter swaps or BookFunnel/Bookclicker promos (those belong to the Book Promo Command Center).
---

# Genre Group Finder

Help an author discover the Facebook and Goodreads communities where their readers gather, and produce a sortable spreadsheet they can work through. The goal is a practical promo/engagement target list — not a data dump.

This skill uses **public web search only**. It needs no logins and can run anytime. Membership counts and activity levels are best-effort estimates pulled from search results, so always mark how confident the data is rather than presenting guesses as fact.

## Inputs to confirm before searching

Get these from the conversation; ask only for what's genuinely missing:

1. **Genre / subgenre** — the more specific the better ("paranormal cozy mystery" beats "mystery"). If they give a broad genre, search the main subgenres under it too.
2. **Platforms** — Facebook groups, Goodreads groups, or both. Default to both if unspecified.
3. **Purpose** — reader engagement, author networking, or promo placement. This changes which groups matter (promo-friendly groups vs. discussion-only groups) and how you tag them.
4. **Pen name** (optional) — only relevant if they want the list framed for a specific identity.

Don't over-interrogate. If they said "find FB groups for my cozy mystery," that's enough to start.

## How to search

Run a batch of targeted web searches — aim for breadth, then dedupe. Vary the query phrasing because each pattern surfaces different results:

**Facebook patterns:**
- `[genre] readers Facebook group`
- `[genre] book lovers Facebook group`
- `[genre] authors Facebook group`
- `[genre] book promotion Facebook group` (for promo-friendly ones)
- `site:facebook.com/groups [genre]`
- subgenre and trope variants (e.g. `enemies to lovers romance Facebook group`)

**Goodreads patterns:**
- `[genre] Goodreads group`
- `site:goodreads.com/group [genre]`
- `best Goodreads groups for [genre] readers`
- `[genre] book club Goodreads`

Also look for listicles ("15 best Facebook groups for romance authors") — they're efficient ways to surface many candidates at once, but verify each link rather than trusting the article wholesale.

For any promising group, do a quick follow-up fetch/search to pull what you can: exact name, URL, approximate member count, public vs. private, and — critically — whether it allows author self-promotion and on what terms (many reader groups ban promo; many have "Promo Friday" rules). If you genuinely can't determine promo rules from public info, say "unknown — verify on join."

## Output

Collect results as a JSON array, then run the bundled script to build a formatted, sortable Excel workbook:

```bash
python scripts/build_group_sheet.py results.json "Genre Name" output.xlsx
```

Each result object should have these fields (use `null` or `"unknown"` when you can't determine a value — never invent numbers):

```json
{
  "platform": "Facebook",
  "name": "Cozy Mystery Readers",
  "url": "https://facebook.com/groups/...",
  "members": 12400,
  "privacy": "Public",
  "promo_allowed": "Yes - Promo Fridays only",
  "focus": "Readers",
  "activity": "High",
  "notes": "Very active, ~30 posts/day, admin enforces genre fit"
}
```

`focus` is one of Readers / Authors / Mixed. `activity` is High / Medium / Low / Unknown. The script sorts by platform then member count and color-codes promo-friendliness so the author can see at a glance where they can actually post.

After building the sheet, give the user a short written summary: how many groups found per platform, the 3–5 strongest promo targets, and any caveats about data confidence. Then present the .xlsx file.

## Quality bar

- **Real, current groups only.** A dead group with 50k members from 2016 is worthless. Prefer active communities and flag staleness when you spot it.
- **Be honest about uncertainty.** Estimated member counts and promo rules should be labeled as such. Authors will waste time if you present a guess as a verified fact.
- **Respect group rules in your framing.** When a group bans promo, tag it as engagement-only rather than implying they should spam it. Sustainable visibility comes from being a genuine member, and admins blacklist authors who break rules.
- **Dedupe aggressively.** Search patterns overlap; the same group will surface many times.

## Scope boundary

This finds discussion/reader/author communities via web search. It does NOT handle newsletter swaps, BookFunnel/Bookclicker group promos, or signed-in scraping of Facebook/Goodreads. If the user wants newsletter swaps, point them to the Book Promo Command Center. If they want live, logged-in verification of member counts and rules, offer the Chrome browser tools as a separate follow-up.
