from telegram import Update
from telegram.ext import ContextTypes

from bot.db import delete_item, filter_by_title
import bot.messages as messages

# Define the delete command handler
async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 1:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Use: /delete <title>")
        return

    title = ' '.join(context.args)
    # Check if the title is in the database
    item = filter_by_title(update.effective_user.id, title)
    if not item:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=messages.ITEM_NOT_FOUND)
    delete_item(user_id=update.effective_user.id, item_id=item.id)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=ITEM_DELETED)
