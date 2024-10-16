import os

from typing import Optional
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()  # load environment variables from .env file

TELEGRAM_BOT_TOKEN: Optional[str] = os.getenv("TELEGRAM_BOT_TOKEN")
LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

BASE_DIR: Path = Path(__file__).resolve().parent
SQLITE_DB: Path = BASE_DIR / "reading_list.db"
