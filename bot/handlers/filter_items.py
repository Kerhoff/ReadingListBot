import logging

from typing import List, Optional
from telegram import Update
from telegram.ext import ContextTypes

from bot.db import get_item_by_title, mark_item_completed
import bot.messages as messages


logger = logging.getLogger(__name__)


# Define the filter command handler
async def filter_items(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass
