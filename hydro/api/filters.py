import django_filters
from django_filters import rest_framework as filters
from hydro.models import HydroponicSystem, Measurement


class HydroponicSystemAPIFilter(django_filters.FilterSet):
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


class MeasurementAPIFilter(django_filters.FilterSet):
    created_at = django_filters.DateFromToRangeFilter()
    updated_at = django_filters.DateFromToRangeFilter()
    ph_level = django_filters.RangeFilter()
    tds_level = django_filters.RangeFilter()
    temperature = django_filters.RangeFilter()

    ordering = django_filters.OrderingFilter(
        fields=(
            ('created_at', 'created_at'),
            ('updated_at', 'updated_at'),
            ('ph_level', 'ph_level'),
            ('tds_level', 'tds_level'),
            ('temperature', 'temperature'),
        ),
    )

    class Meta:
        model = Measurement
        fields = [
            'hydroponic_system',
            'created_at',
            'updated_at',
            'ph_level',
            'tds_level',
            'temperature'
        ]
