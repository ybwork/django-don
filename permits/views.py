from django.http import JsonResponse, request
from django.urls import reverse
from django.views.generic import CreateView

from permits.models import Car


class CarView(CreateView):
    model = Car
    fields = ['number', 'mark', 'model']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)