from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from core.utils.texts import start_texts, texts, admin_texts, in_keyboard_texts
from core.utils.config import CHANNELS


class InKeyboards:
    @staticmethod
    def one_button(text, callback):
        return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text=text, callback_data=callback)
            ]
        ])

    identification_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=in_keyboard_texts.identificationButton1,
                                 callback_data="registration_stage_1_advert"),
            InlineKeyboardButton(text=in_keyboard_texts.identificationButton2,
                                 callback_data="registration_stage_1_friends")
        ]
    ])
    menu = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=in_keyboard_texts.createLink, callback_data="create_link")
        ],
        [
            InlineKeyboardButton(text=in_keyboard_texts.profile, callback_data="profile"),
            InlineKeyboardButton(text=in_keyboard_texts.tools, callback_data="tools")
        ],
        [
            InlineKeyboardButton(text=in_keyboard_texts.channels, callback_data="channels"),
        ],
    ])

    profile = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=in_keyboard_texts.hideNickname, callback_data="nickname")
        ],
        [
            InlineKeyboardButton(text=in_keyboard_texts.menu, callback_data="menu"),
            InlineKeyboardButton(text=in_keyboard_texts.tools, callback_data="tools")
        ]
    ])

    channels = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=in_keyboard_texts.all_chat_text_link, switch_inline_query=CHANNELS.ALL_CHAT_LINK)
        ],
        [
            InlineKeyboardButton(text=in_keyboard_texts.profits_text_link, switch_inline_query=CHANNELS.PROFITS_CHAT_LINK),
            InlineKeyboardButton(text=in_keyboard_texts.manuals_text_link, switch_inline_query=CHANNELS.MANUALS_CHAT_LINK)

        ],
        [
            InlineKeyboardButton(text=in_keyboard_texts.how_work_text_link, url=CHANNELS.HOW_TO_WORK_LINK)
        ],
        [
            InlineKeyboardButton(text=in_keyboard_texts.profile, callback_data="profile"),
            InlineKeyboardButton(text=in_keyboard_texts.tools, callback_data="tools")
        ],
        [
            InlineKeyboardButton(text=in_keyboard_texts.menu, callback_data="menu"),
        ]

    ])

    nickname = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=in_keyboard_texts.onOffnickname, callback_data="nickname_status")
        ],
        [
            InlineKeyboardButton(text=in_keyboard_texts.changeNickname, callback_data="change_nickname")
        ],
        [
            InlineKeyboardButton(text=in_keyboard_texts.menu, callback_data="menu"),
            InlineKeyboardButton(text=in_keyboard_texts.profile, callback_data="profile")
        ]

    ])
    confirm_nickname = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=in_keyboard_texts.mask, callback_data="nickname")
        ],
        [
            InlineKeyboardButton(text=in_keyboard_texts.menu, callback_data="menu"),
            InlineKeyboardButton(text=in_keyboard_texts.profile, callback_data="profile")
        ]

    ])

    tools = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=in_keyboard_texts.ad, callback_data="ad"),
            InlineKeyboardButton(text=in_keyboard_texts.createLink, callback_data="create_link")
        ],
        [
            InlineKeyboardButton(text=in_keyboard_texts.smartsupp, callback_data="smartsupp")
        ],
        [
            InlineKeyboardButton(text=in_keyboard_texts.referals, callback_data="referals"),
            InlineKeyboardButton(text=in_keyboard_texts.mentors, callback_data="mentors")
        ],
        [
            InlineKeyboardButton(text=in_keyboard_texts.menu, callback_data="menu"),
            InlineKeyboardButton(text=in_keyboard_texts.profile, callback_data="profile")
        ]
    ])
    smartsupp = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=in_keyboard_texts.new_smartsupp, callback_data="change_smartsupp")
        ],
        [
            InlineKeyboardButton(text=in_keyboard_texts.menu, callback_data="menu"),
            InlineKeyboardButton(text=in_keyboard_texts.tools, callback_data="tools")
        ]
    ])
    confirm_smartsupp = InlineKeyboardMarkup(inline_keyboard=[

        [
            InlineKeyboardButton(text=in_keyboard_texts.smartsupp, callback_data="smartsupp")
        ],
        [
            InlineKeyboardButton(text=in_keyboard_texts.menu, callback_data="menu"),
            InlineKeyboardButton(text=in_keyboard_texts.tools, callback_data="tools")
        ]
    ])
    menu_and_tools = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=in_keyboard_texts.menu, callback_data="menu"),
            InlineKeyboardButton(text=in_keyboard_texts.tools, callback_data="tools")
        ]
    ])
    cancel = InlineKeyboardMarkup(inline_keyboard=[
        [

            InlineKeyboardButton(text=in_keyboard_texts.cancel, callback_data="create_link")
        ]
    ])
    @staticmethod
    def create_link(countries):
        # Создаем кнопки для стран
        country_buttons = [
            InlineKeyboardButton(text=in_keyboard_texts.country(country['flag'], country['name']), callback_data=f"create_link_country_{country['id']}")
            for country in countries
        ]

        # Добавляем кнопки "Menu" и "Tools" внизу


        # Разбиваем кнопки по рядам (по две кнопки в каждом ряду)
        rows = [country_buttons[i:i + 2] for i in range(0, len(country_buttons), 2)]

        rows.append([
            InlineKeyboardButton(text=in_keyboard_texts.menu, callback_data="menu"),
            InlineKeyboardButton(text=in_keyboard_texts.tools, callback_data="tools")
        ])
        # Создаем клавиатуру
        create_link = InlineKeyboardMarkup(inline_keyboard=rows)

        return create_link

    @staticmethod
    def servicesCountry(services):
        # Создаем кнопки для стран
        if services[0]['country']['country_active']:
            service_buttons = [
                InlineKeyboardButton(text=in_keyboard_texts.servicesCountry(service['country']['flag'], service['name']),
                                     callback_data=f"create_link_service_{service['name']}")
                for service in services
            ]

        # Добавляем кнопки "Menu" и "Tools" внизу

        # Разбиваем кнопки по рядам (по две кнопки в каждом ряду)
        rows = [service_buttons[i:i + 2] for i in range(0, len(service_buttons), 2)]

        rows.append([
            InlineKeyboardButton(text=in_keyboard_texts.menu, callback_data="menu"),
            InlineKeyboardButton(text=in_keyboard_texts.tools, callback_data="tools")
        ])
        # Создаем клавиатуру
        services_country = InlineKeyboardMarkup(inline_keyboard=rows)

        return services_country

class AdminInKeyboards:
    @staticmethod
    def new_user_keyboard(id, username, message_id, refferer="0"):
        print(id, username, message_id, sep='--------\n')
        return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text=admin_texts.add_new_user,
                                     callback_data=f"addnewuser#_{id}#_{username}#_{message_id}#_{refferer}"),
                InlineKeyboardButton(text=admin_texts.ban_new_user, callback_data=f"bannewuser#_{id}#_{username}")
            ]
        ])
