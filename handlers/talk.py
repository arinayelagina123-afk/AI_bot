from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from States.states import myStates
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command
from aiogram import F, Router
from services.openai_service import ask_gpt
from keyboards.inlinekeyboard import cancel_dialog, main_menu
from utils.talk_utils import send_text,read_file
router = Router()


@router.message(Command('talk'))
async def talk_cmd(message: Message, state: FSMContext):
    await send_text(message)


@router.callback_query(F.data == 'menu:talk')
async def talk_but(callback: CallbackQuery, state: FSMContext):
    await send_text(callback.message)
    await callback.answer()


@router.callback_query(F.data == 'menu:flatt')
async def flat_state(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer('Вы выбрали Флаттершай')
    await state.set_state(myStates.dialog_with_flatt)



@router.message(myStates.dialog_with_flatt)
async def dialog_with_flatt(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user_data = await state.get_data()
    dialog_history = user_data.get('dialog_history', [])
    system_promt =read_file('prompts/flatt.txt')
    data = message.text
    result = await ask_gpt(user_id,data,system_promt,dialog_history)
    await state.update_data(dialog_history=dialog_history)
    await message.answer(result, reply_markup=cancel_dialog())


@router.callback_query(F.data == 'menu:isk')
async def isk_state(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer('Вы выбрали Искорку')
    await state.set_state(myStates.dialog_with_isk)



@router.message(myStates.dialog_with_isk)
async def dialog_with_isk(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user_data = await state.get_data()
    dialog_history = user_data.get('dialog_history', [])
    system_promt = read_file('prompts/isk.txt')
    data = message.text
    result = await ask_gpt(user_id,data,system_promt,dialog_history)
    await state.update_data(dialog_history=dialog_history)
    await message.answer(result, reply_markup=cancel_dialog())


@router.callback_query(F.data == 'menu:sonic')
async def son(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer('Вы выбрали Соника')
    await state.set_state(myStates.dialog_with_sonic)



@router.message(myStates.dialog_with_sonic)
async def dialog_with_son(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user_data = await state.get_data()
    dialog_history = user_data.get('dialog_history', [])
    system_promt = read_file('prompts/son.txt')
    data = message.text
    result = await ask_gpt(user_id, data, system_promt, dialog_history)
    await state.update_data(dialog_history=dialog_history)
    await message.answer(result, reply_markup=cancel_dialog())


@router.callback_query(F.data == 'menu:luntic')
async def lun_state(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer('Вы выбрали Лунтика')
    await state.set_state(myStates.dialog_with_luntic)



@router.message(myStates.dialog_with_luntic)
async def dialog_with_lun(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user_data = await state.get_data()
    dialog_history = user_data.get('dialog_history', [])
    system_promt = read_file('prompts/lun.txt')
    data = message.text
    result = await ask_gpt(user_id, data, system_promt, dialog_history)
    await state.update_data(dialog_history=dialog_history)
    await message.answer(result, reply_markup=cancel_dialog())


@router.callback_query(F.data == "menu:start")
async def go_start(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.clear()
    photo = FSInputFile('images/welcome.png')
    await callback.message.answer_photo(photo)
    await callback.message.answer('Ты вернулся в главное меню. Напиши /talk чтобы снова поговорить.',
                                  reply_markup=main_menu())
