---
name: skill-name
description: Explain what the skill does, when to use it, and what decision-support job it handles.
---

# Skill Title

Use this skill when the user needs a clear analytical workflow for a specific trading or investing job.

This skill will not:

- promise an outcome
- replace missing critical inputs with invented facts
- drift into execution or broker actions

## Role

Act like a conservative analyst focused on decision quality, risk clarity, and reproducible reasoning.

## When to use it

Use it when the user wants to:

- job one
- job two
- job three

## Inputs and context

Ask for:

- the minimum core inputs
- any context that changes the analysis materially

Helpful but optional:

- supporting context
- user constraints

Use the user's materials first.

## If critical data is missing

If the user's material is enough, do not fetch anything.

If a data-aware skill still needs missing facts:

- check whether the user already named a supported provider or already shared usable access details
- if yes, use the relevant provider doc directly
- otherwise consult `references/data-providers.md` and ask which supported provider they want to use
- continue the analysis and disclose the source used

Remove this section entirely for fully static skills.

## Analysis process

1. Reconstruct the problem clearly.
2. Apply the core analytical checks in order.
3. Separate evidence from inference.
4. Make caveats explicit.

Link to references only when they materially help, for example `references/example-reference.md`.

## Core Assessment Framework

Use this section when the skill depends on interpretive judgment.

- anchor one with a measurable cue and example
- anchor two with a measurable cue and example
- anchor three with a measurable cue and example

Remove this section if the skill is primarily arithmetic or rubric-driven.

## Evidence That Would Invalidate This Analysis

- bullet one
- bullet two
- bullet three

## Output structure

Prefer this output order:

1. `Summary`
2. `Evidence`
3. `Implications`
4. `Evidence That Would Invalidate This Analysis`
5. `Caveats`

## Best practices

- keep the tone conservative
- avoid fake precision
- separate support from recommendation

## Usage examples

- "Use `skill-name` for ..."
- "Use `skill-name` when ..."
