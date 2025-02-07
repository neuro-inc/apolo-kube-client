PYTEST_FLAGS=

.PHONY: all test clean
all test clean:

.PHONY: venv
venv:
	poetry lock;
	poetry install --with dev;
	poetry run pre-commit install;

.PHONY: poetry-plugins
poetry-plugins:
	poetry self add "poetry-dynamic-versioning[plugin]"; \
    poetry self add "poetry-plugin-export";

.PHONY: setup
setup: venv poetry-plugins

format:
ifdef CI_LINT_RUN
	poetry run pre-commit run --all-files --show-diff-on-failure
else
	poetry run pre-commit run --all-files
endif

.PHONY: lint
lint: format
	poetry run mypy apolo_kube_client tests


.PHONY: test_unit
test_unit:
	poetry run pytest -vv --cov-config=pyproject.toml --cov-report xml:.coverage-unit.xml tests/unit

.PHONY: test
test: test_unit
