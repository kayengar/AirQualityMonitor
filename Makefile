source_dir=aqi_monitor

.PHONY: all
all: init test set-env-vars get-aqi

.PHONY: init
init:
	poetry install
	poetry env info

.PHONY: test
test: lint unittest

.PHONY: set-env-vars
set-env-vars:
    include .env
    export

.PHONY: get-aqi
get-aqi:
	poetry run ${source_dir}/app.py

.PHONY: lint
lint: black-check pylint

.PHONY: black
black:
	poetry run black .

.PHONY: black-check
black-check:
	poetry run black --check .

.PHONY: pylint
pylint:
	poetry run pylint ${source_dir} tests

.PHONY: mypy
mypy:
	poetry run mypy ${source_dir}

.PHONY: vulture
vulture:
	poetry run vulture --min-confidence 70 ${source_dir}/ tests/

.PHONY: unittest
unittest:
	poetry run pytest tests/unit

.PHONY: clean
clean:
	rm -f .coverage
	rm -f coverage.xml
	rm -f report.xml
	rm -f requirements.txt
	rm -rf .eggs
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf build
	rm -rf dist
