import pytest

from unittest.mock import AsyncMock
from telegram import Update
from telegram.ext import ContextTypes
from datetime import datetime

from bot.db.models import ReadingItem
from bot.handlers import list


@pytest.mark.parametrize(
    "is_empty, expected_message",
    [
        (True, "Your list is empty."),
        (
            False,
            """1. <i>Title:</i> <a href='https://www.example1.com'>1 Test Item</a>\n\
<i>Status:</i> <b>New</b>\n\
<i>Type:</i> #article\n\
<i>Added:</i> 2024-01-01\n\n\
2. <i>Title:</i> <a href='https://www.example2.com'>2 Test Item</a>\n\
<i>Status:</i> <b>Completed</b>\n\
<i>Type:</i> #video\n\
<i>Added:</i> 2024-01-02\n\n""",
        ),
    ],
)
@pytest.mark.asyncio
async def test_list_handler(mocker, is_empty, expected_message):
    # Mock the Update and Context objects
    mock_update = mocker.Mock(spec=Update)
    mock_context = mocker.Mock(spec=ContextTypes.DEFAULT_TYPE)

    # Mock the ReadingItem objects
    reading_item_1 = ReadingItem(
        title="1 Test Item",
        link="https://www.example1.com",
        item_type="article",
        completed=False,
        created_at=datetime.strptime("2024-01-01 00:00:00", "%Y-%m-%d %H:%M:%S"),
    )
    reading_item_2: ReadingItem = ReadingItem(
        title="2 Test Item",
        link="https://www.example2.com",
        item_type="video",
        completed=True,
        created_at=datetime.strptime("2024-01-02 00:00:00", "%Y-%m-%d %H:%M:%S"),
    )

    if is_empty:
        reading_list = []
    else:
        reading_list = [
            reading_item_1,
            reading_item_2,
        ]

    # Set up the mock Update
    mock_update.effective_user.id = 171717171

    # Mock the database calls
    # mocker.patch("bot.db.get_items", return_value=reading_list)
    mocker.patch("bot.handlers.list.get_items", return_value=reading_list)

    # Mock the send_message method with AsyncMock
    mock_context.bot.send_message = AsyncMock()

    # Run the handlers
    await list(mock_update, mock_context)

    # Verify the bot's send_message method was called
    mock_context.bot.send_message.assert_called_once_with(
        chat_id=mock_update.effective_chat.id, parse_mode="HTML", text=expected_message
    )
