# Don't Remove Credit Tg - @Ashiqi_091
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Ashiqi_091
# Ask Doubt on telegram @BABATILLU

from os import environ

API_ID = int(environ.get("API_ID", "22182189"))
API_HASH = environ.get("API_HASH", "5e7c4088f8e23d0ab61e29ae11960bf5")
BOT_TOKEN = environ.get("BOT_TOKEN", "")


OWNER = int(environ.get("OWNER", "5302639580"))
CREDIT = environ.get("CREDIT", "𓍯ANKIT⚝")

TOTAL_USER = os.environ.get('TOTAL_USERS', '5302639580').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '5302639580, 7887627618').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
