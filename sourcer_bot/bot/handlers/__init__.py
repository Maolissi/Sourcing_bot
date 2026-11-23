from aiogram import Router

from sourcer_bot.bot.handlers.callbacks import router as callbacks_router
from sourcer_bot.bot.handlers.start import router as start_router

router = Router(name="root")
router.include_routers(start_router, callbacks_router)
