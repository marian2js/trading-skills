---
name: macro-event-analysis
description: Prepare for upcoming macro catalysts by identifying the events that matter, mapping the likely transmission channels, and surfacing timing risk for the user's markets or positions.
---

# Macro Event Analysis

Use this skill when the user needs a practical read on upcoming macro event risk before holding positions, increasing size, or planning entries around catalysts.

This skill will not:

- predict the exact price reaction to a release
- treat every calendar entry as decision-relevant
- substitute macro theater for position-specific planning

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

Use the user's materials first: pasted event lists, screenshots, platform notes, transcripts, watchlists, or provider details already mentioned in the conversation.

## If critical data is missing

If the user already gave enough event information to analyze, do not fetch anything.

If the timing or event slate is still incomplete:

- check whether the conversation already points to a supported provider or includes usable access details
- if the user already indicated `FMP` or `TradingEconomics`, use [references/providers/fmp.md](references/providers/fmp.md) or [references/providers/tradingeconomics.md](references/providers/tradingeconomics.md) directly
- otherwise consult [references/data-providers.md](references/data-providers.md) and ask which supported provider they want to use
- once the missing event details are gathered, continue the analysis and disclose the source used

## Analysis process

1. Build the relevant event slate for the requested window.
2. Rank the events by likely decision impact, not by calendar length.
3. Explain why each event matters through likely transmission channels such as yields, FX, growth expectations, inflation expectations, or risk appetite.
4. Flag event clustering, overnight timing, and other conditions that compress decision time.
5. Separate high-visibility events from lower-signal filler.
6. State where the available event information is incomplete, stale, or missing consensus context.
7. Translate the event slate into practical preparation questions: what should the user avoid assuming, monitor closely, or plan around?

Use [references/interpretation-guide.md](references/interpretation-guide.md) when you need a reminder to emphasize event risk over prediction.

## Core Assessment Framework

Rank each event against four anchors before calling it important:

- `Market Sensitivity`: does the user's market historically react to this release or central-bank signal. Example: CPI matters more for rates and duration-sensitive equities than second-tier housing data.
- `Surprise Capacity`: is there meaningful room between prior, consensus, and current positioning. Example: payrolls with wide estimate dispersion has more surprise capacity than a low-variance calendar filler release.
- `Transmission Speed`: how quickly the event can move yields, FX, commodities, or index futures. Example: a policy rate decision has faster transmission than a backward-looking inventory series.
- `Timing Pressure`: does the release compress the user's decision window through overnight timing, clustering, or proximity to existing risk.

Use the anchors to sort events into:

- `primary`: directly relevant, high transmission, and able to change decision quality now
- `secondary`: worth monitoring, but less likely to dominate positioning
- `background`: context only unless the user's book is unusually sensitive

## Evidence That Would Invalidate This Analysis

- the event timing changes materially or the release is revised, delayed, or cancelled
- the consensus or prior values that anchored the importance ranking turn out to be stale or missing
- another event overtakes the stated catalyst by moving yields, FX, or risk appetite more decisively
- the user's actual exposure changes, making the current transmission map less relevant
- market pricing has already absorbed the catalyst so completely that the expected sensitivity is no longer plausible

## Output structure

Prefer this output order:

1. `Event Slate`
2. `Core Assessment Framework`
3. `Transmission Channels`
4. `Preparation Brief`
5. `Evidence That Would Invalidate This Analysis`
6. `Source And Caveats`

Always return:

- a prioritized event slate for the requested window
- why each event matters for the user's market or exposure
- the main transmission channels to watch
- timing notes, including clustered or overnight risk
- a short preparation brief: what to monitor, what to avoid assuming, and where caution is warranted
- explicit source, freshness, and caveats when provider-based data is used

## Best practices

- do not claim that a release guarantees direction
- do not bury missing consensus or stale timestamps
- distinguish event importance from certainty
- keep the output tied to the user's actual markets and holding period

## Usage examples

- "Use `macro-event-analysis` for the next 48 hours. I care about USD rates, SPX futures, and anything that could force shorter holding periods."
- "Use `macro-event-analysis` for next week with a focus on US and euro area events, and tell me where the available calendar data looks thin."
