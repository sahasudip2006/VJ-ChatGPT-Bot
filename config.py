import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "29849415"))
API_HASH = environ.get("API_HASH", "0dd6c10897b85d7f10a8dcdeb74f8b8a")
BOT_TOKEN = environ.get("BOT_TOKEN", "6686609357:AAGRm-baQcSH3wbIHo-aE-7xoxRcLEzGvi8")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1001763943446"))
ADMINS = int(environ.get("ADMINS", "5165943027"))
DB_URI = environ.get("DB_URI", "mongodb+srv://Hacker:sudipsaha2006@cluster0.mcdrruk.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "Hacker")
OPENAI_API = environ.get("OPENAI_API", "")
AI = is_enabled((environ.get("AI","True")), False)
