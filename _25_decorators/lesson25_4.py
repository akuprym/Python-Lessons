import requests

API_KEY = "QEWT9QJLWEFRTT7R4CXS35BCP"

def get_weather_by_hours_for_day_from_api(*, date: str, city: str) -> list[dict]:

    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{date}/{date}?key={API_KEY}"
    response = requests.get(url)
    weather_by_days = response.json()["days"]
    weather_by_hours = weather_by_days[0]["hours"]
    return weather_by_hours

def fahrenheit_to_celsius(*, fahrenheit_temperature: float) -> int:
    return round((fahrenheit_temperature - 32) * 5 / 9)

def get_dangerous_hours(*, weather_by_hour: list[dict]) -> list[dict]:
    dangerous_hours = []
    for weather in weather_by_hour:
        uvindex = weather["uvindex"]
        time = weather["datetime"]
        celcius_temperature = fahrenheit_to_celsius(fahrenheit_temperature=weather["temp"])
        if uvindex >= 3:
            dangerous_hours.append({"time": time, "uvindex": uvindex, "temperature": celcius_temperature})
    return dangerous_hours

date = "2024-07-27"
city = "London,UK"

weather_by_hour = get_weather_by_hours_for_day_from_api(date=date, city=city)
print(get_dangerous_hours(weather_by_hour=weather_by_hour))