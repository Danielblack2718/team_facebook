from core.utils.config import ADMIN_ID
from core.functions.database import Database
class Admin:
    @staticmethod
    def get_admins():
        return ADMIN_ID



class User:

    @staticmethod
    def add_user(id, username, refferer):
        connection = Database.connect_to_mysql()
        cursor = connection.cursor()
        if refferer == "0":
            refferer = None
        cursor.execute("INSERT INTO users (id, username, ref, supportChat, nickname) VALUES (%s, %s, %s, %s, %s)", (id, str(username), str(refferer), 1, str(username)))

        Database.commit_and_close(connection)

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
    async def is_user_exists(user_id):
        connection = Database.connect_to_mysql()
        cursor = connection.cursor()
        # Пример SQL-запроса для проверки наличия пользователя
        query = "SELECT * FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))

        # Получение результата
        result = cursor.fetchone()

        Database.close_mysql_connection(connection)

        return bool(result)

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
