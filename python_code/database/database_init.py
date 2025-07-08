import os
import dotenv # библиотека для доступа к .env файлу

import mysql.connector
from mysql.connector import *


# загрузка переменных окружения
env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env") # устанавливаем универсальный путь к файлу .env
if os.path.exists(env_path): # если файл существует
    print("Система: Файл .env существует! \n"
          "Система: Выгружаем переменные окружения...")
    dotenv.load_dotenv(env_path) # выгружаем переменные окружения
else:
    print("Система: Ошибка!!! Файл .env не существует!")


# токен для телеграмм бота
token_for_telebot=os.getenv("token")


def connect_to_database():
    # функция подключения в базе данных
    try:
        connection_to_database = mysql.connector.connect( # создаем подключение и данные берем из файла .env
        host=os.getenv("host"),
        user=os.getenv("user"),
        password=os.getenv("password"),
        database=os.getenv("database")
        )
        print(f"Система: Успешное подключение к базе данных: {os.getenv("database")}!")
    except Error:
        print(Error)
        return None

    return connection_to_database


def disconnect_from_database(connection):
    # функция отключения от базы данных
    connection.close()
    print("Отключение от базы данных")
    return None