from telegram import Update
from telegram.ext import ContextTypes

from bot.db import get_items
import bot.messages as messages


# Define the list command handler
async def list_items(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get the items from the database
    items = get_items(user_id=update.effective_user.id)
    if not items:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text=messages.LIST_EMPTY
        )
        return

    # Format the items
    item_list = "\n".join(
        [
            f"""\
            {item.id}. Status: {'Completed' if item.completed else 'New'}\n\
                Type: #{item.item_type}.\n\
                Title: [{item.title}]({item.link})"
            """
            for item in items
        ]
    )
    await context.bot.send_message(
        chat_id=update.effective_chat.id, parse_mode="MarkdownV2", text=item_list
    )
