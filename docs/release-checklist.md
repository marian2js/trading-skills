# Release Checklist

- [ ] `make catalog` has been run if metadata changed
- [ ] `VERSION` reflects the intended release
- [ ] `make test` passes locally
- [ ] CI is green on the release branch or main
- [ ] `README.md` is current
- [ ] example walkthrough docs were checked against current behavior
- [ ] `CHANGELOG.md` was updated
- [ ] no accidental fixture drift remains
- [ ] no committed cache, virtualenv, or editor artifacts remain
- [ ] live/example labeling is still explicit in data-backed output
- [ ] schema changes were reviewed for compatibility impact
