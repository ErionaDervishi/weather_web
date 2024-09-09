from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests
import datetime

def index(request):
    appid = '8ffc75920098962a8072946767a50003'
    weather_url = 'https://api.openweathermap.org/data/2.5/weather?'

    if request.method == 'POST':
        city_name = request.POST.get('city', '')
    else:
        city_name = 'Tirana'

    params = {'q': city_name, 'appid': appid, 'units': 'metric'}

    response = requests.get(url=weather_url, params=params)
    data = response.json()

    if response.status_code == 200:
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        latitude = data['coord']['lat']
        longitude = data['coord']['lon']
        day = datetime.date.today()

        context = {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city_name': city_name,
            'latitude': latitude,
            'longitude': longitude
        }

        return render(request, 'base.html', context)
    else:

        error_message = f'Nuk mund të gjejë të dhëna për qytetin {city_name}'
        return render(request, 'base.html', {'error_message': error_message})
