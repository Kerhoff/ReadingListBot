import pytest

from unittest.mock import AsyncMock
from telegram import Update
from telegram.ext import ContextTypes
from bot.handlers import help


@pytest.mark.parametrize(
    "chat_id, expected_message",
    [
        (
            71717171,
            "Bot Commands:\n /start - Start the bot\n /help - Get help\n /add - Add item to reading list\n /complete - Mark item as read\n /list - View reading list\n /show - Filter reading list by type\n /delete - Delete item from reading list\n /clear - Clear reading list\n\n Soon: \n /summary - Get summary of article",
        ),
    ],
    # [
    #     ("""Bot Commands:
    #  /start - Start the bot
    #  /help - Get help
    #  /add - Add item to reading list
    #  /complete - Mark item as read
    #  /list - View reading list
    #  /show - Filter reading list by type
    #  /delete - Delete item from reading list
    #  /clear - Clear reading list
    #
    #  Soon:
    #  /summary - Get summary of article"""),
    # ],
)
@pytest.mark.asyncio
async def test_help_handler(mocker, chat_id, expected_message):
    # Mock the Update and Context objects
    mock_update = mocker.Mock(spec=Update)
    mock_context = mocker.Mock(spec=ContextTypes.DEFAULT_TYPE)

    # Set up the mock Update
    mock_update.effective_chat.id = chat_id

    # Mock the send_message method with AsyncMock
    mock_context.bot.send_message = AsyncMock()

    # Run the handlers
    await help(mock_update, mock_context)

    # Verify the bot's send_message method was called
    mock_context.bot.send_message.assert_called_once_with(
        chat_id=chat_id, text=expected_message
    )
