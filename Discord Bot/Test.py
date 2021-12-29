import python_weather
import asyncio


async def getweather():
    client = python_weather.Client(format=python_weather.IMPERIAL)
    weather = await client.find("Ahmedabad, Gujarat")

    print(weather.current.temperature)

    await client.logout()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())
