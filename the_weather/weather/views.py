from django.shortcuts import render
import requests
from decouple import config

def index(request):
    city_name = request.POST.get('city_name')
    if city_name == None:
        city_name = 'Ahmedabad' #my-city
    city = city_name
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={config('API')}"
    r = requests.get(url.format(city)).json()

    city_weather = {
        'city': city,
        'temperate': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
        'country': r['sys']['country'],
    }

    context = {'city_weather': city_weather}
    return render(request, 'weather/weather.html', context)
