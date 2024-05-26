import django_filters
from django_filters import rest_framework as filters
from hydro.models import HydroponicSystem, Measurement


class HydroponicSystemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    installation_date = django_filters.DateFromToRangeFilter()
    created_at = django_filters.DateFromToRangeFilter()
    updated_at = django_filters.DateFromToRangeFilter()
    ordering = django_filters.OrderingFilter(
        fields=(
            ('created_at', 'created_at'),
        ),
    )

    class Meta:
        model = HydroponicSystem
        fields = [
            'name',
            'description',
            'installation_date',
            'created_at',
            'updated_at',
            'size',
            'system_type'
        ]
