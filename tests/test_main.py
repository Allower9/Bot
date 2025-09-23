import pytest
import os
from unittest.mock import patch, MagicMock
from bot.main import create_app

def test_create_app_success():
    """Тест успешного создания приложения"""
    with patch.dict(os.environ, {'TELEGRAM_BOT_TOKEN': 'test_token'}):
        with patch('bot.main.Application.builder') as mock_builder:
            mock_app = MagicMock()
            mock_builder.return_value.token.return_value.build.return_value = mock_app
            
            app = create_app()
            
            assert app == mock_app
            # Проверяем, что обработчики добавлены
            assert mock_app.add_handler.call_count == 3

def test_create_app_missing_token():
    """Тест отсутствия токена"""
    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(ValueError, match="TELEGRAM_BOT_TOKEN not set"):
            create_app()
