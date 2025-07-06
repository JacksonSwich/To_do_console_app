from To_do_console_app.python_code.database.database_request import * # импортируем все функции по запросам CRUD к БД
from To_do_console_app.python_code.database.database_init import disconnect_from_database # импортируем функцию отключение от БД

# прототип
def choose():
    try:
        print("1. Создать задачу\n"
              "2. Посмотреть все задачи\n"
              "3. Выход")
        choice = int(input("Ввод: "))

        match choice:
            case 1:
                task_name = input("Название задачи: ")
                task_date = input("Ведите дату (формат YYYY-MM-DD): ")
                create_task(task_name, task_date)
                choose()
            case 2:
                read_all_task()
                choose()
            case 3:
                disconnect_from_database(connection)
            case default:
                print("Ошибка! Неверное значение!")
                choose()
    except ValueError:
        print("Ошибка! Неверные данные!")
        choose()

choose()