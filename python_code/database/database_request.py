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


def read_task_by(choice, key):
    # функция просмотра задачи по номеру или ключевому слову
    cursor = connection.cursor()
    if choice == 1:
        cursor.execute(
            """SELECT id, name, status, date FROM tasks
            WHERE id = %s""",
            [key]
        )
    elif choice == 2:
        cursor.execute(
            f"""SELECT id, name, status, date FROM tasks
            WHERE name LIKE %s""",
            [f"%{key}%"]
        )
    else:
        print("Ошибка!")

    row = cursor.fetchall()
    for word in row:
        print(word)

    cursor.close()
    print("Система: Запрос выполнен!")


def update_task_by(task_id, choice, new_data):
    # функция изменения задачи
    cursor = connection.cursor()
    if choice == 1: # изменение статуса
        cursor.execute(
        """UPDATE tasks SET status = %s WHERE id = %s""",
            (new_data, task_id)
        )
    elif choice == 2: # изменение названия
        cursor.execute(
        """UPDATE tasks SET name = %s WHERE id = %s""",
            (new_data, task_id)
        )
    elif choice == 3: # изменение даты
        cursor.execute(
            """UPDATE tasks SET date = %s WHERE id = %s""",
            (new_data, task_id)
        )
    else:
        print("Ошибка!")

    connection.commit()
    cursor.close()
    print("Система: Запрос выполнен!")


def delete_task(task_id):
    # функция удаления записи в базе данных
    cursor = connection.cursor()
    cursor.execute(  # параметризованный запрос на создание новой задачи
        """DELETE FROM tasks WHERE id = %s""",
        [task_id]
    )
    connection.commit()  # сохраняем изменения в БД
    cursor.close()
    print("Система: Запрос выполнен!")