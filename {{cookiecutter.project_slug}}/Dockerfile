FROM python:3.10-slim-buster as build
ENV DEBIAN_FRONTEND=noninteractive \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100
WORKDIR /usr/src/app
RUN pip install -U pip poetry==1.1.13 && \
    poetry config virtualenvs.create false

COPY . /usr/src/app
RUN poetry build --no-interaction --no-ansi --format wheel

{% if cookiecutter.use_edgedb == "yes" -%}
FROM edgedb/edgedb-cli as edgedb-cli
{% endif -%}

FROM python:3.10-slim-buster as prod
ENV DEBIAN_FRONTEND=noninteractive \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  PATH="/usr/src/app/scripts:${PATH}"

WORKDIR /usr/src/app

RUN mkdir -p /opt/app
COPY --from=build /usr/src/app/dist/{{cookiecutter.project_slug}}-*.whl /opt/app

RUN pip install /opt/app/{{cookiecutter.project_slug}}-*.whl && \
    rm /opt/app/{{cookiecutter.project_slug}}-*.whl

COPY scripts /usr/src/app/scripts/
RUN chmod +x /usr/src/app/scripts/*

{% if cookiecutter.use_i18n == "yes" -%}
COPY locales /usr/src/app/locales/
{% endif -%}

{% if cookiecutter.use_edgedb == "yes" -%}
COPY --from=edgedb-cli /usr/bin/edgedb /usr/bin/
COPY dbschema /usr/src/app/dbschema/
COPY edgedb.toml /usr/src/app/
{% endif -%}

ENTRYPOINT [ "start.sh" ]