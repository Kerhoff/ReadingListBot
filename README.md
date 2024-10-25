# ReadingListBot
The Telegram Bot to manage your reading list.

## Features
The bot allows users to:
- Add links to articles, videos, podcasts to their reading list.
- View their reading list.
- Mark item as “Read”
- Delete item from the list.
- TBD:
    - Filter the reading list by type (articles, videos, podcasts or articles).
    - Summarise articles of find information.

### Commands:
- /start - Start the bot
- /help - Get help
- /add - Add item to reading list
- /list - View reading list
- /complete - Mark item as read
- /delete - Delete item from reading list
- TBD:
    - /show - Filter reading list by type
    - /summary - Get summary of article

## Installation
1. Clone this repository.
2. Install dependencies: `poetry install`.
3. Set up your bot token in `.env` file. There is `.env.example` file in the repo for example.

## Usage
- `/start` - Start the bot
- `/add <link> <title> <type>` - Add a book to your reading list
- `/list` - View your reading list

## TODO
- [ ] Docker
- [ ] CI
- [ ] CD
- [ ] Postgres
- [ ] Tests
- [ ] Metrics
