import smtplib
import os
from email.mime.text import MIMEText
from pathlib import Path
from dotenv import load_dotenv
from find_birthday import find_birthday


# Функция отправки поздравления
def send_congratulations(email, names):
    # Загружаем переменные (пароли, пути файлов и т.д.)
    dotenv_path = Path('./setenv.env')
    load_dotenv(dotenv_path=dotenv_path)
    password = os.environ.get('EMAIL_PASSWORD')
    # Вводим почту отправителя
    sender = "foremailautosend1991@gmail.com"
    # Создаем сервер на основе gmail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # Предусмотриваем отлов исключений при любых взаимодействиях с сервером
    try:
        # Устанавливаем tls (transport layer security) с сервером
        server.starttls()
        # Логинимся на сервер
        server.login(sender, password)
        # Для каждого элемента списка имён
        for i in range(len(names)):
            # Текст сообщения
            message = f"Dear {names[i]}, Happy Birthday! We wish you best of luck in the upcomming year!"
            # Формируем тему письма, отправителя и получателей
            msg = MIMEText(message)
            msg['Subject'] = 'Happy Birthday!'
            msg['From'] = sender
            msg['To'] = email[i]
            print(f'{names[i]=}, {email[i]=}')
            # # Отправляем письмо
            server.sendmail(sender, email[i], msg.as_string())
    # Обязательно закрываем подключение к серверу, что бы ни произошло
    finally:
        server.quit()


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
    # Делаем рассылку поздравления
    send_congratulations(email_birthday, name_birthday)
    print('Рассылка поздравлений выполнена')
