include ./Makefile.in.mk


.PHONY: format
format:
	$(call log, reorganizing imports & formatting code)
	$(RUN) isort "$(DIR_SRC)"
	$(RUN) black "$(DIR_SRC)"
	$(call log, All good!)


.PHONY: run
run:
	$(call log, starting app)
	$(PYTHON) src/runner.py


.PHONY: test
test:
	$(call log, testing app)
	$(RUN) pytest


.PHONY: cov
cov:
	$(call log, test coverage)
	$(RUN) pytest --cov


.PHONY: venv
venv:
	$(call log, installing packages)
	$(VENV_INSTALL)


.PHONY: venv-dev
venv-dev:
	$(call log, installing development packages)
	$(VENV_INSTALL) --dev

