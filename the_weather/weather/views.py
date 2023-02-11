from django.shortcuts import render
import requests


def index(request):
    city_name = request.POST.get('city_name')
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=d8092ef62da14cfdd64d9a05f1646a26'
    city = city_name
    r = requests.get(url.format(city)).json()

    city_weather = {
        'city': city,
        'temperate': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }

    context = {'city_weather': city_weather}
    return render(request, 'weather/weather.html', context)