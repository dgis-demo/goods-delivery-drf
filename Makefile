#!make
.DEFAULT_GOAL := cq

# Makefile target args
args = $(filter-out $@,$(MAKECMDGOALS))

# Command shortcuts
mypy = mypy apps Project
flake = flake8 ./apps ./tests ./Project
isort = isort apps tests Project
pytest = ENV=testing pytest

test:
	$(pytest) --no-cov -s ${args}

test-verbose:
	$(pytest) --no-cov -svvl ${args}

test-cov:
	$(pytest) -vv ${args}

test-watch:
	$(pytest) --no-cov -f -svv --ff ${args}

.PHONY: format
format:
	$(isort)

.PHONY: lint
lint:
	$(flake)
	$(isort) --check-only

.PHONY: clean
clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -rf dist *.egg-info
	rm -rf .cache
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf htmlcov
	rm -f .coverage
	rm -f .coverage.*
	rm -rf artefacts/{htmlcov,test_report.xml}
