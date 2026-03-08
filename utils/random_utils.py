from services.openai_service import ask_gpt
from aiogram.types import FSInputFile, Message
from keyboards.inlinekeyboard import random_start


async def send_random(message: Message,user_id):
    result = await ask_gpt(user_id,'Привет, скажи мне кратко абсолютно рандомный факт. И говори об этом так чтобы было интересно.')
    photo = FSInputFile('images/random.png')
    await message.answer_photo(photo)
    await message.answer(result, reply_markup=random_start())