import logging
import re

from typing import List
from telegram import Update
from telegram.ext import ContextTypes

from bot.db import add_item
import bot.messages as messages


logger = logging.getLogger(__name__)


# Define the add command handler
async def add(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_chat is not None:
        chat_id: int = update.effective_chat.id
    else:
        logger.error("Chat ID not found")
        return

    if update.effective_user is not None:
        user_id: int = update.effective_user.id
    else:
        logger.error("User ID not found")
        return

    # Get the user input
    user_input: List[str] = context.args or []
    if len(user_input) < 1:
        await context.bot.send_message(chat_id=chat_id, text=messages.ADD_ITEM_USAGE)
        return

    # Use the last word as the item type
    # And validate the item type
    item_type: str = user_input[-1].lower()
    if item_type not in ["book", "article", "post", "video", "podcast"]:
        await context.bot.send_message(chat_id=chat_id, text=messages.INVALID_ITEM_TYPE)
        return

    # Use the first words as the link URL
    # And validate the URL
    link: str = user_input[0]
    if not re.match(r"^https?://", link):
        await context.bot.send_message(chat_id=chat_id, text=messages.INVALID_URL)
        return

    # Use the middle words as the title
    # Use link as title if title is not provided
    title: str = " ".join(user_input[1:-1])
    if not title:
        title = link

    # Add the item to the database
    add_item(user_id=user_id, link=link, title=title, item_type=item_type)
    await context.bot.send_message(
        chat_id=chat_id, text=messages.ITEM_ADDED.format(title=title)
    )
