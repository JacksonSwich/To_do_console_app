import os
import dotenv # библиотека для доступа к .env файлу

import mysql.connector
from mysql.connector import *


# загрузка переменных окружения
env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env") # устанавливаем универсальный путь к файлу .env
if os.path.exists(env_path): # если файл существует
    print("Система: Файл .env существует! \n"
          "Система: Выгружаем переменные окружения...")
    dotenv.load_dotenv(env_path) # выгружаем переменные окружения
else:
    print("Система: Ошибка!!! Файл .env не существует!")


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
        return connection_to_database
    except Error:
        print(Error)
        return None

# теперь CRUD надо описать в этом файле в отдельных функциях.
# log 04.07.2025: подключение к бд работает, запросы выполняются

def create_task(name, data):
    # функция создания записи в базе данных
    connection = connect_to_database() # данная функция вызывает функцию подключения к БД
    cursor = connection.cursor()
    cursor.execute( # параметризованный запрос на создание новой задачи
        """INSERT INTO tasks(name, date)
        VALUES (%s, %s)""",
        (name, data)
    )
    connection.commit() # сохраняем изменения в БД
    print("Система: Запрос выполнен!")
    cursor.close()
    connection.close()

def read_all_task():
    # функция просмотра всех задач в базе данных
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute(
        """SELECT * FROM tasks"""
    )

    table = cursor.fetchall()
    for row in table:
        print(row)

    print("Система: Запрос выполнен!")
    cursor.close()
    connection.close()