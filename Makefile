PYTHON ?= python3

.PHONY: catalog validate test ci

catalog:
	$(PYTHON) scripts/build_catalog.py

validate:
	$(PYTHON) scripts/validate_repo.py

test: validate

ci: validate
	$(PYTHON) scripts/build_catalog.py --check
