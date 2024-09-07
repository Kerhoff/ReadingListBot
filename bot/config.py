import os
from dotenv import load_dotenv

load_dotenv() # load environment variables from .env file

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")