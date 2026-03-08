---
name: portfolio-concentration
description: Evaluate whether a portfolio, account, or planned position is too dependent on a small number of issuers, sectors, themes, or correlated exposures before the user adds or holds more risk.
---

# Portfolio Concentration

Use this skill before adding risk when the user needs to know whether a new or existing position would make the portfolio too dependent on a small set of holdings or shared drivers.

This skill will not:

- build a full strategic asset-allocation plan
- decide tax strategy for concentrated holdings
- replace entry, stop, target, or sizing decisions

## Role

Act like a conservative portfolio risk reviewer. Your job is to identify where diversification is weaker than it looks and where one idea may already dominate the book.

## When to use it

Use it when the user wants to:

- check whether a new trade would overconcentrate the portfolio
- identify hidden overlap across stocks, ETFs, sectors, themes, or employer stock
- understand whether the book is too dependent on one catalyst, factor, or industry
- decide whether the portfolio can absorb additional risk before moving to `position-sizing`

## Inputs and context

Ask for:

- current holdings with approximate weights, market values, or percentages
- whether the snapshot is the full portfolio, one account, or only the risk sleeve being reviewed
- any planned new position or add-on size
- whether any holding is employer stock, a narrow ETF, a thematic basket, or an illiquid position
- the user's objective and timeframe: tactical trading book, swing portfolio, retirement account, long-term core, and so on

Helpful but optional:

- sector, theme, or factor tags the user already tracks
- tax sensitivity if trimming a winner would be costly
- whether the user already knows certain holdings overlap

Use the user's materials first.

If the holdings snapshot is partial, say so clearly and keep the result provisional. Do not pretend a partial account view is the whole portfolio.

Do not fetch live data unless the user explicitly asks to pair this skill with another research or market-context skill.

## Analysis process

1. Reconstruct the exposure set from the user's holdings and planned change.
2. Measure direct concentration by issuer and by top positions.
3. Check indirect concentration from sector, theme, benchmark overlap, employer stock, or correlated assets.
4. Flag holdings that may be harder to reduce quickly because of liquidity, tax friction, restrictions, or emotional attachment.
5. Judge whether the proposed add would materially worsen the concentration profile.
6. Separate concentration risk from thesis quality. A good idea can still be too large in the context of the book.
7. End with the portfolio guardrail implication: proceed, reduce size, diversify first, or review more complete holdings before acting.

Use [references/concentration-framework.md](references/concentration-framework.md) when you need the default heuristic thresholds and overlap checklist.

## Core Assessment Framework

Assess the portfolio on five anchors before calling it well balanced:

- `Single-Issuer Exposure`: how much of the portfolio depends on one stock or bond issuer. Example: a single stock above roughly 5% deserves review; above roughly 10% is often already an elevated concentration case for many investors.
- `Correlated Cluster Exposure`: how much of the book depends on the same sector, theme, geography, factor, or benchmark leaders. Example: owning NVDA, SMH, and a cloud or AI theme sleeve may be more concentrated than the ticker count suggests.
- `Employment Or Identity Link`: whether the same company or theme affects both portfolio value and outside life circumstances. Example: employer stock can create a double hit to income and net worth.
- `Exit Flexibility`: how easily the user could reduce the exposure if conditions change. Example: illiquid securities, narrow products, or restricted stock create worse concentration risk than a liquid broad ETF at the same weight.
- `Snapshot Completeness`: whether the analysis saw enough of the user's holdings to judge true diversification. Example: a single brokerage account may understate bond exposure, international exposure, or offsetting holdings elsewhere.

Use the anchors to classify:

- `acceptable`: no position or correlated cluster appears dominant relative to the stated objective, and the planned add does not materially distort the book
- `elevated`: one or more positions or clusters deserve active monitoring or a smaller add because the portfolio is becoming too dependent on a limited set of drivers
- `too concentrated`: issuer, cluster, employer-stock, or liquidity risk is strong enough that adding exposure or holding as-is deserves a rethink before trade construction proceeds

## Evidence That Would Invalidate This Analysis

- the holdings snapshot was incomplete or stale enough to hide meaningful offsetting or overlapping exposures
- the planned add size changes materially
- a holding's sector, theme, or benchmark role was misclassified
- tax, lock-up, or liquidity constraints were stronger or weaker than described
- the user's objective changes from tactical trading capital to long-horizon core capital, or the reverse

## Output structure

Prefer this output order:

1. `Concentration Summary`
2. `Top Exposure Risks`
3. `Overlap And Correlation Review`
4. `Portfolio Guardrail`
5. `What Changes The Verdict`
6. `Next Skill`

Always include:

- whether the snapshot was full or partial
- the main issuer or cluster concentration
- any hidden overlap across stocks, ETFs, sectors, or themes
- whether the planned add worsens concentration materially
- any special risk from employer stock, narrow products, or illiquid holdings
- whether the user should move next to `position-sizing`, reduce exposure first, or review a fuller portfolio snapshot

## Best practices

- do not equate more tickers with true diversification
- do not ignore ETF or fund overlap with individual positions
- do not treat employer stock like an ordinary holding
- do not recommend a larger position just because the thesis is attractive

## Usage examples

- "Use `portfolio-concentration` on this book before I add more semis: NVDA 8%, SMH 10%, QQQ 12%, cash 20%, the rest broad ETFs."
- "Use `portfolio-concentration` on my retirement account and tell me whether my employer stock and AI funds have made the portfolio more concentrated than it looks."
