from django.views.generic import CreateView

from permits.models import Car


class AjaxResponseMixin:
    pass

class CarView(CreateView):
    model = Car
    fields = ['number', 'mark', 'model']
