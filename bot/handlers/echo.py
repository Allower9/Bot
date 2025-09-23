from telegram import Update
from telegram.ext import ContextTypes

async def echo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Эхо-обработчик"""
    text = update.message.text
    await update.message.reply_text(f"Вы сказали: {text}")
