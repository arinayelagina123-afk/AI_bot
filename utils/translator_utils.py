from aiogram.types import FSInputFile, Message
from keyboards.inlinekeyboard import translate_keyboard
from services.openai_service import ask_gpt
import json


async def send_mes(message: Message):
    photo = FSInputFile('images/translator.png')
    await message.answer_photo(photo)
    await message.answer('Выберите на какой нужно перевести.', reply_markup=translate_keyboard())


async def translate(user_id, lang,message):
    prompt = f"""
Переведи текст с русского языка на {lang}.
Верни строго JSON без чего либо лишнего только json:
{{
    "translate":{{"translate":"перевод"}}
}}
    """
    trans = await ask_gpt(user_id, message,prompt)
    trans = trans.replace("```json", "").replace("```", "").strip()
    trans = json.loads(trans)
    trans = trans["translate"]["translate"]
    return trans
