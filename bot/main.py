import logging
from telegram.ext import ApplicationBuilder, CommandHandler
from bot.config import TELEGRAM_BOT_TOKEN
from bot.handlers import start, help, add, list_items, delete, complete, filter_items, summary, clear_list

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG # change to logging.INFO to reduce verbosity
)
def main():
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # Register and add command handlers to the application
    # /start
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    # /help
    help_handler = CommandHandler('help', help)
    application.add_handler(help_handler)

    # /add
    add_handler = CommandHandler('add', add)
    application.add_handler(add_handler)

    # /list
    list_items_handler = CommandHandler('list', list_items)
    application.add_handler(list_items_handler)

    # /delete
    delete_handler = CommandHandler('delete', delete)
    application.add_handler(delete_handler)

    # /complete
    complete_handler = CommandHandler('complete', complete)
    application.add_handler(complete_handler)

    # /filter
    filter_items_handler = CommandHandler('filter', filter_items)
    application.add_handler(filter_items_handler)

    # /summary
    summary_handler = CommandHandler('summary', summary)
    application.add_handler(summary_handler)

    # /clear
    clear_handler = CommandHandler('clear', clear_list)
    application.add_handler(clear_handler)

    application.run_polling()


if __name__ == '__main__':
    main()