import datetime
import os

import requests
from django.shortcuts import render


def index(request):
    API_KEY = os.environ.get("API_KEY")
    curr_weather_data = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    forecast_url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid{}"

    if request.method == "POST":
        city1 = request.POST['city1']
        city2 = request.POST['city2', None]

        weather_data1, daily_forecast1 = fetch_weather_and_forecast(city1, API_KEY, curr_weather_data, forecast_url)

        if city2:
            weather_data2, daily_forecast2 = fetch_weather_and_forecast(city2, API_KEY, curr_weather_data, forecast_url)
        else:
            weather_data2, daily_forecast2 = None, None

        context = {
            "weather_data1": weather_data1,
            "daily_forecast1": daily_forecast1,
            "weather_data2": weather_data2,
            "daily_forecast2": daily_forecast2,
        }
        return render(request, "weather/index.html", context)

    else:
        return render(request, "weather/index.html")


def fetch_weather_and_forecast(city, api_key, curr_weather_url, forecast_url):
    response = requests.get(curr_weather_url.format(city, api_key)).json()
    lat, lon = response['coord']['lat'], response['coord']['lon']
    forecast_response = requests.get(forecast_url.format(lat, lon, api_key)).json()

    weather_data = {
        "city": city,
        "temperature": round(response['main']['temp'] - 273.15, 2),
        "description": response['weather']['description'],
        "icon": response['weather']['icon']
    }

    daily_forecasts = []
    for daily_data in forecast_response['daily'][:5]:
        daily_forecasts.append({
            'day': datetime.datetime.fromtimestamp(daily_data['dt']).strftime("%A"),
            "min_temp": round(daily_data['temp']['min'] - 273.15, 2),
            "max_temp": round(daily_data['temp']['max'] - 273.15, 2),
            "description": daily_data['weather']['description'],
            "icon": daily_data["weather"]["icon"]
        })

    return weather_data, daily_forecasts
