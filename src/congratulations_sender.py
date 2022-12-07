import smtplib
from email.mime.text import MIMEText
from src.find_birthday import find_birthday, get_db_connection
from configuration import sender, password, DB_PATH


def configure_congratulations(email, name) -> MIMEText:
    """Функция для установки параметров поздравления."""
    message = f"Dear {name}, Happy Birthday! We wish you all the very best for the coming year!"  # Текст сообщения
    msg = MIMEText(message)  # Формируем тему письма, отправителя и получателей
    msg['Subject'] = 'Happy Birthday!'  # Тема сообщения
    msg['From'] = sender  # Отправитель
    msg['To'] = email  # Получатель
    return msg


def send_congratulations(birthdays: dict) -> None:
    """Функция отправки поздравления."""
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Устанавливаем tls (transport layer security) с сервером
        server.login(sender, password)  # Логинимся на сервер
        for email, name in birthdays.items():  # Проходимся по словарю с именинниками
            server.sendmail(sender, email, configure_congratulations(email, name).as_string())  # Отправляем письмо


if __name__ == '__main__':
    send_congratulations(find_birthday(get_db_connection(DB_PATH)))
