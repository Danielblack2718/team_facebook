import asyncio
import logging

from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile, InputMediaPhoto

from core.keyboards.inline import InKeyboards, AdminInKeyboards
from core.utils.config import TOKEN, ADMIN_CHANNEL_ID
from core.utils.texts import texts, start_texts, admin_texts, in_keyboard_texts
from core.utils.paths import paths
from core.functions.function import Admin, User, Country, Service
from core.states.state import FriendTextWait, ChangeNickname, ChangeSmartSupp, CreateLink

Form_router = Router()
Bot_router = Router()

bot = Bot(TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

@dp.message(CommandStart())
async def command_start(message: types.Message):
    user_id = message.from_user.id
    if await User.is_user_exists(user_id):
        photo = FSInputFile(path=paths.menu)
        # Пользователь есть в базе, отправляем главное меню
        await bot.send_photo(
            chat_id=message.chat.id,
            caption=texts.menu,
            photo=photo,
            reply_markup=InKeyboards.menu
        )
    else:
        if message.from_user.username is None:
            await bot.send_message(chat_id=message.chat.id, text=start_texts.errorUsername)
            return
        photo = FSInputFile(path=paths.start)

        await bot.send_photo(
            chat_id=message.chat.id,
            caption=start_texts.start,
            photo=photo,
            reply_markup=InKeyboards.one_button(
                text=in_keyboard_texts.inlineStart,
                callback="start"
            )
        )

@dp.callback_query(F.data == 'start')
async def confirm_rules(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_caption(
        caption=start_texts.rules,
        reply_markup=InKeyboards.one_button(
            text=in_keyboard_texts.confirmRules,
            callback="identification",
        ),
        parse_mode="MarkdownV2"
    )


@dp.callback_query(F.data == 'identification')
async def identification(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_caption(
        caption=start_texts.identification,
        reply_markup=InKeyboards.identification_keyboard
    )


@dp.callback_query(F.data.startswith('registration_stage_1_advert'))
async def register_stage_1(callback: types.CallbackQuery, state: FSMContext):
    main_message = await callback.message.edit_caption(caption=start_texts.waitText)
    await bot.send_message(
        text=admin_texts.new_user_text(
            callback.from_user.username,
            "Реклама"
        ),
        chat_id=ADMIN_CHANNEL_ID,
        reply_markup=AdminInKeyboards.new_user_keyboard(
            callback.from_user.id,
            callback.from_user.username,
            main_message.message_id
        )
    )

@dp.callback_query(F.data.startswith('registration_stage_1_friends'))
async def register_stage_1(callback: types.CallbackQuery, state: FSMContext):
    message = await callback.message.edit_caption(
        caption=start_texts.friendWaitText,
        reply_markup=InKeyboards.one_button(
            text=in_keyboard_texts.backIdentification,
            callback="identification"
        )
    )
    await state.set_state(FriendTextWait.message)
    await state.update_data(message=message.message_id)
    await state.set_state(FriendTextWait.username)


@Form_router.message(FriendTextWait.username)
async def friend_text_wait(message: types.Message, state: FSMContext):
    data = await state.update_data(username=message.text)
    main_message = await bot.edit_message_caption(
        chat_id=message.chat.id,
        message_id=data['message'],
        caption=start_texts.waitText
    )
    await bot.delete_message(
        message_id=message.message_id,
        chat_id=message.chat.id
    )
    await bot.send_message(
        text=admin_texts.new_user_text(
            message.from_user.username,
            "Друг",
            message.text
        ),
        chat_id=ADMIN_CHANNEL_ID,
        reply_markup=AdminInKeyboards.new_user_keyboard(
            message.from_user.id,
            message.from_user.username,
            main_message.message_id,
            message.text
        )
    )

@dp.callback_query(F.data.startswith('addnewuser#_'))
async def register_stage_1(callback: types.CallbackQuery, state: FSMContext):
    data = callback.data.split('#_')
    chat_id = data[1]
    username = data[2]
    message_id = data[3]
    refferer = data[4]
    print(message_id)
    print("1-1-1-1-1--1-1-1--1-")
    print(chat_id, username, message_id, sep='\n---------')
    User.add_user(chat_id, username, refferer)
    delete_messge = await callback.message.edit_text(text=admin_texts.confirmed_user(username, callback.from_user.username))
    await bot.send_message(text=texts.confirm_user, chat_id=chat_id)
    await bot.edit_message_caption(chat_id=chat_id, message_id=int(message_id), caption=texts.menu, reply_markup=InKeyboards.menu)

@dp.callback_query(F.data.startswith('bannewuser#_'))
async def register_stage_1(callback: types.CallbackQuery, state: FSMContext):
    data = callback.data.split('#_')
    chat_id = data[1]
    username = data[2]
    print(chat_id, username, sep='\n---------')
    delete_message = await callback.message.edit_text(text=admin_texts.not_confirmed_user(username, callback.from_user.username))
    await bot.send_message(text=texts.not_confirm_user, chat_id=chat_id)

@dp.callback_query(F.data == "profile")
async def profile(callback: types.CallbackQuery):
    user = User.find_user(callback.from_user.id)
    media = InputMediaPhoto(
        media=FSInputFile(
            path=paths.profile
        ),
        caption=texts.profile(
            user['id'],
            user['hide'],
            user['supportChat'],
            0,
            0
        ),
        parse_mode="MARKDOWN")
    await bot.edit_message_media(
        media=media,
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        reply_markup=InKeyboards.profile,
    )

@dp.callback_query(F.data.startswith("nickname"))
async def nickname(callback: types.CallbackQuery):
    user = User.find_user(callback.from_user.id)
    data = callback.data.split('_')
    hide = user['hide']
    if len(data) == 2:
        hide = User.change_status_nickname_status(callback.from_user.id)
        print(hide)
    await callback.message.edit_caption(
        caption=texts.nickname(hide, user['nickname']),
        reply_markup=InKeyboards.nickname,
        parse_mode="MARKDOWN"
    )

@dp.callback_query(F.data == "smartsupp")
async def smartsupp(callback: types.CallbackQuery):
    user = User.find_user(callback.from_user.id)
    api = "Не указан"
    if user['supportChatApi'] is not None:
        api = user['supportChatApi']
    await callback.message.edit_caption(
        caption=texts.smartsupp(api),
        reply_markup=InKeyboards.smartsupp
    )

@dp.callback_query(F.data == "change_smartsupp")
async def change_smartsupp(callback: types.CallbackQuery, state: FSMContext):
    user = User.find_user(callback.from_user.id)
    api = "Не указан"
    if user['supportChatApi'] is not None:
        api = user['supportChatApi']
    message = await callback.message.edit_caption(
        caption=texts.new_smartsupp,
        reply_markup=InKeyboards.one_button("Оставить @" + api, "smartsupp"),
        parse_mode="MARKDOWN"
    )
    await state.set_state(ChangeSmartSupp.message)
    await state.update_data(message=message.message_id)
    await state.set_state(ChangeSmartSupp.last_key)
    await state.update_data(last_key=api)
    await state.set_state(ChangeSmartSupp.key)

@Bot_router.message(ChangeSmartSupp.key)
async def change_smartsupp_confirm(message: types.Message, state: FSMContext):
    data = await state.update_data(key=message.text)
    key = User.change_smartsupp(message.from_user.id, message.text)
    print(key)
    if key != "error":
        await bot.edit_message_caption(
            chat_id=message.chat.id,
            message_id=data['message'],
            caption=texts.confirm_smartsupp(message.text),
            reply_markup=InKeyboards.confirm_smartsupp

        )
        await state.clear()
    else:
        await bot.edit_message_caption(
            chat_id=message.chat.id,
            message_id=data['message'],
            caption=texts.error_nickname,
            reply_markup=InKeyboards.one_button("Оставить @" + data['last_key'], "smartsupp")
        )
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

@dp.callback_query(F.data == "create_link")
async def create_link(callback: types.CallbackQuery, state: FSMContext):
    countries = Country.get_all_countries()
    await state.clear()
    print(countries)
    if countries != False:
        await callback.message.edit_caption(
            caption=texts.create_link_caption,
            reply_markup=InKeyboards.create_link(countries)
        )
    else:
        await callback.message.edit_caption(
            caption=texts.none_active_countries,
            reply_markup=InKeyboards.error_get_countries
        )


@dp.callback_query(F.data.startswith("create_link_country_"))
async def hungary_link(callback: types.CallbackQuery):
    data = callback.data.split('_')[3]
    print(data)
    services = Service.get_services_in_country(data)

    if services != False:
        await callback.message.edit_caption(
            caption=texts.select_service,
            reply_markup=InKeyboards.servicesCountry(services)
        )
    else:
        await callback.message.edit_caption(
            caption=texts.none_active_services,
            reply_markup=InKeyboards.menu_and_tools
        )

@dp.callback_query(F.data.startswith("create_link_service_"))
async def hungary_link(callback: types.CallbackQuery, state:FSMContext):
    data = callback.data.split('_')[3]
    message = await callback.message.edit_caption(
        caption=texts.link_name,
        reply_markup=InKeyboards.cancel
    )
    await state.set_state(CreateLink.message)
    await state.update_data(message=message.message_id)
    await state.set_state(CreateLink.name)

@Bot_router.message(CreateLink.name)
async def create_link_name(message: types.Message, state:FSMContext):
    data = await state.update_data(name=message.text)
    await state.set_state(CreateLink.price)
    await bot.delete_message(message_id=message.message_id, chat_id=message.chat.id)
    await bot.edit_message_caption(
        chat_id=message.chat.id,
        message_id=data['message'],
        caption=texts.link_price,
        reply_markup=InKeyboards.cancel
    )


@Bot_router.message(CreateLink.price)
async def create_link_name(message: types.Message, state:FSMContext):
    data = await state.update_data(price=message.text)
    await state.set_state(CreateLink.description)
    await bot.delete_message(message_id=message.message_id, chat_id=message.chat.id)
    await bot.edit_message_caption(
        chat_id=message.chat.id,
        message_id=data['message'],
        caption=texts.link_description,
        reply_markup=InKeyboards.cancel
    )

@Bot_router.message(CreateLink.description)
async def create_link_name(message: types.Message, state:FSMContext):
    data = await state.update_data(description=message.text)
    await state.clear()
    await bot.delete_message(message_id=message.message_id, chat_id=message.chat.id)
    await bot.edit_message_caption(
        chat_id=message.chat.id,
        message_id=data['message'],
        caption=str(data),
        reply_markup=InKeyboards.cancel
    )

@dp.callback_query(F.data == "change_nickname")
async def change_nickname(callback: types.CallbackQuery, state: FSMContext):
    user = User.find_user(callback.from_user.id)
    message = await callback.message.edit_caption(
        caption=texts.nickname_edit(user['hide'], user['nickname']),
        reply_markup=InKeyboards.one_button("Оставить @" + user['nickname'], "nickname"),
        parse_mode="MARKDOWN"
    )
    await state.set_state(ChangeNickname.message)
    await state.update_data(message=message.message_id)
    await state.set_state(ChangeNickname.last_nickname)
    await state.update_data(last_nickname=user['nickname'])
    await state.set_state(ChangeNickname.nickname)

@Bot_router.message(ChangeNickname.nickname)
async def change_nickname_confirm(message: types.Message, state: FSMContext):
    data = await state.update_data(nickname=message.text)
    nickname = User.change_nickname(message.from_user.id, message.text)
    print(nickname)
    if nickname != "error":
        await bot.edit_message_caption(
            chat_id=message.chat.id,
            message_id=data['message'],
            caption=texts.confirm_nickname(message.text),
            reply_markup=InKeyboards.confirm_nickname

        )
        await state.clear()
    else:
        await bot.edit_message_caption(
            chat_id=message.chat.id,
            message_id=data['message'],
            caption=texts.error_nickname,
            reply_markup=InKeyboards.one_button("Оставить @" + data['last_nickname'], "nickname")
        )
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


@dp.callback_query(F.data == "tools")
async def tools(callback: types.CallbackQuery):
    media = InputMediaPhoto(media=FSInputFile(path=paths.tools),
                            caption=texts.tools)
    await callback.message.edit_media(
        media=media,
        reply_markup=InKeyboards.tools
    )

@dp.callback_query(F.data == "referals")
async def referals(callback: types.CallbackQuery):
    await callback.message.edit_caption(
        caption=texts.referrals,
        reply_markup=InKeyboards.menu_and_tools
    )

@dp.callback_query(F.data == "menu")
async def menu(callback: types.CallbackQuery):
    media = InputMediaPhoto(media=FSInputFile(path=paths.menu),
                            caption=texts.menu)
    await callback.message.edit_media(
       media=media,
        reply_markup=InKeyboards.menu
    )

@dp.callback_query(F.data == "channels")
async def links(callback: types.CallbackQuery):
    media = InputMediaPhoto(media=FSInputFile(path=paths.channels),
                            caption=texts.channels)
    await callback.message.edit_media(
        media=media,
        reply_markup=InKeyboards.channels
    )
# Запуск бота
async def main():
    dp.include_router(Form_router)
    dp.include_router(Bot_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
