# Aiogram 3.x Base Bot Generator


## Features
- Based on **[Aiogram 3.x](https://github.com/aiogram/aiogram/tree/dev-3.x)** - modern Telegram Bot API framework.

- **Docker** integration.

- **Docker Compose** for local development.

- **EdgeDB** with migrations.

- **Internationalization** via `Babel` and aiogram's built-in i18n middlewares.

## How to use it
### Install

```
pip install cookiecutter

cookiecutter https://github.com/gabbhack/skelet-bot
```
### Check input variables
<details>
  <summary>Input variables</summary>

  
- `python_major_version`: The Python major version. Default: `3`.

- `python_minor_version`: The Python minor version. Default: `10`.

- `project_name`: The name of the project.

- `project_slug`: The development friendly name of the project. By default, based on the project name.

- `author`: The author of the project.

- `author_email`: The email of author.

- `description`: The description of the project.

- `license`: The license of the project.

- `repository`: The repository of the project.

- `setup_json_logger`: Setup [python-json-logger](https://github.com/madzak/python-json-logger). Default: `yes`.

- `use_pytest`: Install pytest, create `tests` directory, add shortcuts to the `Makefile`. Default: `yes`.

- `use_orjson`: Install [orjson](https://github.com/ijl/orjson) and setup it in the bot client. Default: `yes`.

- `use_i18n`: Install `i18n` stuff and add shortcuts to the `Makefile`. Default: `yes`.

- `i18n_dir`: Setup `i18n` directory. Ignored if you do not use i18n. Default: `locales`.

- `i18n_domain`: Setup `i18n` domain. Ignored if you do not use i18n. Default: `messages`.

- `i18n_default_locale`: Setup `i18n` defaut locale. Ignored if you do not use i18n. Default: `en`.

- `use_edgedb`: Install [edgedb-python](https://github.com/edgedb/edgedb-python), add shortcuts to the `Makefile`, add `edgedb` service to the `docker-compose.yaml` and setup migrationn (if you use Docker). Default: `yes`.

- `use_docker`: Setup `Docker` and `docker-compose.yaml` files, add shortcuts to the `Makefile`. Default: `yes`.

- `use_pre_commit`: Setup [pre-commit](https://pre-commit.com/) framework with linters (See the linter installation below). Default: `yes`.

- `use_black`: Setup [black](https://github.com/psf/black) formatter. Default: `yes`.

- `use_isort`: Setup [isort](https://github.com/PyCQA/isort) formatter. Default: `yes`.

- `use_mypy`: Setup [mypy](https://github.com/python/mypy) linter. Default: `yes`.

- `use_flake8`: Setup [flake8](https://github.com/pycqa/flake8) linter. Default: `yes`.

- `use_wemake_python_styleguide`: Setup [wemake-python-styleguide](https://wemake-python-stylegui.de/en/latest/). Default: `yes`.
</details>

### First run
After generation, you need to install the dependencies. You can do this with the `make install` command.

This command will install dependencies from `pyproject.toml` file. If you use `edgedb` and/or `pre-commit`, this command will install those as well.

After that, it is recommended that you run the `make reformat` command to format the code.

If you are using `i18n`, read about it below before running the bot.

After installation, you must set the `BOT_TOKEN` environment variable and run bot via `make run` command.

### Run via `docker-compose`
1. Setup environment variables via `docker-compose.yaml`
1. Run `make docker-up-db` command if you use `edgedb`.
2. Run `make docker-up-app` command.

### Migrations
If you are using `Docker`, the migrations are performed before the bot starts. Read the [EdgeDB documentation](https://www.edgedb.com/docs/guides/migrations/index) on how to create a migration file.

### I18n
**First run**:
1. Run `make text-init` command to create directories and first language (`i18n_default_locale`)
1. Translate.
1. Run `make text-compile` command.

**Updating**:
1. Run `make text-update` command.
1. Translate.
1. Run `make text-compile` command.

**Add new language**:
1. Run `make text-create-language language=your_lang`.
1. Translate.
1. Run `make text-compile` command.

### How to deploy it
I don't know yet.

### More details
Run `make help` command to find out all the commands.
