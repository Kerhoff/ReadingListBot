import logging

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    InlineQueryHandler,
)
from bot import config, handlers

COMMAND_HANDLERS = {
    "add": handlers.add,
    "clear": handlers.clear_list,
    "complete": handlers.complete,
    "delete": handlers.delete,
    "filter": handlers.filter_items,
    "help": handlers.help,
    "list": handlers.list_items,
    "start": handlers.start,
    "summary": handlers.summary,
}

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,  # change to logging.INFO to reduce verbosity
)
logger = logging.getLogger(__name__)


if not config.TELEGRAM_BOT_TOKEN:
    raise ValueError(
        "Please set the TELEGRAM_BOT_TOKEN environment variable in .env file"
    )


def main():
    application = ApplicationBuilder().token(config.TELEGRAM_BOT_TOKEN).build()

    # Register and add command handlers to the application
    for command, handler in COMMAND_HANDLERS.items():
        command_handler = CommandHandler(command, handler)
        application.add_handler(command_handler)

    # Add inline query handler
    application.add_handler(InlineQueryHandler(handlers.inline_query))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback

        logger.warning(traceback.format_exc())
    finally:
        pass
        # close_db_connection()
