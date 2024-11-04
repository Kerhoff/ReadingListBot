import logging

from telegram import Update
from telegram.ext import ContextTypes


logger = logging.getLogger(__name__)


# Define the filter command handler
async def show(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass
