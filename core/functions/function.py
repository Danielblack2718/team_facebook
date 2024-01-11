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
    def change_mentor(user_id):
        try:
            connection = Database.connect_to_mysql()
            cursor = connection.cursor(dictionary=True)

            cursor.execute("UPDATE users SET mentor = NOT mentor WHERE id = %s", (int(user_id),))

            print(cursor.rowcount)
            if cursor.rowcount == 0:
                Database.commit_and_close(connection)
                print(False)
                return False
            Database.commit_and_close(connection)
            return True
        except:
            return False


    @staticmethod
    def add_user(id, username, refferer):
        try:
            connection = Database.connect_to_mysql()
            cursor = connection.cursor()
            if refferer == "0" and refferer == "":
                refferer = None
            cursor.execute("INSERT INTO users (id, username, ref, supportChat, nickname, status) VALUES (%s, %s, %s, %s, %s, %s)", (id, str(username), str(refferer), 1, str(username), str("worker")))

            Database.commit_and_close(connection)
            return True
        except:
            return False
    @staticmethod
    def find_user(user_id):
        try:
            print(user_id)
            connection = Database.connect_to_mysql()
            cursor = connection.cursor(dictionary=True)
            # Пример SQL-запроса для проверки наличия пользователя
            query = "SELECT * FROM users WHERE id = %s"
            cursor.execute(query, (user_id,))


            # Получение результата
            result = cursor.fetchone()

            links = len(Link.get_links_in_user(user_id))
            result['links_count'] = links

            cursor.execute("SELECT COUNT(*), SUM(amount) FROM profits WHERE user_id = %s AND status = %s", (user_id, "success"))
            profits_data = cursor.fetchone()

            result['profits_count'] = profits_data['COUNT(*)'] if profits_data else 0
            result['profits_sum'] = profits_data['SUM(amount)'] if profits_data else 0

            cursor.execute("SELECT * FROM requests WHERE user_id = %s ORDER BY id DESC LIMIT 1", (user_id,))
            latest_request = cursor.fetchone()
            result['request_id'] = latest_request['id'] if latest_request else 0
            result['request_status'] = latest_request['status'] if latest_request else 0

            Database.close_mysql_connection(connection)

            return result
        except:
            return False
    @staticmethod
    def change_status_nickname_status(id):
        try:
            connection = Database.connect_to_mysql()
            cursor = connection.cursor(dictionary=True)

            # Assuming `hide` is a column in the `user` table
            query = "UPDATE users SET hide = NOT hide WHERE id = %s"
            cursor.execute(query, (id,))

            cursor.execute("SELECT hide FROM users WHERE id = %s", (id,))
            updated_user = cursor.fetchone()

            Database.commit_and_close(connection)

            return updated_user['hide'] if updated_user else None
        except:
            return False

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
        try:
            connection = Database.connect_to_mysql()
            cursor = connection.cursor()
            # Пример SQL-запроса для проверки наличия пользователя
            query = "SELECT * FROM users WHERE id = %s"
            cursor.execute(query, (user_id,))

            # Получение результата
            result = cursor.fetchone()

            Database.close_mysql_connection(connection)

            return bool(result)
        except:
            return False

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
    def get_all_active_countries():
        try:
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
        except:
            return False

    @staticmethod
    def get_all_countries():
        try:
            connection = Database.connect_to_mysql()
            cursor = connection.cursor(dictionary=True)

            cursor.execute("SELECT * FROM countries")
            result = cursor.fetchall()
            if len(result) == 0:
                Database.close_mysql_connection(connection)
                print(False)
                return False
            print(result)
            Database.close_mysql_connection(connection)
            return result
        except:
            return False
    @staticmethod
    def find_country(id):
        try:
            connection = Database.connect_to_mysql()
            cursor = connection.cursor(dictionary=True)

            cursor.execute("SELECT * FROM countries WHERE id = %s", (id,))
            result = cursor.fetchall()
            if len(result) == 0:
                Database.close_mysql_connection(connection)
                print(False)
                return False
            print(result)
            Database.close_mysql_connection(connection)
            return result
        except:
            return False


    @staticmethod
    def change_active(country):
        try:
            connection = Database.connect_to_mysql()
            cursor = connection.cursor(dictionary=True)

            cursor.execute("UPDATE countries SET active = NOT active WHERE id = %s", (int(country),))

            print(cursor.rowcount)
            if cursor.rowcount == 0:
                Database.commit_and_close(connection)
                print(False)
                return False
            Database.commit_and_close(connection)
            return True
        except:
            return False
class Service:
    @staticmethod
    def get_services_in_country(country):
        try:
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
        except:
            return False


    @staticmethod
    def get_all_services():
        connection = Database.connect_to_mysql()
        cursor = connection.cursor(dictionary=True)

        try:
            select_query = "SELECT * FROM services"
            cursor.execute(select_query)

            result = cursor.fetchall()

            Database.close_mysql_connection(connection)
            return result
        except Exception as e:
            print(f"Error: {e}")
            Database.close_mysql_connection(connection)
            return False

    @staticmethod
    def find_service(id):
        connection = Database.connect_to_mysql()
        cursor = connection.cursor(dictionary=True)


        select_query = "SELECT * FROM services WHERE id = %s"
        cursor.execute(select_query, (id,))

        result = cursor.fetchall()

        Database.close_mysql_connection(connection)
        return result


    @staticmethod
    def change_subdomain(service, domain):
        try:
            connection = Database.connect_to_mysql()
            cursor = connection.cursor(dictionary=True)

            cursor.execute("UPDATE services SET subdomain = %s WHERE id = %s", (domain, int(service),))

            print(cursor.rowcount)
            if cursor.rowcount == 0:
                Database.commit_and_close(connection)
                print(False)
                return False
            Database.commit_and_close(connection)
            return True
        except:
            return False
    @staticmethod
    def change_active(service):
        try:
            connection = Database.connect_to_mysql()
            cursor = connection.cursor(dictionary=True)

            cursor.execute("UPDATE services SET active = NOT active WHERE id = %s", (int(service),))

            print(cursor.rowcount)
            if cursor.rowcount == 0:
                Database.commit_and_close(connection)
                print(False)
                return False
            Database.commit_and_close(connection)
            return True
        except:
            return False
class Settings:
    @staticmethod
    def get_settings():
        connection = Database.connect_to_mysql()
        cursor = connection.cursor(dictionary=True)

        try:
            select_query = "SELECT * FROM settings WHERE id = 1"
            cursor.execute(select_query)

            result = cursor.fetchall()

            Database.close_mysql_connection(connection)
            return result
        except Exception as e:
            print(f"Error: {e}")
            Database.close_mysql_connection(connection)
            return False

    @staticmethod
    def change_domain(domain):
        try:
            connection = Database.connect_to_mysql()
            cursor = connection.cursor(dictionary=True)

            # Предположим, что у вас есть таблица links и поле checker, которое вы хотите обновить
            update_query = "UPDATE settings SET domain = %s WHERE id = 1"
            cursor.execute(update_query, (domain,))

            # Подтверждаем транзакцию и закрываем соединение
            Database.commit_and_close(connection)

            return True
        except:
            return False
    @staticmethod
    def change_percent(percent):
        try:
            connection = Database.connect_to_mysql()
            cursor = connection.cursor(dictionary=True)

            # Предположим, что у вас есть таблица links и поле checker, которое вы хотите обновить
            update_query = "UPDATE settings SET percent_worker = %s WHERE id = 1"
            cursor.execute(update_query, (percent,))

            # Подтверждаем транзакцию и закрываем соединение
            Database.commit_and_close(connection)
            return True
        except:
            return False
class Link:

    @staticmethod
    def create_link(data):
        try:
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
        except:
            return False

    @staticmethod
    def change_checker(id):
        try:
            connection = Database.connect_to_mysql()
            cursor = connection.cursor(dictionary=True)

            # Предположим, что у вас есть таблица links и поле checker, которое вы хотите обновить
            update_query = "UPDATE links SET checker = NOT checker WHERE id = %s"
            cursor.execute(update_query, (id,))

            # Подтверждаем транзакцию и закрываем соединение
            Database.commit_and_close(connection)

            return True
        except:
            return False

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
        try:
            connection = Database.connect_to_mysql()
            cursor = connection.cursor(dictionary=True)

            query = """
                SELECT links.*, services.id AS service_id, services.name AS service_name, services.country_id AS service_country, services.active AS service_active,
                 countries.id AS countries_id, countries.name AS countries_name, countries.flag AS countries_flag, countries.active AS countries_active, countries.code AS countries_code
                FROM links
                JOIN services ON links.service = services.id
                JOIN countries ON services.country_id = countries.id
                WHERE links.id = %s
            """

            cursor.execute(query, (id,))
            result = cursor.fetchall()
            print(result)
            Database.close_mysql_connection(connection)
            print(len(result))
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
                    'active': row['countries_active'],
                    'code': row['countries_code']
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
        except:
            return False
    @staticmethod
    def get_links_at_service(service_id):
        connection = Database.connect_to_mysql()
        cursor = connection.cursor(dictionary=True)

        try:
            select_query = "SELECT * FROM links WHERE service = %s"
            cursor.execute(select_query, (service_id,))

            result = cursor.fetchall()

            Database.close_mysql_connection(connection)
            return result
        except Exception as e:
            print(f"Error: {e}")
            Database.close_mysql_connection(connection)
            return False

class Request:
    @staticmethod
    def create_request(username, id, type, message_id, text = None):
        try:
            connection = Database.connect_to_mysql()
            cursor = connection.cursor(dictionary=True)

            cursor.execute("INSERT INTO requests (type, textType, username, user_id, status, message_id) VALUES (%s, %s, %s, %s, %s, %s)", (type, text, username, id, "wait", message_id))

            Database.commit_and_close(connection)
        except:
            return False
    @staticmethod
    def change_status(user_id, new_status):
        try:
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
        except:
            return False
    @staticmethod
    def get_all_requests():
        connection = Database.connect_to_mysql()
        cursor = connection.cursor(dictionary=True)

        try:
            select_query = "SELECT * FROM requests"
            cursor.execute(select_query)

            result = cursor.fetchall()

            Database.close_mysql_connection(connection)
            return result
        except Exception as e:
            print(f"Error: {e}")
            Database.close_mysql_connection(connection)
            return False

    @staticmethod
    def find_request(id):
        connection = Database.connect_to_mysql()
        cursor = connection.cursor(dictionary=True)

        try:
            select_query = "SELECT * FROM requests WHERE id = %s"
            cursor.execute(select_query, (id,))

            result = cursor.fetchall()

            Database.close_mysql_connection(connection)
            return result
        except Exception as e:
            print(f"Error: {e}")
            Database.close_mysql_connection(connection)
            return False

    @staticmethod
    def find_request_at_user(user_id):
        connection = Database.connect_to_mysql()
        cursor = connection.cursor(dictionary=True)

        try:
            select_query = "SELECT * FROM requests WHERE user_id = %s ORDER BY id DESC LIMIT 1"
            cursor.execute(select_query, (user_id,))

            result = cursor.fetchone()
            print(result)
            Database.close_mysql_connection(connection)
            return result
        except Exception as e:
            print(f"Error: {e}")
            Database.close_mysql_connection(connection)
            return False
class Profits:
    @staticmethod
    def get_profits_in_user(user_id):
        connection = Database.connect_to_mysql()
        cursor = connection.cursor(dictionary=True)

        try:
            # Предположим, что у вас есть таблица links и поле user_id, которое связывает ссылки с пользователями
            print(user_id)
            select_query = "SELECT * FROM profits WHERE user_id = %s"
            cursor.execute(select_query, (user_id,))

            result = cursor.fetchall()

            Database.close_mysql_connection(connection)
            return result
        except Exception as e:
            print(f"Error: {e}")
            Database.close_mysql_connection(connection)
            return False

    @staticmethod
    def get_all_profits():
        connection = Database.connect_to_mysql()
        cursor = connection.cursor(dictionary=True)

        try:
            select_query = "SELECT * FROM profits"
            cursor.execute(select_query)

            result = cursor.fetchall()

            Database.close_mysql_connection(connection)
            return result
        except Exception as e:
            print(f"Error: {e}")
            Database.close_mysql_connection(connection)
            return False

class Logs:
    @staticmethod
    def change_online(id):
        try:
            connection = Database.connect_to_mysql()
            cursor = connection.cursor(dictionary=True)
            print(id)
            # Предположим, что у вас есть таблица links и поле checker, которое вы хотите обновить
            update_query = "UPDATE logs SET check_online = NOT check_online WHERE id = %s"
            cursor.execute(update_query, (id,))

            # Подтверждаем транзакцию и закрываем соединение
            Database.commit_and_close(connection)

            return True
        except:
            return False

    @staticmethod
    def check_online(id):
        connection = Database.connect_to_mysql()
        cursor = connection.cursor(dictionary=True)


        select_query = "SELECT check_online FROM logs WHERE id = %s"
        cursor.execute(select_query, (id,))

        result = cursor.fetchone()
        Database.close_mysql_connection(connection)
        print(result)
        if result['check_online'] == True:
            return True
        else:
            return False

    @staticmethod
    def find_log(id):
        try:
            connection = Database.connect_to_mysql()
            cursor = connection.cursor(dictionary=True)

            select_query = "SELECT * FROM logs WHERE id = %s"
            cursor.execute(select_query, (id,))

            result = cursor.fetchone()
            Database.close_mysql_connection(connection)

            return result
        except:
            return False

    @staticmethod
    def change_custom_text(id,text):
        try:
            connection = Database.connect_to_mysql()
            cursor = connection.cursor(dictionary=True)

            # Предположим, что у вас есть таблица links и поле checker, которое вы хотите обновить
            update_query = "UPDATE logs SET custom_text = %s WHERE id = %s"
            cursor.execute(update_query, (text,id,))

            # Подтверждаем транзакцию и закрываем соединение
            Database.commit_and_close(connection)

            return True
        except:
            return False
    @staticmethod
    def change_status(id, status):
        try:
            connection = Database.connect_to_mysql()
            cursor = connection.cursor(dictionary=True)

            # Предположим, что у вас есть таблица links и поле checker, которое вы хотите обновить
            update_query = "UPDATE logs SET status = %s WHERE id = %s"
            cursor.execute(update_query, (status, id))

            # Подтверждаем транзакцию и закрываем соединение
            Database.commit_and_close(connection)

            return True
        except:
            return False
    @staticmethod
    def change_vbiver(id, admin_id):
        try:
            connection = Database.connect_to_mysql()
            cursor = connection.cursor(dictionary=True)
            print(id)

            update_query = "UPDATE logs SET admin_id = %s WHERE id = %s"
            cursor.execute(update_query, (admin_id,id))

            # Подтверждаем транзакцию и закрываем соединение
            Database.commit_and_close(connection)

            return True
        except:
            return False