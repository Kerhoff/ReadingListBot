from telegram import Update
from telegram.ext import ContextTypes

import bot.messages as messages


# Define the help command handler
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=messages.HELP)
