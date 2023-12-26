from aiogram.fsm.state import StatesGroup, State

class FriendTextWait(StatesGroup):
    username = State()
    message = State()

class ChangeNickname(StatesGroup):
    nickname = State()
    message = State()
    last_nickname =State()

class ChangeSmartSupp(StatesGroup):
    key = State()
    message = State()
    last_key = State()

class CreateLink(StatesGroup):
    name = State()
    price = State()
    description = State()
    message = State()


