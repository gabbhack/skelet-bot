#!/usr/bin/env bash

set -e

{% if cookiecutter.use_edgedb == "yes" -%}
edgedb migrate --dsn="${EDGEDB_DSN}" --tls-security="${EDGEDB_TLS_SECURITY}"
{% endif -%}

{{cookiecutter.project_slug}}