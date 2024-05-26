from django.shortcuts import render
from django.views.generic import ListView
from .models import HydroponicSystem, Measurement

# Create your views here.


def home_page(request):
    return render(request, 'hydro/home.html')


def hydro_list_view(request):
    search = request.GET.get('search')
    systems = HydroponicSystem.objects.filter(owner=request.user)

    if search:
        systems = systems.filter(name__icontains=search)

    context = {
        'systems': systems,
        'search': search,
    }

    return render(request, 'hydro/systems_list.html', context)


class HydroListView(ListView):
    model = HydroponicSystem
    template_name = 'hydro/hydro_list.html'


class MeasurementsListView(ListView):
    model = Measurement
    template_name = 'hydro/measurements_list.html'
