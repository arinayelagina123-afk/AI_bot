from aiogram.fsm.state import State, StatesGroup


class myStates(StatesGroup):
    waiting_gpt=State()
    dialog_with_flatt=State()
    dialog_with_isk=State()
    dialog_with_sonic=State()
    dialog_with_luntic=State()
