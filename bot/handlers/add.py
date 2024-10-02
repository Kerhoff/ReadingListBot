from telegram import Update
from telegram.ext import ContextTypes
import re

from bot.db import add_item
import bot.messages as messages

# Define the add command handler
async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get the user input
    user_input = context.args
    if len(user_input) < 1:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=messages.ADD_ITEM_USAGE)
        return

    # Use the last word as the item type
    # And validate the item type
    item_type = user_input[-1].lower()
    if item_type not in ['book', 'article', 'post', 'video', 'podcast']:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=messages.INVALID_ITEM_TYPE)
        return

    # Use the first words as the link URL
    # And validate the URL
    link = user_input[0]
    if not re.match(r'^https?://', link):
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=messages.INVALID_URL)
        return

    # Use the middle words as the title
    # Use link as title if title is not provided
    title = ' '.join(user_input[1:-1])
    if not title:
        title = link

    # Add the item to the database
    add_item(user_id=update.effective_user.id, link=link, title=title, item_type=item_type)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=messages.ITEM_ADDED.format(title=title))
