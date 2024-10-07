from telegram import Update
from telegram.ext import ContextTypes
import logging

from bot.db import get_items
import bot.messages as messages


logger = logging.getLogger(__name__)


# Define the list command handler
async def list_items(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Print message text
    logger.debug(f"Received command: {update.message.text}")

    # Print the user ID
    logger.debug(f"User ID: {update.effective_user.id}")

    # Get the items from the database
    items = get_items(user_id=update.effective_user.id)
    if not items:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text=messages.LIST_EMPTY
        )
        return

    # Format the items
    item_list = "\n".join(
        [
            f"""- <i>Title:</i> <a href="{item.link}">{item.title}</a>\
            \n<i>Status:</i> <b>{'Completed' if item.completed else 'New'}</b>\
            \n<i>Type:</i> #{item.item_type}\n"""
            for item in items
        ]
    )
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        parse_mode="HTML",
        text=item_list,
    )
