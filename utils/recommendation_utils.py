from aiogram.types import FSInputFile
from aiogram.types import Message
from services.openai_service import ask_gpt
import json
from keyboards.inlinekeyboard import choice_category


async def take_recommendation(user_id, category: str, genre: str, dont_like: list):
    prompt = f"""Я пишу бота предлагающего книги,игры,фильмы пользователям по жанррам.
    Предложи {category} c жанром:{genre}.Но учти что пользователю не нравится(если ничего не написано то ему все нравится):{dont_like}
    Верни строго JSON без чего либо лишнего только json:
    {{
        "recomindation":{{"recomindation":"сама рекоминдация"}}
    }}
        """
    rec = await ask_gpt(user_id, prompt)
    rec = rec.replace("```json", "").replace("```", "").strip()
    rec = json.loads(rec)
    rec = rec["recomindation"]["recomindation"]
    return rec


async def send_text(message: Message):
    photo = FSInputFile('images/recomindation.jpg')
    await message.answer_photo(photo)
    await message.answer('Выберите категорию.', reply_markup=choice_category())
