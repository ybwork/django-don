from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from django.views.generic.edit import DeletionMixin
from django.views.generic.list import MultipleObjectMixin

from permits.models import Car


# class CarListMixin(object):
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['cars'] = Car.objects.filter(user_id=self.request.user.id)
#         return context


class CarView(SuccessMessageMixin, MultipleObjectMixin, DeletionMixin, CreateView):
    model = Car
    fields = ['number', 'mark', 'model']
    success_message = 'Success!'
    success_url = reverse_lazy('cars')

    def form_invalid(self, form):
        return super().form_invalid(form)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
