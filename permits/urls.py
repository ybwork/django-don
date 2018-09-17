from django.urls import path

from permits.views import CarView

urlpatterns = [
    path('cars', CarView.as_view(), name='car_create')
]