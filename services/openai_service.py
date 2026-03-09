from openai import AsyncOpenAI
from config import AI_BOT_TOKEN
import logging

client = AsyncOpenAI(api_key=AI_BOT_TOKEN)
MODEL = 'gpt-4o-mini'

logger = logging.getLogger(__name__)


async def ask_gpt(user_id: int, user_message: str,
                  system_prompt: str = 'Ты полезный ассистент.Отвечай кратко и по делу и вежливо',
                  history_from_fsm: list = None) -> str:
    try:
        messages = [{'role': 'system', 'content': system_prompt}]
        if history_from_fsm:
            messages.extend(history_from_fsm)  # Добавляет в лист без списков
        messages.append({'role': 'user', 'content': user_message})
        logger.info(f'GPT запрос (user_id: {user_id}): {user_message[:20]}')

        response = await client.chat.completions.create(
            model=MODEL,
            messages=messages,
            max_tokens=1000,
            temperature=0.8
        )

        answer = response.choices[0].message.content
        logger.info(f'Ответ GPT (user_id: {user_id}): {len(answer)} символов')
        if history_from_fsm is None:
            history_from_fsm = []
        history_from_fsm.append({'role': 'user', 'content': user_message})  # обновляет историю из fsm
        history_from_fsm.append({'role': 'assistant', 'content': answer})

        return answer

    except Exception as e:
        logger.error(f'Ошибка GPT (user_id: {user_id}): {e}')
        return 'Произошла ошибка при общении с искусственным интеллектом. Пожалуйста, попробуйте позже.'
