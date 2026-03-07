from aiogram.fsm.state import State, StatesGroup


class myStates(StatesGroup):
    waiting_random = State()
