from aiogram.types import FSInputFile, Message

async def send_gpt(message: Message):
    photo = FSInputFile('images/GPT.png')
    await message.answer_photo(photo)
    await message.answer('Напиши свой вопрос.')