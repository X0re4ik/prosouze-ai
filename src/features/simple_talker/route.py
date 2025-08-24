from fastapi import APIRouter
from aiogram import Router as TelegramRoute, types

from .dto import MessageDTO
from src.shared.api.postgresql import get_async_session

from .schema import RequestSchema, ResponseSchema

from src.shared.lib.fastapi.request import ResponseBaseModel

from .use_case import simple_talker_use_case_factory

route = APIRouter(
    prefix="/simple-talker",
)

telegram_route = TelegramRoute()


@route.post("")
async def simple_talker_route(
    schema: RequestSchema,
) -> ResponseBaseModel[ResponseSchema]:

    async with get_async_session() as session:
        simple_talker_use_case = simple_talker_use_case_factory(session)

        answers = await simple_talker_use_case.execute(
            MessageDTO(
                message=schema.message,
            ),
        )

    return ResponseBaseModel(
        data=ResponseSchema(
            answers=answers,
        )
    )


@telegram_route.message()
async def simple_talker_telegram_route(message: types.Message):

    if message.text is None:
        return await message.answer("Введите текст")

    async with get_async_session() as session:
        simple_talker_use_case = simple_talker_use_case_factory(session)

        answers = await simple_talker_use_case.execute(
            MessageDTO(
                message=message.text,
            ),
        )

    return await message.answer("\n\n".join(answers))
