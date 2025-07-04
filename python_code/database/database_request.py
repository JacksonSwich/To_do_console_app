from To_do_console_app.python_code.database.database_init import *

# Теперь CRUD надо описать в этом файле в отдельных функциях.

connection = connect_to_database()  # данная функция вызывает функцию подключения к БД
cursor = connection.cursor()

def create_task(name, data):
    # функция создания записи в базе данных
    cursor.execute( # параметризованный запрос на создание новой задачи
        """INSERT INTO tasks(name, date)
        VALUES (%s, %s)""",
        (name, data)
    )
    connection.commit() # сохраняем изменения в БД
    print("Система: Запрос выполнен!")


def read_all_task():
    # функция просмотра всех задач в базе данных
    cursor.execute(
        """SELECT * FROM tasks"""
    )

    table = cursor.fetchall()
    for row in table:
        print(row)

    print("Система: Запрос выполнен!")


cursor.close()
connection.close()