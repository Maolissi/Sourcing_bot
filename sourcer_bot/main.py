import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand

from sourcer_bot.bot.handlers import router
from sourcer_bot.config import get_settings
from sourcer_bot.logging_config import configure_logging

logger = logging.getLogger(__name__)


async def main() -> None:
    settings = get_settings()
    configure_logging(settings.log_level)

    bot = Bot(
        token=settings.bot_token.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()
    dp.include_router(router)
    await bot.set_my_commands([
        BotCommand(command="start", description="Open Sourcer Workspace"),
        BotCommand(command="help", description="Show help"),
    ])

    logger.info("Starting Telegram Sourcer Bot (%s)", settings.app_env)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
