from django.views.generic import CreateView

from skip.models import Car


class CarCreate(CreateView):
    model = Car
    fields = ['number', 'mark', 'model']
