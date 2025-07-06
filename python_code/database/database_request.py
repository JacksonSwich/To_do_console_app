from To_do_console_app.python_code.database.database_init import connect_to_database # импортируем функцию подключение к БД

# Теперь CRUD надо описать в этом файле в отдельных функциях.

connection = connect_to_database()  # данная функция вызывает функцию подключения к БД

def create_task(name, data):
    # функция создания записи в базе данных
    cursor = connection.cursor()
    cursor.execute( # параметризованный запрос на создание новой задачи
        """INSERT INTO tasks(name, date)
        VALUES (%s, %s)""",
        (name, data)
    )
    connection.commit() # сохраняем изменения в БД
    cursor.close()
    print("Система: Запрос выполнен!")


def read_all_task():
    # функция просмотра всех задач в базе данных
    cursor = connection.cursor()
    cursor.execute(
        """SELECT * FROM tasks"""
    )
    table = cursor.fetchall()
    for row in table:
        print(row)

    cursor.close()
    print("Система: Запрос выполнен!")


