import pytest
import sqlite3
from tests.configuration import TEST_DB_PATH
from tests.builders.employee import EmployeeBuilder


@pytest.fixture
def build_item_type():
    """Фикстура для строительства объекта в билдере."""
    return EmployeeBuilder()  # Возвращаем объект


@pytest.fixture
def get_sqlite_connect():
    """Фикстура для создания коннекта с тестовым файлом SQLite."""
    connection = sqlite3.connect(TEST_DB_PATH)
    try:
        yield connection  # Отдаем коннект в тест
    finally:
        connection.close()  # Чтобы сессия не зависала в воздухе в случае разрыва соединения во время теста
