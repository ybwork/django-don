from django.forms import ModelForm

from cars.models import Car


class SearchCarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['number']
