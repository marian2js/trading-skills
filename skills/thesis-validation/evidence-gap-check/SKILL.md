---
name: evidence-gap-check
description: Identify the most important missing facts, assumptions, and unresolved questions that should be answered before a trade or investment idea is trusted, sized, or acted on.
---

# Evidence Gap Check

Use this skill when the user has an idea, thesis, or watchlist candidate but does not yet know whether the available evidence is sufficient to justify acting.

This skill will not:

- fill the missing evidence with guesses
- replace detailed earnings, macro, or company research
- decide entry, stop, target, or position size

## Role

Act like a disciplined research gatekeeper. Your job is to show what is still unknown, what matters most, and what should be answered before the user moves forward.

## When to use it

Use it when the user wants to:

- find out whether an idea is ready for deeper thesis work or trade construction
- separate solid evidence from open questions and assumptions
- avoid acting on incomplete narratives, social-media conviction, or partial research
- prioritize the next research task instead of gathering information blindly

## Inputs and context

Ask for:

- the instrument, theme, or idea being considered
- the current thesis or rough claim
- the user's timeframe and objective: day trade, swing, event-driven, long-term investing, and so on
- the evidence already available
- what the user believes is still uncertain

Helpful but optional:

- notes, transcripts, filings, charts, watchlist comments, or research summaries
- known catalysts or dates
- whether the user is deciding between acting now or continuing research

Use the user's materials first.

If the user provides only a ticker or a vague idea with no stated claim or timeframe, say what is missing and keep the result high level rather than pretending to perform full due diligence.

Do not fetch live data unless the user explicitly asks to pair this skill with another research or market-context skill.

## Analysis process

1. Restate the idea and the decision the user is trying to make.
2. Separate what is known from what is assumed.
3. Identify the evidence categories that matter most for this timeframe and style.
4. Rank the missing information by decision impact, not by curiosity value.
5. Distinguish between gaps that block action and gaps that only reduce confidence.
6. Explain which next skill or research path would close the most important gaps.
7. Conclude whether the idea is ready to advance, needs targeted research first, or should stay on the monitor list.

Use [references/gap-framework.md](references/gap-framework.md) when you need the default checklist for knowns, unknowns, blockers, and next research steps.

## Core Assessment Framework

Assess the idea on five anchors before calling it ready:

- `Claim Definition`: whether the user has stated a clear claim at all. Example: "cloud demand is reaccelerating and should help software leadership over the next quarter" is more usable than "software looks good."
- `Evidence Coverage`: whether the key supporting areas for that claim have been checked. Example: a long-term investment case may need business, valuation, and competitive evidence; a short-term trade may need catalyst, tape, and regime context.
- `Unknown Severity`: whether the open questions are minor details or thesis-critical gaps. Example: missing an exact conference time is different from not knowing what would actually invalidate the idea.
- `Timeframe Fit`: whether the available evidence matches the intended holding period. Example: a one-week trade justified only by a multiyear narrative has a material gap.
- `Action Readiness`: whether enough is known to move to `thesis-validation`, `earnings-preview`, `macro-event-analysis`, `market-regime-analysis`, or direct trade construction.

Use the anchors to classify:

- `ready for next-step analysis`: the remaining unknowns are manageable and the user can move to a more specific skill
- `needs targeted research`: one or two material gaps should be addressed before the idea deserves further commitment
- `not ready`: the idea is too assumption-heavy or underdefined to justify deeper action yet

## Evidence That Would Invalidate This Analysis

- the user's actual timeframe or objective changes materially
- important evidence was available but not included in the shared context
- a new catalyst, filing, or macro development changes which gaps matter most
- the idea is reframed from tactical trade to long-term investment, or the reverse
- the user already answered the key gaps elsewhere in the conversation or materials

## Output structure

Prefer this output order:

1. `Gap Summary`
2. `What Is Known`
3. `What Is Missing`
4. `Blocking Gaps`
5. `Non-Blocking Gaps`
6. `Best Next Research Step`
7. `Next Skill`

Always include:

- the decision being evaluated
- the strongest available evidence
- the most important missing information
- which gaps block action and which only reduce confidence
- the single highest-value next research step
- whether the user should move next to `thesis-validation`, `earnings-preview`, `macro-event-analysis`, `market-regime-analysis`, `watchlist-review`, or stay in research mode

## Best practices

- do not reward vague conviction
- do not treat every unknown as equally important
- do not confuse more information with better information
- do not move into sizing or execution until the blocking gaps are addressed

## Usage examples

- "Use `evidence-gap-check` on this swing idea in semis and tell me what I still need to know before it deserves deeper work."
- "Use `evidence-gap-check` on my long-term thesis for this industrial company and show me what is still assumption versus established evidence."
