import sqlite3


# Конфигурирование базы данных
def configure_db(conn):
    # Создаем курсор - специальный объект, который делает запросы и получает их результаты
    cur = conn.cursor()
    # Делаем CREATE запрос к базе данных, используя обычный SQL-синтаксис
    # Создаем таблицу Employees
    # cur.execute("CREATE TABLE Employees"
    #             "    (Id        INTEGER    PRIMARY KEY  AUTOINCREMENT,"
    #             "     Name      CHAR(128)  NOT NULL,"
    #             "     Email     CHAR(128)  NOT NULL,"
    #             "     Birthday  CHAR(128)  NOT NULL,")
    cur.execute('''CREATE TABLE Employees
                   (Id, Name, Email, Birthday)''')


# Добавление записей в таблицу Employees
def insert_employee(conn, id, name, email, birthday):
    # Создаем курсор - специальный объект, который делает запросы и получает их результаты
    cur = conn.cursor()
    # Делаем INSERT запрос к базе данных, используя обычный SQL-синтаксис
    cur.execute("INSERT INTO Employees (Id, Name, Email, Birthday)"
                " VALUES (:id, :name, :email, :birthday)",
                {'id': id, 'name': name, 'email': email, 'birthday': birthday})
    conn.commit()


# Файл базы данных
db_name = 'example.db'
# Создаем соединение с нашей базой данных
# Если файл базы данных еще не создан, он создастся автоматически.
con = sqlite3.connect(db_name)
# Создаем таблицу
configure_db(con)
# Вставляем инфо о сотруднике в таблицу
employee_id = 1
employee_name = 'John'
employee_email = 'example@gmail.com'
employee_birthday = '1991-01-01'  # Формат строго такой (год-месяц-день)
insert_employee(con, employee_id, employee_name, employee_email, employee_birthday)
# Не забываем закрыть соединение с базой данных после работы
con.close()
