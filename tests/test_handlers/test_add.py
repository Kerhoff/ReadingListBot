import pytest

from unittest.mock import AsyncMock
from telegram import Update
from telegram.ext import ContextTypes
from bot.handlers import add


@pytest.mark.parametrize(
    "args, expected_message",
    [
        (
            ['"Test Article"', "https://www.example.com", "#article"],
            "Item added to your reading list.",
        ),
        ([], 'Invalid format. Use: /add "title" link #type'),
        (
            ["Test URL Validation", "invalid-url", "#article"],
            "Invalid URL. Please provide a valid URL.",
        ),
        (
            ["Test Invalid Item Type", "https://www.example.com", "#unknown"],
            "Invalid item type. Please, use one of: #book, #article, #video or #podcast.",
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
    mocker.patch("bot.handlers.add.add_item", return_value=None)

    # Mock the send_message method with AsyncMock
    mock_context.bot.send_message = AsyncMock()

    # Run the handlers
    await add(mock_update, mock_context)

    # Verify the bot's send_message method was called
    mock_context.bot.send_message.assert_called_once_with(
        chat_id=mock_update.effective_chat.id, text=expected_message
    )
