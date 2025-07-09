from telebot import *

from To_do_console_app.python_code.database.database_request import * # импортируем все функции по запросам CRUD к БД
from To_do_console_app.python_code.database.database_init import disconnect_from_database, token_for_telebot  # импортируем функцию отключение от БД и токен для бота

"""# прототип
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
# main()"""

token = token_for_telebot # сохраняем токен для тг бота
bot = TeleBot(token) # создаем бота

@bot.message_handler(commands=["start","info","help"])
def start_message(message):
    bot.send_message(message.chat.id, "Здравствуйте! Это бот для записи дел на день!\n"
                                      "Для управления задачами введите команду /menu")


@bot.message_handler(commands=["menu"])
def main_menu(message):

    tasks_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    create_task_button = types.KeyboardButton("Создать задачу")
    all_tasks_button = types.KeyboardButton("Посмотреть все задачи")
    find_task_button = types.KeyboardButton("Найти нужную задачу")
    update_task_button = types.KeyboardButton("Изменить существующую задачу")
    delete_task_button = types.KeyboardButton("Удалить задачу")
    exit_button = types.KeyboardButton("Выход")

    tasks_keyboard.add(create_task_button, all_tasks_button, find_task_button, update_task_button, delete_task_button, exit_button)

    bot.send_message(message.chat.id, "Главное меню: ", reply_markup=tasks_keyboard)

# обработчик на нажатие кнопки "Создать задачу"
@bot.message_handler(func = lambda message : message.text == "Создать задачу")
def start_create_handler(message):
    bot.send_message(message.chat.id, "Название задачи: ")
    bot.register_next_step_handler(message, name_handler) # бот ожидает текста от пользователя
def name_handler(message):
    task_name = message.text # сообщение пользователя записывается в переменную
    bot.send_message(message.chat.id, "Ведите дату (формат YYYY-MM-DD): ")
    bot.register_next_step_handler(message, lambda m : date_handler(m, task_name)) # бот ожидает след сообщение
def date_handler(message, task_name):
    task_date = message.text # сообщение пользователя записывается в переменную
    create_task(task_name, task_date) # вызывается функция по из database_request
    bot.send_message(message.chat.id, "Задача создана!")
    main_menu(message)


# обработчик на нажатие кнопки "Посмотреть все задачи"
@bot.message_handler(func = lambda message : message.text == "Посмотреть все задачи")
def bot_read_all_tasks(message):
    table = read_all_task()
    if not table:
        bot.send_message(message.chat.id, "У вас пока нет задач")
    else:
        response = "Ваши задачи: \n\n"
        for task_id, name, status, date in table:
            if status == 0:
                status = "Не выполнено"
            else:
                status = "Выполнено"

            response += f"{task_id}. {name} - {status} ({date}) \n"

        bot.send_message(message.chat.id, response)
        main_menu(message)


# обработчик на нажатие кнопки "Посмотреть все задачи"
@bot.message_handler(func = lambda message : message.text == "Найти нужную задачу")
def find_menu(message):

    find_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    find_number_button = types.KeyboardButton("Номеру задачи")
    find_word_button = types.KeyboardButton("Ключевому слову")
    find_exit_button = types.KeyboardButton("Выход в главное меню")

    find_keyboard.add(find_number_button, find_word_button, find_exit_button)

    bot.send_message(message.chat.id, "Поиск задачи по: ", reply_markup = find_keyboard)


# обработчик на нажатие кнопки "Номеру задачи"
@bot.message_handler(func = lambda message : message.text == "Номеру задачи")
def start_find_by_id(message):
    bot.send_message(message.chat.id,"Введите номер задачи: ")
    bot.register_next_step_handler(message, find_by_id)
def find_by_id(message):
    key_id = int(message.text)
    row = read_task_by("Номеру задачи", key_id)

    if not row:
        bot.send_message(message.chat.id, "Задача не найдена!")
        find_menu(message)
    else:
        task = "Ваша задача: \n\n"
        for task_id, name, status, date in row:
            if status == 0:
                status = "Не выполнено"
            else:
                status = "Выполнено"

            task = f"{task_id}. {name} - {status} ({date}) \n"

        bot.send_message(message.chat.id, task)
        main_menu(message)


# обработчик на нажатие кнопки "Ключевому слову"
@bot.message_handler(func = lambda message : message.text == "Ключевому слову")
def start_find_by_word(message):
    bot.send_message(message.chat.id,"Введите название задачи или ключевое слово: ")
    bot.register_next_step_handler(message, find_by_word)
def find_by_word(message):
    key_word = message.text
    table = read_task_by("Ключевому слову", key_word)

    if not table:
        bot.send_message(message.chat.id, "Задача не найдена!")
        find_menu(message)
    else:
        task = "Совпадения в Ваших задачах: \n\n"
        for task_id, name, status, date in table:
            if status == 0:
                status = "Не выполнено"
            else:
                status = "Выполнено"

            task += f"{task_id}. {name} - {status} ({date}) \n"

        bot.send_message(message.chat.id, task)
        main_menu(message)


# обработчик на нажатие кнопки "Выход в главное меню"
@bot.message_handler(func = lambda message : message.text == "Выход в главное меню")
def exit_from_find(message):
    bot.send_message(message.chat.id, "Переходим в главное меню...")
    main_menu(message)






bot.polling(non_stop = True)