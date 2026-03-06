# Versioning And Releases

The repository should version changes conservatively because users may depend on:

- skill behavior
- canonical schemas
- example outputs
- install metadata

## Suggested release interpretation

### Patch-level changes

Use for:

- docs-only corrections
- fixture improvements that do not change behavior contracts
- validation or CI improvements
- error-message improvements that do not change outputs materially

### Minor changes

Use for:

- additive skill improvements
- new example fixtures
- non-breaking adapter additions
- richer output fields that do not remove or rename existing fields

### Major changes

Use for:

- breaking schema changes
- renamed skill metadata fields
- removed output fields
- changes that alter public skill behavior in a way contributors or tooling must adapt to

## Change types to call out explicitly

- docs-only changes
- skill behavior changes
- schema changes
- adapter changes
- breaking changes

## Release documentation expectations

Before tagging a release:

- update `CHANGELOG.md`
- make sure README examples still match the current repo
- verify `catalog.json` and generated README sections are current
- confirm example-mode outputs are clearly labeled as example data
