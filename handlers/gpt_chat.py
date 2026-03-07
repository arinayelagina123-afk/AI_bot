from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from States.states import myStates
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, CallbackQuery, Message
from aiogram.filters import Command
from aiogram import F, Router
from services.openai_service import ask_gpt
from utils.gpt_utils import send_gpt

router = Router()


@router.message(Command('gpt'))
async def gpt_text(message: Message, state: FSMContext):
    await send_gpt(message)
    await state.set_state(myStates.waiting_gpt)


@router.callback_query(F.data == 'menu:gpt')
async def gpt_text_but(callback: CallbackQuery, state: FSMContext):
    await send_gpt(callback.message)
    await state.set_state(myStates.waiting_gpt)
    await callback.answer()


@router.message(myStates.waiting_gpt)
async def gpt_answer(message: Message, state: FSMContext):
    data = message.text
    result = await ask_gpt(data)
    await message.answer(result)
    await state.clear()