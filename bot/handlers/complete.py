from telegram import Update
from telegram.ext import ContextTypes
import logging

from bot.db import get_item_by_title, mark_item_completed, filter_by_title
import bot.messages as messages


logger = logging.getLogger(__name__)


# Define the complete command handler
async def complete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 1:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="Use: /complete <title>"
        )
        return

    user_id = update.effective_user.id
    logger.degub(f"User ID: {user_id}")

    title = " ".join(context.args)
    logging.debug(f"Title: {title}")

    # Check if the title is in the database
    item = get_item_by_title(user_id, title)
    logging.debug(f"Item: {item}")

    if not item:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text=messages.ITEM_NOT_FOUND
        )
    mark_item_completed(user_id, item.id)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Item '{item.title}' marked as completed.",
    )
