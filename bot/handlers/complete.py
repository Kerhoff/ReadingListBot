import logging

from typing import List, Optional
from telegram import Update
from telegram.ext import ContextTypes

from bot.db.db import get_item_by_title, mark_item_completed
import bot.messages as messages


logger = logging.getLogger(__name__)


# Define the complete command handler
async def complete(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args: List[str] = context.args or []

    if update.effective_chat is None:
        logger.error("Chat ID not found")
        return

    chat_id: int = update.effective_chat.id

    if update.effective_user is None:
        logger.error("User ID not found")
        return

    user_id: int = update.effective_user.id

    if len(args) < 1:
        await context.bot.send_message(chat_id=chat_id, text="Use: /complete <title>")
        return

    title: str = " ".join(args)

    # Check if the title is in the database
    try:
        item: Optional[object] = get_item_by_title(user_id, title)
    except Exception as e:
        logger.error(f"Error getting item by title: {e}")
        return

    if item is not None:
        try:
            mark_item_completed(user_id, item.id)
            await context.bot.send_message(
                chat_id=chat_id,
                text=f"Item '{item.title}' marked as completed.",
            )
        except Exception as e:
            logger.error(f"Error mark item as completed: {e}")
            return
    else:
        await context.bot.send_message(chat_id=chat_id, text=messages.ITEM_NOT_FOUND)
