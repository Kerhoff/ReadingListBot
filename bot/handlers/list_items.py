from telegram import Update
from telegram.ext import ContextTypes
import re

from bot.db import add_item, get_items, mark_item_completed, delete_item, filter_by_title
import bot.messages as messages

# Define the list command handler
async def list_items(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get the items from the database
    items = get_items(user_id=update.effective_user.id)
    if not items:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=messages.LIST_EMPTY)
        return

    # Format the items
    item_list = "\n".join([f"{item.id}. type: #{item.item_type} - {'Completed' if item.completed else 'New'}\n  title: {item.title}\n  link: {item.link}\n" for item in items])
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=item_list)
