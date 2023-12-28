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

    @staticmethod
    def menu(admin):

        keyboard = [
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
        ]
        if admin:
            keyboard.append([InlineKeyboardButton(text=in_keyboard_texts.admin_panel, callback_data="admin")])

        kb = InlineKeyboardMarkup(inline_keyboard=keyboard)
        return kb

    profile = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=in_keyboard_texts.hideNickname, callback_data="nickname")
        ],
        [
            InlineKeyboardButton(text=in_keyboard_texts.menu, callback_data="menu"),
            InlineKeyboardButton(text=in_keyboard_texts.tools, callback_data="tools")
        ]
    ])
    @staticmethod
    def checker_in_create_link(link_id):
        return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text=in_keyboard_texts.checker_create_link_on, callback_data=f"checker_change_{link_id}"),
            ],
            [
              InlineKeyboardButton(text=in_keyboard_texts.skip, callback_data=f"link_{link_id}")
            ]
        ])
    skip = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=in_keyboard_texts.skip, callback_data="skip_photo_create_link")
        ],
        [
            InlineKeyboardButton(text=in_keyboard_texts.cancel, callback_data="create_link")
        ]
    ])
    @staticmethod
    def back(id):
        return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text=in_keyboard_texts.back, callback_data=f"link_{id}")
            ]
        ])
    @staticmethod
    def link_info(id, checker):
        return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text= in_keyboard_texts.link_check_off if checker else in_keyboard_texts.link_check_on, callback_data=f"checker_change_{id}")
            ],
            [
              InlineKeyboardButton(text=in_keyboard_texts.link_change_price, callback_data=f"change_link_price_{id}")
            ],
            [
              InlineKeyboardButton(text=in_keyboard_texts.link_delete, callback_data=f"delete_*link_*{id}")
            ],
            [
                InlineKeyboardButton(text=in_keyboard_texts.back, callback_data="menu")
            ]
        ])
    @staticmethod
    def links(links_info):
        # Создаем кнопки для стран
        print(links_info)
        links_buttons = [
            InlineKeyboardButton(text=link['name'],callback_data=f"link_{link['id']}")
            for link in links_info
        ]
        # Добавляем кнопки "Menu" и "Tools" внизу

        # Разбиваем кнопки по рядам (по две кнопки в каждом ряду)
        rows = [links_buttons[i:i + 2] for i in range(0, len(links_buttons), 2)]

        rows.append([
            InlineKeyboardButton(text=in_keyboard_texts.menu, callback_data="menu"),
            InlineKeyboardButton(text=in_keyboard_texts.tools, callback_data="tools")
        ])
        # Создаем клавиатуру
        links_button = InlineKeyboardMarkup(inline_keyboard=rows)
        return links_button

    @staticmethod
    def delete_link(id):
        return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text=in_keyboard_texts.delete_link_confirm, callback_data=f"delete_link_confirm_{id}")
            ],
            [
                InlineKeyboardButton(text=in_keyboard_texts.back, callback_data=f"link_{id}")
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
            InlineKeyboardButton(text=in_keyboard_texts.ad, callback_data="links"),
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
                                     callback_data=f"create_link_service_{service['id']}")
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
    back = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=in_keyboard_texts.back, callback_data="admin")
        ]
    ])
    admin_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=in_keyboard_texts.admin_stop_work, callback_data="stop_work")
        ],
        [
            InlineKeyboardButton(text=in_keyboard_texts.admin_send_all, callback_data="admin_send_all"),
            InlineKeyboardButton(text=in_keyboard_texts.admin_users, callback_data="admin_users")
        ],
        [
            InlineKeyboardButton(text=in_keyboard_texts.admin_services, callback_data="admin_service"),
            InlineKeyboardButton(text=in_keyboard_texts.admin_profits, callback_data="admin_profits")
        ],
        [
            InlineKeyboardButton(text=in_keyboard_texts.admin_requests, callback_data="admin_requests")
        ],
        [
            InlineKeyboardButton(text=in_keyboard_texts.admin_settings, callback_data="admin_settings")
        ],
        [
            InlineKeyboardButton(text=in_keyboard_texts.admin_countries, callback_data="admin_countries")
        ],
        [
          InlineKeyboardButton(text=in_keyboard_texts.back, callback_data="menu")
        ]
    ])