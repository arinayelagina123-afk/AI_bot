import json
from services.openai_service import ask_gpt
import asyncio
from aiogram.types import FSInputFile
from aiogram.types import Message
from keyboards.inlinekeyboard import quiz
from pathlib import Path


async def create_quiz(tema,user_id):
    prompt = f"""
Сгенерируй новый квиз вопрос по теме {tema}. Не повторяй предыдущие вопросы. 1 вопрос.
Верни строго JSON без чего либо лишнего только json:
{{
    "questions":{{"question":"вопрос", "answer":"ответ"}}
}}
    """
    quiz = await ask_gpt(user_id, prompt)
    quiz = quiz.replace("```json", "").replace("```", "").strip()
    quiz = json.loads(quiz)
    print(quiz)
    print(type(quiz))
    return quiz


async def check_answer(question, answer,user_id,correct_answer):
    prompt = f"""
    Правилен ли ответ: пользователя:{answer} на вопрос: {question}(правильный ответ{correct_answer}).Ответ верни строго JSON без чего либо лишнего только json(true/false)
"""
    quiz = await ask_gpt(user_id,prompt)
    quiz = quiz.replace("```json", "").replace("```", "").strip()
    quiz = json.loads(quiz)
    print(quiz)
    print(type(quiz))
    return quiz



REAL_DIR = Path(__file__).resolve().parent.parent


async def send_text(message: Message):
    photo = FSInputFile('images/quiz.png')
    await message.answer_photo(photo)
    await message.answer('Выберите викторину.', reply_markup=quiz())


def read_file(file):
    with open(REAL_DIR / file, "r", encoding="utf-8") as f:
        return f.read()
