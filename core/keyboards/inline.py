from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from core.utils.texts import start_texts, texts, admin_texts, in_keyboard_texts, log
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
    def links(links_info, callback):
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
            InlineKeyboardButton(text=in_keyboard_texts.menu, callback_data=callback),
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
            InlineKeyboardButton(text=in_keyboard_texts.ad, callback_data="links_"),
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
    def new_user_keyboard(id, username, message_id,oldRequest, refferer="0"):
        print(id, username, message_id, sep='--------\n')
        keyboard = [[
                InlineKeyboardButton(text=admin_texts.add_new_user,
                                     callback_data=f"addnewuser#_{id}#_{username}#_{message_id}#_{refferer}"),
                InlineKeyboardButton(text=admin_texts.ban_new_user, callback_data=f"bannewuser#_{id}#_{username}")
            ]]
        if oldRequest:
            keyboard.append(
                [
                    InlineKeyboardButton(
                        text=in_keyboard_texts.back,
                        callback_data="admin"
                    )
                ]
            )
        kb = InlineKeyboardMarkup(inline_keyboard=keyboard)
        return kb
    back = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=in_keyboard_texts.back, callback_data="admin_text")
        ]
    ])
    admin_settings = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=admin_texts.change_percent, callback_data="change_percent_worker")
        ],
        [
            InlineKeyboardButton(text=admin_texts.change_all_domain, callback_data="change_all_domain")
        ],
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
            InlineKeyboardButton(text=in_keyboard_texts.admin_users, callback_data="admin_users_page_0")
        ],
        [
            InlineKeyboardButton(text=in_keyboard_texts.admin_services, callback_data="admin_services_page_0"),
            InlineKeyboardButton(text=in_keyboard_texts.admin_profits, callback_data="admin_profits_page_0")
        ],
        [
            InlineKeyboardButton(text=in_keyboard_texts.admin_requests, callback_data="admin_request_page_0")
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
    @staticmethod
    def services(services, end_index, page):
        # Добавляем кнопки "Menu" и "Tools" внизу
        services_buttons = [
            InlineKeyboardButton(
                text=("🟢 " if service['active'] else "🔴 ") + str(service['name'])+" "+ service['country'], callback_data=f"service_{service['id']}")
            for service in services
        ]

        # Разбиваем кнопки по рядам (по две кнопки в каждом ряду)
        rows = [services_buttons[i:i + 2] for i in range(0, len(services_buttons), 2)]

        # Добавляем кнопки навигации, только если они не пустые
        navigation_buttons = [
            InlineKeyboardButton(text="⬅️ Назад",
                                 callback_data=f"admin_services_page_{page - 1}") if page > 0 else None,
            InlineKeyboardButton(text=f"Страница {page + 1}", callback_data="empty"),
            InlineKeyboardButton(text="➡️ Вперед",
                                 callback_data=f"admin_services_page_{page + 1}") if end_index < len(
                services) else None
        ]

        # Убираем пустые кнопки
        navigation_buttons = [button for button in navigation_buttons if button is not None]

        if navigation_buttons:
            rows.append(navigation_buttons)

        rows.append([
            InlineKeyboardButton(text=in_keyboard_texts.back, callback_data="admin"),
        ])

        # Создаем клавиатуру
        users_button = InlineKeyboardMarkup(inline_keyboard=rows)
        return users_button

    @staticmethod
    def profits(page, end_index, profits, userid = None):
        # Добавляем кнопки "Menu" и "Tools" внизу
        profits_buttons = [
            InlineKeyboardButton(text=("🟢 " if profit['status'] == "success" else "🔴 ")+str(profit['id'])+" ("+str(profit['amount'])+"$)", callback_data=f"profit_{profit['id']}")
            for profit in profits
        ]

        # Разбиваем кнопки по рядам (по две кнопки в каждом ряду)
        rows = [profits_buttons[i:i + 2] for i in range(0, len(profits_buttons), 2)]

        # Добавляем кнопки навигации, только если они не пустые
        navigation_buttons = [
            InlineKeyboardButton(text="⬅️ Назад", callback_data=f"admin_profits_page_{page - 1}_"+userid if userid else "") if page > 0 else None,
            InlineKeyboardButton(text=f"Страница {page + 1}", callback_data="empty"),
            InlineKeyboardButton(text="➡️ Вперед", callback_data=f"admin_profits_page_{page + 1}_"+userid if userid else "") if end_index < len(profits) else None
        ]

        # Убираем пустые кнопки
        navigation_buttons = [button for button in navigation_buttons if button is not None]

        if navigation_buttons:
            rows.append(navigation_buttons)

        rows.append([
            InlineKeyboardButton(text=in_keyboard_texts.back, callback_data="admin"),
        ])

        # Создаем клавиатуру
        users_button = InlineKeyboardMarkup(inline_keyboard=rows)
        return users_button

    @staticmethod
    def admin_requests(requests, page, end_index):
        request_buttons = [
            InlineKeyboardButton(text=("✅ " if request['status'] == "accepted" else ("⏳ " if request['status'] == "wait" else "❌ "))+str(request['id']), callback_data=f"request_{request['id']}")
            for request in requests
        ]
        # Добавляем кнопки "Menu" и "Tools" внизу

        # Разбиваем кнопки по рядам (по две кнопки в каждом ряду)
        rows = [request_buttons[i:i + 2] for i in range(0, len(request_buttons), 2)]

        # Добавляем кнопки навигации, только если они не пустые
        navigation_buttons = [
            InlineKeyboardButton(text="⬅️ Назад", callback_data=f"admin_request_page_{page - 1}") if page > 0 else None,
            InlineKeyboardButton(text=f"Страница {page + 1}", callback_data="empty"),
            InlineKeyboardButton(text="➡️ Вперед", callback_data=f"admin_request_page_{page + 1}") if end_index < len(requests) else None
        ]

        # Убираем пустые кнопки
        navigation_buttons = [button for button in navigation_buttons if button is not None]

        if navigation_buttons:
            rows.append(navigation_buttons)

        rows.append([
            InlineKeyboardButton(text=in_keyboard_texts.back, callback_data="admin_text"),
        ])

        # Создаем клавиатуру
        users_button = InlineKeyboardMarkup(inline_keyboard=rows)
        return users_button

    @staticmethod
    def admin_users(users, page, end_index):
        print(users)
        users_buttons = [
            InlineKeyboardButton(text=user['username'], callback_data=f"user_{user['id']}")
            for user in users
        ]
        # Добавляем кнопки "Menu" и "Tools" внизу

        # Разбиваем кнопки по рядам (по две кнопки в каждом ряду)
        rows = [users_buttons[i:i + 2] for i in range(0, len(users_buttons), 2)]

        # Добавляем кнопки навигации, только если они не пустые
        navigation_buttons = [
            InlineKeyboardButton(text="⬅️ Назад", callback_data=f"admin_users_page_{page - 1}") if page > 0 else None,
            InlineKeyboardButton(text=f"Страница {page + 1}", callback_data="empty"),
            InlineKeyboardButton(text="➡️ Вперед", callback_data=f"admin_users_page_{page + 1}") if end_index < len(
                users) else None
        ]

        # Убираем пустые кнопки
        navigation_buttons = [button for button in navigation_buttons if button is not None]

        if navigation_buttons:
            rows.append(navigation_buttons)

        rows.append([
            InlineKeyboardButton(text=in_keyboard_texts.back, callback_data="admin"),
        ])

        # Создаем клавиатуру
        users_button = InlineKeyboardMarkup(inline_keyboard=rows)
        return users_button

    @staticmethod
    def admin_user(user_id, mentor):
        return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text=in_keyboard_texts.admin_profits, callback_data=f"admin_profits_page_0_{user_id}")
            ],
            [
                InlineKeyboardButton(text=in_keyboard_texts.admin_links, callback_data=f"links_{user_id}")
            ],
            [
                InlineKeyboardButton(text=in_keyboard_texts.admin_make_mentor(mentor), callback_data=f"make_mentor_{user_id}")
            ],
            [
                InlineKeyboardButton(text=in_keyboard_texts.admin_user_block, callback_data=f"block_{user_id}")
            ],
            [
                InlineKeyboardButton(text=in_keyboard_texts.admin_change_status, callback_data=f"status*_{user_id}")
            ],
            [
                InlineKeyboardButton(text=in_keyboard_texts.admin_user_request, callback_data=f"request_user_{user_id}")
            ],
            [
                InlineKeyboardButton(text=in_keyboard_texts.back, callback_data="admin")
            ]
        ])

    @staticmethod
    def admin_country(country, count):
        return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text=in_keyboard_texts.country_active(country['active']), callback_data=f"on_country_off_{country['id']}")
            ],
            [
                InlineKeyboardButton(text=in_keyboard_texts.menu, callback_data="admin")
            ]
        ])

    menu = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=in_keyboard_texts.back, callback_data="admin")
        ]
    ])
    @staticmethod
    def back(callback):
        return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text=in_keyboard_texts.back, callback_data=callback)
            ]
        ])
    @staticmethod
    def service(service_id, active):
        return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text=admin_texts.change_subdomain, callback_data=f"change_domain_service_{service_id}")
            ],
            [
                InlineKeyboardButton(text=admin_texts.hide_service(active), callback_data=f"hide_service_{service_id}")
            ],
            [
                InlineKeyboardButton(text=in_keyboard_texts.back, callback_data="admin_services_page_0")
            ]
        ])
    @staticmethod
    def admin_countries(countries):
        print(countries)
        countries_buttons = [
            InlineKeyboardButton(
                text=in_keyboard_texts.AdminServicesCountry(country['flag'], country['name'], country['active']),
                callback_data=f"country_{country['id']}")
            for country in countries
        ]
        # Разбиваем кнопки по рядам (по две кнопки в каждом ряду)
        rows = [countries_buttons[i:i + 2] for i in range(0, len(countries_buttons), 2)]

        rows.append([
            InlineKeyboardButton(text=in_keyboard_texts.menu, callback_data="menu"),
            InlineKeyboardButton(text=in_keyboard_texts.tools, callback_data="tools")
        ])
        # Создаем клавиатуру
        services_country = InlineKeyboardMarkup(inline_keyboard=rows)

        return services_country
    @staticmethod
    def back(id):
        return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text=in_keyboard_texts.back, callback_data=f"log_{id}")
            ]
        ])
    @staticmethod
    def log(_log, link, service, user):
        return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text=log.success, callback_data=f"success_log_{_log['id']}")
            ],
            [
              InlineKeyboardButton(text=log.status(_log['status']), callback_data=f"status_log_{_log['id']}")
            ],
            [
                InlineKeyboardButton(text=log.vbiver(user['nickname']), callback_data=f"vbiver_log_{link['id']}")
            ],
            [
                InlineKeyboardButton(text=log.online, callback_data=f"check_online_{_log['id']}")
            ],
            [
                InlineKeyboardButton(text=log.custom_error, callback_data=f"custom_error_{_log['id']}"),
                InlineKeyboardButton(text=log.custom_text, callback_data=f"custom_text_{_log['id']}")
            ],
            [
                InlineKeyboardButton(text=log.push, callback_data=f"push_log_{_log['id']}"),
                InlineKeyboardButton(text=log.sms, callback_data=f"sms_log_{_log['id']}"),
                InlineKeyboardButton(text=log.accurate, callback_data=f"accurate_log_{_log['id']}")
            ],
            [
                InlineKeyboardButton(text=log.change, callback_data=f"change_log_{_log['id']}"),
                InlineKeyboardButton(text=log.deposit, callback_data=f"deposit_log_{_log['id']}"),
                InlineKeyboardButton(text=log.limits, callback_data=f"limit_log_{_log['id']}")
            ],
            [
                InlineKeyboardButton(text=log.success_hold, callback_data=f"success_hold_log_{_log['id']}"),
                InlineKeyboardButton(text=log.error_hold, callback_data=f"error_hold_log_{_log['id']}")
            ],
            [
                InlineKeyboardButton(text=log.lk, callback_data=f"lk_log_{_log['id']}"),
                InlineKeyboardButton(text=log.pin_code, callback_data=f"pin_code_log_{_log['id']}")
            ],
            [
                InlineKeyboardButton(text=log.app_code,callback_data=f"app_code_log_{_log['id']}"),
                InlineKeyboardButton(text=log.call_code, callback_data=f"call_code_log_{_log['id']}")
            ],
            [
                InlineKeyboardButton(text=log.error_code, callback_data=f"error_code_log_{_log['id']}"),
                InlineKeyboardButton(text=log.error_push, callback_data=f"error_push_log_{_log['id']}")
            ],
            [
                InlineKeyboardButton(text=log.image, callback_data=f"image_log_{_log['id']}"),
            ],
            [
                InlineKeyboardButton(text=log.decline, callback_data=f"decline_log_{_log['id']}")
            ]
        ])