# TELEGRAM_AI_BOT Telegram-бот на aiogram, который использует OpenAI для нескольких сценариев: - ответы на вопросы через /gpt - случайные факты через /random - диалог с персонажами через /talk - квиз по темам через /quiz - перевод текста через /translate - рекомендации книг, фильмов и игр через /recommendation Это мой первый pet-project с несколькими пользовательскими сценариями, FSM-состояниями, клавиатурами, промптами и отдельным сервисным слоем для работы с OpenAI. ## Стек - Python 3.12 - aiogram 3 - OpenAI Python SDK - python-dotenv ## Структура проекта
text
TELEGRAM_AI_BOT/
├── README.md
└── AI_bot/
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
## Что умеет бот ### /start Показывает главное меню с inline-кнопками. ### /gpt Принимает один вопрос пользователя и отправляет его в OpenAI. ### /random Генерирует случайный интересный факт. ### /talk Запускает диалог с выбранным персонажем. Для персонажей используются отдельные system prompts из папки prompts/. ### /quiz Создает квиз-вопрос по теме, проверяет ответ пользователя и считает результат. ### /translate Переводит введенный текст на выбранный язык. ### /recommendation Подбирает книгу, фильм или игру по жанру. Если рекомендация не понравилась, можно запросить другую. ## Установка и запуск ### 1. Клонировать проект
bash
git clone <repo_url>
cd TELEGRAM_AI_BOT/AI_bot
### 2. Создать и активировать виртуальное окружение
bash
python -m venv .venv
source .venv/bin/activate
### 3. Установить зависимости
bash
pip install -r requirements.txt
### 4. Создать файл .env Создай файл .env в папке AI_bot:
env
TG_BOT_TOKEN=your_telegram_bot_token
AI_BOT_TOKEN=your_openai_api_key
### 5. Запустить бота
bash
python main.py
## Конфигурация В [AI_bot/config.py] загружаются две переменные окружения: - TG_BOT_TOKEN - токен Telegram-бота - AI_BOT_TOKEN - API-ключ OpenAI ## Как устроен код - handlers/ - обработчики команд, кнопок и состояний - services/openai_service.py - единая точка отправки запросов в OpenAI - utils/ - вспомогательная логика для отдельных сценариев - states/states.py - FSM-состояния - keyboards/inlinekeyboard.py - inline-клавиатуры - prompts/ - system prompts для ролевого диалога - images/ - картинки для интерфейса бота
