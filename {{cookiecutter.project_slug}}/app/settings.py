from typing import Optional

{% if cookiecutter.use_edgedb == "yes" -%}
from pydantic import AnyUrl
{%- endif %}
from pydantic import BaseSettings


{% if cookiecutter.use_edgedb == "yes" -%}
class EdgedbDsn(AnyUrl):
    allowed_schemes = {
        'edgedb'
    }
    user_required = True
{%- endif %}


class Settings(BaseSettings):
    bot_token: str
    {%- if cookiecutter.use_edgedb == "yes" %}
    edgedb_dsn: Optional[EdgedbDsn] = None
    edgedb_tls_security: Optional[str] = None
    {% endif %}

    {%- if cookiecutter.use_i18n == "yes" %}
    i18n_path = "{{cookiecutter.i18n_dir}}"
    i18n_domain = "{{cookiecutter.i18n_domain}}"
    i18n_default_locale = "{{cookiecutter.i18n_default_locale}}"
    {%- endif %}


SETTINGS = Settings()
