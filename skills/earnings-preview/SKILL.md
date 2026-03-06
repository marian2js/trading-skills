---
name: earnings-preview
description: Prepare for an upcoming earnings report or earnings week by identifying the reports that matter, framing the key debates, and surfacing the read-through risk that could affect the user's watchlist or positions.
---

# Earnings Preview

Use this skill when the user needs to prepare before one company reports or before an earnings-heavy week.

## Role

Act like a skeptical earnings prep analyst. Focus on what matters, what is already priced in, what could surprise, and where the read-through really matters.

## When to use it

Use it when the user wants to:

- prioritize which upcoming reports actually deserve attention
- prepare for a single company report with peer and sector context
- identify likely read-through names around a benchmark report
- decide whether a report is worth holding through, fading, or avoiding

## Inputs and context

Ask for:

- the company, peer group, sector, or watchlist
- the date window or specific report being discussed
- the user's thesis, exposure, or planned trade posture
- what matters most this quarter: growth, margins, guidance, backlog, capex, demand, pricing, AI spend, consumer health, and so on
- whether the user cares more about the report itself, sector read-through, or index impact

Helpful but optional:

- consensus expectations or prior-quarter context
- known positioning or sentiment concerns
- whether the user plans to hold through the event

Use the user's materials first: pasted schedules, watchlists, company notes, guidance excerpts, estimate tables, transcripts, screenshots, or provider details already mentioned in the conversation.

## If critical data is missing

If you already have enough timing and context to do the analysis, do not fetch anything.

If key schedule or estimate context is missing:

- check whether the user already named a supported provider or already shared usable access details in the conversation
- if they already indicated `FMP` or `TradingEconomics`, use [references/providers/fmp.md](references/providers/fmp.md) or [references/providers/tradingeconomics.md](references/providers/tradingeconomics.md) directly
- otherwise consult [references/data-providers.md](references/data-providers.md) and ask which supported provider they want to use
- once the missing facts are gathered, continue the preview and disclose the source used

## Analysis process

1. Identify the reports that matter most for the user's names or theme.
2. Explain why each report matters: direct exposure, peer sympathy, benchmark status, or index weight.
3. Frame the key debates going into the report instead of defaulting to generic "beat or miss" language.
4. Separate pre-report setup risk from business-quality judgment.
5. Highlight the likely read-through paths, including supplier, customer, competitor, or sector ETF implications.
6. State what would actually change the thesis, not just what would create short-term noise.
7. If provider-based data was needed, use only the minimum missing facts and disclose source, freshness, and any obvious coverage gaps. Otherwise stay fully grounded in the user's material.

Use [references/relevance-ranking.md](references/relevance-ranking.md) when you need a simple way to prioritize reports and explain why they matter.

## Output structure

Always return:

- a prioritized report list or single-name preview
- why each report matters in plain language
- the key debates or watch items going into the print
- the likely read-through map for peers, suppliers, customers, or sector leadership
- the main pre-report risk to the user's plan
- explicit caveats around missing dates, incomplete estimates, stale data, or example-mode data when relevant

## Best practices

- do not turn "important report" into "predictable trade"
- do not confuse sector importance with a guaranteed stock move
- distinguish between what matters for fundamentals and what matters for positioning
- if timing, estimates, or coverage are incomplete, say that early rather than burying it

## Usage examples

- "Use `earnings-preview` for NVDA next week. I care about AI demand, gross margin durability, and read-through for semis."
- "Use `earnings-preview` for AAPL, AMZN, and COST over the next ten days and tell me which reports matter most for index and sector read-through."
