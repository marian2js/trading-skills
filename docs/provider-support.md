# Provider Support

Provider support in this repo is markdown-first and optional.

The goal is not to hide a mini SDK behind each skill. The goal is to let a skill fill in critical missing facts when the user did not already provide enough information.

## Skill-level pattern

For data-aware skills:

1. Start with the user's material.
2. Only if critical information is missing, consult `references/data-providers.md`.
3. If the conversation already points to a supported provider, use that provider path directly.
4. Otherwise ask the user which supported provider they want to use.
5. Gather the missing facts, then return to the analysis.

## What provider docs should contain

Keep provider docs short and practical:

- what the provider is useful for
- which missing facts it can supply
- how to use it only when needed
- the reminder to disclose the source used

Avoid turning provider docs into large operational manuals.

## What provider docs should not become

- a Python integration layer
- hidden repo plumbing that the skill never mentions
- a replacement for user-provided data
- a provider-branded public skill
