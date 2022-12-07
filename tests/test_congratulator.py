import os
import pytest
from src.find_birthday import find_birthday
from src.congratulations_sender import configure_congratulations, send_congratulations
from email.mime.text import MIMEText
from tests.configuration import TEST_DB_PATH
from tests.builders.sqlite import configure_db, insert_employee, find_the_highest_id, select_all_employees, \
    update_name, delete_employee


class TestMockDbSQLite:
    """Тестируем mock-базу данных SQLite через DB-API."""
    def test_create_employees_table(self, get_sqlite_connect):
        """Проверяем создание базы данных."""
        configure_db(get_sqlite_connect)  # Передаем коннект в метод создания таблицы
        assert os.path.exists(TEST_DB_PATH)

    def test_build_and_insert_employee(self, get_sqlite_connect, build_item_type):
        """Проверяем добавление данных."""
        item = build_item_type.build()  # Строим объект
        insert_employee(get_sqlite_connect, item)  # Добавляем объект в базу
        print(item)  # id остался None - недостаток DB-API

    def test_select_all_items(self, get_sqlite_connect):
        """Проверяем чтение всех данных."""
        print(select_all_employees(get_sqlite_connect))

    def test_update_name(self, get_sqlite_connect):
        """Проверяем обновление данных."""
        item = {'id': 1, 'name': 'Robert'}  # Указываем обновленный объект, который должен быть
        update_name(get_sqlite_connect, item)  # Заменяем значение по id

    @pytest.mark.skip
    def test_delete_item(self, get_sqlite_connect):
        """Проверяем удаление данных с кастомным фильтром."""
        item = {'id': 1}  # Указываем объект
        delete_employee(get_sqlite_connect, item)  # Удаляем объект из базы

    def test_find_max_id(self, get_sqlite_connect):
        """Проверяем максимальный id."""
        print(find_the_highest_id(get_sqlite_connect)[0])  # max id

    def test_build_insert_and_delete_item(self, get_sqlite_connect, build_item_type):
        """Пример идеального flow - создаём, добавляем и удаляем объект в базе,
        тем самым оставляя тест чистым."""
        item = build_item_type.build()  # Строим объект
        insert_employee(get_sqlite_connect, item)  # Добавляем объект в базу
        print(item)  # Смотрим id и имя, но в базе их уже не будет
        item_id = find_the_highest_id(get_sqlite_connect)[0]  # Находим id добавленного объекта
        item = {'id': item_id}  # Указываем объект
        delete_employee(get_sqlite_connect, item)  # Удаляем объект из базы


class TestFindBirthday:
    """Тестируем нахождение дня рождения в тестовой базе данных."""
    def test_find_birthday(self, get_sqlite_connect):
        """Находим E-mail'ы именинников."""
        print(find_birthday(get_sqlite_connect))


class TestConfigureCongratulations:
    """Тестируем сетап поздравления."""
    def test_type_congratulations(self):
        """Тестируем тип возвращаемых данных."""
        mock_email = "my_email@gmail.com"
        mock_name = "my name"
        assert type(configure_congratulations(mock_email, mock_name)) == MIMEText
        assert configure_congratulations(mock_email, mock_name)['To'] == mock_email


class TestSendCongratulations:
    """Тестируем отправку поздравления."""
    def test_send_congratulations(self):
        """Написать mock в конфтесте."""
        # d = {'foremailautosend1991@gmail.com': 'Ivan'}
        # send_congratulations(d)
        pass


class TestDeleteMockDbSQLite:
    """Тестируем удаление mock-базы данных SQLite."""
    def test_delete_db(self):
        os.remove(TEST_DB_PATH)
        with pytest.raises(AssertionError):
            assert os.path.exists(TEST_DB_PATH)


if __name__ == '__main__':
    pytest.main()
