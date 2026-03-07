from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from aiogram.filters import Command
from utils.random_utils import send_random
from keyboards.inlinekeyboard import main_menu

router = Router()


@router.message(Command("random"))
async def random_fact(message: Message):
    await send_random(message)


@router.callback_query(F.data == 'menu:random')
async def start_random(callback: CallbackQuery):
    await callback.answer()
    await send_random(callback.message)


@router.callback_query(F.data == "menu:start")
async def go_start(callback: CallbackQuery):
    await callback.answer()

    await callback.message.answer('Ты вернулся в главное меню. Напиши /random чтобы получить факт.',reply_markup=main_menu())

