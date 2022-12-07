import os
from definitions import ROOT_DIR
from dotenv import load_dotenv


DB_RELATIVE_PATH = 'db.db'
DB_PATH = os.path.join(ROOT_DIR, DB_RELATIVE_PATH)

ENV_RELATIVE_PATH = 'setenv.env'
ENV_PATH = os.path.join(ROOT_DIR, ENV_RELATIVE_PATH)

load_dotenv(dotenv_path=ENV_PATH)

if os.path.exists(ENV_PATH):
    # Пароль приложения в почте
    password = os.environ.get('APP_EMAIL_PASSWORD')
    # Email отправителя
    sender = os.environ.get('SENDER')
else:
    print(f"No such file {ENV_PATH}")
