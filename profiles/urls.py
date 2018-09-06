from django.urls import path

from profiles import views

urlpatterns = [
    path('profiles/balance', views.get_user_balance)
]