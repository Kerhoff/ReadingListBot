import logging

from typing import List, Optional
from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)


# Define the clear command handler
async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_chat is None:
        logger.warning("No effective chat found")
        return

    chat_id: int = update.effective_chat.id

    if update.effective_user is None:
        logger.warning("No effective user found")
        return

    user_id: int = update.effective_user.id

    items: List[str] = get_items(user_id)

    for item in items:
        delete_item(item_id=int(item.id))

    await context.bot.send_message(
        chat_id=chat_id, text="All items marked as completed."
    )
