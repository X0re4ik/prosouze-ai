from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

from src.features.simple_talker import simple_talker_telegram_route


TOKEN = "8497447368:AAGYmJ1Kfd47z8NrJCo0HGwEdVDBzDLjNz4"  # вставь сюда токен бота

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Задавай любой вопрос, я отвечу 'Да'.")


async def main():
    dp.include_router(simple_talker_telegram_route)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
