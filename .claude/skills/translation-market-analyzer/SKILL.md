---
name: translation-market-analyzer
description: >
  Analyzes which foreign language markets to translate your books into first, based on genre, pen name, heat level, and current market data. Produces a professional spreadsheet with market rankings, genre viability by language, per-pen-name recommendations, and a prioritized action plan. Use this skill whenever an author wants to know which languages to translate into, which markets are most profitable for their genre, or needs a translation priority roadmap. Triggers on: 'which languages should I translate into', 'what markets should I target', 'translation priority', 'best language markets', 'market analysis for translation', 'where should I publish internationally', 'foreign market analysis', 'translation ROI', 'which language first', 'international publishing strategy', or any request about choosing translation target markets. Works with single books or full catalogs across multiple pen names.
---

# Translation Market Analyzer

Helps authors decide which language markets to invest in first by analyzing genre fit, market size, competition, and expected ROI per language.

## When to Use This Skill

Before spending time and resources translating a book, use this analyzer to determine:
1. Which of the 5 supported languages (German, Spanish, French, Italian, Brazilian Portuguese) offers the best return for YOUR specific genre and heat level
2. How to prioritize if translating multiple books or running multiple pen names
3. What the realistic revenue expectations are per market

## Input Required

Ask the user for:

1. **Book(s) to analyze**: Title, genre, subgenre, heat level (1-5), word count, current English sales rank or monthly revenue if available
2. **Pen name(s)**: If multiple, analyze each separately — different genres perform differently in different markets
3. **Current catalog size**: How many books are already published in English? Series or standalones?
4. **Budget context**: Are they translating one book to test, or planning to translate a full catalog?
5. **Existing translations**: Have they already translated into any language? Results?

## Analysis Framework

### Market Size Scoring (per language)

Score each language market 1-10 on these factors:

| Factor | What to Assess |
|--------|---------------|
| **Market size** | Total ebook readership in that language. Raw population × ebook adoption rate. |
| **Genre appetite** | How well does this specific genre/subgenre perform in this market? Romance is huge everywhere, but subgenres vary wildly. |
| **KDP penetration** | How dominant is Amazon/KDP in this market? High KDP penetration = easier distribution. |
| **Competition density** | How many translated romance titles already exist? Low competition = opportunity. Oversaturated = harder to rank. |
| **Price tolerance** | What do ebooks sell for in this market? Higher average price = better per-unit revenue. |
| **Heat level acceptance** | Does this market's readership match the book's heat level? Some markets are more conservative. |
| **Series potential** | If it's a series, does this market reward series reading? (Kindle Unlimited availability, read-through culture) |
| **Discoverability** | How easy is it to get found? Category competition, keyword search behavior, BookTok/social media in that language. |

### Genre-Language Matrix

Use this as a starting framework (adjust based on current market research):

| Genre/Subgenre | German | Spanish | French | Italian | BR Portuguese |
|---------------|--------|---------|--------|---------|--------------|
| Contemporary Romance | 9 | 8 | 8 | 7 | 9 |
| Small-Town Romance | 8 | 6 | 6 | 5 | 7 |
| Billionaire Romance | 7 | 9 | 8 | 8 | 9 |
| Dark Romance | 8 | 8 | 7 | 8 | 10 |
| Romantasy/Fantasy Romance | 8 | 7 | 9 | 7 | 8 |
| Paranormal/Vampire | 7 | 7 | 8 | 7 | 8 |
| Regency/Historical | 6 | 5 | 7 | 6 | 5 |
| Romantic Comedy | 7 | 7 | 7 | 6 | 8 |
| Mafia/MC Romance | 7 | 7 | 6 | 9 | 9 |
| Psychological Thriller | 9 | 7 | 8 | 7 | 7 |
| Horror/Gothic | 8 | 6 | 7 | 7 | 6 |
| Clean/Sweet Romance | 6 | 7 | 5 | 6 | 6 |
| Hockey/Sports Romance | 8 | 4 | 5 | 4 | 5 |
| Western Romance | 5 | 4 | 3 | 3 | 4 |
| Cowboy Romance | 5 | 4 | 3 | 3 | 4 |

**Important**: These scores are starting points. Use web search to verify current market conditions, as the romance translation market shifts quickly. Search for: "[genre] [language] kindle bestseller" and "[genre] romance [country] market 2025 2026" to get current data.

### Revenue Modeling

For each language, estimate monthly revenue using:

```
Estimated Monthly Revenue = (English monthly units × Market Multiplier × Price Factor) - Translation Cost Amortized

Where:
- Market Multiplier: typically 0.1-0.3 for first book (grows with catalog)
- Price Factor: target market price / English price
- Translation Cost Amortized: one-time cost spread over 12 months
```

**If the user doesn't have English sales data**, use genre benchmarks:
- New author, first book: 50-200 units/month English
- Established author, active marketing: 200-1000 units/month English
- Series with read-through: multiply by 0.5-0.7 for subsequent books

### KDP Market Specifics

| Market | KDP Store | Currency | Typical Ebook Price | KU Available | Notes |
|--------|-----------|----------|-------------------|--------------|-------|
| Germany | amazon.de | EUR | 2.99-4.99€ | Yes | Largest non-English ebook market in the world |
| Spain | amazon.es | EUR | 2.99-3.99€ | Yes | Growing market, good for romance |
| France | amazon.fr | EUR | 2.99-4.99€ | Yes | Strong literary culture, "New Romance" genre |
| Italy | amazon.it | EUR | 2.99-3.99€ | Yes | Growing romance market, strong dark romance |
| Brazil | amazon.com.br | BRL | R$4.99-12.99 | Yes | Massive population, price-sensitive, huge romance readership |

## Output: The Translation Priority Report

Generate an Excel spreadsheet (.xlsx) using the xlsx skill with these tabs:

### Tab 1: Executive Summary
- Top 3 recommended languages with brief rationale
- Estimated first-year ROI per language
- Recommended translation order
- Total investment estimate vs. projected revenue

### Tab 2: Market Scores
- Full scoring matrix (all factors × all languages)
- Weighted total score per language
- Visual ranking (conditional formatting: green/yellow/red)

### Tab 3: Per-Pen-Name Breakdown
- If multiple pen names: separate analysis for each
- Genre-specific scores
- Recommended first book to translate per pen name per language

### Tab 4: Revenue Projections
- Monthly revenue estimates per language (months 1-12)
- Break-even timeline per language
- Cumulative ROI chart data
- Best case / likely case / conservative case scenarios

### Tab 5: Action Plan
- Prioritized translation queue (which book, which language, in what order)
- Estimated timeline
- Budget allocation recommendation
- Key milestones

### Tab 6: Market Research Notes
- Sources consulted
- Current bestseller data points
- Category competition observations
- Any caveats or data limitations

## Process

1. Gather user input (books, pen names, genres, goals)
2. Research current market conditions via web search
3. Score each language across all factors
4. Model revenue projections
5. Generate the priority ranking
6. Build the spreadsheet
7. Present the top recommendation with reasoning

Always explain your reasoning. Don't just give scores — tell the author WHY German scored higher than Spanish for their specific book, or why Brazilian Portuguese is a sleeper opportunity for dark romance.

## Important Caveats to Include

- Market conditions change. This analysis is a snapshot, not a permanent truth.
- Translation quality matters enormously — a bad translation can damage a pen name's reputation in a market permanently.
- First book in a new language market is always the hardest. Returns improve with catalog depth.
- KU (Kindle Unlimited) page reads can be significant revenue in some markets — factor this in.
- Social media presence in the target language accelerates discoverability. Note if the author has any existing foreign-language following.
