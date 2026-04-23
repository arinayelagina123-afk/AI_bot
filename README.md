# TELEGRAM_AI_BOT

Telegram-бот на `aiogram` и `OpenAI API`.

Бот умеет:

- отвечать на вопросы
- генерировать случайные факты
- вести диалог с персонажами
- проводить квиз по темам
- переводить текст
- подбирать книги, фильмы и игры

## Возможности

- `/start` - главное меню
- `/gpt` - один вопрос к модели
- `/random` - случайный факт
- `/talk` - диалог с персонажем
- `/quiz` - викторина по теме
- `/translate` - перевод текста
- `/recommendation` - рекомендации по жанру

## Стек

- Python 3.12
- aiogram 3
- OpenAI SDK
- python-dotenv

## Структура

```text
AI_bot/
├── main.py
├── config.py
├── requirements.txt
├── handlers/
├── services/
├── utils/
├── states/
├── keyboards/
├── prompts/
└── images/
```

## Запуск

1. Перейти в папку проекта:

```bash
cd AI_bot
```

2. Создать виртуальное окружение:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Установить зависимости:

```bash
pip install -r requirements.txt
```

4. Создать файл `.env`:

```env
TG_BOT_TOKEN=your_telegram_bot_token
AI_BOT_TOKEN=your_openai_api_key
```

5. Запустить бота:

```bash
python main.py
```

## Как устроен проект

- `handlers/` - команды, кнопки и сценарии бота
- `services/` - работа с OpenAI
- `utils/` - вспомогательная логика
- `states/` - FSM-состояния
- `keyboards/` - inline-клавиатуры
- `prompts/` - промпты для персонажей
- `images/` - изображения для интерфейса
