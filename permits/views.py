from django.http import JsonResponse, request
from django.views.generic import CreateView

from permits.models import Car


class AjaxResponseMixin(object):
    def form_invalid(self, form):
        response = super().form_invalid(form)

        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        return response

    def form_valid(self, form):
        response = super().form_valid(form)

        if self.request.is_ajax():
            data = {
                'pk': self.object.pk
            }
            return JsonResponse(data)
        return response


class CarView(AjaxResponseMixin, CreateView):
    model = Car
    fields = ['number', 'mark', 'model']
