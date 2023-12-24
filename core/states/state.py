from aiogram.fsm.state import StatesGroup, State

class FriendTextWait(StatesGroup):
    username = State()
    message = State()

class ChangeNickname(StatesGroup):
    nickname = State()
    message = State()
    last_nickname =State()