import logging

from typing import Optional
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
)
from bot import config, handlers

COMMAND_HANDLERS = {
    "add": handlers.add,
    "clear": handlers.clear_list,
    "complete": handlers.complete,
    "delete": handlers.delete,
    "show": handlers.filter_items,
    "help": handlers.help,
    "list": handlers.list_items,
    "start": handlers.start,
}

# Enable logging
LOG_LEVELS: dict[str, int] = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}

log_level: int = LOG_LEVELS.get(config.LOG_LEVEL.upper(), logging.INFO)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=log_level
)
logger = logging.getLogger(__name__)

TOKEN: Optional[str] = config.TELEGRAM_BOT_TOKEN
if not TOKEN:
    raise ValueError(
        "Please set the TELEGRAM_BOT_TOKEN environment variable in .env file"
    )


def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()

    # Register and add command handlers to the application
    for command, handler in COMMAND_HANDLERS.items():
        command_handler = CommandHandler(command, handler)
        application.add_handler(command_handler)

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
