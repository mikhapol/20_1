from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from meterials.models import Meterial


class MeterialCreateView(CreateView):
    model = Meterial
    fields = ('title', 'body',)
    success_url = reverse_lazy('meterials:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)


class MeterialUpdateView(UpdateView):
    model = Meterial
    fields = ('title', 'body',)
    # success_url = reverse_lazy('meterials:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('meterials:view', args=[self.kwargs.get('pk')])


class MeterialListView(ListView):
    model = Meterial

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class MeterialDetailView(DetailView):
    model = Meterial

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class MeterialDeleteView(DeleteView):
    model = Meterial
    success_url = reverse_lazy('meterials:list')
