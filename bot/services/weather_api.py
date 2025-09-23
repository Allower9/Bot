import aiohttp
import os


async def get_weather(city: str) -> str:
    """Получение погоды через OpenWeatherMap"""
    api_key = os.getenv('WEATHER_API_KEY', 'demo_key')
    url = f"http: //api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                temp = data['main']['temp']
                desc = data['weather'][0]['description']
                return f"Погода в {city}: {temp}°C, {desc}"
            else:
                return "Город не найден"
