from django.http import HttpResponse
from django.shortcuts import render
from weather_app.services.api import weather_api

async def getWeatherInformations(request):
    api = weather_api.weatherApi()
    basis_informations = await api.get_weather('New York')

    context = {
        'basis_informations': basis_informations
    }
    return render(request, "weather/index.html", context)