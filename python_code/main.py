from To_do_console_app.python_code.database.database_request import *

task_name = input("Название задачи: ")
task_date = input("Ведите дату (формат YYYY-MM-DD): ")

create_task(task_name, task_date)

read_all_task()