import pytest

from unittest.mock import AsyncMock
from telegram import Update
from telegram.ext import ContextTypes
from bot.handlers import delete
from bot.db import ReadingItem


@pytest.mark.parametrize(
    "args, expected_message",
    [
        (
            ["1"],
            "Item 'Test Article' deleted from your list.",
        ),
        ([], "Use: /delete <item number>"),
        (["100"], "Invalid item number"),
    ],
)
#TODO: Add callback tests
@pytest.mark.asyncio
async def test_complete_handler(mocker, args, expected_message):
    # Mosck the Update and Context objects
    mock_update = mocker.Mock(spec=Update)
    mock_context = mocker.Mock(spec=ContextTypes.DEFAULT_TYPE)

    # Set up the mock Update
    mock_update.effective_user.id = 171717171
    mock_context.args = args

    # Mock the database calls
    mocker.patch(
        "bot.handlers.complete.get_item_by_title",
        return_value=ReadingItem(id=1, title="Test Article"),
    )
    mocker.patch("bot.handlers.delete.delete_item", return_value=None)

    # Mock the send_message method with AsyncMock
    mock_context.bot.send_message = AsyncMock()

    # Run the handlers
    await delete(mock_update, mock_context)

    # Verify the bot's send_message method was called
    mock_context.bot.send_message.assert_called_once_with(
        chat_id=mock_update.effective_chat.id, text=expected_message
    )
