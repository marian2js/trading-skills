PYTHON ?= python3
SKILL_DOCTOR_VERSION ?= 0.1.0

.PHONY: catalog validate doctor test ci

catalog:
	$(PYTHON) scripts/build_catalog.py

validate:
	$(PYTHON) scripts/validate_repo.py

doctor:
	npx -y skill-doctor@$(SKILL_DOCTOR_VERSION) . --verbose --fail-on error

test: validate

ci: validate doctor
	$(PYTHON) scripts/build_catalog.py --check
