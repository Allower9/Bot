from telegram import Update
from telegram.ext import ContextTypes
from bot.services.weather_api import get_weather

async def weather_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик погоды"""
    if not context.args:
        await update.message.reply_text("Укажите город: /weather Москва")
        return
    
    city = ' '.join(context.args)
    try:
        weather = await get_weather(city)
        await update.message.reply_text(weather)
    except Exception as e:
        await update.message.reply_text(f"Ошибка: {str(e)}")
