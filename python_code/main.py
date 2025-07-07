from To_do_console_app.python_code.database.database_request import * # импортируем все функции по запросам CRUD к БД
from To_do_console_app.python_code.database.database_init import disconnect_from_database # импортируем функцию отключение от БД

# прототип
def main():
    try:
        print("1. Создать задачу\n"
              "2. Посмотреть все задачи\n"
              "3. Найти нужную задачу\n"
              "4. Изменить существующую задачу\n"
              "5. Удалить задачу\n"
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
                    key_id = int(input("Введите номер задачи: "))
                    read_task_by(choice_for_function, key_id)
                    main()
                elif choice_for_function == 2: # найти по ключевому слову
                    key_word = input("Введите название задачи или ключевое слово: ")
                    read_task_by(choice_for_function, key_word)
                    main()
                elif choice_for_function == 3: # выход в главное меню
                    main()
                else: # ошибка
                    print("Ошибка! Неверное значение")
                    main()

            case 4: # изменение существующей задачи
                task_id = int(input("Введите номер задачи: "))
                choice_for_function = int(input("Изменить: \n1. Статус задачи(выполнено/не выполнено) \n2. Название \n3. Дату \n4. Выход в главное меню \nВвод: "))
                if choice_for_function == 1: # изменение статуса задачи
                    status = int(input("Введите статус: \n1. Выполнено \n2. Не выполнено \n3. Выход в главное меню \nВвод: "))
                    if status == 1: # выполнена
                        update_task_by(task_id, choice_for_function, status)
                        main()
                    elif status == 2: # не выполнена
                        status = 0
                        update_task_by(task_id, choice_for_function, status)
                        main()
                    elif status == 3: # выход
                        main()
                    else: # ошибка
                        print("Ошибка! Неверное значение")
                        main()
                elif choice_for_function == 2: # изменение названия
                    name_task = input("Введите новое название задачи: ")
                    update_task_by(task_id, choice_for_function, name_task)
                    main()
                elif choice_for_function == 3: # изменение даты
                    date_task = input("Введите новую дату (YYYY-MM-DD): ")
                    update_task_by(task_id, choice_for_function, date_task)
                    main()
                elif choice_for_function == 4: # выход в главное меню
                    main()
                else: # ошибка
                    print("Ошибка! Неверное значение")
                    main()

            case 5: # удаление задачи
                id_delete_task = int(input("Введите номер задачи для УДАЛЕНИЯ: "))
                delete_task(id_delete_task)
                main()

            case 6: # отключиться от БД
                disconnect_from_database(connection)

            case default: # дефолтный кейс
                print("Ошибка! Неверное значение!")
                main()

    except ValueError:
        print("Ошибка! Неверные данные!")
        main()


# глобальная программа
main()