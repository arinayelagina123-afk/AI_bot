from aiogram.fsm.state import State, StatesGroup


class myStates(StatesGroup):
    waiting_gpt=State()
    dialog_with__persson=State()
