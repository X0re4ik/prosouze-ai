from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from contextlib import asynccontextmanager
from src.shared.config import PROJECT_SETTINGS

engine = create_async_engine(
    PROJECT_SETTINGS.postgresql.database_url_async,
    echo=PROJECT_SETTINGS.postgresql.echo,
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
)


@asynccontextmanager
async def get_async_session(*, commit: bool = False):
    async with AsyncSessionLocal() as session:
        try:
            yield session
            if commit:
                await session.commit()  # подтверждаем изменения
        except SQLAlchemyError:
            await session.rollback()  # откатываем транзакцию при ошибке
            raise
        finally:
            await session.close()
