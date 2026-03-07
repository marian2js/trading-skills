# Versioning And Releases

The repository should version changes conservatively because users may depend on:

- skill behavior
- example outputs
- install metadata

The current release anchor lives in the top-level [VERSION](../VERSION) file.

## Suggested release interpretation

### Patch-level changes

Use for:

- docs-only corrections
- validation or CI improvements
- error-message improvements that do not change outputs materially

### Minor changes

Use for:

- additive skill improvements
- new example docs
- non-breaking provider support additions
- richer output fields that do not remove or rename existing fields

### Major changes

Use for:

- renamed skill metadata fields
- removed output fields
- changes that alter public skill behavior in a way contributors or tooling must adapt to

## Change types to call out explicitly

- docs-only changes
- skill behavior changes
- provider support changes
- breaking changes

## Release documentation expectations

Before tagging a release:

- update `CHANGELOG.md`
- bump `VERSION` if the release intent changed
- make sure README examples still match the current repo
- verify `catalog.json` and generated README sections are current
- confirm example-mode outputs are clearly labeled as example data
