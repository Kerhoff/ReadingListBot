from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=
"""Welcome to the Reading List Bot!

I can help you keep track of the information you want to read, listen or watch.

1. To add a new item to your list, use the /add command followed by the title and the URL.
   For example: /add How to Win Friends and Influence People https://www.goodreads.com/book/show/4865.How_to_Win_Friends_and_Influence_People
2. To view your list, use the /list command.
3. To remove an item from your list, use the /remove command followed by the title.
   For example: /remove How to Win Friends and Influence People
4. To clear your list, use the /clear command.""")