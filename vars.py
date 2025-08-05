#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "20619533"))
API_HASH = environ.get("API_HASH", "5893568858a096b7373c1970ba05e296")
BOT_TOKEN = environ.get("BOT_TOKEN", "8146069942:AAHUml7dOsNQg2B0vEDy7-bXWAzc5pugP7A")
OWNER = int(environ.get("OWNER", "7447651332"))
CREDIT = "✿𝐒𝐔𝐉𝐀𝐋✿"

AUTH_USER = os.environ.get('AUTH_USERS', '7447651332').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))

# ➕ MongoDB config (Render env se aayega)
MONGO_URI = environ.get("MONGO_URI", "")
DB_NAME = environ.get("DB_NAME", "Telegrambot")
COLLECTION_NAME = environ.get("COLLECTION_NAME", "Telegrambot")
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
