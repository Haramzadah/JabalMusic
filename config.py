from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
ARQ_API_KEY = getenv("ARQ_API_KEY", "QFOTZM-GSZUFY-CHGHRX-TDEHOZ-ARQ")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Update_Grouppp")
OWNER = getenv("OWNER", "zaenmad")
STICKER_ID = getenv(
    "STICKER_ID",
    "CAACAgUAAxkBAAFF-Bdg-i8JvMgppo9DCVkFV9pPVSprzgACdwIAAsgM0VdqqiQQ6Hdw7CAE",
)
BOT_IMAGE = getenv("BOT_IMAGE", "https://telegra.ph/file/d3a5e5665caabdcf0317d.jpg")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ . , - : ; !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
