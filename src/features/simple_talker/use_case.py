from .dto import MessageDTO

from src.infrastructure.gigachat import (
    giga_chat_auth_factory,
    giga_chat_driver_factory,
)

from sqlalchemy.ext.asyncio import AsyncSession

from .service import SimpleTalkerService

class SimpleTalkerUseCase:
    
    def __init__(self, session: AsyncSession):
        self._session = session

    async def execute(
        self,
        dto: MessageDTO,
    ) -> list[str]:
        
        access_token: str = giga_chat_auth_factory().get_access_token()
        giga_chat_driver = giga_chat_driver_factory(access_token)
        
        simple_talker_service = SimpleTalkerService(self._session, giga_chat_driver,)
        return await simple_talker_service.get_answer(dto)


def simple_talker_use_case_factory(session: AsyncSession):
    return SimpleTalkerUseCase(
        session,
    )