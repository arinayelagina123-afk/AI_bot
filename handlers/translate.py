from aiogram.fsm.context import FSMContext
from states.states import myStates
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command
from aiogram import F, Router
from utils.translator_utils import send_mes, translate
from keyboards.inlinekeyboard import main_menu, in__translate_keyboard, translate_keyboard

router = Router()


@router.message(Command('translate'))
async def translate_(message: Message):
    await send_mes(message)


@router.callback_query(F.data == 'menu:translate')
async def menu(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await send_mes(callback.message)


@router.callback_query(F.data == 'translate:Eng')
async def translate_eng(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Введите текст чтобы перевести его на Английский:')
    await state.set_state(myStates.trans)
    await state.update_data(lang='Английский')
    await callback.answer()


@router.callback_query(F.data == 'translate:Ger')
async def translate_ger(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Введите текст чтобы перевести его на Немецкий:')
    await state.set_state(myStates.trans)
    await state.update_data(lang='Немецкий')
    await callback.answer()


@router.callback_query(F.data == 'translate:Fren')
async def translate_fren(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Введите текст чтобы перевести его на Французский:')
    await state.set_state(myStates.trans)
    await state.update_data(lang='Французский')
    await callback.answer()


@router.message(myStates.trans)
async def translate_answer(message: Message, state: FSMContext):
    user_id = message.from_user.id
    data_user = message.text
    data = await state.get_data()
    lang = data['lang']
    result = await translate(user_id, lang, data_user)
    await message.answer(result, reply_markup=in__translate_keyboard())
    await state.clear()


@router.callback_query(F.data == 'translate:other')
async def translate_other(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer('Выберите язык', reply_markup=translate_keyboard())


@router.callback_query(F.data == 'translate:cancel')
async def translate_cancel(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer('Ты вернулся в главное меню. Напиши /translate чтобы снова начать перевод.',
                                  reply_markup=main_menu())
