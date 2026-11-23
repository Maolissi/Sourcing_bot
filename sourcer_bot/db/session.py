from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from sourcer_bot.config import get_settings

settings = get_settings()
engine = create_async_engine(
    settings.database_url,
    echo=settings.app_env == "development",
    pool_pre_ping=True,
)
SessionFactory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def dispose_engine() -> None:
    await engine.dispose()
