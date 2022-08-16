import sqlite3
import os


# Конфигурирование базы данных
def configure_db(conn):
    # Создаем курсор - специальный объект, который делает запросы и получает их результаты
    cur = conn.cursor()
    # Делаем CREATE запрос к базе данных, используя обычный SQL-синтаксис
    # Создаем таблицу Employees
    cur.execute('''CREATE TABLE Employees
                   (Id, Name, Email, Birthday)''')
    # Создаем уникальный индекс по полю Birthday
    cur.execute('''CREATE UNIQUE INDEX BirthdayId
                   ON Employees(Birthday)''')


# Добавление записей в таблицу Employees
def insert_employee(conn, id, name, email, birthday):
    # Создаем курсор - специальный объект, который делает запросы и получает их результаты
    cur = conn.cursor()
    # Делаем INSERT запрос к базе данных, используя обычный SQL-синтаксис
    cur.execute("INSERT INTO Employees (Id, Name, Email, Birthday)"
                " VALUES (:id, :name, :email, :birthday)",
                {'id': id, 'name': name, 'email': email, 'birthday': birthday})
    conn.commit()


if __name__ == '__main__':
    # Файл базы данных
    db_name = 'example.db'
    db_exists = os.path.exists(db_name)  # Проверка существования базы данных
    # Создаем соединение с нашей базой данных через менеджер контекста
    # Если файл базы данных еще не создан, он создастся автоматически.
    with sqlite3.connect(db_name) as con:
        # Если базы данных не существует, создаем и заполняем
        if not db_exists:
            # Создаем таблицу
            configure_db(con)
            # Вставляем инфо о сотруднике в таблицу
            employee_id = 1
            employee_name = 'John'
            employee_email = 'example@gmail.com'
            employee_birthday = '01-01'  # Формат строго такой (месяц-день)
            insert_employee(con, employee_id, employee_name, employee_email, employee_birthday)
