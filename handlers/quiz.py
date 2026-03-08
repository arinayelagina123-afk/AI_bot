from aiogram.fsm.context import FSMContext
from States.states import myStates
from aiogram.types import  CallbackQuery, Message
from aiogram.filters import Command
from aiogram import F, Router
from keyboards.inlinekeyboard import in_quiz, main_menu, quiz
from utils.quiz_utils import create_quiz, send_text, check_answer

router = Router()


@router.message(Command('quiz'))
async def talk_cmd(message: Message, state: FSMContext):
    await send_text(message)


@router.callback_query(F.data == 'menu:quiz')
async def talk_but(callback: CallbackQuery):
    await send_text(callback.message)
    await callback.answer()


@router.callback_query(F.data == 'cosmos')
async def cosmos_quiz(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer('Вы выбрали космос')
    user_id = callback.message.from_user.id
    await state.update_data(
        tema='космос',
        correct_counter=0,
        main_counter=0,
    )
    data = await state.get_data()
    tema = data["tema"]
    quiz = await create_quiz(tema,user_id)
    question = quiz["questions"]["question"]
    correct_answer = quiz['questions']['answer']
    await state.update_data(question=question,correct_answer=correct_answer)

    await callback.message.answer(question)
    await state.set_state(myStates.quiz)


@router.callback_query(F.data == 'country')
async def country_quiz(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer('Вы выбрали страны')
    user_id = callback.message.from_user.id
    await state.update_data(
        tema='Страны',
        correct_counter=0,
        main_counter=0,
    )
    data = await state.get_data()
    tema = data["tema"]
    quiz = await create_quiz(tema,user_id)
    question = quiz["questions"]["question"]
    correct_answer = quiz['questions']['answer']
    await state.update_data(question=question,correct_answer=correct_answer)

    await callback.message.answer(question)
    await state.set_state(myStates.quiz)


@router.callback_query(F.data == 'animal')
async def animal_quiz(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer('Вы выбрали Животные')
    user_id = callback.message.from_user.id
    await state.update_data(
        tema='Животные',
        correct_counter=0,
        main_counter=0,
    )
    data = await state.get_data()
    tema = data["tema"]
    quiz = await create_quiz(tema,user_id)
    question = quiz["questions"]["question"]
    correct_answer = quiz['questions']['answer']
    await state.update_data(question=question, correct_answer=correct_answer)

    await callback.message.answer(question)
    await state.set_state(myStates.quiz)


@router.callback_query(F.data == 'all')
async def all_quiz(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer('Вы выбрали обо всем')
    user_id = callback.message.from_user.id
    await state.update_data(
        tema='Обо всем',
        correct_counter=0,
        main_counter=0,
    )
    data = await state.get_data()
    tema = data["tema"]
    quiz = await create_quiz(tema,user_id)
    question = quiz["questions"]["question"]
    correct_answer = quiz['questions']['answer']
    await state.update_data(question=question, correct_answer=correct_answer)

    await callback.message.answer(question)
    await state.set_state(myStates.quiz)


@router.callback_query(F.data == 'quiz:result')
async def quiz_result(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    data = await state.get_data()
    correct_counter = data["correct_counter"]
    main_counter = data["main_counter"]
    await callback.message.answer(
        f'Результат: {correct_counter}/{main_counter}\nТы вернулся в главное меню. Напиши /quiz чтобы снова поиграть.',
        reply_markup=main_menu())
    await state.clear()


@router.callback_query(F.data == 'quiz:other')
async def quiz_other(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    data = await state.get_data()
    correct_counter = data.get("correct_counter", 0)
    main_counter = data.get("main_counter", 0)
    await callback.message.answer(
        f'Результат: {correct_counter}/{main_counter}\nТы вернулся в выбор тем.',
        reply_markup=quiz())
    await state.clear()

@router.callback_query(F.data == 'quiz:ece')
async def quiz_ece(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    data = await state.get_data()
    tema = data.get('tema')
    user_id = callback.message.from_user.id
    if not tema:
        await callback.message.answer("Сначала выбери тему!")
    quiz = await create_quiz(tema,user_id)
    question = quiz["questions"]["question"]
    correct_answer = quiz['questions']['answer']
    await state.update_data(question=question,correct_answer=correct_answer ,correctness_of_the_answer=None)
    await callback.message.answer(question)
    await state.set_state(myStates.quiz)


@router.message(myStates.quiz)
async def quiz_state(message: Message, state: FSMContext):
    data = await state.get_data()
    question = data["question"]
    correct_counter = data.get("correct_counter", 0)
    main_counter = data.get("main_counter", 0)
    correct_answer = data["correct_answer"]
    checked_answer = await check_answer(question, message.text,user_id=message.from_user.id,correct_answer=correct_answer)
    if checked_answer:
        correct_counter += 1
        await message.answer('Верно!')
    else:
        await message.answer(f'Неверно.Правильный ответ: {correct_answer}')
    main_counter += 1
    await state.update_data(
        correct_counter=correct_counter,
        main_counter=main_counter
    )
    await message.answer('Выбери что будешь делать:', reply_markup=in_quiz())
    await state.set_state(None)

