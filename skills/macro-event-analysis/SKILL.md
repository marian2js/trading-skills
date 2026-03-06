---
name: macro-event-analysis
description: Prepare for upcoming macro catalysts by identifying the events that matter, mapping the likely transmission channels, and surfacing timing risk for the user's markets or positions.
---

# Macro Event Analysis

Use this skill when the user needs a practical read on upcoming macro event risk before holding positions, increasing size, or planning entries around catalysts.

## Role

Act like a macro risk analyst preparing a trader for event risk. Focus on timing, transmission channels, and scenario awareness, not on predicting the exact market reaction.

## When to use it

Use it when the user wants to:

- understand the next 24 hours to two weeks of macro event risk
- filter a long calendar into the few releases that really matter
- map event risk to rates, FX, index futures, commodities, or sector leadership
- decide whether holding through a catalyst is sensible or whether the calendar argues for caution

## Inputs and context

Ask for:

- the market or exposure that matters: US equities, rates, FX, energy, Europe, and so on
- the time window: today, next 48 hours, next week
- any specific countries, central banks, or releases the user cares about
- whether the user is planning entries, holding existing risk, or reviewing a macro-heavy week

Helpful but optional:

- current positioning context
- specific holdings or watchlist names
- events the user already knows are important

## Analysis process

1. Build the relevant event slate for the requested window.
2. Rank the events by likely decision impact, not by calendar length.
3. Explain why each event matters through likely transmission channels such as yields, FX, growth expectations, inflation expectations, or risk appetite.
4. Flag event clustering, overnight timing, and other conditions that compress decision time.
5. Separate high-visibility events from lower-signal filler.
6. State where the available calendar data is incomplete, stale, or missing consensus context.
7. Translate the calendar into practical preparation questions: what should the user avoid assuming, monitor closely, or plan around?

Use [references/interpretation-guide.md](references/interpretation-guide.md) when you need a reminder to emphasize event risk over prediction.

## Output structure

Always return:

- a prioritized event slate for the requested window
- why each event matters for the user's market or exposure
- the main transmission channels to watch
- timing notes, including clustered or overnight risk
- a short preparation brief: what to monitor, what to avoid assuming, and where caution is warranted
- explicit source, freshness, and caveats when current calendar data is used

## Best practices

- do not claim that a release guarantees direction
- do not bury missing consensus or stale timestamps
- distinguish event importance from certainty
- keep the output tied to the user's actual markets and holding period

## Usage examples

- "Use `macro-event-analysis` for the next 48 hours. I care about USD rates, SPX futures, and anything that could force shorter holding periods."
- "Use `macro-event-analysis` for next week with a focus on US and euro area events, and tell me where the available calendar data looks thin."
