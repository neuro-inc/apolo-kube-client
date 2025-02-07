PYTEST_FLAGS=

.PHONY: all test clean
all test clean:

.PHONY: venv
venv:
	poetry lock
	poetry install --with dev;

.PHONY: poetry-plugins
poetry-plugins:
	poetry self add "poetry-dynamic-versioning[plugin]"; \
    poetry self add "poetry-plugin-export";

.PHONY: build
build: venv poetry-plugins

.PHONY: setup
setup: venv
	poetry run pre-commit install;

.PHONY: lint
lint:
	poetry run pre-commit run --all-files
	poetry run mypy apolo_kube_client tests


.PHONY: test_unit
test_unit:
	poetry run pytest -vv --cov-config=pyproject.toml --cov-report xml:.coverage-unit.xml tests/unit

.PHONY: test
test: test_unit
