import asyncio
import logging

from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, Command
from aiogram.types import FSInputFile, InputMediaPhoto

from core.keyboards.inline import InKeyboards, AdminInKeyboards
from core.utils.config import TOKEN, ADMIN_CHANNEL_ID
from core.utils.texts import texts, start_texts, admin_texts, in_keyboard_texts
from core.utils.paths import paths
from core.functions.function import Admin, User, Country, Service, Link, Request
from core.states.state import FriendTextWait, ChangeNickname, ChangeSmartSupp, CreateLink, ChangePrice,SendAll

Form_router = Router()
Bot_router = Router()

bot = Bot(TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

@dp.message(CommandStart())
async def command_start(message: types.Message):
    user_id = message.from_user.id
    user = User.find_user(message.from_user.id)
    if User.is_user_exists(user_id):
        photo = FSInputFile(path=paths.menu)
        # Пользователь есть в базе, отправляем главное меню
        await bot.send_photo(
            chat_id=message.chat.id,
            caption=texts.menu,
            photo=photo,
            reply_markup=InKeyboards.menu(user['admin'])
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
    Request.create_request(callback.from_user.username, callback.from_user.id, "Реклама")
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
        message_id=data['message'],
        chat_id=message.chat.id,
        caption=start_texts.waitText
    )
    Request.create_request(message.from_user.username, message.from_user.id, "Друг", text=message.text)
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
    user = User.add_user(chat_id, username, refferer)
    Request.change_status(chat_id, 'accepted')
    if not user:
        await callback.message.edit_text(text=admin_texts.error_confirm_user)
        return
    await callback.message.edit_text(text=admin_texts.confirmed_user(username, callback.from_user.username))
    await bot.send_message(text=texts.confirm_user, chat_id=chat_id)
    await bot.edit_message_caption(chat_id=chat_id, message_id=int(message_id), caption=texts.menu, reply_markup=InKeyboards.menu(False))

@dp.callback_query(F.data.startswith('bannewuser#_'))
async def register_stage_1(callback: types.CallbackQuery, state: FSMContext):
    data = callback.data.split('#_')
    chat_id = data[1]
    username = data[2]
    print(chat_id, username, sep='\n---------')
    Request.change_status(chat_id, 'decided')
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
    countries = Country.get_all_active_countries()
    await state.clear()
    print(countries)
    if countries != False:
        media = InputMediaPhoto(
            media=FSInputFile(
                path=paths.link
            ),
            caption=texts.create_link_caption
        )
        await callback.message.edit_media(
            media=media,
            reply_markup=InKeyboards.create_link(countries)
        )
    else:
        media = InputMediaPhoto(
            media=FSInputFile(
                path=paths.link
            ),
            caption=texts.none_active_countries
        )
        await callback.message.edit_media(
            media=media,
            reply_markup=InKeyboards.error_get_countries
        )


@dp.callback_query(F.data.startswith("create_link_country_"))
async def create_link_country(callback: types.CallbackQuery):
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
async def create_link_service(callback: types.CallbackQuery, state:FSMContext):
    data = callback.data.split('_')[3]
    message = await callback.message.edit_caption(
        caption=texts.link_name,
        reply_markup=InKeyboards.cancel
    )
    await state.set_state(CreateLink.message)
    await state.update_data(message=message.message_id)
    await state.set_state(CreateLink.service)
    await state.update_data(service=data)
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
async def create_link_price(message: types.Message, state:FSMContext):
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
async def create_link_description(message: types.Message, state:FSMContext):
    data = await state.update_data(description=message.text)
    await state.set_state(CreateLink.author)
    await bot.delete_message(message_id=message.message_id, chat_id=message.chat.id)
    await bot.edit_message_caption(
        chat_id=message.chat.id,
        message_id=data['message'],
        caption=texts.link_author,
        reply_markup=InKeyboards.cancel
    )

@Bot_router.message(CreateLink.author)
async def create_link_author(message: types.Message, state:FSMContext):
    data = await state.update_data(author=message.text)
    await state.set_state(CreateLink.photo)
    await bot.delete_message(message_id=message.message_id, chat_id=message.chat.id)
    await bot.edit_message_caption(
        chat_id=message.chat.id,
        message_id=data['message'],
        caption=texts.link_photo,
        reply_markup=InKeyboards.skip
    )

@Bot_router.message(CreateLink.photo)
async def create_link_author(message: types.Message, state:FSMContext):
    data = await state.update_data(photo=message.text)

    await state.set_state(CreateLink.number)
    await bot.delete_message(message_id=message.message_id, chat_id=message.chat.id)
    await bot.edit_message_caption(
        chat_id=message.chat.id,
        message_id=data['message'],
        caption=texts.link_number,
        reply_markup=InKeyboards.cancel
    )

@dp.callback_query(F.data == "skip_photo_create_link")
async def skip_photo_create_link(callback: types.CallbackQuery, state:FSMContext):
    data = await state.update_data(photo=0)
    await state.set_state(CreateLink.number)
    await bot.edit_message_caption(
        chat_id=callback.message.chat.id,
        message_id=data['message'],
        caption=texts.link_number,
        reply_markup=InKeyboards.cancel
    )

@Bot_router.message(CreateLink.number)
async def create_link_address(message: types.Message, state:FSMContext):
    data = await state.update_data(number=message.text)
    await state.set_state(CreateLink.address)
    await bot.edit_message_caption(
        chat_id=message.chat.id,
        message_id=data['message'],
        caption=texts.link_address,
        reply_markup=InKeyboards.cancel
    )

@Bot_router.message(CreateLink.address)
async def create_link_address(message: types.Message, state:FSMContext):
    data = await state.update_data(address=message.text)
    await state.clear()
    await bot.delete_message(message_id=message.message_id, chat_id=message.chat.id)
    data['id'] = message.from_user.id
    link = Link.create_link(data)
    print(link)
    print('___________________')
    print(data)
    await bot.edit_message_caption(
        chat_id=message.chat.id,
        message_id=data['message'],
        caption=texts.link_checker,
        reply_markup=InKeyboards.checker_in_create_link(link['id'])
    )

@dp.callback_query(F.data.startswith("checker_change_"))
async def create_link_checker(callback: types.CallbackQuery, state: FSMContext):
    data = callback.data.split('_')[2]
    link1 = Link.change_checker(data)
    print(data)
    link = Link.find_link(data)
    name = link['country']['flag']+link['name']
    await callback.message.edit_caption(
        caption=texts.link(link['author'], link['price'], link['author'], link['number'], link['address'], link['checker'], "23432", name),
        reply_markup=InKeyboards.link_info(data, link['checker'])
    )

@dp.callback_query(F.data.startswith("delete_*link_*"))
async def link_delete(callback: types.CallbackQuery, state: FSMContext):
    data = callback.data.split('_*')[2]
    print(data)
    link = Link.find_link(data)
    print(link)
    await callback.message.edit_caption(
        caption=texts.delete_link(link['name']),
        reply_markup=InKeyboards.delete_link(link['id'])
    )

@dp.callback_query(F.data.startswith("delete_link_confirm_"))
async def delete_link(callback: types.CallbackQuery):
    data = callback.data.split('_')[3]
    print(data)
    link = Link.delete_link(data)
    print(link)
    await callback.message.edit_caption(
        caption=texts.delete_link_confirm(link['name']),
        reply_markup=InKeyboards.menu_and_tools
    )

@dp.callback_query(F.data.startswith("admin_countries"))
async def admin_countries(callback: types.CallbackQuery):
    countries = Country.get_all_countries()
    await callback.message.edit_caption(
        caption=texts.choose_country,
        reply_markup=AdminInKeyboards.admin_countries(countries)
    )

@dp.callback_query(F.data.startswith("links_"))
async def links_info(callback: types.CallbackQuery):
    data = callback.data.split('_')
    id = callback.from_user.id
    callback_text = "menu"
    if len(data) > 1:
        callback_text = "admin"
        id = data[1]
    links = Link.get_links_in_user(id)
    print(links)
    count = len(links)
    await callback.message.edit_caption(
        caption=texts.links(count),
        reply_markup=InKeyboards.links(links, callback_text)
    )

@dp.callback_query(F.data.startswith("link_"))
async def link_info(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    data = callback.data.split('_')[1]
    print(data)
    link = Link.find_link(data)
    name = link['country']['flag'] + link['name']
    await callback.message.edit_caption(
        caption=texts.link(link['author'], link['price'], link['author'], link['number'], link['address'], link['checker'], "23432", name),
        reply_markup=InKeyboards.link_info(data, link['checker'])
    )

@dp.callback_query(F.data.startswith("change_link_price_"))
async def link_change_price(callback: types.CallbackQuery, state:FSMContext):
    data = callback.data.split('_')[3]
    link = Link.find_link(data)
    await callback.message.edit_caption(
        caption=texts.change_price_link,
        reply_markup=InKeyboards.back(data)
    )
    await state.set_state(ChangePrice.message)
    await state.update_data(message=callback.message.message_id)
    await state.set_state(ChangePrice.last_price)
    await state.update_data(last_price=link['price'])
    await state.set_state(ChangePrice.id)
    await state.update_data(id=link['id'])
    await state.set_state(ChangePrice.price)

@Bot_router.message(ChangePrice.price)
async def change_price(message: types.Message,state:FSMContext):
    data = await state.update_data(price=message.text)
    link = Link.change_price(data['id'], message.text)
    caption = texts.change_price_link_success(message.text)
    await message.delete()
    if not link:
        caption = texts.change_price_link_error
    await bot.edit_message_caption(
        chat_id=message.chat.id,
        message_id=data['message'],
        caption=caption,
        reply_markup=InKeyboards.back(data['id'])
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
    user = User.find_user(callback.from_user.id)
    media = InputMediaPhoto(media=FSInputFile(path=paths.menu),
                            caption=texts.menu)
    await callback.message.edit_media(
        media=media,
        reply_markup=InKeyboards.menu(user['admin'])
    )

@dp.callback_query(F.data == "channels")
async def channels(callback: types.CallbackQuery):
    media = InputMediaPhoto(media=FSInputFile(path=paths.channels),
                            caption=texts.channels)
    await callback.message.edit_media(
        media=media,
        reply_markup=InKeyboards.channels
    )

@dp.callback_query(F.data == "admin_send_all")
async def admin_send_all(callback: types.CallbackQuery,state:FSMContext):
    await callback.message.edit_caption(
        caption=admin_texts.admin_send_all,
        reply_markup=AdminInKeyboards.back
    )
    await state.set_state(SendAll.message)
    await state.update_data(message=callback.message.message_id)
    await state.set_state(SendAll.text)

@Bot_router.message(SendAll.text)
async def send_all_text(message: types.Message, state: FSMContext):
    data = await state.update_data(text=message.text)
    await state.clear()
    users = User.get_all_users()
    admin_menu = Admin.get_admin_menu()
    for user in users:
        await bot.send_message(
            chat_id=user['id'],
            text=message.text
        )
    await bot.edit_message_caption(
        caption=texts.admin_menu(admin_menu),
        chat_id=message.chat.id,
        message_id=data['message'],
        reply_markup=AdminInKeyboards.admin_keyboard
    )

    message_send = await bot.send_message(
        chat_id=message.from_user.id,
        text=admin_texts.stop_work_text(len(users))
    )
    await message.delete()
    await asyncio.sleep(10)
    await message_send.delete()

@dp.callback_query(F.data.startswith("admin_users_page_"))
async def admin_users(callback: types.CallbackQuery):
    page = int(callback.data.split("_")[-1])  # Извлекаем номер страницы из данных коллбэка
    print(page)
    items_per_page = 10  # Количество пользователей на одной странице
    users = User.get_all_users()
    print(users[1])

    start_index = page * items_per_page
    end_index = (page + 1) * items_per_page
    current_users = users[start_index:end_index]
    print(current_users)

    # Редактируем сообщение с клавиатурой
    await callback.message.edit_caption(
        caption=admin_texts.admin_users(len(users)),
        reply_markup=AdminInKeyboards.admin_users(current_users, page,end_index)
    )


@dp.callback_query(F.data == "stop_work")
async def stop_work(callback:types.CallbackQuery):
    users = User.get_all_users()
    for user in users:
        await bot.send_message(
            chat_id=user['id'],
            text=texts.stop_work
        )
    message = await bot.send_message(
        chat_id=callback.from_user.id,
        text=texts.stop_work_text(len(users))
    )
    await asyncio.sleep(10)
    await message.delete()

@dp.callback_query(F.data.startswith("user_"))
async def user_profile(callback: types.CallbackQuery):
    data = callback.data.split('_')[1]
    user = User.find_user(int(data))
    await callback.message.edit_caption(
        caption=admin_texts.admin_user_profile(user),
        reply_markup=AdminInKeyboards.admin_user(user['id'])
    )


@dp.message(F.text, Command("admin"))
async def admin(message: types.Message):
    user = User.find_user(message.from_user.id)
    admin_menu = Admin.get_admin_menu()
    if not user['admin']:
        await bot.send_message(
            chat_id=message.chat.id,
            text=texts.admin_error,
        )
        return
    photo = FSInputFile(path=paths.menu)
    await  bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=texts.admin_menu(admin_menu),
        reply_markup=AdminInKeyboards.admin_keyboard
    )
@dp.callback_query(F.data == "admin")
async def admin(callback: types.CallbackQuery):
    user = User.find_user(callback.from_user.id)
    admin_menu = Admin.get_admin_menu()
    if not user['admin']:
        await callback.message.edit_caption(
            caption=texts.admin_error,
            reply_markup=InKeyboards.menu(False)
        )
        return
    await callback.message.edit_caption(
        caption=texts.admin_menu(admin_menu),
        reply_markup=AdminInKeyboards.admin_keyboard
    )

# Запуск бота
async def main():
    dp.include_router(Form_router)
    dp.include_router(Bot_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
