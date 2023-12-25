from aiogram.dispatcher.filters.state import StatesGroup, State


class NewPost(StatesGroup):
    kursm = State()
    NewMessage = State()
    yosh = State()
    termiz = State()
    phone = State()
    Confirm = State()
