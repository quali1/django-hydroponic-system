from rest_framework import serializers
from rest_framework.reverse import reverse

from hydro.models import HydroponicSystem, Measurement
from .validators import unique_hydroponic_system_name


class HydroponicSystemSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(view_name='hydro-detail', lookup_field='pk')
    name = serializers.CharField(
        validators=[unique_hydroponic_system_name]
    )

    class Meta:
        model = HydroponicSystem
        fields = '__all__'
        read_only_fields = ['owner']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'