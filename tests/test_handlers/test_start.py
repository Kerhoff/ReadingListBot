# import pytest
#
# # from unittest.mock import AsyncMock
# from telegram import Update
# from telegram.ext import ContextTypes
# from bot.handlers import start
#
#
# @pytest.mark.parametrize(
#     "user_id, expected_message",
#     [
#         (171717171, "Welcome to the Reading List Bot!"),
#         (0, "User not found"),
#     ],
# )
# async def test_start_handler(mocker, user_id, expected_message):
#     # Mock the Update and Context objects
#     mock_update = mocker.Mock(spec=Update)
#     mock_context = mocker.Mock(spec=ContextTypes.DEFAULT_TYPE)
#
#     # Set up the mock Update
#     mock_update.effective_user.id = user_id
#
#     # Mock the database calls
#     mocker.patch("bot.db.get_user", return_value=None)
#     mocker.patch("bot.db.add_user", return_value=None)
#
#     # Run the handlers
#     await start(mock_update, mock_context)
#
#     # Verify the bot's send_message method was called
#     mock_context.bot.send_message.assert_called_once_with(
#         chat_id=mock_update.effective_chat.id, text=expected_message
#     )
