import logging
import sys

{% if cookiecutter.setup_json_logger == "yes" -%}
from pythonjsonlogger.jsonlogger import JsonFormatter
{%- endif %}


def get() -> logging.Logger:
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    log_handler = logging.StreamHandler(stream=sys.stdout)
    {% if cookiecutter.setup_json_logger == "yes" -%}
    formatter = JsonFormatter(
        "%(levelname)s %(name)s %(lineno)s %(asctime)s %(message)s"  # noqa: WPS323
    )
    log_handler.setFormatter(formatter)
    {%- endif %}

    logger.addHandler(log_handler)
    return logger
