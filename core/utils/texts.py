class texts():
    start="4234234"
    confirm_user = '''🎉Поздравляем, вы были приняты!

Используйте меню выше, что ознакомится с функционалом нашего бота, в случае, если меню пропадёт, просто пропишите /start.'''
    not_confirm_user = "Вы не приняты."
    menu = '''Жизнь коротка, и каждая минута на счету. Посвящая своё время нашему проекту сейчас, вы делаете вложение в будущее. Ваша отдача и усердие в нашем деле приведут к результатам, которые не только оправдают затраченное время, но и принесут плоды, экономя ваше время в долгосрочной перспективе!\n\n🕒График работы проекта: с 08:00 до 00:30 по МСК.'''
    channels = "Чем больше вы изучите, тем больше вы получите!"
    @staticmethod
    def profile(id, nickHide,SmartSupp,  sumProfits, countProfits):
        SmartSupp_text = "🟢"
        if not SmartSupp:
            SmartSupp_text = "🔴"
        nickHide_text = "cкрыт"
        if not nickHide:
            nickHide_text = "открыт"
        return f'''👤 Ваш уникальный ID: `{id}`

🛡Ник: `{nickHide_text}`

🌑 SmartSupp: {SmartSupp_text}

🎩 Сумма профитов: ${sumProfits}
🏦 Количество профитов: {countProfits}

`Помните золотое правило успеха: стремление + упорный труд = финансовое вознаграждение и бесценный опыт!`'''
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
    ad = "🗂Мои обьявления🗂"

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
    def new_user_text(username, identification, friend = None):
        friend_text = ""
        if friend is not None:
            friend_text = f"Друг: {friend}"
        return f"Пришла новая заявка на вступление!\n\ntg: @{username}\nОткуда узнал: {identification}\n{friend_text}"

    add_new_user = "Принять"
    ban_new_user  = "Отклонить"

    @staticmethod
    def confirmed_user(username, admin_username):
        return f"@{admin_username} успешно принял заявку от @{username}"

    @staticmethod
    def not_confirmed_user(username, admin_username):
        return f"@{admin_username} отклонил заявку от @{username}"