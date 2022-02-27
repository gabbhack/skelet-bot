from aiogram import Router

from app.routers import base

router = Router()
router.include_router(base.router)
