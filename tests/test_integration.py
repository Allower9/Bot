from unittest.mock import patch, MagicMock
from bot.main import main


class TestIntegration:
    """Интеграционные тесты"""

    @patch('bot.main.Application.run_polling')
    @patch('bot.main.create_app')
    def test_main_function(self, mock_create_app, mock_run_polling):
        """Тест главной функции"""
        mock_app = MagicMock()
        mock_app.run_polling = MagicMock()
        mock_create_app.return_value = mock_app

        main()

        mock_create_app.assert_called_once()
        mock_app.run_polling.assert_called_once()


class TestErrorHandling:
    """Тесты обработки ошибок"""

    def test_logging_import(self):
        """Тест что логирование импортируется корректно"""
        from bot.main import logger
        assert logger is not None
        assert logger.name == 'bot.main'


class TestEdgeCases:
    """Тесты крайних случаев"""

    @patch.dict('os.environ', {'TELEGRAM_BOT_TOKEN': 'test', 'WEATHER_API_KEY': 'test'})
    def test_environment_variables(self):
        """Тест переменных окружения"""
        from bot.services.weather_api import get_weather
        assert callable(get_weather)
