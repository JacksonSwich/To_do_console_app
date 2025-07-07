from To_do_console_app.python_code.database.database_request import * # импортируем все функции по запросам CRUD к БД
from To_do_console_app.python_code.database.database_init import disconnect_from_database # импортируем функцию отключение от БД

# прототип
def main():
    try:
        print("1. Создать задачу\n"
              "2. Посмотреть все задачи\n"
              "3. Найти нужную задачу\n"
              "4. Изменить существующую задачу\n"
              "5. Удалить задачу"
              "6. Выход")
        choice = int(input("Ввод: "))

        match choice:
            case 1: # создать задачу
                task_name = input("Название задачи: ")
                task_date = input("Ведите дату (формат YYYY-MM-DD): ")
                create_task(task_name, task_date)
                main()
            case 2: # посмотреть все задачи
                read_all_task()
                main()
            case 3: # найти нужную задачу
                choice_for_function = int(input("Поиск по: \n1. Номеру задачи \n2. Ключевому слову \n3. Выход в главное меню \nВвод: "))
                if choice_for_function == 1: # найти по номеру
                    key = int(input("Введите номер задачи: "))
                    read_task_by_id(key)
                    main()
                elif choice_for_function == 2: # найти по ключевому слову
                    key = input("Введите название задачи: ")
                    read_task_by_name(key)
                    main()
                elif choice_for_function == 3: # выход в главное меню
                    main()
                else: # ошибка
                    print("Ошибка! Неверное значение")
                    main()
            case 4: # изменение существующей задачи
                choice_for_function = int(input("Изменить: \n1. Статус задачи(выполнено/не выполнено) \n2. Название \n3. Дату \n4. Выход в главное меню \nВвод: "))
                if choice_for_function == 1: # изменение статуса задачи
                    changes = int(input("Введите статус: \n1. Выполнена \n2. Не выполнена \n3. Выход в главное меню \nВвод: "))
                    # вызов функции
                    main()
                elif choice_for_function == 2: # изменение названия
                    name_task = input("Введите новое название задачи: ")

                    main()
                elif choice_for_function == 3: # изменение даты
                    date_task = input("Введите новую дату: ")

                    main()
                elif choice_for_function == 4: # выход в главное меню
                    main()
                else: # ошибка
                    print("Ошибка! Неверное значение")
                    main()
            case 5: # удаление задачи
                delete_task = int(input("Введите номер задачи для УДАЛЕНИЯ: "))
            case 6: # отключиться от БД
                disconnect_from_database(connection)
            case default: # ошибка
                print("Ошибка! Неверное значение!")
                main()
    except ValueError:
        print("Ошибка! Неверные данные!")
        main()

main()