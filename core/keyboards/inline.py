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
    refferals = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=in_keyboard_texts.menu, callback_data="menu"),
            InlineKeyboardButton(text=in_keyboard_texts.tools, callback_data="tools")
        ]

    ])

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
