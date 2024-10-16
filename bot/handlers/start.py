import logging

from telegram import Update
from telegram.ext import ContextTypes

from bot.db import add_user
import bot.messages as messages


logger = logging.getLogger(__name__)


# Define the start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_user is not None:
        user = update.effective_user
        tg_user_id: int = user.id
        tg_username: str = user.username
    else:
        logger.error("User not found")
        return

    # Add the user to the database
    add_user(tg_user_id=tg_user_id, tg_username=tg_username)
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=messages.GREETINGS
    )
