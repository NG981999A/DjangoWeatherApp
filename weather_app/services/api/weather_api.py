import python_weather

class weatherApi:
    def __init__(self, unit=python_weather.IMPERIAL):
        self.unit = unit

    async def get_weather(self, location: str):
        async with python_weather.Client(unit=self.unit) as client:
            weather = await client.get(location)
            return weather
