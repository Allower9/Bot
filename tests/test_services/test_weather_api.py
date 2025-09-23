import pytest
from unittest.mock import patch, AsyncMock
from bot.services.weather_api import get_weather


@pytest.mark.asyncio
async def test_get_weather_success():
    """Тест успешного получения погоды"""
    mock_response = {
        'main': {'temp': 20},
        'weather': [{'description': 'ясно'}]
    }

    with patch('aiohttp.ClientSession.get') as mock_get:
        mock_get.return_value.__aenter__.return_value.status = 200
        mock_get.return_value.__aenter__.return_value.json = AsyncMock(return_value=mock_response)

        result = await get_weather('Moscow')

        assert result == "Погода в Moscow: 20°C, ясно"


@pytest.mark.asyncio
async def test_get_weather_city_not_found():
    """Тест для ненайденного города"""
    with patch('aiohttp.ClientSession.get') as mock_get:
        mock_get.return_value.__aenter__.return_value.status = 404

        result = await get_weather('UnknownCity')

        assert result == "Город не найден"


@pytest.mark.asyncio
async def test_get_weather_network_error():
    """Тест ошибки сети"""
    with patch('aiohttp.ClientSession.get') as mock_get:
        mock_get.side_effect = Exception("Network error")

        with pytest.raises(Exception, match="Network error"):
            await get_weather('Moscow')
