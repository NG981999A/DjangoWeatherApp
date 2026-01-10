from django.urls import path
from . import views

urlpatterns = [
    path('', views.getWeatherInformations, name='weather_informations'),
]

