from os import getenv

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(raise_error_if_not_found=True))

TOKEN = getenv('TELEGRAM_TOKEN')
ADMIN_ID = getenv('ADMIN_ID')
