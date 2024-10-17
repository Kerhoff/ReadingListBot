# import pytest
#
# # from unittest.mock import AsyncMock
# from telegram import Update
# from telegram.ext import ContextTypes
# from bot.handlers import add
#
#
# @pytest.mark.parametrize(
#     "args, expected_message",
#     [
#         (
#             ["https://www.example.com", "Test Article", "article"],
#             "Item added to the reading list",
#         ),
#         (
#             ["https://www.invalid-url", "Test URL Validation", "article"],
#             "Invalid URL provided",
#         ),
#         (
#             ["https://www.example.com", "Test Invalid Item Type", "unknown"],
#             "Invalid item type",
#         ),
#     ],
# )
# async def test_add_handler(mocker, args, expected_message):
#     # Mosck the Update and Context objects
#     mock_update = mocker.Mock(spec=Update)
#     mock_context = mocker.Mock(spec=ContextTypes.DEFAULT_TYPE)
#
#     # Set up the mock Update
#     mock_update.effective_chat.id = 71717171
#     mock_update.effective_user.id = 171717171
#     mock_context.args = args
#     # Mock the database calls
#     mocker.patch("bot.db.add_item", return_value=None)
#
#     # Run the handlers
#     await add(mock_update, mock_context)
#
#     # Verify the bot's send_message method was called
#     mock_context.bot.send_message.assert_called_once_with(
#         chat_id=71717171, text=expected_message
#     )
