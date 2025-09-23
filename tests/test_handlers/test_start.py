import pytest
from bot.handlers.start import start_handler

@pytest.mark.asyncio
async def test_start_handler(mock_update, mock_context):
    """Тест обработчика /start"""
    await start_handler(mock_update, mock_context)
    
    # Проверяем, что ответ отправлен
    mock_update.message.reply_html.assert_called_once()
    
    # Проверяем, что упоминание пользователя вызвано
    mock_update.effective_user.mention_html.assert_called_once()

@pytest.mark.asyncio
async def test_start_handler_content(mock_update, mock_context):
    """Тест содержимого ответа /start"""
    await start_handler(mock_update, mock_context)
    
    call_args = mock_update.message.reply_html.call_args[0][0]
    assert "Привет" in call_args
    assert "/start" in call_args
    assert "/weather" in call_args
