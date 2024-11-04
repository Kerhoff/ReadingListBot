import logging

from typing import Optional
from telegram import Update
from telegram.ext import ContextTypes

from bot.db.db import add_user, get_user
import bot.messages as messages


logger = logging.getLogger(__name__)


# Define the start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_user is None:
        logger.error("User not found")
        return

    tg_user_id: int = update.effective_user.id
    tg_username: str = update.effective_user.username

    # Check User in the database and add if not found
    user: Optional[object] = get_user(tg_user_id=tg_user_id)
    if user is None:
        add_user(tg_user_id=tg_user_id, tg_username=tg_username)
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=messages.GREETINGS
    )
