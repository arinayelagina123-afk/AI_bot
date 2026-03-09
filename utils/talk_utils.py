from aiogram.types import FSInputFile
from aiogram.types import Message
from keyboards.inlinekeyboard import dialog


async def send_text(message: Message):
    photo = FSInputFile('images/talk.png')
    await message.answer_photo(photo)
    await message.answer('Выберите с кем будете разговаривать.', reply_markup=dialog())
