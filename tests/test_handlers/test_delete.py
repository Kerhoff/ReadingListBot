import pytest

from unittest.mock import AsyncMock
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from bot.handlers import delete, delete_callback
from bot.db.models import ReadingItem


@pytest.mark.parametrize(
    "args, expected_message",
    [
        (["1"], "Are you sure you want to delete '1. Test Article'?"),
        ([], "Use: /delete <item number>"),
        (["100"], "Invalid item number"),
    ],
)
@pytest.mark.asyncio
async def test_delete_handler(mocker, args, expected_message):
    # Mosck the Update and Context objects
    mock_update = mocker.Mock(spec=Update)
    mock_context = mocker.Mock(spec=ContextTypes.DEFAULT_TYPE)

    # Set up the mock Update
    mock_update.effective_user.id = 171717171
    mock_context.args = args

    # Create the confirmation keyboard
    expected_keyboard = [
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
    expected_reply_markup = InlineKeyboardMarkup(expected_keyboard)

    # Mock the database calls
    mocker.patch(
        "bot.handlers.delete.get_items",
        return_value=[
            ReadingItem(id=1, title="Test Article"),
        ],
    )

    # Mock the send_message method with AsyncMock
    mock_context.bot.send_message = AsyncMock()

    # Run the handlers
    await delete(mock_update, mock_context)

    # Verify the bot's send_message method was called
    if not args or args[0] == "100":
        mock_context.bot.send_message.assert_called_once_with(
            chat_id=mock_update.effective_chat.id,
            text=expected_message,
        )
    else:
        mock_context.bot.send_message.assert_called_once_with(
            chat_id=mock_update.effective_chat.id,
            text=expected_message,
            reply_markup=expected_reply_markup,
        )


@pytest.mark.parametrize(
    "callback_data, expected_result_message",
    [
        ("delete_confirm:1", "Item '1' deleted from your list."),
        ("delete_cancel", "Deletion cancelled."),
    ],
)
@pytest.mark.asyncio
async def test_delete_callback_handler(mocker, callback_data, expected_result_message):
    # Mosck the Update and Context objects
    mock_update = mocker.Mock(spec=Update)
    mock_context = mocker.Mock(spec=ContextTypes.DEFAULT_TYPE)

    # Mock the callback_query data
    mock_query = mocker.Mock()
    mock_query.data = callback_data
    mock_update.callback_query = mock_query

    # Set up the mock Update
    mock_update.effective_user.id = 171717171

    # Mock the database calls
    mocker.patch("bot.handlers.delete.delete_item", return_value=None)

    # Mock the send_message method with AsyncMock
    mock_context.bot.send_message = AsyncMock()

    # Mock the answer_callback_query method with AsyncMock
    mock_query.answer = AsyncMock()

    # Run the handlers
    await delete_callback(mock_update, mock_context)

    # Verify the bot's send_message method was called
    mock_context.bot.send_message.assert_called_once_with(
        chat_id=mock_update.effective_chat.id, text=expected_result_message
    )
