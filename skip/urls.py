from django.urls import path

from skip.views import CarCreate

patterns = [
    path('cars', CarCreate.as_view(), name='car_create')
]