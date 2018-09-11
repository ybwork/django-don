from django.contrib.auth.models import User
from django.db import models


class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=15, unique=True)
    mark = models.CharField(max_length=255)
    model = models.CharField(max_length=255)


class People(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
