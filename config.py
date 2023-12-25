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
BOT_TOKEN = environ.get("BOT_TOKEN", "6253974886:AAGB11jJzxP_uKLCUDKQ9JvFf8qy4rJJq1Q")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1001763943446"))
ADMINS = int(environ.get("ADMINS", "5165943027"))
DB_URI = environ.get("DB_URI", "mongodb+srv://dahif89943:sudipsaha2006@cluster0.iscxsme.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "chatgptvjbot")
OPENAI_API = environ.get("OPENAI_API", "")
AI = is_enabled((environ.get("AI","True")), False)
