# Skill Design Principles

## What a great trading skill does

A great trading skill improves process quality. It helps the user:

- frame risk clearly
- inspect assumptions
- plan execution deliberately
- review mistakes honestly
- identify when information quality is weak

The point is decision support, not mystical prediction.

It should also make clear what it will not do. Strong boundaries are part of trust.

## Product standards

Each skill should be:

- practical
- conservative
- auditable
- explicit about uncertainty
- useful to both technical and non-technical users

If the workflow depends on external data, the skill should still make the limits of that data visible.

## What to avoid

Do not write skills that:

- claim hidden edge without evidence
- imply guaranteed returns
- present black-box outputs as fact
- assign theatrical confidence scores with no defensible basis
- confuse precision with accuracy

This repo should feel more like a disciplined operator's toolkit than a signal marketplace.

## Tone guidelines

Prefer language like:

- "base case"
- "risk factor"
- "coverage limitation"
- "requires confirmation"
- "likely undercounts"
- "do not treat this as a prediction"

Avoid language like:

- "high-probability winner"
- "guaranteed setup"
- "alpha engine"
- "institutional-grade signal"

## Output design

Strong outputs usually include:

- the input assumptions used
- the reasoning steps or framework
- the main risks and caveats
- the parts that remain unknown
- a clear separation between observation and judgment
- a clear statement of what the skill is not claiming

For data-backed skills, always include:

- source or provider
- freshness or last update
- missing-field notes
- coverage caveats

## Examples should feel real

Usage examples should reflect plausible workflows:

- sizing an equity swing trade
- checking an event-heavy macro session
- reviewing a stop-out with slippage
- assessing whether a target is reasonable relative to the stop

Avoid toy examples that make the skill look easier or smarter than it really is.
