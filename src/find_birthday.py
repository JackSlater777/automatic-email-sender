import sqlite3
from datetime import datetime


def get_db_connection(path):
    """Функция для создания коннекта с файлом SQLite."""
    with sqlite3.connect(path) as conn:
        return conn


def find_birthday(connect) -> dict:
    """Находим E-mail'ы именинников."""
    birthdays = {}  # Задаем словарь под E-mail'ы и имена именинников
    day = datetime.today().strftime("%d-%m")  # Сегодняшний день - day-month (str)
    cur = connect.cursor()  # Проходимся по БД с точным запросом по дате, совпадающей с сегодняшним днем
    for row in cur.execute(
            '''SELECT E.id, E.name, E.email, E.birthday
            FROM Employees AS E
            WHERE Birthday = ?''',
            (day,)):
        birthdays[row[2]] = row[1]  # Добавляем email и имя в словарь

    return birthdays  # Возвращаем словарь с именинниками
