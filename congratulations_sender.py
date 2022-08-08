import smtplib
import os
from email.mime.text import MIMEText
from pathlib import Path
from dotenv import load_dotenv
from find_birthday import email_birthday
from find_birthday import name_birthday


# Функция отправки поздравления
def send_congratulations(email, names):
    # Загружаем переменные (пароли, пути файлов и т.д.)
    dotenv_path = Path('./setenv.env')
    load_dotenv(dotenv_path=dotenv_path)
    password = os.environ.get('EMAIL_PASSWORD')
    # Вводим почту отправителя
    sender = "foremailautosend1991@gmail.com"
    # Текст сообщения
    for i in range(len(names)):
        message = f"Dear {names[i]}, Happy Birthday! We wish you best of luck in the upcomming year!"
        # Формируем тему письма, отправителя и получателей
        msg = MIMEText(message)
        msg['Subject'] = 'Happy Birthday!'
        msg['From'] = sender
        msg['To'] = email[i]
        print(f'{names[i]=}, {email[i]=}')
        # Создаем сервер на основе gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        # Устанавливаем tls (transport layer security) с сервером
        server.starttls()
        # Логинимся на сервер
        server.login(sender, password)
        # Отправляем письмо
        server.sendmail(sender, email[i], msg.as_string())
        server.quit()  # не нужно, если рассылка идёт по графику


if __name__ == '__main__':
    # Делаем рассылку поздравления
    send_congratulations(email_birthday, name_birthday)
    print('Рассылка поздравлений выполнена')
