import logging

from typing import List, Optional
from telegram import Update
from telegram.ext import ContextTypes

from bot.db import ReadingItem, get_items
import bot.messages as messages


logger = logging.getLogger(__name__)


# Define the list command handler
async def list_items(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_user is not None:
        user_id: int = update.effective_user.id
    else:
        logger.warning("No effective user found")
        return

    if update.effective_chat is not None:
        chat_id: int = update.effective_chat.id
    else:
        logger.warning("No effective chat found")
        return

    # Get the items from the database
    try:
        items: Optional[List[ReadingItem]] = get_items(user_id)
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
            chat_id=chat_id,
            parse_mode="HTML",
            text=item_list,
        )
    except Exception as e:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text=messages.LIST_EMPTY
        )
        logger.error(f"Error getting items: {e}")
        return
