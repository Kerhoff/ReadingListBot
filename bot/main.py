import logging
from telegram.ext import ApplicationBuilder, CommandHandler
from bot.config import TELEGRAM_BOT_TOKEN
from bot.handlers import start

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG # change to logging.INFO to reduce verbosity
)
def main():
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # Register command handlers
    start_handler = CommandHandler('start', start)

    # Add the handlers to the application
    application.add_handler(start_handler)

    # Start the application with polling
    application.run_polling()


if __name__ == '__main__':
    main()