import asyncio
from typing import Any, Dict

from aiogram import Bot, Dispatcher

from app.routers import master
from app.settings import SETTINGS
from app.utils import (
    commands,
    {%- if cookiecutter.use_edgedb == "yes" %}
    edgedb_client,
    {% endif %}
    {%- if cookiecutter.use_i18n == "yes" %}
    i18n,
    {% endif %}
    logger,
    session
)


async def main() -> None:
    bot = Bot(token=SETTINGS.bot_token, parse_mode="HTML")
    dp = Dispatcher()

    workflow: Dict[str, Any] = {}

    for util in (
        session,
        {%- if cookiecutter.use_i18n == "yes" %}
        i18n,
        {% endif %}
        {%- if cookiecutter.use_edgedb == "yes" %}
        edgedb_client,
        {% endif %}
        commands
    ):
        util.setup(bot, dp, workflow)

    # Setup routers
    dp.include_router(master.router)

    await dp.start_polling(
        bot, allowed_updates=dp.resolve_used_update_types(), **workflow
    )

log = logger.get()


try:
    asyncio.run(main())
except (KeyboardInterrupt, SystemExit):
    log.warning("Exit")
