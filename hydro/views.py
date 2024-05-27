from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .filters import MeasurementFilter, HydroponicSystemFilter
from .models import HydroponicSystem, Measurement


# Create your views here.


def home_page(request):
    return render(request, 'hydro/home.html')


@login_required(login_url="login")
def hydro_list_view(request):
    systems = HydroponicSystem.objects.filter(owner=request.user)
    system_filter = HydroponicSystemFilter(request.GET, queryset=systems)

    context = {
        'systems': system_filter.qs,
        'filter': system_filter,
    }

    return render(request, 'hydro/systems_list.html', context)


@login_required(login_url="login")
def measurements_list_view(request):
    systems = HydroponicSystem.objects.filter(owner=request.user)
    filter = MeasurementFilter(request.GET, queryset=Measurement.objects.all())
    context = {
        'filter': filter,
        'systems': systems,
    }
    return render(request, 'hydro/measurements_list.html', context)
