from typing import Any, Dict

from aiogram import Bot, Dispatcher
from aiogram.utils.i18n import I18n, SimpleI18nMiddleware

from app.settings import SETTINGS


def setup(bot: Bot, dp: Dispatcher, workflow: Dict[str, Any]) -> None:
    i18n = I18n(
        path=SETTINGS.i18n_path,
        default_locale=SETTINGS.i18n_default_locale,
        domain=SETTINGS.i18n_domain,
    )
    i18n_middleware = SimpleI18nMiddleware(i18n)
    dp.update.outer_middleware(i18n_middleware)
    workflow["i18n"] = i18n
