import pytest
from unittest.mock import patch
from bot.handlers.weather import weather_handler

@pytest.mark.asyncio
async def test_weather_handler_no_city(mock_update, mock_context):
    """Тест погоды без указания города"""
    await weather_handler(mock_update, mock_context)
    
    mock_update.message.reply_text.assert_called_once_with(
        "Укажите город: /weather Москва"
    )

@pytest.mark.asyncio
async def test_weather_handler_with_city(mock_update, mock_context_with_args):
    """Тест погоды с указанием города"""
    with patch('bot.handlers.weather.get_weather') as mock_weather:
        mock_weather.return_value = "Погода в Moscow: 20°C, ясно"
        
        await weather_handler(mock_update, mock_context_with_args)
        
        mock_weather.assert_called_once_with('Moscow')
        mock_update.message.reply_text.assert_called_once_with("Погода в Moscow: 20°C, ясно")

@pytest.mark.asyncio
async def test_weather_handler_api_error(mock_update, mock_context_with_args):
    """Тест обработки ошибки API"""
    with patch('bot.handlers.weather.get_weather') as mock_weather:
        mock_weather.side_effect = Exception("API недоступно")
        
        await weather_handler(mock_update, mock_context_with_args)
        
        mock_update.message.reply_text.assert_called_once_with("Ошибка: API недоступно")
