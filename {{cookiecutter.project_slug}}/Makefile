PROJECT := {{cookiecutter.project_slug}}
{%- if cookiecutter.use_i18n == "yes" %}
LOCALES_DIR := {{cookiecutter.i18n_dir}}
LOCALES_DOMAIN := {{cookiecutter.i18n_domain}}
LOCALES_DEFAULT := {{cookiecutter.i18n_default_locale}}
{%- endif %}
VERSION := 0.1.0
{%- if cookiecutter.author != "None" and cookiecutter.author_email != "None" %}
COPYRIGHT := "{{cookiecutter.author}} <{{cookiecutter.author_email}}>"
{%- endif %}

CODE_DIR := app
REPORTS_DIR := reports

py := poetry run

.PHONY: help
help:
	@echo "======================================================================================="
	@echo "                    {{cookiecutter.project_slug}} tools                                  "
	@echo "======================================================================================="
	@echo "Environment:"
	@echo "    help: Show this message"
	@echo "    install: Install development dependencies"
	@echo ""
	@echo "Code quality:"
	@echo "    lint: Lint code by isort, black, flake8 and mypy tools"
	@echo "    reformat: Reformat code by isort and black tools"
	{%- if cookiecutter.use_pytest == "yes" %}
	@echo ""
	@echo "Tests:"
	@echo "    test: Run tests"
	@echo "    test-coverage: Run tests with HTML reporting (results + coverage)"
	@echo "    test-coverage-report: Open coverage report in default system web browser"
	@echo ""
	{%- endif %}
	@echo "Development"
	@echo "    run: Run bot"
	{%- if cookiecutter.use_docker == "yes" %}
	@echo ""
	@echo "Docker"
	@echo "    docker-ps: Run docker-compose ps"
	@echo "    docker-build: Run docker-compose build"
	{% if cookiecutter.use_edgedb == "yes" -%}
	@echo "    docker-up-db: Run docker-compose up -d edgedb"
	@echo "    docker-stop-db: docker-compose stop edgedb"
	{%- endif %}
	@echo "    docker-up-app: Run docker-compose up --remove-orphans {{cookiecutter.project_slug}}"
	@echo "    docker-up-app-daemon: Run docker-compose up -d --remove-orphans {{cookiecutter.project_slug}}"
	@echo "    docker-stop-app: Run docker-compose stop {{cookiecutter.project_slug}}"
	@echo "    docker-down: Run docker-compose down"
	@echo "    docker-destroy: Run docker-compose down -v --remove-orphans"
	{%- endif %}
	{%- if cookiecutter.use_i18n == "yes" %}
	@echo ""
	@echo "Internationalization"
	@echo "    text-init: Init babel with default language"
	@echo "    text-update: Extract and update an existing new translations"
	@echo "    text-compile: Compile translation catalogs into binary MO files"
	@echo "    text-extract: Extract localizable messages from a collection of source files"
	@echo "    text-create-language: Init babel with new language"
	@echo ""
	{%- endif %}

# =================================================================================================
# Environment
# =================================================================================================
.PHONY: install
install:
	git init .
	{%- if cookiecutter.use_edgedb == "yes" %}
	curl --proto '=https' -sSf1 https://sh.edgedb.com | sh -s -- -y
	{%- endif %}
	poetry install
	{%- if cookiecutter.use_pre_commit == "yes" %}
	$(py) pre-commit install
	{% endif %}

# =================================================================================================
# Code quality
# =================================================================================================
.PHONY: lint
lint:
	{%- if cookiecutter.use_isort == "yes" %}
	$(py) isort --check-only $(CODE_DIR)
	{%- endif %}

	{%- if cookiecutter.use_black == "yes" %}
	$(py) black --check --diff $(CODE_DIR)
	{%- endif %}

	{%- if cookiecutter.use_flake8 == "yes" %}
	$(py) flake8 $(CODE_DIR)
	{%- endif %}

	{%- if cookiecutter.use_mypy == "yes" %}
	$(py) mypy $(CODE_DIR)
	{% endif %}

.PHONY: reformat
reformat:
	{%- if cookiecutter.use_black == "yes" %}
	$(py) black $(CODE_DIR)
	{%- endif %}

	{%- if cookiecutter.use_isort == "yes" %}
	$(py) isort $(CODE_DIR)
	{% endif %}

{% if cookiecutter.use_pytest == "yes" -%}
# =================================================================================================
# Tests
# =================================================================================================
.PHONY: test
test:
	$(py) pytest --cov=${PROJECT} --cov-config .coveragerc tests/

.PHONY: test-coverage
test-coverage:
	mkdir -p ${REPORTS_DIR}/tests/
	$(py) pytest --cov=${PROJECT} --cov-config .coveragerc --html=${REPORTS_DIR}/tests/index.html tests/

.PHONY: test-coverage-report
test-coverage-report:
	$(py) coverage html -d ${REPORTS_DIR}/coverage
{%- endif %}

# =================================================================================================
# Development
# =================================================================================================
.PHONY: run
run:
	$(py) python -m app

{% if cookiecutter.use_docker == "yes" -%}
# =================================================================================================
# Docker
# =================================================================================================

.PHONY: docker-ps
docker-ps:
	docker-compose ps

.PHONY: docker-build
docker-build:
	docker-compose build

{% if cookiecutter.use_edgedb == "yes" -%}
.PHONY: docker-up-db
docker-up-db:
	docker-compose up -d edgedb

.PHONY: docker-stop-db
docker-stop-db:
	docker-compose stop edgedb
{% endif -%}

PHONY: docker-up-app
docker-up-app:
	docker-compose up --remove-orphans {{cookiecutter.project_slug}}

PHONY: docker-up-app-daemon
docker-up-app-daemon:
	docker-compose up -d --remove-orphans {{cookiecutter.project_slug}}

PHONY: docker-stop-app
docker-stop-app:
	docker-compose stop {{cookiecutter.project_slug}}

PHONY: docker-down
docker-down:
	docker-compose down

PHONY: docker-destroy
docker-destroy:
	docker-compose down -v --remove-orphans
{% endif -%}

{% if cookiecutter.use_i18n == "yes" -%}
# =================================================================================================
# Internationalization
# =================================================================================================
.PHONY: text-extract
text-extract:
	$(py) pybabel extract . -o ${LOCALES_DIR}/${LOCALES_DOMAIN}.pot --project=${PROJECT} --version=${VERSION} --copyright-holder=${COPYRIGHT}

.PHONY: text-create-language
text-create-language:
	$(py) pybabel init -i ${LOCALES_DIR}/${LOCALES_DOMAIN}.pot -d ${LOCALES_DIR} -D ${LOCALES_DOMAIN} -l ${language}

.PHONY: text-init
text-init:
	mkdir ${LOCALES_DIR}
	$(MAKE) text-extract
	$(MAKE) text-create-language language=${LOCALES_DEFAULT}

.PHONY: text-update
text-update:
	$(MAKE) text-extract
	$(py) pybabel update \
		-d ${LOCALES_DIR} \
		-D ${LOCALES_DOMAIN} \
		--update-header-comment \
		-i ${LOCALES_DIR}/${LOCALES_DOMAIN}.pot

.PHONY: text-compile
text-compile:
	$(py) pybabel compile -d ${LOCALES_DIR} -D ${LOCALES_DOMAIN}
{% endif %}

# Inspired by:
# https://github.com/aiogram/aiogram/blob/1b8e22d90fab54a0360efabb750efa84ec3b2e66/Makefile
# https://github.com/aiogram/bot/blob/092f34757233d79bf54b45091540743891c86c9f/Makefile