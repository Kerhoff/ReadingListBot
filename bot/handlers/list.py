import logging

from typing import List, Optional
from telegram import Update
from telegram.ext import ContextTypes

from bot.db import ReadingItem, get_items
import bot.messages as messages


logger = logging.getLogger(__name__)


# Define the list command handler
async def list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_user is None:
        logger.error("No effective user found")
        return

    user_id: int = update.effective_user.id

    if update.effective_chat is None:
        logger.warning("No effective chat found")
        return

    chat_id: int = update.effective_chat.id

    # Get the items from the database
    items: List[ReadingItem] = get_items(user_id)
    # Format the items
    if len(items) == 0:
        await context.bot.send_message(
            chat_id=chat_id, parse_mode="HTML", text=messages.LIST_EMPTY
        )
        return

    item_list = "\n".join(
        [
            # f"""- <i>Title:</i> <a href="{item.link}">{item.title}</a>\
            # \n<i>Status:</i> <b>{'Completed' if item.completed else 'New'}</b>\
            # \n<i>Type:</i> #{item.item_type}\n"""
            messages.LIST_ITEMS.format(
                link=item.link,
                title=item.title,
                status="Completed" if item.completed else "New",
                item_type=item.item_type,
            )
            for item in items
        ]
    )
    await context.bot.send_message(
        chat_id=chat_id,
        parse_mode="HTML",
        text=item_list,
    )
