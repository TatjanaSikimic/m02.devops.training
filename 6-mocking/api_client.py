import datetime

def fetch_weather_data(city):
    return {
        "city": city,
        "temp": 11,
        "condition": "sunny",
        "humidity": 78
    }


def fetch_forecast(city, days=3):
    return [{"day": i, "temp": 11 + i, "condition": "sunny"} for i in range(days)]


def get_current_hour():
    return datetime.datetime.now().hour
