from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from meterials.models import Meterial


class MeterialCreateView(CreateView):
    model = Meterial
    fields = ('title', 'body',)
    success_url = reverse_lazy('meterials:list')


class MeterialUpdateView(UpdateView):
    model = Meterial
    fields = ('title', 'body',)
    success_url = reverse_lazy('meterials:list')


class MeterialListView(ListView):
    model = Meterial


class MeterialDetailView(DetailView):
    model = Meterial


class MeterialDeleteView(DeleteView):
    model = Meterial
    success_url = reverse_lazy('meterials:list')
