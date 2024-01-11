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
    service = State()
    number = State()
    name = State()
    price = State()
    description = State()
    message = State()
    author = State()
    address = State()
    photo = State()
    checker = State()

class ChangePrice(StatesGroup):
    price = State()
    message = State()
    id =  State()
    last_price = State()

class SendAll(StatesGroup):
    message = State()
    text = State()


class ChangeSubDomain(StatesGroup):
    message = State()
    text = State()
    service = State()


class ChangePercent(StatesGroup):
    message = State()
    text = State()

class ChangeDomain(StatesGroup):
    message = State()
    text = State()

class CustomText(StatesGroup):
    message = State()
    text = State()
    log = State()