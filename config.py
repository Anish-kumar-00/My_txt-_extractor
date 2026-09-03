from os import getenv

API_ID = int(getenv("API_ID", "34677259"))
API_HASH = getenv("API_HASH", "f149c400ef1ee7662fcd6e74d6529d5b")
BOT_TOKEN = getenv("BOT_TOKEN", "8922703959:AAFtLcR2M1IsyHjvqzwVAuT2ksGM58jOZtc")
OWNER_ID = int(getenv("OWNER_ID", "5968883359"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5968883359").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://<db_username>:3DGoh7sYhfdKCwcx@extractordb.cu1uofn.mongodb.net/?appName=ExtractorDB")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1003881333048"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1003881333048"))
