from django.shortcuts import render
from django.views.generic import ListView
from .models import HydroponicSystem, Measurement


# Create your views here.


def home_page(request):
    return render(request, 'hydro/home.html')


def hydro_list_view(request):
    search = request.GET.get('search')
    systems = HydroponicSystem.objects.filter(owner=request.user)

    name = request.GET.get('name')
    if name:
        systems = systems.filter(name__icontains=name)

    description = request.GET.get('description')
    if description:
        systems = systems.filter(description__icontains=description)

    installation_date = request.GET.get('installation_date')
    if installation_date:
        systems = systems.filter(installation_date=installation_date)

    created_at_start = request.GET.get('created_at_start')
    created_at_end = request.GET.get('created_at_end')
    if created_at_start and created_at_end:
        systems = systems.filter(created_at__range=[created_at_start, created_at_end])

    updated_at_start = request.GET.get('updated_at_start')
    updated_at_end = request.GET.get('updated_at_end')
    if updated_at_start and updated_at_end:
        systems = systems.filter(updated_at__range=[updated_at_start, updated_at_end])

    size = request.GET.get('size')
    if size:
        systems = systems.filter(size=size)

    system_type = request.GET.get('system_type')
    if system_type:
        systems = systems.filter(system_type__icontains=system_type)

    ordering = request.GET.get('ordering')
    if ordering:
        if ordering == 'name_asc':
            systems = systems.order_by('name')
        elif ordering == 'name_desc':
            systems = systems.order_by('-name')
        elif ordering == 'date_asc':
            systems = systems.order_by('installation_date')
        elif ordering == 'date_desc':
            systems = systems.order_by('-installation_date')

    context = {
        'systems': systems,
        'search': search,
    }

    return render(request, 'hydro/systems_list.html', context)


class MeasurementsListView(ListView):
    model = Measurement
    template_name = 'hydro/measurements_list.html'
