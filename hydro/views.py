from django.shortcuts import render
from django.views.generic import ListView
from .models import HydroponicSystem, Measurement


# Create your views here.


def home_page(request):
    return render(request, 'hydro/home.html')


class HydroListView(ListView):
    model = HydroponicSystem
    template_name = 'hydro/hydro_list.html'


class MeasurementsListView(ListView):
    model = Measurement
    template_name = 'hydro/measurements_list.html'
