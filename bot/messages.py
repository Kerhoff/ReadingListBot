GREETINGS="""Welcome to the Reading List Bot!

I can help you keep track of the information you want to read, listen or watch.

1. To add a new item to your list, use the `/add` command followed by the title, URL and type.
   For example: /add 'How to Win Friends and Influence People' https://www.goodreads.com/book/show/4865.How_to_Win_Friends_and_Influence_People

2. To view your list, use the `/list` command.

3. To remove an item from your list, use the `/delete` command followed by the title.
   For example: /delete 'How to Win Friends and Influence People'
"""

HELP="""Bot Commands:
 /start - Start the bot
 /help - Get help
 /add - Add item to reading list
 /list - View reading list
 /delete - Delete item from reading list
 /complete - Mark item as read
 /filter - Filter reading list by type
 /summary - Get summary of article
 /clear - Clear reading list"""

ADD_ITEM_USAGE="""Usage: /add <link> <title> <type>"""

ITEM_ADDED="Item '{title}' added to your list."

INVALID_ITEM_TYPE="Invalid item type. Please choose from 'book', 'article', 'video', or 'podcast'."

CLEAR_LIST_CONFIRMATION="Are you sure you want to clear your list? This action cannot be undone. Type /confirm to proceed."

LIST_EMPTY="Your list is empty."

INVALID_URL="Invalid URL. Please provide a valid URL."

ITEM_NOT_FOUND="Item not found in your list."

ITEM_DELETED="Item '{}' deleted from your list."