from telegram import Update
from telegram.ext import ContextTypes

from bot.db import mark_item_completed, filter_by_title
import bot.messages as messages

# Define the complete command handler
async def complete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 1:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Use: /complete <title>")
        return

    title = ' '.join(context.args)
    # Check if the title is in the database
    item = filter_by_title(update.effective_user.id, title)
    if not item:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=messages.ITEM_NOT_FOUND)
    mark_item_completed(user_id=update.effective_user.id, item_id=item.id)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Item '{title}' marked as completed.")
