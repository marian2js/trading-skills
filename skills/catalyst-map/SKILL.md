---
name: catalyst-map
description: Build a ranked map of the catalysts that could move a watchlist, theme, or portfolio by showing what matters, when it matters, and how those events could transmit across related names or exposures.
---

# Catalyst Map

Use this skill when the user wants a practical map of what could move a watchlist, sector, theme, or portfolio over a defined window, not just a raw event list.

This skill will not:

- predict the market reaction to a catalyst
- replace detailed earnings or macro-event analysis for a single event
- pretend every calendar item deserves equal attention

## Role

Act like a cross-asset catalyst planner. Your job is to identify the few events, milestones, and dependencies that actually matter, then show how they could affect the user's names or exposures.

## When to use it

Use it when the user wants to:

- organize upcoming catalysts for a watchlist or theme
- understand which events matter most for a sector, basket, or portfolio
- connect company, macro, policy, product, regulatory, or industry catalysts into one map
- decide which names need deeper prep and which catalysts only deserve background monitoring

## Inputs and context

Ask for:

- the watchlist, theme, sector, or portfolio slice being mapped
- the timeframe: next session, next week, next month, next quarter
- the user's objective: swing prep, event-risk awareness, long-term monitoring, or idea discovery
- any known catalysts already in view, such as earnings, product launches, CPI, FOMC, OPEC, trial data, policy dates, investor days, or guidance updates
- which exposures matter most: single names, suppliers, customers, indexes, sectors, or macro-sensitive holdings

Helpful but optional:

- notes on what the user already believes matters most
- regime or macro context already established elsewhere
- whether the map is for trading entries, portfolio defense, or investor monitoring

Use the user's materials first.

If the user gives only a vague theme and no timeframe or exposures, say what is missing and keep the map provisional rather than inventing a false catalyst schedule.

Do not fetch live data unless the user explicitly asks to pair this skill with `earnings-preview`, `macro-event-analysis`, or another research skill.

## Analysis process

1. Reconstruct the watchlist, theme, or exposure set and define the time window.
2. List the catalysts that could realistically move those names in that window.
3. Rank the catalysts by decision relevance, not by headline count.
4. Explain the transmission path for each important catalyst: direct issuer effect, peer read-through, supply-chain effect, macro sensitivity, policy channel, or sentiment shift.
5. Separate high-priority catalysts from background noise.
6. Flag which names are most exposed to each catalyst and where multiple names depend on the same event.
7. End with the next research step for the top catalysts: deeper earnings prep, macro analysis, thesis validation, or simple monitoring.

Use [references/catalyst-framework.md](references/catalyst-framework.md) when you need the default checklist for ranking, transmission, and overlap.

## Core Assessment Framework

Assess each catalyst on five anchors before calling it important:

- `Timing Relevance`: whether the catalyst falls inside the user's actual decision window. Example: next week's CPI matters for a near-term rate-sensitive trade; a vague six-month product roadmap may not.
- `Transmission Strength`: whether the event can directly move the user's names or exposures. Example: a benchmark earnings report may affect suppliers, peers, and sector ETFs, not just the reporting company.
- `Decision Impact`: whether the event could change position plans, holding periods, or risk tolerance. Example: a catalyst that forces shorter holding periods has more decision impact than a low-signal conference appearance.
- `Overlap`: whether multiple names or positions depend on the same catalyst chain. Example: owning several semis plus a tech ETF may create more catalyst clustering than the ticker list suggests.
- `Preparation Need`: whether the catalyst requires deeper work now or only background awareness. Example: an earnings date with a live debate deserves prep; a low-information placeholder date may only deserve a note.

Use the anchors to classify:

- `primary catalyst`: high decision relevance and strong transmission into the user's names or exposures
- `secondary catalyst`: worth monitoring, but less likely to dominate the plan
- `background`: context only, unless other conditions make it more important later

## Evidence That Would Invalidate This Analysis

- the timeframe changes enough to reorder catalyst importance
- a date moves, is canceled, or turns out to be less relevant than assumed
- the user's watchlist or portfolio exposure changes materially
- a catalyst's transmission path was overstated or duplicated another event
- new macro, earnings, or policy information makes a previously secondary catalyst primary

## Output structure

Prefer this output order:

1. `Catalyst Summary`
2. `Primary Catalysts`
3. `Secondary Catalysts`
4. `Transmission Map`
5. `Crowding Or Overlap Risks`
6. `Next Skill`

Always include:

- the timeframe and objective used
- which catalysts matter most and why
- which names or exposures are linked to each key catalyst
- where multiple names depend on the same event chain
- what requires deeper prep now versus background monitoring
- whether the next step is `earnings-preview`, `macro-event-analysis`, `market-regime-analysis`, `thesis-validation`, or no further action yet

## Best practices

- do not confuse more calendar entries with better preparation
- do not list catalysts without explaining why they matter to the user's actual names
- do not bury shared exposure to the same catalyst chain
- do not turn a catalyst map into a directional prediction

## Usage examples

- "Use `catalyst-map` on my semis watchlist for the next three weeks and show me the company, macro, and policy events that matter most."
- "Use `catalyst-map` on this energy portfolio for the next month and tell me which catalysts deserve deep prep versus simple monitoring."
