from aiogram import Bot, Dispatcher
import asyncio
import logging
from aiogram.types import Message
from config import TG_BOT_TOKEN
from handlers import router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s %(message)s")

bot = Bot(token=TG_BOT_TOKEN)
dp = Dispatcher()
dp.include_router(router)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
