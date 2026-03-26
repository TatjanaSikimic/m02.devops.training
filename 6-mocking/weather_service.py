import api_client


def get_weather(city):
    return api_client.fetch_weather_data(city)


def get_forecast(city, days=3):
    return api_client.fetch_forecast(city, days)


def is_good_weather(conditions):
    for condition in conditions:
        if condition not in ["sunny", "partly cloudy"]:
            return False
    return True

def get_greeting_based_on_time():
    hour = api_client.get_current_hour()

    if hour < 12:
        return "Good morning!"
    elif hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"
