from django.urls import path

from permits.views import CarListView, CarCreateView, CarDeleteView, CarUpdateView, CarSearchView

urlpatterns = [
    path('car/list', CarListView.as_view(), name='car-list'),
    path('car/create', CarCreateView.as_view(), name='car-create'),
    path('car/<int:pk>/update', CarUpdateView.as_view(), name='car-update'),
    path('car/<int:pk>/delete', CarDeleteView.as_view(), name='car-delete'),
    path('car/search', CarSearchView.as_view(), name='car-search')
]