from django.urls import path

from permits.views import CarView

urlpatterns = [
    path('cars', CarView.as_view(), name='cars'),
    path('cars/<int:pk>', CarView.as_view(), name='cars_del')
]