import logging

from typing import List, Optional
from telegram import Update
from telegram.ext import ContextTypes

from bot.db import delete_item, get_item_by_title
import bot.messages as messages

logger = logging.getLogger(__name__)


# Define the delete command handler
async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args: List[str] = context.args or []

    if update.effective_chat is not None:
        chat_id: int = update.effective_chat.id
    else:
        logger.warning("No effective chat found")
        return

    if update.effective_user is not None:
        user_id: int = update.effective_user.id
    else:
        logger.warning("No effective user found")
        return

    if len(args) < 1:
        await context.bot.send_message(chat_id=chat_id, text="Use: /delete <title>")
        return

    title: str = " ".join(args)

    try:
        # Check if the title is in the database
        item: Optional[object] = get_item_by_title(user_id, title)
    except Exception as e:
        logger.error(f"Error getting item by title: {e}")
        return

    if item is not None:
        try:
            delete_item(user_id=user_id, item_id=item.id)
            await context.bot.send_message(chat_id=chat_id, text=messages.ITEM_DELETED)
        except Exception as e:
            logger.error(f"Error deleting item: {e}")
            return
    else:
        await context.bot.send_message(chat_id=chat_id, text=messages.ITEM_NOT_FOUND)
