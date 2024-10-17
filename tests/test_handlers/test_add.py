import pytest

from unittest.mock import AsyncMock
from telegram import Update
from telegram.ext import ContextTypes
from bot.handlers import add


@pytest.mark.parametrize(
    "args, expected_message",
    [
        (
            ["https://www.example.com", "Test Article", "article"],
            "Item 'Test Article' added to your reading list.",
        ),
        ([], "Usage: /add <link> <title> <type>"),
        (
            ["invalid-url", "Test URL Validation", "article"],
            "Invalid URL. Please provide a valid URL.",
        ),
        (
            ["https://www.example.com", "Test Invalid Item Type", "unknown"],
            "Invalid item type. Please choose from 'book', 'article', 'video' or 'podcast'.",
        ),
    ],
)
@pytest.mark.asyncio
async def test_add_handler(mocker, args, expected_message):
    # Mosck the Update and Context objects
    mock_update = mocker.Mock(spec=Update)
    mock_context = mocker.Mock(spec=ContextTypes.DEFAULT_TYPE)

    # Set up the mock Update
    # mock_update.effective_chat.id = 71717171
    mock_update.effective_user.id = 171717171
    mock_context.args = args

    # Mock the database calls
    mocker.patch("bot.db.add_item", return_value=None)

    # Mock the send_message method with AsyncMock
    mock_context.bot.send_message = AsyncMock()

    # Run the handlers
    await add(mock_update, mock_context)

    # Verify the bot's send_message method was called
    mock_context.bot.send_message.assert_called_once_with(
        chat_id=mock_update.effective_chat.id, text=expected_message
    )
