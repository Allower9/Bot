import os
import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from bot.handlers.start import start_handler
from bot.handlers.echo import echo_handler
from bot.handlers.weather import weather_handler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_app():
    """Создание и настройка приложения бота"""
    token = os.getenv('8152838489:AAEMVE8uxdD5STO3fpXfk9sNmgX1Rc4osFc')
    if not token:
        raise ValueError("TELEGRAM_BOT_TOKEN not set")
    
    application = Application.builder().token(token).build()
    
    # Регистрация обработчиков
    application.add_handler(CommandHandler("start", start_handler))
    application.add_handler(CommandHandler("weather", weather_handler))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_handler))
    
    return application

def main():
    """Запуск бота"""
    app = create_app()
    logger.info("Bot is starting...")
    app.run_polling()

if __name__ == "__main__":
    main()
