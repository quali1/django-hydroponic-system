from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .filters import MeasurementFilter, HydroponicSystemFilter
from .models import HydroponicSystem, Measurement


# Create your views here.

def home_page(request):
    return render(request, 'hydro/home.html')


@login_required(login_url="login")
def hydro_list_view(request):
    hydroponic_systems = HydroponicSystem.objects.filter(owner=request.user)
    hydroponic_system_filter = HydroponicSystemFilter(request.GET, queryset=hydroponic_systems)

    context = {
        'systems': hydroponic_system_filter.qs,
        'filter': hydroponic_system_filter,
    }

    return render(request, 'hydro/systems_list.html', context)


@login_required(login_url="login")
def measurements_list_view(request):
    hydroponic_systems = HydroponicSystem.objects.filter(owner=request.user)
    measurement_filter = MeasurementFilter(request.GET,
                                           queryset=Measurement.objects.filter(hydroponic_system__owner=request.user))
    context = {
        'filter': measurement_filter,
        'systems': hydroponic_systems,
    }
    return render(request, 'hydro/measurements_list.html', context)
