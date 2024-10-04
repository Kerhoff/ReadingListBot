# ReadingListBot
The Telegram Bot to manage your reading list.

# Features
The bot should allow users to:
	•	Add links to articles, videos, podcasts and messages from telegram channels to their reading list.
	•	View their reading list.
    •	Filter the reading list by type (articles, videos, podcasts, messages or articles).
	•	Mark item as “Read”
	•	Delete item from the list.
	•	Optionally, integrate with an external API to summarise articles of find information.

Commands:
    •	/start - Start the bot
    •	/help - Get help
    •	/add - Add item to reading list
    •	/list - View reading list
    •	/delete - Delete item from reading list
    •	/complete - Mark item as read
    •	/show - Filter reading list by type
    •	/summary - Get summary of article

## Installation
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your bot token in an environment variable or directly in `main.py`.
4. Run the bot: `python bot/main.py`.

## Usage
- `/start` - Start the bot
- `/add <book title>` - Add a book to your reading list
- `/list` - View your reading list

    "add": handlers.add,
    "clear": handlers.clear_list,
    "complete": handlers.complete,
    "delete": handlers.delete,
    "filter": handlers.filter_items,
    "help": handlers.help,
    "list": handlers.list_items,
    "start": handlers.start,
    "summary": handlers.summary,
