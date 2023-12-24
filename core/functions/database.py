from core.utils.config import DatabaseInfo
import mysql.connector
from mysql.connector import Error
class Database:
    @staticmethod
    def connect_to_mysql():
        try:
            connection = mysql.connector.connect(
                host=DatabaseInfo.MYSQL_HOST,
                user=DatabaseInfo.MYSQL_USER,
                password=DatabaseInfo.MYSQL_PASSWORD,
                database=DatabaseInfo.MYSQL_DATABASE
            )
            return connection
        except Error as e:
            print(f"Error: {e}")
            return None

    @staticmethod
    def commit_and_close(connection):
        if connection:
            connection.commit()
            connection.close()

    @staticmethod
    def close_mysql_connection(connection):
        if connection:
            connection.close()