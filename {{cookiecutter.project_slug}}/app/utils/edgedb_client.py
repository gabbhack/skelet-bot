from typing import Any, Dict

from aiogram import Bot, Dispatcher
from edgedb.asyncio_client import AsyncIOClient, create_async_client

from app.settings import SETTINGS


async def close_client(edgedb_client: AsyncIOClient) -> None:
    await edgedb_client.aclose()  # type: ignore  # `aclose` is untyped


def setup(bot: Bot, dp: Dispatcher, workflow: Dict[str, Any]) -> None:
    edgedb_client = create_async_client(dsn=SETTINGS.edgedb_dsn, tls_security=SETTINGS.edgedb_tls_security)
    dp.shutdown.register(close_client)
    workflow["edgedb_client"] = edgedb_client
