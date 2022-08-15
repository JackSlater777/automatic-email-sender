import sqlite3
from datetime import datetime


# Узнаем E-mail'ы именинников
def find_birthday(d, email_lst, name_lst):
    # Файл базы данных
    db_name = "BirthdaysDB.db"
    # Создаем соединение с нашей базой данных
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    # Проходимся по БД
    for row in cur.execute('SELECT * FROM Employees'):
        # Если день и месяц совпадают, добавляем email и имя в списки
        if row[3].find(d) != -1:
            email_lst.append(row[2])
            name_lst.append(row[1])
    # Не забываем закрыть соединение с базой данных после работы
    conn.close()
    return email_lst, name_lst


# Сегодняшний день
today = datetime.today()
# Конвертируем дату в нужный формат
day = today.strftime("-%m-%d")  # -month-day (str)
print(f'{day=}')
# Создаем список email'ов именинников
email_birthday = []
# Создаем список имен именинников
name_birthday = []
# Узнаем E-mail'ы именинников
find_birthday(day, email_birthday, name_birthday)
print(f'{email_birthday=}')
print(f'{name_birthday=}')
