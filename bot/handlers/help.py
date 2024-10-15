import logging

from telegram import Update
from telegram.ext import ContextTypes

import bot.messages as messages


logger = logging.getLogger(__name__)


# Define the help command handler
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_chat is not None:
        chat_id: int = update.effective_chat.id
    else:
        logger.warning("No effective chat found")
        return

    await context.bot.send_message(chat_id=chat_id, text=messages.HELP)
