import pytest

from unittest.mock import AsyncMock
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from bot.handlers import delete, delete_callback
from bot.db import ReadingItem


@pytest.mark.parametrize(
    "args, expected_message, callback_data",
    [
        (
            ["1"],
            "Item '1' deleted from your list.",
            "delete_confirm:1",
        ),
        ( ["1"],
            "Deletion cancelled.",
            "delete_cancel",
        ),
        ([], "Use: /delete <item number>", ""),
        (["100"], "Invalid item number", ""),
    ],
)
@pytest.mark.asyncio
async def test_delete_handler(mocker, args, expected_message, callback_data):
    # Mosck the Update and Context objects
    mock_update = mocker.Mock(spec=Update)
    mock_context = mocker.Mock(spec=ContextTypes.DEFAULT_TYPE)

    # Mock the callback_query data
    mock_query = mocker.Mock()
    mock_query.data = callback_data
    mock_update.callback_query = mock_query

    # Set up the mock Update
    mock_update.effective_user.id = 171717171
    mock_context.args = args

    # Create the confirmation keyboard
    keyboard = [
        [
            InlineKeyboardButton(
                "Yes",
                callback_data="delete_confirm:1",
            ),
            InlineKeyboardButton(
                "No",
                callback_data="delete_cancel",
            ),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Set up the mock Confirmation message
    confirmation_message = "Are you sure you want to delete '1. Test Article'?"

    # Mock the database calls
    mocker.patch(
        "bot.handlers.delete.get_items",
        return_value=[ReadingItem(id=1, title="Test Article"),],
    )
    mocker.patch("bot.handlers.delete.delete_item", return_value=None)

    # Mock the send_message method with AsyncMock
    mock_context.bot.send_message = AsyncMock()

    # Mock the answer_callback_query method with AsyncMock
    mock_query.answer = AsyncMock()

    # Run the handlers
    await delete(mock_update, mock_context)

    # Verify the bot's send_message method was called
    mock_context.bot.send_message.assert_any_call(
        chat_id=mock_update.effective_chat.id,
        text=confirmation_message,
        reply_markup=reply_markup,
        )
    
    # Run the callback_query handlers
    await delete_callback(mock_update, mock_context)

    # Verify the bot's send_message method was called
    mock_context.bot.send_message.assert_any_call(
        chat_id=mock_update.effective_chat.id, text=expected_message
    )

    assert mock_context.bot.send_message.call_count == 2
