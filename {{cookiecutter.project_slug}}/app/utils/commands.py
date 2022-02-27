from typing import Any, Dict, List

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram.utils.i18n import I18n


def get(i18n: I18n) -> List[BotCommand]:
    return [
        BotCommand(
            command="start",
            description=i18n.gettext("Get info about bot"),
        ),
        BotCommand(command="settings", description=i18n.gettext("Configure something")),
        BotCommand(
            command="privacy",
            description=i18n.gettext("How the bot processes and stores your data"),
        ),
        BotCommand(command="license", description=i18n.gettext("Library licenses")),
    ]


async def set_commands(bot: Bot, i18n: I18n) -> None:
    # Default commands for unknown languages
    with i18n.use_locale("en"):
        await bot.set_my_commands(commands=get(i18n), scope=BotCommandScopeDefault())

    for lang in i18n.locales:
        with i18n.use_locale(lang):
            await bot.set_my_commands(
                commands=get(i18n),
                scope=BotCommandScopeDefault(),
                language_code=lang,
            )


def setup(bot: Bot, dp: Dispatcher, workflow: Dict[str, Any]) -> None:
    dp.startup.register(set_commands)
