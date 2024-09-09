from telegram import Update
from telegram.ext import ContextTypes
import re

from bot.db import add_item, get_items, mark_item_completed, delete_item, filter_by_title
import bot.messages as messages

# Define the start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=messages.GREETINGS)
# Define the help command handler
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=messages.HELP)
# Define the add command handler
async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get the user input
    print("from add function")
    user_input = context.args
    print(user_input)
    if len(user_input) < 1:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=messages.ADD_ITEM_USAGE)
        return

    # Use the last word as the item type
    # And validate the item type
    item_type = user_input[-1].lower()
    print(item_type)
    if item_type not in ['book', 'article', 'post', 'video', 'podcast']:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=messages.INVALID_ITEM_TYPE)
        return

    # Use the first words as the link URL
    # And validate the URL
    link = user_input[0]
    print(link)
    if not re.match(r'^https?://', link):
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=messages.INVALID_URL)
        return

    # Use the middle words as the title
    # Use link as title if title is not provided
    title = ' '.join(user_input[1:-1])
    print(title)
    if not title:
        title = link

    # Add the item to the database
    add_item(user_id=update.effective_user.id, link=link, title=title, item_type=item_type)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=messages.ITEM_ADDED.format(title=title))

# Define the list command handler
async def list_items(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get the items from the database
    items = get_items(user_id=update.effective_user.id)
    if not items:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=messages.LIST_EMPTY)
        return

    # Format the items
    item_list = "\n".join([f"- #{item.item_type} {item.title} {item.link} - {'Completed' if item.completed else 'New'}" for item in items])
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=item_list)

# Define the delete command handler
async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 1:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Usage: /delete <title>")
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

# Define the complete command handler
async def complete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 1:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Usage: /complete <title>")
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

# Define the filter command handler
async def filter_items(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass

# Define the summary command handler
async def summary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass

# Define the clear command handler
async def clear_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass