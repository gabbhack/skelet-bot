import logging

from aiogram import Router
from aiogram.dispatcher.filters import Command
from aiogram.types import Message
{% if cookiecutter.use_i18n == "yes" %}
from aiogram.utils.i18n import I18n
{% endif %}

logger = logging.getLogger(__name__)
router = Router()
router.message.filter(Command(commands=["start", "settings", "privacy", "license"]))

{% if cookiecutter.use_i18n == "yes" %}
@router.message(Command(commands="start"))
async def cmd_start(message: Message, i18n: I18n) -> None:
    # TODO
    await message.answer(
        i18n.gettext(
            "#TODO"
        )
    )


@router.message(Command(commands="settings"))
async def cmd_settings(message: Message, i18n: I18n) -> None:
    # TODO
    await message.answer(
        i18n.gettext(
            "#TODO"
        )
    )


@router.message(Command(commands="privacy"))
async def cmd_privacy(message: Message, i18n: I18n) -> None:
    # TODO
    await message.answer(
        i18n.gettext(
            "#TODO"
        )
    )


@router.message(Command(commands="license"))
async def cmd_license(message: Message, i18n: I18n) -> None:
    # TODO
    await message.answer(
        i18n.gettext(
            "#TODO"
        )
    )
{% else %}
@router.message(Command(commands="start"))
async def cmd_start(message: Message) -> None:
    # TODO
    await message.answer("#TODO")


@router.message(Command(commands="settings"))
async def cmd_settings(message: Message) -> None:
    # TODO
    await message.answer("#TODO")


@router.message(Command(commands="privacy"))
async def cmd_privacy(message: Message) -> None:
    # TODO
    await message.answer("#TODO")


@router.message(Command(commands="license"))
async def cmd_license(message: Message) -> None:
    # TODO
    await message.answer("#TODO")
{% endif %}
