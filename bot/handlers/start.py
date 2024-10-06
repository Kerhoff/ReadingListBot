from telegram import Update
from telegram.ext import ContextTypes

import bot.messages as messages


# Define the start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=messages.GREETINGS
    )
