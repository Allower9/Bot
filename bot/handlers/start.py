from telegram import Update
from telegram.ext import ContextTypes

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    user = update.effective_user
    await update.message.reply_html(
        f"Привет, {user.mention_html()}! 👋\n\n"
        "Я тестовый бот с CI/CD pipeline!\n"
        "Доступные команды:\n"
        "/start - начать работу\n"
        "/weather <город> - погода\n"
        "Просто напиши что-нибудь, и я отвечу"
    )
