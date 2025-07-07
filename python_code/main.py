from To_do_console_app.python_code.database.database_request import * # импортируем все функции по запросам CRUD к БД
from To_do_console_app.python_code.database.database_init import disconnect_from_database # импортируем функцию отключение от БД

# прототип
def main():
    try:
        print("1. Создать задачу\n"
              "2. Посмотреть все задачи\n"
              "3. Найти нужную задачу\n"
              "4. Выход")
        choice = int(input("Ввод: "))

        match choice:
            case 1:
                task_name = input("Название задачи: ")
                task_date = input("Ведите дату (формат YYYY-MM-DD): ")
                create_task(task_name, task_date)
                main()
            case 2:
                read_all_task()
                main()
            case 3:
                choice_for_function = int(input("Поиск по: \n1. Номеру задачи \n2. Ключевому слову \n3. Выход в главное меню \nВвод: "))
                if choice_for_function == 1:
                    key = int(input("Введите номер задачи: "))
                    read_task_by_id(key)
                    main()
                elif choice_for_function == 2:
                    key = input("Введите название задачи: ")
                    read_task_by_name(key)
                    main()
                elif choice_for_function == 3:
                    main()
                else:
                    print("Ошибка! Неверное значение")
                    main()
            case 4:
                disconnect_from_database(connection)
            case default:
                print("Ошибка! Неверное значение!")
                main()
    except ValueError:
        print("Ошибка! Неверные данные!")
        main()

main()