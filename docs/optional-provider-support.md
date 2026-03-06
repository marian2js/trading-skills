# Optional Provider Support

This repo is a library of analysis-first skills.

External providers are optional support for cases where critical facts are missing. They are not the identity of the skill.

## Default behavior

Data-aware skills should follow this order:

1. Use the user's material first.
2. If critical data is missing, check whether the conversation already indicates a supported provider or already includes usable access details.
3. If yes, use that provider path directly.
4. If not, consult the skill's `references/data-providers.md` file and ask which supported provider they want to use.
5. Continue the analysis and disclose the source used.

## What counts as user material

Use these before reaching for any provider:

- pasted schedules
- uploaded reports or transcripts
- screenshots
- estimates already shared in text
- watchlists
- platform notes
- prior messages that already mention a provider or access method

## Supported provider references

Provider support is markdown-first.

Each data-aware skill should keep provider guidance small:

- `references/data-providers.md`
- `references/providers/<provider>.md`

These files should explain only enough to gather the missing facts and then return to the analysis.

## What not to assume

- do not assume auth lives in environment variables
- do not assume Python is the right way to gather the missing data
- do not assume provider usage is required
- do not silently switch to a provider path when the user already gave enough context
