from aiogram.dispatcher.filters.state import State, StatesGroup


class HelloState(StatesGroup):
    name = State()
