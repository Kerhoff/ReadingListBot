import logging

from typing import List
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from bot.db import ReadingItem, delete_item, get_items
import bot.messages as messages

logger = logging.getLogger(__name__)


# Define the delete command handler
async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_chat is None:
        logger.warning("No effective chat found")
        return

    if update.effective_user is None:
        logger.warning("No effective user found")
        return

    args: List[str] = context.args or []
    chat_id: int = update.effective_chat.id
    user_id: int = update.effective_user.id

    if len(args) < 1:
        await context.bot.send_message(
            chat_id=chat_id, text="Use: /delete <item number>"
        )
        return

    try:
        item_number: int = int(args[0])
        print(item_number)
    except ValueError:
        await context.bot.send_message(chat_id=chat_id, text="Invalid item number")
        return

    items: List[ReadingItem] = get_items(user_id=user_id)
    print(items)
    if item_number < 1 or item_number > len(items):
        await context.bot.send_message(chat_id=chat_id, text="Invalid item number")
        return

    # Get the item to delete
    item_to_delete: ReadingItem = items[item_number - 1]
    print(item_to_delete)
    item_id: int = item_to_delete.id

    # Create the confirmation keyboard
    keyboard = [
        [
            InlineKeyboardButton(
                "Yes",
                callback_data=f"delete_confirm:{item_id}",
            ),
            InlineKeyboardButton(
                "No",
                callback_data="delete_cancel",
            ),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Ask for confirmation
    await context.bot.send_message(
        chat_id=chat_id,
        text=messages.ITEM_DELETE_CONFIRM.format(
            item_number=item_number, title=item_to_delete.title
        ),
        reply_markup=reply_markup,
    )

    # Delete the item
    # try:
    #     delete_item(item_id=int(item_to_delete.id))
    #     await context.bot.send_message(
    #         chat_id=chat_id,
    #         text=messages.ITEM_DELETED.format(
    #             item_number=item_number, title=item_to_delete.title
    #         ),
    #     )
    # except Exception as e:
    #     logger.error(f"Error deleting item: {e}")
    #     return


# TODO: Refactor delete_callback to use type hints
async def delete_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    chat_id = update.effective_chat.id

    data = query.data

    if data.startswith("delete_confirm:"):
        item_id = int(data.split(":")[1])
        # Delete the item
        delete_item(item_id=item_id)
        await context.bot.send_message(chat_id=chat_id, text=messages.ITEM_DELETED.format(item_number = item_id))
    elif data == "delete_cancel":
        await context.bot.send_message(chat_id=chat_id, text="Deletion cancelled.")
