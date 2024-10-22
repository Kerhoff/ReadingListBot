GREETINGS = """Welcome to the Reading List Bot!

I can help you keep track of the information you want to read, listen or watch.

1. To add a new item to your list, use the `/add` command followed by the title, URL and type.
   For example: /add 'How to Win Friends and Influence People' https://www.goodreads.com/book/show/4865.How_to_Win_Friends_and_Influence_People

2. To view your list, use the `/list` command.

3. To remove an item from your list, use the `/delete` command followed by the title.
   For example: /delete 'How to Win Friends and Influence People'
"""

HELP = """Bot Commands:
 /start - Start the bot
 /help - Get help
 /add - Add item to reading list
 /complete - Mark item as read
 /list - View reading list
 /show - Filter reading list by type
 /delete - Delete item from reading list
 /clear - Clear reading list

 Soon: 
 /summary - Get summary of article"""

ADD_ITEM_USAGE = 'Invalid format. Use: /add "title" link #type'

ITEM_ADDED = "Item added to your reading list."

INVALID_ITEM_TYPE = (
    "Invalid item type. Please, use one of: #book, #article, #video or #podcast."
)

INVALID_URL = "Invalid URL. Please provide a valid URL."

CLEAR_LIST_CONFIRMATION = "Are you sure you want to clear your list? This action cannot be undone. Type /confirm to proceed."

LIST_ITEMS = "- <i>Title:</i> <a href='{link}'>{title}</a>\n  <i>Status:</i> <b>{status}</b>\n  <i>Type:</i> #{item_type}\n"

LIST_EMPTY = "Your list is empty."

ITEM_NOT_FOUND = "Item not found in your list."

ITEM_DELETED = "Item '{item_number}. {title}' deleted from your list."

ITEM_DELETE_CONFIRM = "Are you sure you want to delete '{item_number}. {title}'?"
