from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


# Create your views here.
def index(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=822c81394797e4e26ca425c02b0ce2f3"
    city = City.objects.all()
    weather_data = []

    if request.method == "POST":
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    for city in city:
        r = requests.get(url.format(city)).json()

        city_weather = {
            "city": city.name,
            "temperature": r["main"]["temp"],
            "description": r["weather"][0]["description"],
            "icon": r["weather"][0]["icon"]
        }

        weather_data.append(city_weather)

    context = {"weather_data": weather_data, "form": form}

    return render(request, "weather/weather.html", context)
