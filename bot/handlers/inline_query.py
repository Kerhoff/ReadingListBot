# from uuid import uuid4

from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.ext import ContextTypes, InlineQueryHandler

# import bot.messages as messages

# Define the start command handler
async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.inline_query.query
    print(f"Query: {query}")

    if not query:
        return

    results = [
        InlineQueryResultArticle(
            id='1',
            title="Title",
            input_message_content=InputTextMessageContent("Hello, world!"),
        ),
    ]


    await update.inline_query.answer(results)
