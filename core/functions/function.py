from core.utils.config import ADMIN_ID
from core.functions.database import Database
class Admin:
    @staticmethod
    def get_admins():
        return ADMIN_ID

    @staticmethod
    def get_admin_menu():
        connection = Database.connect_to_mysql()
        cursor = connection.cursor()

        try:
            cursor.execute("SELECT COUNT(*) FROM users")
            users_count = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM services")
            services_count = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM profits")
            profits_count = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM links")
            links_count = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM requests")
            requests_count = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM requests WHERE status = 'wait'")
            requests_wait_count = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM requests WHERE status = 'accepted'")
            requests_accepted_count = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM requests WHERE status = 'error'")
            request_error_count = cursor.fetchone()[0]

            cursor.execute("SELECT SUM(amount) FROM profits WHERE status = 'decide'")
            sum_non_paid = cursor.fetchone()[0]

            cursor.execute("SELECT SUM(amount) FROM profits WHERE status = 'success'")
            sum_paid = cursor.fetchone()[0]

            cursor.execute("SELECT percent_worker FROM settings WHERE id = 1")
            percent = cursor.fetchone()

            # Возвращаем массив с данными
            return {
                "users": users_count,
                "services": services_count,
                "profits": profits_count,
                "links": links_count,
                "requests": requests_count,
                "requests_wait": requests_wait_count,
                "requests_accepted": requests_accepted_count,
                "request_error": request_error_count,
                "sum_non_paid": sum_non_paid,
                "sum_paid": sum_paid,
                "percent": percent
            }
        finally:
            Database.close_mysql_connection(connection)


class User:

    @staticmethod
    def add_user(id, username, refferer):
        try:
            connection = Database.connect_to_mysql()
            cursor = connection.cursor()
            if refferer == "0":
                refferer = None
            cursor.execute("INSERT INTO users (id, username, ref, supportChat, nickname) VALUES (%s, %s, %s, %s, %s)", (id, str(username), str(refferer), 1, str(username)))

            Database.commit_and_close(connection)
            return True
        except:
            return False
    @staticmethod
    def find_user(user_id):
        connection = Database.connect_to_mysql()
        cursor = connection.cursor(dictionary=True)
        # Пример SQL-запроса для проверки наличия пользователя
        query = "SELECT * FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))

        # Получение результата
        result = cursor.fetchone()

        Database.close_mysql_connection(connection)

        return result

    @staticmethod
    def change_status_nickname_status(id):
        connection = Database.connect_to_mysql()
        cursor = connection.cursor(dictionary=True)

        # Assuming `hide` is a column in the `user` table
        query = "UPDATE users SET hide = NOT hide WHERE id = %s"
        cursor.execute(query, (id,))

        cursor.execute("SELECT hide FROM users WHERE id = %s", (id,))
        updated_user = cursor.fetchone()

        Database.commit_and_close(connection)

        return updated_user['hide'] if updated_user else None

    @staticmethod
    def change_nickname(id, nickname):
        if len(nickname) > 10:
            return "error"
        connection = Database.connect_to_mysql()
        cursor = connection.cursor(dictionary=True)
        try:
            # Assuming `hide` is a column in the `user` table
            query = "UPDATE users SET nickname = %s WHERE id = %s"
            cursor.execute(query, (nickname, id))

            # Check the number of affected rows
            if cursor.rowcount > 0:
                cursor.execute("SELECT nickname FROM users WHERE id = %s", (id,))
                updated_user = cursor.fetchone()

                Database.commit_and_close(connection)

                return updated_user['nickname'] if updated_user else None
            else:
                Database.commit_and_close(connection)
                return "error"
        except:
            return "error"
    @staticmethod
    def change_smartsupp(id, key):
        if len(key) > 10:
            return "error"
        connection = Database.connect_to_mysql()
        cursor = connection.cursor(dictionary=True)
        try:
            # Assuming `hide` is a column in the `user` table
            query = "UPDATE users SET supportChatApi = %s WHERE id = %s"
            cursor.execute(query, (key, id))

            # Check the number of affected rows
            if cursor.rowcount > 0:
                cursor.execute("SELECT supportChatApi FROM users WHERE id = %s", (id,))
                updated_user = cursor.fetchone()

                Database.commit_and_close(connection)

                return updated_user['supportChatApi'] if updated_user else None
            else:
                Database.commit_and_close(connection)
                return "error"
        except:
            return "error"
    @staticmethod
    def is_user_exists(user_id):
        connection = Database.connect_to_mysql()
        cursor = connection.cursor()
        # Пример SQL-запроса для проверки наличия пользователя
        query = "SELECT * FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))

        # Получение результата
        result = cursor.fetchone()

        Database.close_mysql_connection(connection)

        return bool(result)

    @staticmethod
    def get_all_users():
        connection = Database.connect_to_mysql()
        cursor = connection.cursor(dictionary=True)

        try:
            # Выбираем всех пользователей из таблицы users
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()

            return users
        except Exception as e:
            # Обработка ошибок, например, логирование
            print(f"Ошибка при получении пользователей: {e}")
        finally:
            # Всегда закрываем соединение
            Database.commit_and_close(connection)
class Country:
    @staticmethod
    def get_all_countries():
        connection = Database.connect_to_mysql()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM countries WHERE active = %s", (True,))
        result = cursor.fetchall()
        if len(result) == 0:
            Database.close_mysql_connection(connection)
            print(False)
            return False
        print(result)
        Database.close_mysql_connection(connection)
        return result

class Service:
    @staticmethod
    def get_services_in_country(country):
        connection = Database.connect_to_mysql()
        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT services.id,services.name, services.active, services.country_id, countries.id AS country_id, countries.name AS country_name, countries.flag AS country_flag, countries.active AS country_active
        FROM services
        JOIN countries ON services.country_id = countries.id
        WHERE services.active = 1 AND services.country_id = %s
        """

        cursor.execute(query, (country,))
        result = cursor.fetchall()

        if len(result) == 0:
            Database.close_mysql_connection(connection)
            print(False)
            return False

        for row in result:
            print(row)
            row['country'] = {'id': row['country_id'], 'name': row['country_name'], 'flag': row['country_flag'], 'country_active':row['country_active']}
            del row['country_id']  # Убираем избыточный столбец
            del row['country_flag']
            del row['country_name']
            del row['country_active']
        print(result)
        Database.close_mysql_connection(connection)
        return result


class Link:

    @staticmethod
    def create_link(data):
        connection = Database.connect_to_mysql()
        cursor = connection.cursor(dictionary=True)

        name = data['name']
        user_id = data['id']
        price = data['price']
        service_id = data['service']
        description = data['description']
        checker = 0
        photo = data['photo']
        address = data['address']
        author = data['author']
        number  = data['number']


        cursor.execute("INSERT INTO links (name, price, service, description, checker, photo, address, author, number, user) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (name, price, service_id, description, checker, photo, address, author, number, user_id))

        cursor.execute("SELECT * FROM links WHERE id = LAST_INSERT_ID()")

        # Извлекаем данные
        created_link_data = cursor.fetchone()

        # Подтверждаем транзакцию и закрываем соединение
        Database.commit_and_close(connection)

        # Возвращаем данные созданной записи
        return created_link_data

    @staticmethod
    def change_checker(id):
        connection = Database.connect_to_mysql()
        cursor = connection.cursor(dictionary=True)

        # Предположим, что у вас есть таблица links и поле checker, которое вы хотите обновить
        update_query = "UPDATE links SET checker = NOT checker WHERE id = %s"
        cursor.execute(update_query, (id,))

        # Подтверждаем транзакцию и закрываем соединение
        Database.commit_and_close(connection)

        return True

    @staticmethod
    def change_price(id, price):
        connection = Database.connect_to_mysql()
        cursor = connection.cursor(dictionary=True)

        try:
            # Предположим, что у вас есть таблица links и поле checker, которое вы хотите обновить
            update_query = "UPDATE links SET price = %s WHERE id = %s"
            cursor.execute(update_query, (price, id))

            # Подтверждаем транзакцию и закрываем соединение
            Database.commit_and_close(connection)

            return True
        except Exception as e:
            print(f"Error: {e}")
            Database.close_mysql_connection(connection)
            return False

    @staticmethod
    def get_links_in_user(user_id):
        connection = Database.connect_to_mysql()
        cursor = connection.cursor(dictionary=True)

        try:
            # Предположим, что у вас есть таблица links и поле user_id, которое связывает ссылки с пользователями
            print(user_id)
            select_query = "SELECT * FROM links WHERE user = %s"
            cursor.execute(select_query, (user_id,))

            result = cursor.fetchall()

            Database.close_mysql_connection(connection)
            return result
        except Exception as e:
            print(f"Error: {e}")
            Database.close_mysql_connection(connection)
            return False

    @staticmethod
    def delete_link(id):
        connection = Database.connect_to_mysql()
        cursor = connection.cursor(dictionary=True)

        try:
            name_query = "SELECT name FROM links WHERE id = %s"
            cursor.execute(name_query, (id,))
            result = cursor.fetchone()
            # Предположим, что у вас есть таблица links и вы хотите удалить запись с указанным id
            delete_query = "DELETE FROM links WHERE id = %s"
            cursor.execute(delete_query, (id,))

            # Подтверждаем транзакцию и закрываем соединение
            Database.commit_and_close(connection)

            return result
        except Exception as e:
            print(f"Error: {e}")
            Database.close_mysql_connection(connection)
            return False
    @staticmethod
    def find_link(id):
        connection = Database.connect_to_mysql()
        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT links.*, services.id AS service_id, services.name AS service_name, services.country_id AS service_country, services.active AS service_active,
             countries.id AS countries_id, countries.name AS countries_name, countries.flag AS countries_flag, countries.active AS countries_active
            FROM links
            JOIN services ON links.service = services.id
            JOIN countries ON services.country_id = countries.id
            WHERE links.id = %s
        """

        cursor.execute(query, (id,))
        result = cursor.fetchall()
        print(result)
        Database.close_mysql_connection(connection)

        if len(result) == 0:
            return False

        for row in result:
            row['service'] = {
                'id': row['service_id'],
                'name': row['service_name'],
                'country_id': row['service_country'],
                'active': row['service_active']
                # Добавьте остальные поля, если нужно
            }
            row['country'] = {
                'id': row['countries_id'],
                'name': row['countries_name'],
                'flag': row['countries_flag'],
                'active': row['countries_active']
                # Добавьте остальные поля, если нужно
            }
            del row['service_id']
            del row['service_name']
            del row['service_country']
            del row['service_active']
            del row['countries_id']
            del row['countries_name']
            del row['countries_flag']
            del row['countries_active']

        print(result)
        return result[0]

class Request:
    @staticmethod
    def create_request(username, id, type, text = None):
        connection = Database.connect_to_mysql()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("INSERT INTO requests (type, textType, username, user_id, status) VALUES (%s, %s, %s, %s, %s)", (type, text, username, id, "wait"))

        Database.commit_and_close(connection)

    @staticmethod
    def change_status(user_id, new_status):
        connection = Database.connect_to_mysql()
        cursor = connection.cursor(dictionary=True)

        # Найдем последнюю запись с заданным user_id
        cursor.execute("SELECT * FROM requests WHERE user_id = %s ORDER BY created_at DESC LIMIT 1", (user_id,))
        latest_request = cursor.fetchone()

        if latest_request:
            # Изменяем статус
            cursor.execute("UPDATE requests SET status = %s WHERE id = %s", (new_status, latest_request['id']))

            # Завершаем транзакцию и закрываем соединение
            Database.commit_and_close(connection)
