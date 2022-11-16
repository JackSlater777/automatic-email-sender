import os
from pathlib import Path
from dotenv import load_dotenv

# Указываем путь к переменным окружения
dotenv_path = Path('./setenv.env')
# Альтернатива - без использования Path
# dotenv_path = os.path.join(os.path.dirname(__file__), 'setenv.env')
load_dotenv(dotenv_path=dotenv_path)

if os.path.exists(dotenv_path):
    # Пароль приложения в почте
    password = os.environ.get('APP_EMAIL_PASSWORD')
    # Email отправителя
    sender = os.environ.get('SENDER')
else:
    print(f"No such file {dotenv_path}")
