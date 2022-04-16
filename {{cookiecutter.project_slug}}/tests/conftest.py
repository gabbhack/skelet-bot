{%- if cookiecutter.use_edgedb == "yes" %}
import pytest
from edgedb import create_async_client


@pytest.fixture
async def edgedb_client():
    client = create_async_client(database="tests")
    try:
        yield client
    finally:
        await storage_.aclose()
{%- endif %}
