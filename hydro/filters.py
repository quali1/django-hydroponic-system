import django_filters
from .models import Measurement, HydroponicSystem


class MeasurementFilter(django_filters.FilterSet):
    created_at_start = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')
    created_at_end = django_filters.DateFilter(field_name='created_at', lookup_expr='lte')
    updated_at_start = django_filters.DateFilter(field_name='updated_at', lookup_expr='gte')
    updated_at_end = django_filters.DateFilter(field_name='updated_at', lookup_expr='lte')
    ph_level_start = django_filters.NumberFilter(field_name='ph_level', lookup_expr='gte')
    ph_level_end = django_filters.NumberFilter(field_name='ph_level', lookup_expr='lte')
    tds_level_start = django_filters.NumberFilter(field_name='tds_level', lookup_expr='gte')
    tds_level_end = django_filters.NumberFilter(field_name='tds_level', lookup_expr='lte')
    temperature_start = django_filters.NumberFilter(field_name='temperature', lookup_expr='gte')
    temperature_end = django_filters.NumberFilter(field_name='temperature', lookup_expr='lte')

    class Meta:
        model = Measurement
        fields = [
            'hydroponic_system', 'created_at_start', 'created_at_end',
            'updated_at_start', 'updated_at_end', 'ph_level_start',
            'ph_level_end', 'tds_level_start', 'tds_level_end',
            'temperature_start', 'temperature_end'
        ]

    ordering = django_filters.OrderingFilter(
        fields=(
            ('created_at', 'created_at'),
            ('updated_at', 'updated_at'),
            ('ph_level', 'ph_level'),
            ('tds_level', 'tds_level'),
            ('temperature', 'temperature'),
        ),
        field_labels={
            'created_at': 'Created At',
            'updated_at': 'Updated At',
            'ph_level': 'pH Level',
            'tds_level': 'TDS Level',
            'temperature': 'Temperature'
        },
        label='Sort By'
    )


class HydroponicSystemFilter(django_filters.FilterSet):
    ordering = django_filters.OrderingFilter(
        fields=(
            ('name', 'name'),
            ('installation_date', 'installation_date'),
        ),
        field_labels={
            'name': 'Name',
            'installation_date': 'Installation Date',
        },
    )

    class Meta:
        model = HydroponicSystem
        fields = {
            'name': ['exact'],
            'description': ['exact'],
            'installation_date': ['exact'],
            'created_at': ['gte', 'lte'],
            'updated_at': ['gte', 'lte'],
            'size': ['exact'],
            'system_type': ['exact'],
        }
