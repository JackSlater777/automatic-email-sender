from datetime import datetime


class EmployeeBuilder:
    """Класс-билдер, который генерирует необходимый объект. Использованы классические сеттеры."""
    def __init__(self):
        self.result = {}  # Пустой словарь, который можно декодировать в json
        self.reset()  # Сразу же наполняем объект значениями по умолчанию

    def set_id(self, id=None):
        """Билдим id - None, в базе данных стоит AUTOINCREMENT."""
        self.result['id'] = id
        return self

    def set_name(self, name='Ivan'):
        """Билдим имя."""
        self.result['name'] = name
        return self

    def set_email(self, email='foremailautosend1991@gmail.com'):
        """Билдим почту."""
        self.result['email'] = email
        return self

    def set_birthday(self, birthday=datetime.today().strftime("%d-%m")):
        """Билдим день рождения."""
        self.result['birthday'] = birthday
        return self

    def reset(self):
        """Задаем поля по умолчанию."""
        self.set_id()
        self.set_name()
        self.set_email()
        self.set_birthday()
        return self

    def build(self):
        """Билдим."""
        return self.result


if __name__ == '__main__':
    # Билдим item_type:
    me = EmployeeBuilder().build()
    print(f"{me=}")  # me={'id': None, 'name': 'Ivan', 'email': 'dualking1991@gmail.com', 'birthday': '06-12'}

    # Смотрим поля
    me_keys = [key for key in EmployeeBuilder().build()]
    print(me_keys)  # ['id', 'name', 'email', 'birthday']
