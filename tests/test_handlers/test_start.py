import pytest

from unittest.mock import AsyncMock
from telegram import Update
from telegram.ext import ContextTypes
from bot.handlers import start


@pytest.mark.parametrize(
    "user_id, user_name, expected_message",
    [
        (
            171717171,
            "test_user_name",
            """Welcome to the Reading List Bot!

I can help you keep track of the information you want to read, listen or watch.

1. To add a new item to your list, use the `/add` command followed by the title, URL and type.
   For example: /add 'How to Win Friends and Influence People' https://www.goodreads.com/book/show/4865.How_to_Win_Friends_and_Influence_People

2. To view your list, use the `/list` command.

3. To remove an item from your list, use the `/delete` command followed by the title.
   For example: /delete 'How to Win Friends and Influence People'
""",
        ),
    ],
)
@pytest.mark.asyncio
async def test_start_handler(mocker, user_id, user_name, expected_message):
    # Mock the Update and Context objects
    mock_update = mocker.Mock(spec=Update)
    mock_context = mocker.Mock(spec=ContextTypes.DEFAULT_TYPE)

    # Set up the mock Update
    mock_update.effective_user.id = user_id
    mock_update.effective_user.username = user_name

    # Mock the database calls
    mocker.patch("bot.db.db.get_user", return_value=None)
    mocker.patch("bot.db.db.add_user", return_value=None)

    # Mock the send_message method with AsyncMock
    mock_context.bot.send_message = AsyncMock()

    # Run the handlers
    await start(mock_update, mock_context)

    # Verify the bot's send_message method was called
    mock_context.bot.send_message.assert_called_once_with(
        chat_id=mock_update.effective_chat.id, text=expected_message
    )
