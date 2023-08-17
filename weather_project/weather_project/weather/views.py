import os

from django.shortcuts import render


def index(request):
    API_KEY = os.environ.get("API_KEY")
    curr_weather_data = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    four_days_weather_data = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid{}"

    if request.method == "POST":
        city1 = request.POST['city1']
        city2 = request.POST['city2', None]
    else:
        return render(request, "weather/index.html")
