from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.inlinekeyboard import main_menu
from aiogram.types import FSInputFile

router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
    keyboard = main_menu()
    photo = FSInputFile('images/welcome.png')
    await message.answer_photo(photo)
    await message.answer('Что ты хочешь сделать?', reply_markup=keyboard)
