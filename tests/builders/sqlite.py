def configure_db(connect):
    """Создание базы данных."""
    cur = connect.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Employees
                (id       INTEGER   PRIMARY KEY   AUTOINCREMENT, 
                name      TEXT      NOT NULL, 
                email     TEXT      NOT NULL, 
                birthday  TEXT      NOT NULL)''')


def insert_employee(connect, item: dict):
    """Добавление записи."""
    cur = connect.cursor()
    cur.execute(
        '''INSERT INTO Employees
        VALUES (?, ?, ?, ?)''',
        list(item.values())
    )
    connect.commit()


def find_the_highest_id(connect):
    """Установление самого большого id."""
    cur = connect.cursor()
    cur.execute(
        '''SELECT id FROM Employees
        ORDER BY id DESC'''
    )
    return cur.fetchone()


def select_all_employees(connect):
    """Чтение всех записей."""
    cur = connect.cursor()
    cur.execute(
        '''SELECT * FROM Employees'''
    )
    return cur.fetchall()


def update_name(connect, item: dict):
    """Обновление записи."""
    cur = connect.cursor()
    cur.execute(
        '''UPDATE Employees
        SET name = :new_name
        WHERE id = :id''',
        {'id': item['id'], 'new_name': item['name']}
    )
    connect.commit()


def delete_employee(connect, item: dict):
    """Удаление записи."""
    cur = connect.cursor()
    cur.execute(
        '''DELETE FROM Employees
        WHERE id = :id''',
        {'id': item['id']}
    )
    connect.commit()
