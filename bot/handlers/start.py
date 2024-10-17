import logging

from typing import Optional
from telegram import Update
from telegram.ext import ContextTypes

from bot.db import add_user, get_user
import bot.messages as messages


logger = logging.getLogger(__name__)


# Define the start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_user is not None:
        tg_user_id: int = update.effective_user.id
        tg_username: str = update.effective_user.username
        logger.debug(f"User ID: {tg_user_id}, Username: {tg_username}")
    else:
        logger.error("User not found")
        return

    # Check User in the database and add if not found
    user: Optional[object] = get_user(tg_user_id=tg_user_id)
    logger.debug(f"User: {user}")
    if user is None:
        user = add_user(tg_user_id=tg_user_id, tg_username=tg_username)
        logger.debug(f"User: {user}")
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=messages.GREETINGS
    )
