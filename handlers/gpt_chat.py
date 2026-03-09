from aiogram.fsm.context import FSMContext
from States.states import myStates
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command
from aiogram import F, Router
from services.openai_service import ask_gpt
from utils.gpt_utils import send_gpt
from keyboards.inlinekeyboard import main_menu

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
    user_id = message.from_user.id
    result = await ask_gpt(user_id, data)
    await message.answer(result)
    await state.clear()
    keyboard = main_menu()
    await message.answer('Ты вернулся в главное меню. Напиши /gpt чтобы задать вопрос.', reply_markup=keyboard)
