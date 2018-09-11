from django.urls import path

from permits.views import CarCreate

urlpatterns = [
    path('cars', CarCreate.as_view(), name='car_create')
]