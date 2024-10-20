# ReadingListBot
The Telegram Bot to manage your reading list.

# Features
The bot should allow users to:
	•	Add links to articles, videos, podcasts to their reading list.
	•	View their reading list.
    •	Filter the reading list by type (articles, videos, podcasts or articles).
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
- `/add <link> <title> <type>` - Add a book to your reading list
- `/list` - View your reading list
