PYTHON ?= python3
VENV_DIR ?= .venv
VENV_PYTHON := $(VENV_DIR)/bin/python
VENV_READY := $(VENV_DIR)/.deps-installed

.PHONY: catalog validate test

catalog:
	$(PYTHON) scripts/build_catalog.py

validate:
	$(PYTHON) scripts/validate_repo.py

$(VENV_READY): requirements-dev.txt
	$(PYTHON) -m venv $(VENV_DIR)
	$(VENV_PYTHON) -m pip install -r requirements-dev.txt
	touch $(VENV_READY)

test: validate $(VENV_READY)
	$(VENV_PYTHON) -m pytest
