# Settings for ORM
from dotenv import load_dotenv
import dotenv

load_dotenv(".env")

BOT_TOKEN = dotenv.get_key('.env', 'BOTTOKEN')

DATABASE = {
    'ENGINE': 'postgresql',
    'NAME': 'test_db',
    'USER': 'postgres',
    'PASSWORD': 'root',
    'HOST': 'localhost',
    'PORT': '5432',
}

LOCALES = ['en', 'fa']

ADMIN_USERNAME = dotenv.get_key('.env', 'DEFAULT_ADMIN_USERNAME').split(',')
ADMIN_TGID = map(int, dotenv.get_key('.env', 'DEFAULT_ADMIN_TGID').split(','))