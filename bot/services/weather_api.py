import aiohttp
import os


async def get_weather(city: str) -> str:
    """Получение погоды через OpenWeatherMap"""
    api_key = os.getenv('WEATHER_API_KEY', 'demo_key')

    # ИСПРАВЛЕННЫЙ URL - убрал лишние слеши
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"  # noqa: E231

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                temp = data['main']['temp']
                desc = data['weather'][0]['description']
                return f"Погода в {city}: {temp}°C, {desc}"
            elif response.status == 404:
                return "Город не найден"
            else:
                return f"Ошибка API: {response.status}"
