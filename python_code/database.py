import os
import dotenv # библиотека для доступа к .env файлу

import mysql.connector
from mysql.connector import *


# загрузка переменных окружения
env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env") # устанавливаем универсальный путь к файлу .env
if os.path.exists(env_path): # если файл существует
    print("Файл существует! "
          "Выгружаем переменные окружения...")
    dotenv.load_dotenv(env_path) # выгружаем переменные окружения
else:
    print("Ошибка!!! Файл .env не существует!")


def connect_to_database():
    # функция подключения в базе данных
    try:
        connection_to_database = mysql.connector.connect( # создаем подключение и данные берем из файла .env
        host=os.getenv("host"),
        user=os.getenv("user"),
        password=os.getenv("password"),
        database=os.getenv("database")
        )
        print(f"Успешное подключение к базе данных: {os.getenv("database")}!")
        return connection_to_database
    except Error:
        print(Error)
        return None


# теперь CRUD надо описать в этом файле в отдельных функциях.
# log 04.07.2025: подключение к бд работает, запросы выполняются

connection = connect_to_database() # будет в main

#########################################################
cursor = connection.cursor()
cursor.execute(
    """INSERT INTO tasks(name, date)
    VALUES ('ТЕст по русски', '2025-07-04')"""        # тест
)
connection.commit()
print("Запрос выполнен!")
#########################################################

cursor.close() # будет в main
connection.close() # будет в main
