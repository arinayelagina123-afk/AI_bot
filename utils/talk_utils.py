from aiogram.types import FSInputFile
from aiogram.types import Message
from keyboards.inlinekeyboard import dialog
from pathlib import Path

REAL_DIR = Path(__file__).resolve().parent.parent


async def send_text(message: Message):
    photo = FSInputFile('images/talk.png')
    await message.answer_photo(photo)
    await message.answer('Выберите с кем будете разговаривать.', reply_markup=dialog())


def read_file(file):
    with open(REAL_DIR / file, "r", encoding="utf-8") as f:
        return f.read()
