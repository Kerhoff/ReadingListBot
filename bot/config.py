import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env file

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

BASE_DIR = Path(__file__).resolve().parent
SQLITE_DB = BASE_DIR / "reading_list.db"
