from aiogram.fsm.context import FSMContext
from states.states import myStates
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command
from aiogram import F, Router
from utils.recommendation_utils import take_recommendation, send_text
from keyboards.inlinekeyboard import dont_like_keyboard, main_menu

router = Router()


@router.message(Command('recommendation'))
async def recommend_cmd(message: Message, state: FSMContext):
    await send_text(message)


@router.callback_query(F.data == 'menu:rec')
async def recommend_btn(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await send_text(callback.message)


@router.callback_query(F.data == 'category:books')
async def books(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.update_data(category='книгу')
    await callback.message.answer('Напишите какой жанр вам нравится:')
    await state.set_state(myStates.waiting_genre)


@router.callback_query(F.data == 'category:movies')
async def movies(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.update_data(category='фильм')
    await callback.message.answer('Напишите какой жанр вам нравится:')
    await state.set_state(myStates.waiting_genre)


@router.callback_query(F.data == 'category:games')
async def games(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.update_data(category='игру')
    await callback.message.answer('Напишите какой жанр вам нравится:')
    await state.set_state(myStates.waiting_genre)


@router.message(myStates.waiting_genre)
async def waiting_genre(message: Message, state: FSMContext):
    user_id = message.from_user.id
    genre = message.text
    data = await state.get_data()
    category = data.get('category', None)
    await state.update_data(genre=genre)
    dont_like = data.get('dont_like', [])
    result = await take_recommendation(user_id, category, genre, dont_like)
    dont_like.append(result)
    await state.update_data(dont_like=dont_like)
    await message.answer(result, reply_markup=dont_like_keyboard())


@router.callback_query(F.data == 'dont_like')
async def dont_like_btn(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    user_id = callback.message.from_user.id
    data = await state.get_data()
    category = data.get('category', None)
    genre = data.get('genre', None)
    dont_like = data.get("dont_like", [])
    result = await take_recommendation(user_id, category, genre, dont_like)
    dont_like.append(result)
    await state.update_data(dont_like=dont_like)
    await callback.message.answer(result, reply_markup=dont_like_keyboard())


@router.callback_query(F.data == 'cancel')
async def cancel(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.clear()
    await callback.message.answer('Ты вернулся в главное меню. Напиши /recommendation чтобы снова начать выбирать.',
                                  reply_markup=main_menu())
