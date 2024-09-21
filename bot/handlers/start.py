from telegram import Update
from telegram.ext import ContextTypes
import re

from bot.db import add_item, get_items, mark_item_completed, delete_item, filter_by_title
import bot.messages as messages

# Define the start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=messages.GREETINGS)
