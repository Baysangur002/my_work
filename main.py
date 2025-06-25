from aiogram import Bot, Dispatcher, Router
import logging
import asyncio
from config import TOKEN
from config import ADMIN
from handlers.commands import router


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

