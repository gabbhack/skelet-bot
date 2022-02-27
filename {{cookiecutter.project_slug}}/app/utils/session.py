from typing import Any, Dict

import orjson
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession


def orjson_dumps(something: Any) -> str:
    return orjson.dumps(something).decode("utf-8")


def setup(bot: Bot, dp: Dispatcher, workflow: Dict[str, Any]) -> None:
    bot.session = AiohttpSession(json_loads=orjson.loads, json_dumps=orjson_dumps)
