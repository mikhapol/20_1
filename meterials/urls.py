from django.urls import path

from meterials.apps import MeterialsConfig
from meterials.views import MeterialCreateView, MeterialListView, MeterialDetailView, MeterialUpdateView, \
    MeterialDeleteView

app_name = MeterialsConfig.name

urlpatterns = [
    path('create/', MeterialCreateView.as_view(), name='create'),
    path('', MeterialListView.as_view(), name='list'),
    path('view/<int:pk>', MeterialDetailView.as_view(), name='view'),
    path('edit/<int:pk>', MeterialUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', MeterialDeleteView.as_view(), name='delete'),
]
