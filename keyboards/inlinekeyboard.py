from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='🎲 Случайный факт', callback_data='menu:random')],
            [InlineKeyboardButton(text='🤖 Chat GPT', callback_data='menu:gpt')],
            [InlineKeyboardButton(text='🗣️ Диалог с линостью', callback_data='menu:talk')],
            [InlineKeyboardButton(text='🎯 Квиз', callback_data='menu:quiz')],
            [InlineKeyboardButton(text='яаокачтонезнаю что', callback_data='menu:idk')],
            [InlineKeyboardButton(text='idk', callback_data='menu:idk')]
        ]
    )
    return keyboard


def random_start():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Еще факт', callback_data='menu:random')],
            [InlineKeyboardButton(text='Отменить', callback_data='menu:start')],
        ]
    )
    return keyboard


def dialog():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Флаттершай', callback_data='menu:flatt')],
            [InlineKeyboardButton(text='Искорка', callback_data='menu:isk')],
            [InlineKeyboardButton(text='Соник', callback_data='menu:sonic')],
            [InlineKeyboardButton(text='Лунтик', callback_data='menu:luntic')]
        ]
    )
    return keyboard

def cancel_dialog():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Прекратить.', callback_data='menu:start')]
        ]
    )
    return keyboard