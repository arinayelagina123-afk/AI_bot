from aiogram.filters import callback_data
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# /start
def main_menu():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='🎲 Случайный факт', callback_data='menu:random')],
            [InlineKeyboardButton(text='🤖 Chat GPT', callback_data='menu:gpt')],
            [InlineKeyboardButton(text='🗣️ Диалог с линостью', callback_data='menu:talk')],
            [InlineKeyboardButton(text='🎯 Квиз', callback_data='menu:quiz')],
            [InlineKeyboardButton(text='📄Переводчик', callback_data='menu:translate')],
            [InlineKeyboardButton(text='📈Рекомендации', callback_data='menu:rec')]
        ]
    )
    return keyboard


# /random
def random_start():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='→Еще факт', callback_data='menu:random')],
            [InlineKeyboardButton(text='❌Отменить', callback_data='menu:start')],
        ]
    )
    return keyboard


# /talk
def dialog():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='→Флаттершай', callback_data='menu:flatt')],
            [InlineKeyboardButton(text='→Искорка', callback_data='menu:isk')],
            [InlineKeyboardButton(text='→Соник', callback_data='menu:sonic')],
            [InlineKeyboardButton(text='→Лунтик', callback_data='menu:luntic')]
        ]
    )
    return keyboard


def cancel_dialog():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='❌Прекратить.', callback_data='menu:start')]
        ]
    )
    return keyboard


# /quiz
def quiz():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='→Космос', callback_data='cosmos')],
            [InlineKeyboardButton(text='→Страны', callback_data='country')],
            [InlineKeyboardButton(text='→Животные', callback_data='animal')],
            [InlineKeyboardButton(text='→Обо всем', callback_data='all')],
        ]
    )
    return keyboard


def in_quiz():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='→Результат', callback_data='quiz:result')],
            [InlineKeyboardButton(text='→Еще вопрос', callback_data='quiz:ece')],
            [InlineKeyboardButton(text='→Сменить тему', callback_data='quiz:other')],
        ]
    )
    return keyboard


# /translate
def translate_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='🇬🇧Английский', callback_data='translate:Eng')],
            [InlineKeyboardButton(text='🇩🇪Немецкий', callback_data='translate:Ger')],
            [InlineKeyboardButton(text='🇫🇷Французский', callback_data='translate:Fren')]
        ]
    )
    return keyboard


def in__translate_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='→Выбрать другой язык', callback_data='translate:other')],
            [InlineKeyboardButton(text='❌Закончить', callback_data='translate:cancel')]
        ]
    )
    return keyboard


# /recommendation
def choice_category():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='📖Книги', callback_data='category:books')],
            [InlineKeyboardButton(text='🎥Фильмы', callback_data='category:movies')],
            [InlineKeyboardButton(text='💻Игры', callback_data='category:games')]
        ]
    )
    return keyboard


def dont_like_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='→Не нравится', callback_data='dont_like')],
            [InlineKeyboardButton(text='❌Закончить', callback_data='cancel')]
        ]
    )
    return keyboard
