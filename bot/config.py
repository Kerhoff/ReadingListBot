import os

from typing import Optional
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()  # load environment variables from .env file

# TELEGRAM
TELEGRAM_BOT_TOKEN: Optional[str] = os.getenv("TELEGRAM_BOT_TOKEN")

# DATABASE
DATABASE_URL: Optional[str] = os.getenv("DATABASE_URL")
TEST_DATABASE_URL: Optional[str] = os.getenv("TEST_DATABASE_URL")

# LOGGING
LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

# PATHS
BASE_DIR: Path = Path(__file__).resolve().parent

# SQLITE_DB: Path = BASE_DIR / "reading_list.db"
