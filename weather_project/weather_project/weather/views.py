import os
import requests

from django.shortcuts import render
from django.views import View


class IndexView(View):
    template_name = "weather/city_weather.html"
    current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        API_KEY = os.environ.get("API_KEY")
        city = request.POST['city']

        weather_data = self.fetch_weather(city, API_KEY)

        if weather_data:
            context = {
                "weather_data": weather_data
            }
        else:
            context = {
                "error_message": "This city was not found!"
            }

        return render(request, self.template_name, context)

    def fetch_weather(self, city, api_key):
        response = requests.get(self.current_weather_url.format(city, api_key)).json()

        temperature = response.get("main", None)
        description = response.get("weather", None)
        icon = response.get("weather", None)

        if temperature:
            weather_data = {
                'city': city,
                'temperature': round(temperature.get('temp') - 273.15, 2),
                'description': description[0]['description'],
                'icon': icon[0]['icon'],
            }

            return weather_data
