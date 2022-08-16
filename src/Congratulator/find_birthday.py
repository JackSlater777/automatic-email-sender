import sqlite3
import json
# import os
from datetime import datetime


# Узнаем E-mail'ы именинников
def find_birthday(email_lst, name_lst):
    # Сегодняшний день
    today = datetime.today()
    # Конвертируем дату в нужный формат
    day = today.strftime("%m-%d")  # month-day (str)
    print(f'{day=}')
    # Файл базы данных
    with open("databaseconfig.json") as json_data_file:
        data = json.load(json_data_file)
    # Относительный путь в JSON
    # print(data['mysql']['db'])
    # # Абсолютный путь
    # db_path = os.path.abspath(data['mysql']['db'])
    # Создаем соединение с нашей базой данных через менеджер контекста
    with sqlite3.connect(data['mysql']['db']) as conn:
        cur = conn.cursor()
        # Проходимся по БД с точным запросом по дате, совпадающей с сегодняшним днем
        for row in cur.execute(
                "SELECT E.Id, E.Name, E.Email, E.Birthday"
                " FROM Employees AS E"
                " WHERE Birthday = ?",
                (day,)):
            # Добавляем email и имя в списки
            email_lst.append(row[2])
            name_lst.append(row[1])

    # Возвращаем списки для возможности тестирования
    return email_lst, name_lst


if __name__ == '__main__':
    # Создаем список email'ов именинников
    email_birthday = []
    # Создаем список имен именинников
    name_birthday = []
    # Узнаем E-mail'ы именинников
    find_birthday(email_birthday, name_birthday)
    # Проверяем списки
    print(f'{email_birthday=}')
    print(f'{name_birthday=}')
    # assert email_birthday == ['dualking1991@gmail.com', 'JackSlater777@yandex.ru']
    # assert name_birthday == ['test1', 'test2']
