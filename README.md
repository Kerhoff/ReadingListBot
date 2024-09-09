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
    •	/filter - Filter reading list by type
    •	/summary - Get summary of article

Project Structure:
    •	readinglistbot.py - Main bot script
    •	readinglist.py - Reading list class
    •	summary.py - Summary class
    •	README.md - Project description
    •	requirements.txt - Project dependencies
    •	.gitignore - Git ignore file
    •	.env - Environment variables file
    •	Procfile - Heroku deployment file
    •	Makefile - Makefile for running commands
    •	tests/ - Folder for tests
    •	venv/ - Virtual environment folderq

## Installation
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your bot token in an environment variable or directly in `main.py`.
4. Run the bot: `python bot/main.py`.

## Usage
- `/start` - Start the bot
- `/add <book title>` - Add a book to your reading list
- `/list` - View your reading list