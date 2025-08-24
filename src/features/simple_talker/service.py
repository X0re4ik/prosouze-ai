from sqlalchemy import select, true
from src.entities.promty import Promty

from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.gigachat import GigaChatDriver

import asyncio


from .dto import MessageDTO


class SimpleTalkerService:

    def __init__(
        self,
        session: AsyncSession,
        giga_chat_driver: GigaChatDriver,
    ):
        self._session = session

        self._giga_chat_driver = giga_chat_driver

    async def get_answer(self, dto: MessageDTO) -> list[str]:

        promties = await self._get_active_promties()

        _tasks = [
            self._gigachat_request(str(promty.text).format(message=dto.message))
            for promty in promties
        ]

        answers = await asyncio.gather(*_tasks)
        
        print(answers)

        return [answer for answer in answers if answer is not None]

    async def _gigachat_request(self, user_request: str) -> str | None:
        await asyncio.sleep(0.02)
        return await self._giga_chat_driver.send_request(user_request)

    async def _get_active_promties(self) -> list[Promty]:
        stmt = select(Promty).where(Promty.is_active.is_(true()))

        cursor = await self._session.execute(stmt)

        return list(cursor.scalars().all())
